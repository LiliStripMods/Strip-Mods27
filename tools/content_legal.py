# -*- coding: utf-8 -*-
"""Legal and editorial pages (About, Contact, Privacy, Terms, Disclosure, Disclaimer)."""

COMPACT_VIDEO = {
    "context": (
        "<p>This companion <strong>embedded YouTube video</strong> appears across the "
        "guide and summarizes the core safety advice. It is hosted on YouTube by an "
        "independent publisher and does not autoplay.</p>"
    ),
    "caption": (
        "<strong>Embedded YouTube video:</strong> \u201cStripchat Hack 2026\u20132027? "
        "Free Token Claims Explained (UPDATED!!)\u201d by the YouTube channel "
        "<strong>thenewyorkjets28</strong>."
    ),
    "learn": [
        "Why generator and hack claims cannot be trusted",
        "What to verify before joining a token drawing",
        "How to protect your account credentials",
    ],
}

LEGAL_VIDEO_CONTEXT = (
    "<p>For context, the short <strong>embedded YouTube video</strong> the guide is "
    "built around is included here as well. It summarizes why token-generator claims are "
    "unsafe and what to verify before trusting an offer. It is hosted on YouTube by an "
    "independent publisher and does not autoplay.</p>"
)

PAGES = []

PAGES.append({
    "slug": "/about/",
    "title": "About This Guide: Mission, Standards, and Independence",
    "desc": "Who publishes this independent StripChat token safety guide, how it is researched, its editorial standards, and why it contains no hacks, generators, or guaranteed offers.",
    "breadcrumb": "About",
    "video_context": LEGAL_VIDEO_CONTEXT,
    "body": r"""
<h1>About This Guide</h1>
<p class="lede">This website exists to answer a simple search honestly: are there legitimate ways to find <strong>StripChat free tokens</strong>, and how do you avoid the scams that cluster around that question?</p>
{{VIDEO}}
<div class="legal-body">
<h2>Our mission</h2>
<p>Free-token searches lead users through a dense field of fake generators, phishing pages, sideloaded &ldquo;mod&rdquo; apps, survey funnels, and a smaller number of genuine promotional offers. The goal of this guide is to separate those categories in plain English: explain how token balances actually work, describe the limited ways promotional credits can legitimately appear, and document how each scam pattern operates so it can be recognized and avoided.</p>
<h2>What you will not find here</h2>
<ul>
  <li>No token generators, &ldquo;adders,&rdquo; hacks, cracks, or modified applications, and no instructions for using them;</li>
  <li>No claims of unlimited, guaranteed, instant, or &ldquo;100% working&rdquo; tokens;</li>
  <li>No fabricated testimonials, reviews, statistics, search-volume figures, or author credentials;</li>
  <li>No countdown timers, fake scarcity, forced redirects, automatic downloads, or aggressive pop-ups;</li>
  <li>No claim of official affiliation with, endorsement by, or operation by StripChat.</li>
</ul>
<h2>Editorial standards</h2>
<p>Articles are written for readers rather than search engines: each page opens with a direct answer, uses a clear heading structure, and links to genuinely relevant further reading. Keywords such as &ldquo;StripChat mod APK&rdquo; or &ldquo;StripChat hack&rdquo; appear only as safety topics, never as recommendations. We do not manipulate search rankings, publish doorway pages, use spun content, or buy links, and we make no ranking promises of any kind.</p>
<h2>Independence and commercial relationships</h2>
<p>This is an independent educational resource. Some links to external promotional websites are sponsored (marked with <code>rel=&quot;nofollow sponsored&quot;</code> and a visible notice). Those relationships never convert an unverified third-party site into an &ldquo;official&rdquo; or &ldquo;legal&rdquo; source, and the safety guidance is written to apply equally to every destination, including the ones linked here. Details are on the <a href="{{BASE}}/affiliate-disclosure/">affiliate disclosure page</a>.</p>
<h2>Adult-content notice</h2>
<p>The guide discusses an adult-oriented platform. It contains no explicit imagery and is written as consumer-protection information, but readers should be adults (18+, or the age of majority in their jurisdiction) and should expect destinations linked from this guide to require age verification.</p>
<h2>Corrections</h2>
<p>If a page contains an error, an outdated statement, or a link that should be revisited, please tell us through the <a href="{{BASE}}/contact/">contact page</a>. Factual corrections take priority over any commercial consideration.</p>
<div class="placeholder-line">Placeholder: this guide does not invent an organization, company registration, physical address, or named author. Add verified operator details here only if and when they exist.</div>
</div>
""",
})

