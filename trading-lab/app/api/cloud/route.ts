import { privateHeaders as headers, signedInUser } from '@/lib/storage';
import { readCloudLedger, repository, cloudWorkflow } from '@/lib/cloud-ledger.mjs';

export async function GET(request: Request) {
  if (!signedInUser(request)) return Response.json({ message: 'Sign in to view the virtual portfolio.' }, { status: 401, headers });
  try {
    return Response.json({ ...(await readCloudLedger()), repository, workflow: cloudWorkflow, fetched_at: new Date().toISOString() }, { headers });
  } catch {
    return Response.json({ message: 'The cloud ledger is unavailable. Previously recorded trades have not been changed. Try refreshing shortly.', repository, workflow: cloudWorkflow }, { status: 503, headers });
  }
}
