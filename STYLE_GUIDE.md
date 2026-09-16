# Arthos site — component & tone guide

Working rules for how sections, colors, and copy are used across arthos.ai. Update this file when a decision changes — don't let the site drift from what's written here, and don't let this drift from what the site actually does.

## Color

Two background tones only. No per-section color rotation.

- `--bg` — the default. Most of the page lives here.
- `--card` — reserved for: (1) a card in a set of parallel, independent items (e.g. the use-case cards), (2) a closing CTA band, marking a tonal shift from explaining to inviting, and (3) a self-contained worked-example panel (the flagged-contradiction example lives on How It Works, not Home — it was tried on Home and pulled back off, since a concrete example belongs on the deeper page). If you're reaching for a fourth use, stop and reconsider — it stops meaning anything once it's everywhere.
- `--accent` — reserved for interactive/orientation elements only: eyebrows (section labels), the primary button fill, hover/focus states, and the step tags in a numbered sequence (Detect/Triage/Decide/Resolve). Headlines and body copy stay off-accent so they don't compete with it.

## Typography roles

- **Eyebrow** (small mono, uppercase, accent color): orientation only. Tells you what kind of section you're entering, never carries the point itself.
- **Headline** (h1/h2, neutral text color, full sentence): carries the actual point. Always a complete authored sentence, not a fragment or label.
- **Body copy**: flat and mechanical, not promotional. No superlatives, no "best-in-class." Describe what happens, plainly.

## When to use what

| Pattern | Use it for | Not for |
|---|---|---|
| Solid button (accent fill) | The one primary ask on the page/section | Anything else — there should only ever be one kind of button-weight action per view |
| Quiet underlined link | A secondary, optional path (e.g. a deeper/technical page) | The main conversion action |
| Connected numbered sequence (steps, dividers, no card borders) | Content that is a real, ordered process — each step depends on the last | A set of independent/parallel examples |
| Bordered card | Parallel, independent items a reader scans and self-selects from | Anything sequential — don't box a process into cards, it hides the order |

Numbered markers (01/02/03...) are only used where the content is an actual sequence. Don't add numbering to a list just for visual rhythm.

## Copy conventions

- Periods, not em dashes. If a sentence wants an em dash, it usually means split it into two sentences instead.
- CTA copy is short and human ("Let's partner"), never transactional ("Contact Us," "Schedule a Demo").
- Use-case examples span industries deliberately (regulatory/government, corporate/M&A, entertainment/franchise) to signal the product is industry-agnostic — don't default back to only business-context examples.
- No engineering jargon in customer-facing copy (no "atoms," "orthogonalization," literal "fail loudly" language). That vocabulary is reserved for the How It Works page, aimed at a technical reader vetting the mechanism.

## Navigation

- The nav bar is **sticky** (`position: sticky; top: 0`) on every page — stays visible while scrolling so Contact is always reachable. Give it an explicit `background: var(--bg)` and a `z-index` so content doesn't show through underneath it while scrolling.
- The current page's own nav link is marked with a `.nav-current` class (text color only, matches `--text` instead of the dimmer default) — but it must still be a **real, working link to that page's own URL**, never `href="#"` and never `pointer-events: none`. A current-page indicator that's inert reads as a dead/broken link to a visitor, especially when it's a button-styled CTA like "Contact" rather than a quiet text label.
- **Self-referencing nav/footer links (the current page linking to itself) need an explicit `onclick="window.scrollTo({top:0,behavior:'smooth'});return false;"` handler.** A plain `href` to the exact URL you're already on is a no-op in most browsers — no reload, no navigation event, so `pageshow`/scroll-restoration fixes never fire and clicking does nothing. This was caught twice: once on Contact's own "Contact" links (nav + footer), once on How It Works' own "How it works" links (nav + footer).
- Every page is its own separate published Artifact with its own URL (Home, How It Works, Contact so far — About next). Cross-page links (nav, footer, CTAs) must point to the real URLs, not in-page anchors — a leftover anchor like `#how-it-works-preview` on a page that no longer contains that section is a real broken link, not just a stylistic leftover. When copying the nav/footer markup as a starting point for a new page, double-check which link should now be marked `.nav-current` for *this* page — don't just carry over whichever one was current on the source page you copied from.

## Known gotchas

- **Current dark-mode token values (don't lower without re-checking actual computed contrast, not just eyeballing it):** `--card: #363026` (was `#2c2825` — the original was only ~1.2:1 against `--bg`, different enough on paper but nearly indistinguishable to the eye); `--text-dim: rgba(230,235,241,0.78)` (was 0.64); `--text-faint: rgba(230,235,241,0.70)` (was originally 0.42, briefly 0.56, then raised again — 0.56 technically passed WCAG AA at ~4.9:1 but still read as muddy "gray on gray on black" against the panel; 0.70 was chosen for a comfortable, clearly-legible margin instead of a bare pass). Caught 2026-09-11 on the How It Works worked-example panel; fixed on both Home and How It Works.
- **Buttons don't inherit the page font by default.** Browsers give `<button>` its own default form-control font, not the body's. Any button/its children showing body text (not just icon/label mono text) needs an explicit `font-family: inherit` (or the real font stack) on the button itself, or its text will silently render in the wrong typeface — as the `.example-choice` buttons did until this was caught.

## Source of truth

The homepage mockup this guide describes: see the Arthos Homepage artifact. This file should be updated any time a section pattern changes there, so the two never disagree.