PAGES.append({
    "slug": "/contact/",
    "title": "Contact: Report a Broken Link, Correction, or Suspicious Offer",
    "desc": "How to contact the editors of the StripChat token safety guide about corrections, broken links, accessibility issues, or reports of suspicious token offers.",
    "breadcrumb": "Contact",
    "video_context": LEGAL_VIDEO_CONTEXT,
    "body": r"""
<h1>Contact</h1>
<p class="lede">Corrections, broken-link reports, and tips about new token-scam variants are welcome. This is a static website, so messages are handled by email rather than an online database.</p>
{{VIDEO}}
<div class="legal-body">
<h2>What to include</h2>
<ul>
  <li><strong>Corrections:</strong> the page URL and the statement that appears inaccurate, with a source if you have one;</li>
  <li><strong>Broken or suspicious links:</strong> the link text, its destination, and what you observed;</li>
  <li><strong>New scam patterns:</strong> the URL or screenshot text of any generator, phishing page, fake extension, or mod APK, so the guides can be updated;</li>
  <li><strong>Accessibility issues:</strong> the page, device, browser, and the barrier you encountered.</li>
</ul>
<div class="placeholder-line">
<strong>Contact email (placeholder):</strong> replace
<code>REPLACE-WITH-YOUR-EMAIL@example.com</code> with a monitored mailbox before publishing.
Until replaced, this form cannot deliver messages.
</div>
<h2>Message form</h2>
<p class="form-note">Static sites cannot process server-side forms. The button below opens your email client with the message pre-filled; if JavaScript is disabled, copy the placeholder address above into your email client manually.</p>
<form class="contact-form" id="contact-form" data-to="REPLACE-WITH-YOUR-EMAIL@example.com">
  <div>
    <label for="cf-name">Your name (optional)
      <input id="cf-name" name="name" type="text" autocomplete="name" placeholder="You may remain anonymous">
    </label>
  </div>
  <div>
    <label for="cf-email">Your email (optional, for a reply)
      <input id="cf-email" name="email" type="email" autocomplete="email" placeholder="you@example.com">
    </label>
  </div>
  <div>
    <label for="cf-topic">Topic
      <select id="cf-topic" name="topic">
        <option>Correction or factual issue</option>
        <option>Broken link</option>
        <option>Report a suspicious token offer</option>
        <option>Accessibility issue</option>
        <option>Other</option>
      </select>
    </label>
  </div>
  <div>
    <label for="cf-message">Message
      <textarea id="cf-message" name="message" rows="6" required placeholder="Paste the page URL and describe the issue. Do not include passwords or payment details."></textarea>
    </label>
  </div>
  <button type="submit" class="btn btn-primary">Open in email client</button>
  <p class="form-note">Do not send passwords, two-factor codes, payment details, or screenshots containing them. This inbox is not a support channel for any adult platform; for account problems use that platform&rsquo;s official support.</p>
</form>
<h2>Reporting scams directly</h2>
<p>If your message is about an active phishing page or malicious app, also report it through the official channels listed on the <a href="{{BASE}}/stripchat-token-scams-and-safety/#reporting">reporting section of the safety guide</a>, where takedowns happen fastest.</p>
</div>
""",
})

