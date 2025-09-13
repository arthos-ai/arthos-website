# Arthos.ai Marketing Website

A lean, static single-page marketing website for Arthos.ai - an AI solutions company.

## Purpose

This repository contains a minimal, static website designed to showcase Arthos.ai's AI-powered solutions and services. The site is built with vanilla HTML, CSS, and JavaScript, using Tailwind CSS via CDN for styling.

## Features

- **Single-page design** with smooth scrolling navigation
- **Responsive layout** that works on all devices
- **Contact form** ready for Formspree integration
- **SEO optimized** with proper meta tags and Open Graph support
- **Fast loading** with no build process or dependencies

## Technology Stack

- **HTML5** - Semantic markup
- **Tailwind CSS** - Utility-first CSS framework (via CDN)
- **Vanilla JavaScript** - Minimal interactions and form handling
- **No build tools** - Direct deployment ready

## Directory Structure

```
arthos-website/
├── index.html          # Main single-page site
├── assets/             # Images and static assets
│   ├── arthos3.png     # Company logo
│   ├── favicon.ico     # Site favicon (placeholder)
│   └── og.png          # Social preview image (placeholder)
├── css/
│   └── styles.css      # Optional CSS overrides
└── README.md           # This file
```

## Deployment

### Cloudflare Pages

1. **Connect Repository**: Link this GitHub repository to Cloudflare Pages
2. **Build Settings**:
   - **Build command**: `none` (no build step required)
   - **Build output directory**: `/` (root directory)
   - **Root directory**: `/` (default)
3. **Deploy**: The site will be automatically deployed and available at your custom domain

### Alternative Deployment Options

- **GitHub Pages**: Simply enable Pages in repository settings
- **Netlify**: Drag and drop the repository or connect via Git
- **Vercel**: Import repository and deploy (no build configuration needed)

## Formspree Integration

The contact form is currently set up with a placeholder JavaScript handler. To enable actual form submission:

1. **Sign up** for a [Formspree](https://formspree.io/) account
2. **Create a new form** and get your endpoint URL
3. **Update the form action** in `index.html`:
   ```html
   <form id="contact-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```
4. **Remove or modify** the JavaScript form handler as needed

## Customization

### Styling
- **Primary styling**: Tailwind CSS classes in `index.html`
- **Custom overrides**: Add styles to `css/styles.css`
- **Color scheme**: Modify Tailwind classes or add custom CSS variables

### Content
- **Text content**: Edit directly in `index.html`
- **Images**: Replace placeholder images in `assets/` directory
- **Meta tags**: Update Open Graph and SEO tags in the `<head>` section

### Assets
- **Logo**: Replace `assets/arthos3.png` with your actual logo
- **Favicon**: Add `assets/favicon.ico` (16x16, 32x32, 48x48 sizes)
- **Social preview**: Add `assets/og.png` (1200x630px recommended)

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

- **No JavaScript frameworks** - Minimal bundle size
- **CDN-delivered CSS** - Fast loading with global CDN
- **Optimized images** - Compressed and properly sized
- **Minimal dependencies** - No package.json or node_modules

## Maintenance

This is a static site with minimal maintenance requirements:

- **Content updates**: Edit HTML directly
- **Styling changes**: Modify CSS files
- **Form updates**: Update Formspree endpoint when needed
- **Asset updates**: Replace images as needed

## License

© 2024 Arthos.ai. All rights reserved.

---

**Note**: This is a marketing website template. Replace placeholder content and assets with actual Arthos.ai branding and information before deployment.
