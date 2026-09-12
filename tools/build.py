#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static site generator for the StripChat Token Safety Guide.

Zero third-party dependencies (Python 3 standard library only).
Content lives in tools/content_*.py; this script renders shared chrome
(head, header, age notice, video embeds, TOC, FAQ, footer, sticky CTA bar),
JSON-LD, robots.txt, sitemap.xml, the web manifest and 404 page into the
repository root for GitHub Pages.

Configuration: edit SITE_URL / SITE_BASE_PATH / GSC_TOKEN below (or set the
matching environment variables) before building for a different domain.
"""
import json
import os
import re
import shutil
import sys
from datetime import date, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import content_home
import content_methods
import content_safety
import content_video
import content_legal

# ---------------------------------------------------------------------------
# Configuration --------------------------------------------------------------
# ---------------------------------------------------------------------------
SITE_URL = os.environ.get(
    "SITE_URL", "https://lilistripmods.github.io/Strip-Mods27"
).rstrip("/")
SITE_BASE_PATH = os.environ.get("SITE_BASE_PATH", "/Strip-Mods27")  # "" for apex/custom root
GSC_TOKEN = os.environ.get("GSC_TOKEN", "REPLACE_WITH_AUTHORIZED_TOKEN")
SITE_NAME = "StripChat Token Safety Guide"
BUILD_DATE = date.today().isoformat()
YT_ID = "0gUquIZrdL0"
YT_TITLE = "Stripchat Hack 2026\u20132027? Free Token Claims Explained (UPDATED!!)"
YT_CHANNEL = "thenewyorkjets28"
YT_CHANNEL_URL = "https://www.youtube.com/@thenewyorkjets28"
YT_UPLOAD_DATE = "2026-09-11"
YT_DURATION_ISO = "PT1M40S"
OFFER_URL = "https://striptks.live/"
OFFER_LABEL = "Check the 50 TK Draw Offer"

H1 = {
    "/": "StripChat Free Tokens: Legitimate Methods, Safety Tips & 2026 Guide",
    "/legitimate-stripchat-token-methods/":
        "Legitimate StripChat Token Methods: What Actually Works?",
    "/stripchat-token-scams-and-safety/":
        "StripChat Token Scams, Fake Generators and Online Safety",
    "/stripchat-tokens-video-guide/":
        "StripChat Tokens Video Guide: Legitimate Methods and Safety Advice",
}

# ---------------------------------------------------------------------------
# Small helpers --------------------------------------------------------------
# ---------------------------------------------------------------------------

def rel_base(slug):
    """Relative path prefix for pages served one directory level deep."""
    return "." if slug == "/" else ".."


def abs_url(slug):
    return SITE_URL + (slug if slug != "/" else "/")


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def split_article_body(html_text):
    """Split content around the single <div class=\"article-body\"> wrapper.

    Returns (before, inner, after): 'before' holds the lede and the video
    embed (rendered full width), 'inner' holds the sections, 'after' holds
    anything following the wrapper (conclusion/related blocks).
    """
    marker = '<div class="article-body">'
    start = html_text.find(marker)
    if start == -1:
        return "", html_text, ""
    inner_start = start + len(marker)
    depth = 1
    for m in re.finditer(r"<div\b|</div>", html_text[inner_start:]):
        if m.group(0) == "<div":
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                inner_end = inner_start + m.start()
                after_start = inner_end + len("</div>")
                return (html_text[:start],
                        html_text[inner_start:inner_end],
                        html_text[after_start:])
    raise ValueError("Unmatched article-body div")


def video_block(video, base, eager=False):
    learn = "".join(f"<li>{item}</li>" for item in video.get("learn", []))
    learn_col = f'<ul class="video-learn">{learn}</ul>' if learn else ""
    context = video.get("context", "")
    if "{YT_DESCRIPTION}" in context:
        context = context.replace("{YT_DESCRIPTION}", content_video.YT_DESCRIPTION)
    loading = "" if eager else ' loading="lazy"'
    return f"""
