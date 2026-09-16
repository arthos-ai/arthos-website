# Arthos.ai Marketing Website

A lean, static multi-page marketing website for Arthos.ai — an AI knowledge-conflict-detection company.

## Purpose

This repository contains the static marketing site at arthos.ai: Home, How It Works, About, and Contact. Built with vanilla HTML, CSS, and JavaScript — no framework, no build step.

## Features

- **Four pages** — Home, How It Works, About, Contact — sharing one nav/footer and one dark, warm design system
- **Responsive layout** that works on all devices
- **Contact form** wired to Formspree, with client-side validation and a honeypot field
- **SEO optimized** with proper meta tags and Open Graph support per page
- **Fast loading** with no build process or dependencies

## Technology Stack

- **HTML5** — Semantic markup
- **Vanilla CSS** — Custom properties (`--bg`, `--card`, `--text`, `--accent`, etc.), no CSS framework
- **Vanilla JavaScript** — Minimal interactions and form handling, no libraries
- **No build tools** — Direct deployment ready

## Directory Structure

```
arthos-website/
├── index.html          # Home
├── how-it-works.html   # How It Works
├── about.html          # About / team
├── contact.html        # Contact (Formspree form)
├── assets/             # Shared images and static assets
│   ├── arthos3.png     # Wordmark logo (homepage hero)
│   ├── heart-mark.png  # Heart-mark brand icon (nav + footer)
│   ├── favicon.ico     # Site favicon
│   └── og.png          # Social preview image
├── about-us/            # Team headshots used on about.html
├── css/
│   └── styles.css      # Unused legacy overrides (pre-dates the current design; safe to remove)
├── STYLE_GUIDE.md       # Design system + copy conventions — read before editing any page
└── README.md            # This file
```

## Design system

See `STYLE_GUIDE.md` for the full set of rules (color usage, typography roles, when to use a card vs. a numbered sequence, copy conventions, navigation/self-link gotchas). Every page shares the same CSS custom properties and component patterns — keep new sections consistent with what's there rather than introducing new one-off styles.

## Deployment

### Cloudflare Pages

1. **Connect Repository**: Link this GitHub repository to Cloudflare Pages
2. **Build Settings**:
   - **Build command**: `none` (no build step required)
   - **Build output directory**: `/` (root directory)
   - **Root directory**: `/` (default)
3. **Deploy**: Cloudflare Pages is connected directly to this repo — any push to `main` auto-deploys within ~20 seconds.

## Formspree Integration

The contact form (`contact.html`) posts to a live Formspree endpoint (`https://formspree.io/f/mdkljvvg`). Fields: `name`, `email`, `company`, `message`, plus a hidden `website` honeypot field. To point it at a different form, update the `action` attribute on `#contact-form` and the Formspree dashboard accordingly.

## Customization

### Styling
- Each page's `<style>` block defines the same shared tokens (`--bg`, `--card`, `--text`, `--text-dim`, `--text-faint`, `--accent`, `--line`). Change a token in one page, change it in all four to keep them in sync.
- `css/styles.css` is legacy/unused — none of the four pages link to it.

### Content
- **Text content**: edit directly in the relevant page's HTML.
- **Team bios/photos**: `about.html` + the `about-us/` directory.
- **Meta tags**: update the Open Graph/Twitter/description tags in each page's `<head>` — each page has its own.

### Navigation
- Nav and footer links are relative paths (`/`, `/how-it-works.html`, `/about.html`, `/contact.html`) repeated on all four pages — update all four when adding/removing/renaming a page.
- The current page's own nav link needs a real `href` to itself plus an `onclick="window.scrollTo(...); return false;"` handler (see STYLE_GUIDE.md — a same-URL `href` alone is a no-op in most browsers).

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

- **No JavaScript frameworks** — minimal bundle size
- **No external CSS framework** — no Tailwind CDN dependency
- **Minimal dependencies** — no package.json or node_modules

## Maintenance

- **Content updates**: edit HTML directly, per page.
- **Styling changes**: keep the four pages' `<style>` blocks in sync; update `STYLE_GUIDE.md` when a pattern changes.
- **Form updates**: update the Formspree endpoint/fields in `contact.html` when needed.
- **Asset updates**: replace images in `assets/` or `about-us/` as needed.

## License

© Arthos AI, Inc. All rights reserved.
