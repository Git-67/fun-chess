CREATE TABLE lobbies (
 code TEXT PRIMARY KEY NOT NULL,
 white_token TEXT NOT NULL,
 black_token TEXT,
 state TEXT NOT NULL,
 revision INTEGER DEFAULT 0 NOT NULL,
 expires INTEGER NOT NULL,
 qte_deadline INTEGER DEFAULT 0 NOT NULL
);
--> statement-breakpoint
CREATE INDEX lobbies_expiry ON lobbies (expires);