<figure class="video-block" id="video">
  {context}
  <div class="video-grid">
    <div class="video-frame">
      <iframe
        src="https://www.youtube-nocookie.com/embed/{YT_ID}"
        title="Embedded YouTube video: {esc(YT_TITLE)}, published by {esc(YT_CHANNEL)}"{loading}
        allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin"
        allowfullscreen></iframe>
    </div>
    {learn_col}
  </div>
  <figcaption class="video-caption">{video.get('caption', '')}</figcaption>
  <p class="video-note">
    <svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path fill="#8395ad" d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20Zm1 15h-2v-6h2v6Zm0-8h-2V7h2v2Z"/></svg>
    <span>Embedded third-party YouTube video. It does not autoplay; press play to load it. YouTube&rsquo;s terms and privacy policy apply once you interact with the player. This site does not own or produce the video.</span>
  </p>
</figure>
"""


def toc_html(items):
    lis = []
    for i, (hid, label) in enumerate(items, 1):
        lis.append(f'<li><a href="#{hid}">{esc(label)}</a></li>')
    return (
        '<nav class="toc" aria-label="On this page">\n'
        f'  <h2>On this page</h2>\n  <ol>\n{"".join(lis)}\n  </ol>\n</nav>'
    )


def faq_html(faqs):
    if not faqs:
        return ""
    items = []
    for q, a in faqs:
        items.append(
            '<details class="faq-item">\n'
            f"  <summary>{esc(q)}</summary>\n"
            f'  <div class="faq-a"><p>{a}</p></div>\n'
            "</details>"
        )
    return (
        '<section id="faq" aria-labelledby="faq-h">\n'
        '  <h2 id="faq-h">Frequently asked questions</h2>\n'
        f'  <div class="faq-list">\n{"".join(items)}\n  </div>\n'
        "</section>"
    )


DISCLAIMER_BLOCK = """
<aside class="disclaimer" aria-label="Final disclaimer">
  <p class="mb-0"><strong>Final disclaimer.</strong> This is an independent educational
  website. It is not affiliated with, endorsed by, or operated by StripChat, and it does
  not offer or guarantee tokens, prizes, or search rankings. Token generators, hacks,
  mod APKs, and similar tools are unsafe and are never recommended. External promotional
  links are sponsored and carry separate terms; review destinations carefully. See the
  full <a href="{base}/disclaimer/">disclaimer</a>,
  <a href="{base}/terms-of-use/">terms of use</a>, and
  <a href="{base}/affiliate-disclosure/">affiliate &amp; external links disclosure</a>.</p>
