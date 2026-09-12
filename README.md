# StripChat Free Tokens — Only Legitimate Methods

A fully static, dependency-free English-language website about **StripChat free
tokens**: how token balances work, which promotions can be legitimate, how to
evaluate third-party offers (including the advertised "50 TK draw"), and how to
avoid fake generators, "hacks", mod APKs, phishing pages, and rogue extensions.

> **Independent educational project.** This site is not affiliated with, endorsed
> by, or operated by StripChat. It does **not** promise free tokens, does not host
> generators/hacks/mods, and contains no explicit imagery. External promotional
> links are marked `rel="nofollow sponsored noopener noreferrer"` and carry a
> visible disclosure.

## Site structure

| Page | URL |
| --- | --- |
| Homepage / 2026 guide | `/` |
| Legitimate methods | `/legitimate-stripchat-token-methods/` |
| Scams & safety | `/stripchat-token-scams-and-safety/` |
| Video guide | `/stripchat-tokens-video-guide/` |
| About / Contact / Privacy / Terms / Affiliate disclosure / Disclaimer | `/about/`, `/contact/`, `/privacy-policy/`, `/terms-of-use/`, `/affiliate-disclosure/`, `/disclaimer/` |
| Not found | `/404.html` (noindex) |

Every public page contains the same embedded YouTube video
(`youtube-nocookie.com/embed/0gUquIZrdL0`, no autoplay), a sticky bottom
navigation with the disclosure-aware offer CTA, unique metadata, and an
age/content notice.

## Architecture

Plain **HTML + CSS + minimal vanilla JavaScript** — no frameworks, no build
runtime, no npm. A tiny Python 3 generator (standard library only) renders the
shared template and content modules into static files:

```
tools/
  build.py            # the static-site generator
  content_home.py     # homepage copy, TOC, video block, FAQ
  content_methods.py  # legitimate methods article
  content_safety.py   # scams & safety article
  content_video.py    # video-focused page (includes verified video metadata)
  content_legal.py    # about/contact/privacy/terms/disclosure/disclaimer
assets/
  css/style.css       # single stylesheet (dark, accessible, mobile-first)
  js/main.js          # progressive enhancement only (menu, notice, mailto, scrollspy)
  img/                # original SVG illustrations, PNG icons, OG image
```

The generated files (`index.html`, each folder's `index.html`, `404.html`,
`robots.txt`, `sitemap.xml`, `site.webmanifest`, `.nojekyll`) live at the
repository root so GitHub Pages can serve them directly.

## Local development

Python 3.9+ is the only requirement (used solely for the generator and an
optional local server).

```bash
# 1. Regenerate the site after editing any tools/content_*.py file
python3 tools/build.py

# 2. Preview locally (relative links work from the repository root)
python3 -m http.server 8080
# open http://127.0.0.1:8080/
```

The pages also work when opened directly from disk except for the root-absolute
links in `404.html` (those intentionally assume the deployed subpath).

## Build and validation

There are no compile or lint dependencies. Quick validations:

```bash
python3 tools/build.py          # regenerates all pages/SEO files
python3 -m http.server 8080     # smoke test with a browser or curl
```

The generator always refreshes `sitemap.xml`, `robots.txt`, the web manifest,
and `.nojekyll`. Content checks performed before release (manual/scripted):

- one unique `<title>`, meta description, canonical, and H1 per page;
- the privacy-enhanced YouTube embed on every page, no autoplay;
- sticky CTA bar and external-link notice on every page;
- internal links, TOC fragments, and image references resolve;
- valid JSON-LD (WebSite, Article, BreadcrumbList, FAQPage, VideoObject);
- VideoObject contains only verified data (title, channel, upload date
  2026-09-11, duration 1:40, hqdefault thumbnail, official watch URL);
- no fabricated testimonials, ratings, statistics, or author identities;
- hacks/mods/APKs/generators are covered strictly as safety warnings;
- all visible copy, navigation, alt text, metadata, and structured data are
  in English.

## Deployment to GitHub Pages

The prepared canonical URL assumes a **project page**:

```
https://lilistripmods.github.io/Strip-Mods27/
```