PAGES.append({
    "slug": "/privacy-policy/",
    "title": "Privacy Policy: Cookies, Embeds, and Local Storage",
    "desc": "What this static website collects, how the YouTube privacy-enhanced embed works, the single local-storage preference used here, and how sponsored external links handle your data.",
    "breadcrumb": "Privacy Policy",
    "video_context": LEGAL_VIDEO_CONTEXT,
    "body": r"""
<h1>Privacy Policy</h1>
<p class="lede">This is a static website with no accounts, no server-side tracking, and no advertising network. This policy explains the limited processing that does occur.</p>
{{VIDEO}}
<div class="legal-body">
<h2>The basics</h2>
<ul>
  <li>The site serves static HTML, CSS, JavaScript, and image files;</li>
  <li>There is no login, comment system, shopping cart, or contact database;</li>
  <li>We do not sell personal data, and we place no analytics or advertising cookies of our own.</li>
</ul>
<h2>Embedded YouTube videos</h2>
<p>Videos are embedded with YouTube&rsquo;s privacy-enhanced domain, <code>www.youtube-nocookie.com</code>, and never autoplay. According to YouTube&rsquo;s documentation for this mode, YouTube does not use the embed to serve personalized advertising, but YouTube may still receive connection information (such as your IP address and the page visited) when the page loads, and may set cookies and collect viewing data once you click play. That processing is controlled by Google/YouTube under its privacy policy and terms, not by this site. If you prefer to avoid it, use the provided link to watch on YouTube only if you accept that, or do not press play.</p>
<h2>Local storage preference</h2>
<p>If you dismiss the age/content notice, the site stores a single preference in your browser&rsquo;s local storage so the notice stays dismissed. It contains no personal data, is never transmitted, and can be removed at any time by clearing site data in your browser.</p>
<h2>The contact form</h2>
<p>The contact form creates an email in your own email client; nothing is submitted to this website&rsquo;s server. Do not include sensitive credentials or financial information in messages. Once an email is sent, its handling depends on the configured mailbox (replace the placeholder address before deployment).</p>
<h2>External links</h2>
<p>Sponsored buttons link to independent third-party websites with <code>rel=&quot;nofollow sponsored noopener noreferrer&quot;</code> and open in a new tab. Once you leave this domain, the destination&rsquo;s own privacy policy and terms apply; we do not control and cannot verify their data practices. Review their policies before entering information.</p>
<h2>Hosting</h2>
<p>The site is designed for hosting on GitHub Pages. GitHub may collect standard server logs and connection data under its own privacy statement. This site does not add third-party trackers on top of the host.</p>
<h2>Your rights</h2>
<p>Because this site collects no personal data itself, there is no profile to access, correct, export, or delete. If you sent an email and want it deleted, contact the mailbox operator using the details on the <a href="{{BASE}}/contact/">contact page</a>.</p>
<h2>Changes</h2>
<p>Material changes to this policy will be reflected by updating the revision date at the bottom of the page.</p>
<div class="placeholder-line">Placeholder: add the operator identity and a legal contact email required by your jurisdiction before relying on this policy.</div>
</div>
""",
})

PAGES.append({
    "slug": "/terms-of-use/",
    "title": "Terms of Use",
    "desc": "The terms for using this independent informational website about StripChat token methods and safety, including acceptable use, third-party links, and limitation of liability.",
    "breadcrumb": "Terms of Use",
    "video_context": LEGAL_VIDEO_CONTEXT,
    "body": r"""
<h1>Terms of Use</h1>
<p class="lede">By using this website you accept these terms. If you do not accept them, please do not use the site.</p>
{{VIDEO}}
<div class="legal-body">
<h2>Informational use only</h2>
<p>All content is provided for general consumer information and safety education. It concerns an adult-oriented platform and is intended for adults. Nothing on this site constitutes legal, financial, tax, or professional advice, and nothing creates an agency, partnership, or endorsement relationship.</p>
<h2>No offers or guarantees</h2>
<p>The site describes how token promotions may work and links to third-party destinations that may run offers. It does not itself offer tokens, prizes, drawings, or subscriptions, and it does not guarantee that any third-party offer is available, legitimate, accurate, or safe. Any promotion is governed solely by the terms on the destination website.</p>
<h2>Prohibited use</h2>
<ul>
  <li>Do not use the site to develop, distribute, or promote token generators, hacks, phishing pages, malware, or modified applications;</li>
  <li>Do not attempt to disrupt, scrape abusively, probe, or gain unauthorized access to the site or its host;</li>
  <li>Do not misrepresent the site&rsquo;s independence or present its content as official platform communication;</li>
  <li>Do not use the site where doing so would violate laws applicable to you, including age requirements.</li>
</ul>
<h2>Third-party links and embeds</h2>
<p>Pages contain embedded YouTube content and links to independent websites, some of which are sponsored. These are provided for convenience and discussion only; inclusion is not verification, approval, or a safety guarantee. Third-party sites and embedded players operate under their own terms and policies.</p>
<h2>Trademarks</h2>
<p>&ldquo;StripChat&rdquo; and related names, logos, and terms are trademarks or registered trademarks of their respective owners. Reference to them is descriptive and does not imply affiliation, sponsorship, or endorsement. This website is independent.</p>
<h2>Accuracy</h2>
<p>Promotions and third-party offers change frequently. While content is written carefully, the site cannot guarantee completeness or currency at all times. Verify every offer against the official platform and the destination&rsquo;s current terms.</p>
<h2>Limitation of liability</h2>
<p>To the fullest extent permitted by applicable law, the site and its operators are not liable for any loss arising from use of the site, reliance on its content, interactions with third-party destinations, installed software from external sources, or decisions based on promotional claims. Use the information and external resources at your own informed risk.</p>
<h2>Changes</h2>
<p>These terms may be updated; continued use after an update constitutes acceptance of the revised terms.</p>
<div class="placeholder-line">Placeholder: insert governing-law and jurisdiction clauses appropriate to the operator&rsquo;s verified location before relying on these terms.</div>
</div>
""",
})