</aside>
"""

# ---------------------------------------------------------------------------
# Shared chrome --------------------------------------------------------------
# ---------------------------------------------------------------------------

NAV_LINKS = [
    ("/", "Home"),
    ("/legitimate-stripchat-token-methods/", "Legitimate Methods"),
    ("/stripchat-token-scams-and-safety/", "Scams &amp; Safety"),
    ("/stripchat-tokens-video-guide/", "Video Guide"),
]

FOOTER_GUIDES = NAV_LINKS
FOOTER_LEGAL = [
    ("/about/", "About"),
    ("/contact/", "Contact"),
    ("/privacy-policy/", "Privacy Policy"),
    ("/terms-of-use/", "Terms of Use"),
    ("/affiliate-disclosure/", "Affiliate Disclosure"),
    ("/disclaimer/", "Disclaimer"),
]


def head_html(page, slug, base):
    canonical = abs_url(slug)
    og_type = page.get("og_type", "website")
    noindex = bool(page.get("noindex"))
    ld = []

    if slug == "/":
        ld.append({
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": SITE_NAME,
            "url": SITE_URL + "/",
            "description": page["desc"],
            "inLanguage": "en-US",
        })

    is_article = og_type == "article" or slug == "/"
    if is_article:
        article = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": page["title"],
            "description": page["desc"],
            "url": canonical,
            "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
            "inLanguage": "en",
            "datePublished": BUILD_DATE,
            "dateModified": BUILD_DATE,
            "author": {
                "@type": "Organization",
                "name": SITE_NAME + " editorial team",
                "url": SITE_URL + "/",
            },
            "publisher": {
                "@type": "Organization",
                "name": SITE_NAME,
                "url": SITE_URL + "/",
                "logo": {
                    "@type": "ImageObject",
                    "url": SITE_URL + "/assets/img/favicon.svg",
                },
            },
        }
        if slug == "/stripchat-tokens-video-guide/":
            article["image"] = [SITE_URL + "/assets/img/og-image.png"]
        ld.append(article)

    if page.get("faqs"):
        ld.append({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)},
                }
                for q, a in page["faqs"]
            ],
        })

    if slug == "/stripchat-tokens-video-guide/":
        ld.append({
            "@context": "https://schema.org",
            "@type": "VideoObject",
            "name": YT_TITLE,
            "description": content_video.YT_DESCRIPTION,
            "thumbnailUrl": [f"https://i.ytimg.com/vi/{YT_ID}/hqdefault.jpg"],
            "uploadDate": YT_UPLOAD_DATE,
            "duration": YT_DURATION_ISO,
            "embedUrl": f"https://www.youtube-nocookie.com/embed/{YT_ID}",
            "contentUrl": f"https://www.youtube.com/watch?v={YT_ID}",
            "author": {
                "@type": "Person",
                "name": YT_CHANNEL,
                "sameAs": YT_CHANNEL_URL,
            },
        })

    if slug != "/" and not noindex:
        ld.append({
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home",
                 "item": SITE_URL + "/"},
                {"@type": "ListItem", "position": 2, "name": page.get("breadcrumb", page["title"]),
                 "item": canonical},
            ],
        })

    ld_json = "\n".join(
        '<script type="application/ld+json">\n'
        + json.dumps(item, ensure_ascii=False, indent=2)
        + "\n</script>"
        for item in ld
    )

    article_meta = ""
    if og_type == "article":
        article_meta = (
            f'<meta property="article:published_time" content="{BUILD_DATE}">\n'
            f'  <meta property="article:modified_time" content="{BUILD_DATE}">\n'
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="google-site-verification" content="{GSC_TOKEN}">
  <title>{esc(page['title'])}</title>
  <meta name="description" content="{esc(page['desc'])}">
  <meta name="robots" content="{'noindex, follow' if noindex else 'index, follow, max-image-preview:large'}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:locale" content="en_US">
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="{esc(SITE_NAME)}">
  <meta property="og:title" content="{esc(page['title'])}">
  <meta property="og:description" content="{esc(page['desc'])}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE_URL}/assets/img/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Shield emblem for the independent StripChat token safety guide">
  {article_meta}<meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(page['title'])}">
  <meta name="twitter:description" content="{esc(page['desc'])}">
  <meta name="twitter:image" content="{SITE_URL}/assets/img/og-image.png">
  <meta name="twitter:label1" content="Content type">
  <meta name="twitter:data1" content="Independent safety education">
  <link rel="icon" type="image/svg+xml" href="{base}/assets/img/favicon.svg">
  <link rel="icon" type="image/png" sizes="192x192" href="{base}/assets/img/icon-192.png">
  <link rel="apple-touch-icon" href="{base}/assets/img/icon-180.png">
  <link rel="manifest" href="{base}/site.webmanifest">
  <meta name="theme-color" content="#0b111c">
  <link rel="stylesheet" href="{base}/assets/css/style.css">
  {ld_json}
</head>
"""


