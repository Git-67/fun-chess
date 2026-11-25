# Crown & Cards

Phone and desktop chess-inspired chaos game with a local AI, 24 cycling cards, action points, health bars, animated hazards, and automatic quick-time events.

## GitHub Pages

In **Settings → Pages**, select **Deploy from a branch**, **main**, and **/docs**. No build or secrets are needed. All game assets are bundled locally.

Solo play runs entirely on Pages. Pages cannot run the lobby server. **Online arena** opens the existing multiplayer game at https://crown-cards-jing.bentzebra32.chatgpt.site/; both players need access to that site. The original hosted game is unchanged.

## Play

Tap/click a piece, then a highlighted destination. Moves earn 1 AP (maximum 5); cards use an action. Flip for two actions or none, or take one safe action. Capture the king to win. Ordinary moves do not enforce check; castling requires a safe path. En passant and promotion are supported.

Health: pawn 2, knight/bishop 3, rook 4, queen 5, king 6; cannon/laser 3 and wall 4. Surviving defenders stay put. Dinos move one square per turn from either edge; yellow pellets show Pac-Man’s fixed route.

## Development

Requires Node 24+. No npm dependencies.

- `npm test`: rules, server authorization/race protection, seeded simulations.
- `npm run dev`: preview with local SQLite.
- `npm run build`: optional Cloudflare Worker backend bundle.
- `python scripts/bundle-art.py`: rebuild bundled artwork.

Edit `docs/` for the game, `worker/api.mjs` for the API. Tests validate behavior, not perfect competitive balance.

## Optional independent multiplayer hosting

The complete Worker and D1 backend is included. Deploy the complete game to a Worker for same-origin multiplayer:

1. Create a D1 database named `crown-and-cards` in your Cloudflare account.
2. Replace the placeholder database ID in `wrangler.jsonc`.
3. Set `window.CROWN_PAGES = false` in `docs/pages-config.js` in the Worker deployment checkout; keep it true in the Pages checkout.
4. Run `npm run build`, apply migrations with `npx wrangler d1 migrations apply DB --remote`, then `npx wrangler deploy`.
5. Point `window.CROWN_ONLINE_URL` in the Pages checkout at your Worker URL. Never commit API keys or account tokens.

## Artwork

All artwork was sourced online. Original assets, exact sources and license notices are retained in `docs/assets/` and linked in the rules dialog. Chess: Cburnett/Lichess (GPL v2+); cards: Game-icons.net (CC BY 3.0); interface: Lucide (ISC/MIT); Pac-Man: Tabler (MIT); dinosaur: Chromium Authors (BSD). Display copies are tinted/scaled and opaque card-icon backgrounds removed.