Simplest path (branch deployment):

1. Merge this branch into the repository's default branch (`main`).
2. On GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a
   branch**, choose branch `main` and folder `/ (root)`.
3. Wait for the Actions/Pages build, then open the URL above. The committed
   `.nojekyll` file ensures files are published as-is.

Alternative (Actions deployment): create `.github/workflows/deploy.yml` with
the official `actions/deploy-pages` flow once, then set **Settings → Pages →
Source: GitHub Actions**.

After the real domain is known (custom domain or a different repository name),
rebuild with the correct values:

```bash
SITE_URL="https://your-username.github.io/repo-name" \
SITE_BASE_PATH="/repo-name" \
python3 tools/build.py
# for an apex/custom-domain root, use SITE_BASE_PATH=""
```

`SITE_URL` controls canonicals, Open Graph tags, the sitemap, and robots.txt;
`SITE_BASE_PATH` controls the absolute links in `404.html` and the manifest.

## SEO configuration

- **Canonicals / sitemap / OG / Twitter cards:** set via `SITE_URL` in
  `tools/build.py` (top of file) or the environment variable above.
- **Social image:** `assets/img/og-image.png` (1200×630, original artwork;
  source `og-image.svg`/Pillow script). Replace freely, keep the same filename
  or update the generator.
- **Illustrations:** original SVG files in `assets/img/` with descriptive alt
  text; below-the-fold images use `loading="lazy"`.
- **Structured data:** generated in `tools/build.py` (`head_html`). Only add
  facts that are visibly true on the page; never add ratings/reviews.
- **robots.txt** allows crawling and points to the sitemap.
- Submit `sitemap.xml` in Google Search Console after launch.

### Google Search Console verification token

The token is **intentionally not deployed**. Every page currently contains the
required placeholder:

```html
<meta name="google-site-verification" content="REPLACE_WITH_AUTHORIZED_TOKEN">
```

Deploy the real token (the one provided for this project) **only if you control
the property/domain and are authorized to verify it**:

```bash
# one-off build with the authorized token
GSC_TOKEN="876TWmd0bhMdYz0kV3kv929OFy6yLDBrd2Fk0PUW1P0" python3 tools/build.py
# or edit GSC_TOKEN near the top of tools/build.py and rerun
```

If the property is not yours, keep the placeholder.

## Updating external (sponsored) links

The offer CTA appears in two places generated by `tools/build.py`:

- `OFFER_URL` / `OFFER_LABEL` constants (used in the sticky bar and related
  call-to-actions);
- the approved destination list described on
  `/affiliate-disclosure/` and the methods article (`content_legal.py`,
  `content_methods.py`).

Approved destinations per the site policy:

- `https://striptks.live/`
- `https://stripfreetokens.com/`
- `http://striptokens.live/` (insecure — never presented as recommended)

Rules for any outbound commercial link:

1. Keep `rel="nofollow sponsored noopener noreferrer"` and `target="_blank"`.
2. Keep the visible notice that offers carry separate terms and that tokens,
   prizes, and results are not guaranteed.
3. Never describe third parties as official, verified, safe, or "legal
   sources" unless that status has actually been verified.
4. Rebuild after editing: `python3 tools/build.py`.

## Updating the video

Video metadata used in the visible table and in `VideoObject` JSON-LD lives in
`tools/content_video.py` and as constants in `tools/build.py`
(`YT_ID`, `YT_TITLE`, `YT_CHANNEL`, `YT_UPLOAD_DATE`, `YT_DURATION_ISO`). Only
change them to values you can verify on the public YouTube page; timestamps are
omitted on purpose unless accurate chapter data exists.

## Compliance notes

- No claims of unlimited, guaranteed, instant, or "100% working" tokens.
- No token generators, credential harvesting, malware, cracked/modded apps,
  account bypasses, or instructions for any of them — only safety analysis.
- No fabricated testimonials, reviews, credentials, statistics, or rankings
  promises, and no fake scarcity, countdowns, pop-ups, or forced downloads.
- Trademarks belong to their respective owners; the site is independent.
- See `/disclaimer/`, `/terms-of-use/`, and `/affiliate-disclosure/`.