def header_html(slug, base):
    links = []
    for href, label in NAV_LINKS:
        current = ' aria-current="page"' if href == slug else ""
        links.append(f'<a href="{base}{href}"{current}>{label}</a>')
    return f"""<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container masthead">
    <a class="brand" href="{base}/">
      <img src="{base}/assets/img/favicon.svg" alt="" width="34" height="34">
      <span>StripChat Token Safety Guide<small>Independent educational resource</small></span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav">
      <span class="open" aria-hidden="true">&#9776; Menu</span><span class="close" aria-hidden="true">&#10005; Close</span>
      <span class="visually-hidden">Toggle navigation</span>
    </button>
    <nav class="primary-nav" id="primary-nav" aria-label="Primary">
      {"".join(links)}
    </nav>
  </div>
</header>
<div class="age-notice" id="age-notice" role="note" aria-label="Adult content notice">
  <div class="container">
    <span aria-hidden="true">&#128274;</span>
    <p class="mb-0"><strong>Adults&nbsp;18+ only.</strong> This independent, non-explicit guide discusses an adult-oriented platform. Linked external destinations may require age verification. See the <a href="{base}/disclaimer/">disclaimer</a>.</p>
    <button class="dismiss" type="button" id="age-dismiss" aria-controls="age-notice">Dismiss</button>
  </div>
</div>
"""


def footer_html(base):
    guide_links = "".join(
        f'<li><a href="{base}{href}">{label.replace("&amp;","&")}</a></li>'
        for href, label in FOOTER_GUIDES
    )
    legal_links = "".join(
        f'<li><a href="{base}{href}">{label}</a></li>' for href, label in FOOTER_LEGAL
    )
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">
          <img src="{base}/assets/img/favicon.svg" alt="" width="30" height="30">
          <span>{SITE_NAME}</span>
        </div>
        <p>Independent, non-explicit consumer education about token promotions, giveaways, and online safety. Not affiliated with or endorsed by StripChat. Tokens and prizes are never guaranteed.</p>
      </div>
      <nav aria-label="Guide pages">
        <h2>Guides</h2>
        <ul>{guide_links}</ul>
      </nav>
      <nav aria-label="Legal and editorial pages">
        <h2>About &amp; legal</h2>
        <ul>{legal_links}</ul>
      </nav>
    </div>
    <div class="footer-bottom">
      <span>&copy; {date.today().year} {SITE_NAME}. All rights reserved.</span>
      <a href="{base}/sitemap.xml">Sitemap</a>
      <a href="{base}/privacy-policy/">Privacy</a>
      <span>Trademarks belong to their respective owners.</span>
    </div>
  </div>
</footer>
{sticky_bar_html(base)}
<script src="{base}/assets/js/main.js" defer></script>
</body>
</html>
"""


def sticky_bar_html(base):
    icon_home = (
        '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 3 2 12h3v8h6v-6h2v6h6v-8h3L12 3Z"/></svg>'
    )
    nav = []
    labels = {"/": "Home",
              "/legitimate-stripchat-token-methods/": "Legit methods",
              "/stripchat-token-scams-and-safety/": "Safety",
              "/stripchat-tokens-video-guide/": "Video"}
    for i, (href, _) in enumerate(NAV_LINKS):
        label = labels[href]
        icon = icon_home if i == 0 else ""
        nav.append(f'<a href="{base}{href}">{icon}<span>{label}</span></a>')
    return f"""<div class="sticky-bar">
  <div class="sticky-bar-inner">
    <nav class="sticky-nav" aria-label="Quick links">{"".join(nav)}</nav>
    <div class="sticky-cta-wrap">
      <a class="btn btn-primary btn-sm" href="{OFFER_URL}" target="_blank"
         rel="nofollow sponsored noopener noreferrer">{OFFER_LABEL}</a>
      <span class="sticky-cta-note">External offers may have separate terms, eligibility requirements, and availability. We do not guarantee tokens, prizes, or results. Review each destination carefully before taking action.</span>
    </div>
  </div>