PAGES.append({
    "slug": "/affiliate-disclosure/",
    "title": "Affiliate and External Links Disclosure",
    "desc": "How sponsored and affiliate links to external token-offer websites are used on this guide, including rel attributes, third-party destinations, and the absence of guarantees.",
    "breadcrumb": "Affiliate Disclosure",
    "video_context": LEGAL_VIDEO_CONTEXT,
    "body": r"""
<h1>Affiliate &amp; External Links Disclosure</h1>
<p class="lede">Transparency first: some outbound buttons on this website are promotional links to independent third parties, and the site may receive a referral fee if you visit or sign up through them.</p>
{{VIDEO}}
<div class="legal-body">
<h2>Which links are promotional</h2>
<p>The call-to-action labeled <strong>&ldquo;Check the 50 TK Draw Offer&rdquo;</strong> &mdash; pinned to the bottom of every page &mdash; and equivalent buttons in the articles link to external promotional destinations, including:</p>
<ul>
  <li><code>https://striptks.live/</code></li>
  <li><code>https://stripfreetokens.com/</code></li>
  <li><code>http://striptokens.live/</code> (provided without HTTPS; exercise particular caution)</li>
</ul>
<h2>How the links are marked</h2>
<p>Promotional links open in a new tab and include <code>rel=&quot;nofollow sponsored noopener noreferrer&quot;</code>. They are accompanied in context by a visible notice stating that external offers carry their own terms and eligibility rules, and that tokens, prizes, and results are not guaranteed.</p>
<h2>What these links do not mean</h2>
<ul>
  <li>They do <strong>not</strong> mean the destination is official, operated by, or affiliated with StripChat;</li>
  <li>They do <strong>not</strong> mean the site has been audited, certified, or found &ldquo;legal&rdquo; or safe &mdash; we use neutral terms like &ldquo;external resource&rdquo; because legal status has not been independently verified;</li>
  <li>They do <strong>not</strong> constitute a promise or guarantee of tokens, a 50&nbsp;TK draw prize, or any other outcome;</li>
  <li>They do <strong>not</strong> change the safety guidance: never provide passwords, verification codes, payment details, fees, or app installs to claim a &ldquo;free&rdquo; reward.</li>
</ul>
<h2>How editorial decisions work</h2>
<p>Safety information is written independently of commercial relationships. Every external offer &mdash; including the sponsored destinations &mdash; is evaluated under the same verification framework described in the <a href="{{BASE}}/legitimate-stripchat-token-methods/">legitimate methods guide</a>. We do not accept payment to describe a generator, hack, or mod as safe, and we do not publish fake reviews or ratings.</p>
<h2>Non-commercial authority links</h2>
<p>A small number of outbound links go to genuinely relevant official resources &mdash; for example Google Safe Browsing, the U.S. Federal Trade Commission, and the FBI&rsquo;s IC3 &mdash; solely because they support a specific statement. These are not affiliate links and earn nothing.</p>
<h2>Your choice</h2>
<p>You are never required to click a sponsored link. The educational content is complete without it, and you can verify any promotion directly through your official platform account. If you do visit an external destination, its own terms, privacy policy, and eligibility rules apply.</p>
<h2>Questions</h2>
<p>Questions about this disclosure can be sent via the <a href="{{BASE}}/contact/">contact page</a>.</p>
</div>
""",
})

