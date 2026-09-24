import { env } from 'cloudflare:workers';

export function database(): D1Database {
  const db = (env as unknown as { DB?: D1Database }).DB;
  if (!db) throw new Error('Cloud storage is unavailable. Your current experiment has not been changed.');
  return db;
}

export const privateHeaders = { 'Cache-Control': 'no-store, private', 'X-Content-Type-Options': 'nosniff' };

export function signedInUser(request: Request): string | null {
  return request.headers.get('oai-authenticated-user-id')?.trim() || null;
}

export function sameOrigin(request: Request): boolean {
  const origin = request.headers.get('origin');
  return !!origin && origin === new URL(request.url).origin && request.headers.get('sec-fetch-site') !== 'cross-site';
}