</div>
"""


# ---------------------------------------------------------------------------
# Page assembly --------------------------------------------------------------
# ---------------------------------------------------------------------------

def render_article(mod, slug):
    base = rel_base(slug)
    body = mod.BODY.replace("{YT_DESCRIPTION}", getattr(content_video, "YT_DESCRIPTION", ""))
    body = body.replace("{{BASE}}", base)
    body = body.replace("{{VIDEO}}",
                        video_block(mod.VIDEO, base,
                                    eager=(slug == "/stripchat-tokens-video-guide/")))
    plain = re.sub(r"<[^>]+>", " ", body + " " + " ".join(a for _, a in getattr(mod, "FAQS", [])))
    minutes = max(1, round(len(plain.split()) / 220))
    reading = f"About {minutes} min read"

    faqs = getattr(mod, "FAQS", [])
    page = {
        "title": mod.TITLE,
        "desc": mod.DESCRIPTION,
        "og_type": getattr(mod, "OG_TYPE", "article"),
        "breadcrumb": getattr(mod, "BREADCRUMB", ""),
        "faqs": faqs,
    }

    if slug == "/":
        hero, rest = body.split("<!--SPLIT-->", 1)
        before, inner, after = split_article_body(rest)
        main = f"""
<main id="main">
  <div class="container hero">
    {hero}
  </div>
  <div class="container">
    {before}
  </div>
  <div class="container layout">
    {toc_html(mod.TOC)}
    <div class="layout-main">
      {inner}
      {after}
      {faq_html(faqs)}
      {DISCLAIMER_BLOCK.format(base=base)}
    </div>
  </div>
</main>
"""
    else:
        before, inner, after = split_article_body(body)
        crumb = page["breadcrumb"]
        breadcrumbs = f"""<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>
      <li><a href="{base}/">Home</a></li>
      <li><span aria-current="page">{esc(crumb)}</span></li>
    </ol></nav>"""
        h1 = H1[slug]
        meta = (
            '<div class="article-meta">'
            '<span class="badge"><span class="dot"></span>Independent safety guide</span>'
            f'<span class="badge">Last reviewed: {BUILD_DATE}</span>'
            f'<span class="badge">{reading}</span>'
            "</div>"
        )
        main = f"""
<main id="main">
  <div class="container page-intro">
    {breadcrumbs}
    <h1>{esc(h1)}</h1>
    {meta}
  </div>
  <div class="container article-intro">
    {before}
  </div>
  <div class="container layout">
    {toc_html(mod.TOC)}
    <div class="layout-main">
      {inner}
      {after}
      {faq_html(faqs)}
      {DISCLAIMER_BLOCK.format(base=base)}
    </div>
  </div>
</main>
"""
    return head_html(page, slug, base) + header_html(slug, base) + main + footer_html(base)


def render_legal(p):
    slug = p["slug"]
    base = rel_base(slug)
    vid = dict(content_legal.COMPACT_VIDEO)
    vid["context"] = p.get("video_context", vid["context"])
    body = p["body"].replace("{{BASE}}", base).replace("{{VIDEO}}", video_block(vid, base))
    page = {"title": p["title"], "desc": p["desc"], "og_type": "website",
            "breadcrumb": p["breadcrumb"], "faqs": []}
    breadcrumbs = f"""<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>
      <li><a href="{base}/">Home</a></li>
      <li><span aria-current="page">{esc(p['breadcrumb'])}</span></li>
    </ol></nav>"""
    main = f"""
<main id="main">
  <div class="container page-intro legal-body">
    {breadcrumbs}
    {body}
    {DISCLAIMER_BLOCK.format(base=base)}
  </div>
</main>
"""
    return head_html(page, slug, base) + header_html(slug, base) + main + footer_html(base)


# ---------------------------------------------------------------------------
# Root files -----------------------------------------------------------------
# ---------------------------------------------------------------------------

def write_404():
    base = SITE_BASE_PATH  # absolute project path so links work at any URL depth
    page = {
        "title": "404: Page Not Found \u2014 StripChat Token Safety Guide",
        "desc": "The requested page could not be found. Use the guides to learn about legitimate StripChat token methods and online safety.",
        "og_type": "website", "breadcrumb": "404", "faqs": [], "noindex": True,
    }
    vid = dict(content_legal.COMPACT_VIDEO)
    vid["context"] = (
        "<p>While you are here, the short <strong>embedded YouTube video</strong> below "
        "recaps how to evaluate free-token claims safely. It does not autoplay.</p>"
    )
    main = f"""
