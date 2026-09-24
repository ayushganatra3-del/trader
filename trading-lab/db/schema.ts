import { sqliteTable, text, index } from 'drizzle-orm/sqlite-core';

export const experiments = sqliteTable('research_experiments', {
  id: text('id').primaryKey(),
  ownerId: text('owner_id').notNull(),
  createdAt: text('created_at').notNull(),
  summary: text('summary').notNull(),
  payload: text('payload').notNull(),
}, table => [index('experiments_owner_created').on(table.ownerId, table.createdAt)]);