PAGES.append({
    "slug": "/disclaimer/",
    "title": "Disclaimer: Independent Guide, No Affiliation, and Adult Content",
    "desc": "General disclaimer for the StripChat token safety guide: independent status, no affiliation with StripChat, third-party video and links, adult-content notice, and no guarantees.",
    "breadcrumb": "Disclaimer",
    "video_context": LEGAL_VIDEO_CONTEXT,
    "body": r"""
<h1>Disclaimer</h1>
<p class="lede">Please read this notice alongside the <a href="{{BASE}}/terms-of-use/">Terms of Use</a> and <a href="{{BASE}}/privacy-policy/">Privacy Policy</a>.</p>
{{VIDEO}}
<div class="legal-body">
<h2>Independence and trademarks</h2>
<p>This website is an <strong>independent educational resource</strong>. It is not affiliated with, endorsed by, sponsored by, or operated by StripChat or any related platform, nor by the publisher of the embedded YouTube video. All trademarks, service marks, and brand names are the property of their respective owners and are used descriptively.</p>
<h2>No guarantee of tokens or results</h2>
<p>The site discusses promotional credits, giveaways, drawings (including offers described as a &ldquo;50&nbsp;TK draw&rdquo;), referrals, and third-party promotions for informational purposes. It does not promise, and you should not expect, any specific amount of tokens, any prize, any hourly reward, or any result. Promotions have eligibility rules, deadlines, and limits set entirely by the platform or third party operating them, and may be discontinued at any time.</p>
<h2>Safety and legality</h2>
<p>The site does not provide instructions for hacking, credential theft, token generators, cracked or modified applications, account bypasses, or unauthorized modifications. Topics such as &ldquo;StripChat mod APK,&rdquo; &ldquo;StripChat hack,&rdquo; or &ldquo;StripChat mods&rdquo; are addressed only as warnings. You are responsible for complying with the laws and terms that apply to you, including the platform&rsquo;s terms of service.</p>
<h2>Embedded video belongs to its publisher</h2>
<p>The embedded YouTube video &mdash; &ldquo;Stripchat Hack 2026&ndash;2027? Free Token Claims Explained (UPDATED!!)&rdquo; by the channel <strong>thenewyorkjets28</strong> &mdash; is the property of its respective publisher and is embedded via YouTube&rsquo;s standard, privacy-enhanced embed. This website does not own, host on its own servers, sell, or claim authorship of the video. Statements made in the video are the publisher&rsquo;s and are not verified as promises.</p>
<h2>Third-party websites</h2>
<p>External destinations are not under this site&rsquo;s control. We do not warrant their availability, legality, safety, accuracy, or content, and we are not responsible for any loss from using them. A link or embed is not an endorsement. Review every destination&rsquo;s terms and privacy practices yourself.</p>
<h2>Adult-content notice</h2>
<p>The underlying platform is intended for adults only. This guide contains no explicit material, but it is written for readers aged 18 or older (or the age of majority where higher). Linked external platforms may require age verification and contain adult content.</p>
<h2>No professional advice</h2>
<p>Nothing here is legal, financial, tax, security-licensing, or other professional advice. Where appropriate, consult a qualified professional or the relevant official authority. Official consumer-protection and cybersecurity resources are linked from the <a href="{{BASE}}/stripchat-token-scams-and-safety/">safety guide</a>.</p>
<h2>Use at your own informed risk</h2>
<p>Information is provided &ldquo;as is,&rdquo; without warranties of any kind. Decisions based on it &mdash; including participation in any promotion or visit to any third-party site &mdash; are your responsibility.</p>
</div>
""",
})