<main id="main">
  <div class="container error-page">
    <div>
      <p class="error-code">404</p>
      <h1>Page not found</h1>
      <p class="lede">The page you were looking for does not exist or may have moved. It is also a good moment to remember: there are no legitimate token generators, and free-token links from unknown sites should be treated with caution.</p>
      {video_block(vid, base)}
      <p><a class="btn btn-primary" href="{base}/">Back to the homepage guide</a></p>
      <p class="small muted">Or visit:
        <a href="{base}/legitimate-stripchat-token-methods/">legitimate methods</a> &middot;
        <a href="{base}/stripchat-token-scams-and-safety/">scams and safety</a> &middot;
        <a href="{base}/stripchat-tokens-video-guide/">video guide</a>
      </p>
    </div>
  </div>
</main>
"""
    (ROOT / "404.html").write_text(
        head_html(page, "/404.html", base) + header_html("/404.html", base) +
        main + footer_html(base), encoding="utf-8")


def write_robots():
    txt = (
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {SITE_URL}/sitemap.xml\n"
    )
    (ROOT / "robots.txt").write_text(txt, encoding="utf-8")


def write_sitemap(slugs):
    entries = []
    for s in slugs:
        priority = "1.0" if s == "/" else "0.7"
        entries.append(
            "  <url>\n"
            f"    <loc>{abs_url(s)}</loc>\n"
            f"    <lastmod>{BUILD_DATE}</lastmod>\n"
            "    <changefreq>monthly</changefreq>\n"
            f"    <priority>{priority}</priority>\n"
            "  </url>"
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(entries)
        + "\n</urlset>\n"
    )
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")


def write_manifest():
    manifest = {
        "name": SITE_NAME,
        "short_name": "Token Safety",
        "description": "Independent guide to legitimate StripChat token methods and online safety.",
        "start_url": SITE_BASE_PATH + "/",
        "scope": SITE_BASE_PATH + "/",
        "display": "standalone",
        "background_color": "#0b111c",
        "theme_color": "#0b111c",
        "icons": [
            {"src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml"},
            {"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"},
        ],
    }
    (ROOT / "site.webmanifest").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def write_nojekyll():
    (ROOT / ".nojekyll").write_text(
        "This file tells GitHub Pages to publish the repository contents as-is\n"
        "(plain static HTML/CSS/JS, no Jekyll processing).\n",
        encoding="utf-8")


# ---------------------------------------------------------------------------
# Main -----------------------------------------------------------------------
# ---------------------------------------------------------------------------

def main():
    articles = [
        ("/", content_home),
        ("/legitimate-stripchat-token-methods/", content_methods),
        ("/stripchat-token-scams-and-safety/", content_safety),
        ("/stripchat-tokens-video-guide/", content_video),
    ]
    slugs = []
    for slug, mod in articles:
        out = render_article(mod, slug)
        target = ROOT / ("index.html" if slug == "/" else slug.strip("/") + "/index.html")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(out, encoding="utf-8")
        slugs.append(slug)
        print(f"built {target.relative_to(ROOT)}  ({len(out):,} bytes)")

    for p in content_legal.PAGES:
        out = render_legal(p)
        target = ROOT / (p["slug"].strip("/") + "/index.html")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(out, encoding="utf-8")
        slugs.append(p["slug"])
        print(f"built {target.relative_to(ROOT)}  ({len(out):,} bytes)")

    write_404()
    write_robots()
    write_sitemap(slugs)
    write_manifest()
    write_nojekyll()
    print("built 404.html, robots.txt, sitemap.xml, site.webmanifest, .nojekyll")
    print(f"SITE_URL={SITE_URL}  GSC_TOKEN={GSC_TOKEN}")


if __name__ == "__main__":
    main()
