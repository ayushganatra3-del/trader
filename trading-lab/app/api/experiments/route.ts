import { database, privateHeaders as headers, signedInUser, sameOrigin } from '@/lib/storage';
import { validateExperiment } from '@/lib/experiments.mjs';
import { boundedJSON } from '@/lib/bounded-json.mjs';

export async function GET(request: Request) {
  const owner = signedInUser(request);
  if (!owner) return Response.json({ message: 'Sign in to load your cloud journal.' }, { status: 401, headers });
  try {
    const id = new URL(request.url).searchParams.get('id');
    if (id) {
      if (!/^[a-zA-Z0-9-]{16,80}$/.test(id)) return Response.json({ message: 'Invalid experiment.' }, { status: 400, headers });
      const row = await database().prepare('SELECT payload FROM research_experiments WHERE id = ? AND owner_id = ?').bind(id, owner).first<{ payload: string }>();
      return row ? Response.json({ experiment: JSON.parse(row.payload) }, { headers }) : Response.json({ message: 'Experiment not found.' }, { status: 404, headers });
    }
    const rows = await database().prepare('SELECT summary FROM research_experiments WHERE owner_id = ? ORDER BY created_at DESC LIMIT 100').bind(owner).all<{ summary: string }>();
    return Response.json({ experiments: rows.results.map(row => JSON.parse(row.summary)) }, { headers });
  } catch {
    return Response.json({ message: 'Cloud storage could not be reached. Your current experiment is still available to export.' }, { status: 503, headers });
  }
}

export async function POST(request: Request) {
  const owner = signedInUser(request);
  if (!owner) return Response.json({ message: 'Sign in to save your experiment.' }, { status: 401, headers });
  if (!sameOrigin(request)) return Response.json({ message: 'Save from this website.' }, { status: 403, headers });
  if (!request.headers.get('content-type')?.includes('application/json')) return Response.json({ message: 'Expected an experiment.' }, { status: 415, headers });
  let validated: ReturnType<typeof validateExperiment>;
  try {
    validated = validateExperiment(await boundedJSON(request, 2_000_000));
    if (new TextEncoder().encode(JSON.stringify(validated.payload)).length > 1_800_000) throw Error('This experiment is too large for cloud storage. Export it instead.');
  } catch (error) {
    return Response.json({ message: error instanceof Error ? error.message : 'Invalid experiment.' }, { status: 400, headers });
  }
  try {
    const { summary, payload } = validated;
    // A repeated request ID is idempotent. Never update another owner's record.
    const db = database();
    await db.prepare('INSERT INTO research_experiments (id, owner_id, created_at, summary, payload) VALUES (?, ?, ?, ?, ?) ON CONFLICT(id) DO NOTHING')
      .bind(summary.id, owner, summary.at, JSON.stringify(summary), JSON.stringify(payload)).run();
    const stored = await db.prepare('SELECT summary FROM research_experiments WHERE id = ? AND owner_id = ?').bind(summary.id, owner).first<{ summary: string }>();
    if (!stored) return Response.json({ message: 'This experiment identifier is already used. Save again.' }, { status: 409, headers });
    return Response.json({ experiment: JSON.parse(stored.summary) }, { headers });
  } catch {
    return Response.json({ message: 'The cloud save failed. Keep this page open or export your experiment and try again.' }, { status: 503, headers });
  }
}
