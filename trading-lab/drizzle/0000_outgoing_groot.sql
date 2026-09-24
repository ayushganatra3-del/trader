CREATE TABLE `research_experiments` (
	`id` text PRIMARY KEY NOT NULL,
	`owner_id` text NOT NULL,
	`created_at` text NOT NULL,
	`summary` text NOT NULL,
	`payload` text NOT NULL
);
--> statement-breakpoint
CREATE INDEX `experiments_owner_created` ON `research_experiments` (`owner_id`,`created_at`);