# Gwarmai Global Resources Limited — Website

A professional, production-ready website for **Gwarmai Global Resources Limited (GGR)**, built from the company's official Company Profile (EU VACE / TARED 2026) and official logo.

## What this is

A static, multi-page website (HTML5 + CSS3 + vanilla JavaScript). No build tooling or framework is required to run it — it works as plain static files, which keeps it simple to host, fast to load, and easy to hand off.

```
ggr-website/
├── index.html            Home
├── about.html            About Us
├── services.html         Services
├── expertise.html        Expertise
├── projects.html         Projects / Portfolio
├── approach.html         Our Approach
├── team.html             Team / Leadership
├── resources.html        Resources / Documents
├── contact.html          Contact
├── privacy.html          Privacy Policy (placeholder — see below)
├── 404.html              Not found page
├── netlify.toml          Netlify build & header configuration
├── robots.txt
├── sitemap.xml
├── css/
│   └── style.css         Full design system (tokens, layout, components)
├── js/
│   └── main.js           Nav, scroll reveal, counters, filters, form, lightbox
├── assets/
│   ├── images/           Logo + brand-colour SVG illustrations
│   └── GGR_Company_Profile.pdf   The source company profile (also linked on the Resources page)
├── _partials/            Source templates used to assemble the pages (see below)
└── build.py              The script that assembles _partials/ into the final HTML pages
```

### About `_partials/` and `build.py`

Every page shares the same header and footer. To avoid duplicating that markup nine times, the header/footer live once in `_partials/head.html` and `_partials/footer.html`, and each page's unique content lives in `_partials/body_<page>.html`. Running:

```bash
python3 build.py
```

regenerates all the root-level `.html` files from those pieces. **If you edit navigation, the footer, or SEO meta-tag structure, edit the files in `_partials/` and re-run `build.py` — don't hand-edit the generated root HTML files, or your changes will be overwritten next time the site is rebuilt.** If you're only editing the unique content of one page (e.g. a paragraph on the About page), you can edit `_partials/body_about.html` and re-run the build, or edit `about.html` directly if you don't plan to rebuild.

## Content accuracy

All company information, statistics, project details, and team profiles on this website are drawn directly from the supplied **GGR Company Profile (EU VACE / TARED 2026)**. Where the source document did not include certain content the requested page structure calls for — a formal mission/vision/values statement, a privacy policy, and professional team photographs — the site uses a clearly marked, easy-to-find placeholder rather than inventing content. Search the codebase for `placeholder-note` to find these spots:

- **About → Mission, Vision & Values**: placeholder (not in the source profile)
- **Team page**: initials are shown in place of photographs (none were supplied)
- **Privacy Policy**: placeholder page

Replace these once GGR provides the missing material.

## Design

- **Colours**: Deep Green `#0B5D3B` (primary), Light Green `#2E8B57` (secondary), Gold `#D4A72C` (accent, used sparingly), Charcoal `#1F2937` (text), Soft Background `#F4F8F5`.
- **Typography**: Inter, loaded from Google Fonts.
- **Imagery**: The logo is used exactly as supplied (untouched). All other visuals are original, brand-coloured SVG illustrations rather than stock photography — this avoids misrepresenting GGR's actual field work with generic or fabricated photos. Once GGR supplies real project photographs, swap the files in `assets/images/` (same filenames) and they'll appear automatically.

## Local preview

No build step is required. From the project folder, run any static file server, for example:

```bash
python3 -m http.server 8080
```

Then open `http://localhost:8080/index.html`.

## Deploying to Netlify

1. Push this folder to a new GitHub repository.
2. In Netlify: **Add new site → Import an existing project → connect the repository.**
3. Build settings:
   - **Build command:** *(leave blank — this is a static site with no build step)*
   - **Publish directory:** `.` (already set in `netlify.toml`)
4. Deploy. Netlify will pick up `netlify.toml` automatically for headers and the custom 404 page.
5. Once deployed, connect your custom domain in **Site settings → Domain management**, and update the `https://gwarmaiglobal.com` placeholder URLs in `sitemap.xml`, `robots.txt`, and each page's `<link rel="canonical">` / Open Graph tags to match your real domain.

No environment variables are required for the current static site. If you later add a serverless contact-form handler or connect Supabase (see below), add those variables in **Site settings → Environment variables** — never commit secrets to the repository.

## Contact form

The contact form (`contact.html`) is fully validated on the client side (required fields, email format, error and success states, loading state) but is **not connected to a live email backend** — the PDF did not specify one. It's ready to be wired up to:
- [Netlify Forms](https://docs.netlify.com/forms/setup/) (simplest — add a `netlify` attribute to the `<form>` and a hidden `form-name` field), or
- A serverless function / API endpoint of your choice.

## Future admin system & database readiness

The site is deliberately built as static content today, but is structured so that projects, services, expertise, team members, documents, and homepage content could later be moved into a CMS or database (e.g. Supabase) and rendered dynamically without a full rebuild:

- Content blocks (project cards, team cards, service cards, resource rows) are self-contained, repeatable HTML fragments — the natural shape for records in tables such as `projects`, `services`, `expertise`, `team_members`, `documents`, and `contact_messages`.
- The contact form is isolated in its own component (`#contact-form` in `contact.html` + the `initContactForm()` function in `js/main.js`), ready to POST to an API route that would write to a `contact_messages` table.
- No secrets are present anywhere in the codebase. When backend credentials are introduced, keep them in environment variables (Netlify environment variables, never committed to the repo).

## Accessibility & performance notes

- Semantic HTML, heading hierarchy, skip-to-content link, visible focus states, alt text on all images, and ARIA labels on icon-only controls (menu toggle, back-to-top).
- `prefers-reduced-motion` is respected — animations and smooth scrolling are disabled for users who request it.
- No build-time image optimisation is needed since illustrations are hand-authored SVG (small, resolution-independent, no external requests). The logo PNG is the only raster asset.
- Fonts are loaded from Google Fonts with `preconnect` hints; everything else is self-contained with no external JS dependencies.

## What's next

- Swap in real project/team photography once supplied.
- Fill in Mission, Vision, Core Values, and the Privacy Policy once GGR provides official wording.
- Wire the contact form to a live backend.
- Add further resources/documents to the Resources page as they become available.
