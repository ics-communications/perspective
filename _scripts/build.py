#!/usr/bin/env python3
"""Build the Perspective site.

Writes index.html (the current edition itself, then its most recent past issues),
archive/ (every past issue), subscribe/, option-a/ (the earlier home page: the
edition's cover spread, then the archive, kept for comparison) and option-b/
(a redirect to the home page, where option B now lives),
and puts the ICS masthead and footer around the current edition in place.

    python3 _scripts/build.py

Past issues come from assets/data/issues.json, made from the ICS Institutional
Repository (https://ir.icscanada.edu/handle/10756/271894); each cover is page 1
of that issue's PDF. To add an issue, add its record and cover and rebuild.
When a new edition ships, point CURRENT at it.
"""
import html
import json
import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
E = html.escape

# The edition on the front door. Contents and authors are the edition's own.
CURRENT = {
    "dir": "fall-2026",
    "label": "Fall 2026",
    "volume": 60,
    "number": 1,
    "slug": "2026-v60-n1",
    "cover": "assets/covers/2026-v60-n1.webp",
    "photo": "assets/img/fall-2026-fern.webp",
    "theme": "imagination",
    "lede": ("Faced with ecological devastation, the expanding influence of artificial intelligence, "
             "and uncertainty about our common future, we can struggle to envision possibilities beyond "
             "the arrangements we already know. How might imagination, then, help us recover the capacity to act?"),
    "lede_by": "Héctor Acero Ferrer, from his introduction to the issue",
    "contents": [
        ("about", "About this issue: What might yet be", "Héctor Acero Ferrer", "head-acero-ferrer.jpg", 2),
        ("pedagogy", "Imagination &amp; Pedagogy", "Beth Green", "head-green.jpg", 4),
        ("philosophy", "Imagination in the History of Philosophy and in Our Ordinary Living", "Bob Sweetman", "head-sweetman.jpg", 9),
        ("political", "Feminism, Faith, and Political Imagination", "Nuzhat Khurshid", "dot", 12),
        ("kingdom", "Imagining the Kingdom", "Jacob Benjamins", "head-benjamins.jpg", 15),
        ("wonder", "Finding Wonder on the Side Streets of Biblical Narrative", "David Grills", "head-grills.jpg", 18),
        ("orvieto", "ART in Orvieto, and the masthead", None, None, 20),
    ],
}

IR = "https://ir.icscanada.edu/handle/10756/271894"
DONATE = "https://donate.icscanada.edu/"
GFORM = "https://docs.google.com/forms/d/e/1FAIpQLSfa_T1csOUSmCK0TBnZYBNx5CJUCDxDHd0ev9GXx_qG5LKweA"

ARROW = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'


def load_issues():
    issues = json.loads((ROOT / "assets/data/issues.json").read_text())
    for i in issues:
        i["online"] = False
    issues.append({
        "slug": CURRENT["slug"], "volume": CURRENT["volume"], "number": CURRENT["number"],
        "label": CURRENT["label"], "year": 2026, "issued": "2026-10", "cover": CURRENT["cover"],
        "w": 440, "h": 569, "pdf": CURRENT["dir"] + "/", "pdf_kb": 0, "online": True,
    })
    return issues


def ledger_tree(issues):
    """Decades, newest first; volumes in each, newest first; issues in order."""
    decades = OrderedDict()
    for i in sorted(issues, key=lambda x: (x["volume"], x["issued"], x["number"]), reverse=True):
        d = i["year"] // 10 * 10
        decades.setdefault(d, OrderedDict()).setdefault(i["volume"], []).append(i)
    for vols in decades.values():
        for v in vols:
            vols[v].sort(key=lambda x: (x["issued"], x["number"]))
    return decades


# ── chrome ──────────────────────────────────────────────────────────────

def head(title, desc, p, extra="", robots=""):
    return f"""<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta name="theme-color" content="#000000">
<link rel="icon" type="image/png" href="{p}assets/img/ics-favicon.png">
<link rel="preload" href="{p}assets/fonts/Newsreader-Roman-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}assets/fonts/fonts.css">
<link rel="stylesheet" href="{p}assets/site.css">
<link rel="stylesheet" href="{p}assets/chrome.css">
<script src="{p}assets/js/site.js" defer></script>
{extra}</head>
"""


def nav_items(p):
    """(key, label, href). `p` is the path back to the site root from this page."""
    return [
        ("current", f'{CURRENT["label"]} issue', p or "./"),
        ("archive", "Archive", p + "archive/"),
        ("subscribe", "Subscribe", p + "subscribe/"),
        ("donate", "Donate", DONATE),
    ]


def masthead(p, active):
    items = nav_items(p)
    desk, mob = [], []
    for key, label, href in items:
        on = key == active
        cur = ' aria-current="page"' if on else ""
        btn = " ics-nav__link--donate" if key == "donate" else ""
        desk.append(f'        <li class="ics-nav__item{" ics-nav__item--active" if on else ""}">\n'
                    f'          <a class="ics-nav__link{btn}" href="{href}"{cur}>{label}</a>\n        </li>')
        mob.append(f'  <a class="ics-mobile-menu__link{" ics-mobile-menu__link--current" if on else ""}{" ics-mobile-menu__link--donate" if btn else ""}" href="{href}"{cur}>{label}</a>')
    return f"""<header class="ics-header">
  <div class="ics-header__inner">
    <a class="ics-header__logo-link" href="https://www.icscanada.edu/">
      <img class="ics-header__logo-img" src="{p}assets/img/ics-logo-white-red.png"
           alt="Institute for Christian Studies" width="900" height="160">
    </a>

    <nav aria-label="Main navigation">
      <ul class="ics-nav">
{chr(10).join(desk)}
      </ul>
    </nav>

    <button class="ics-burger" aria-label="Open menu" type="button">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<div class="ics-mobile-menu" id="mobileMenu">
  <button class="ics-mobile-menu__close" aria-label="Close menu" type="button">&times;</button>
{chr(10).join(mob)}
</div>
"""


def footer(p):
    # The ICS footer, injected by a verbatim copy of ics-site/js/footer.js
    return f'<script src="{p}assets/js/footer.js"></script>\n'


# ── sections ────────────────────────────────────────────────────────────

def edition_logo():
    """The ICS mark from the edition's cover, so the home page cover uses the same drawing."""
    src = (ROOT / CURRENT["dir"] / "index.html").read_text()
    m = re.search(r'<svg class="logo".*?</svg>', src, re.S)
    return re.sub(r' role="img" aria-label="[^"]*"', ' aria-hidden="true"', m.group(0))


def feature(p):
    """The edition's cover spread: its cover on the left, its contents on the right,
    in the edition's own type and spacing (fall-2026/index.html, header.cover)."""
    c = CURRENT
    rows = []
    for anchor, title, by, img, pg in c["contents"]:
        if img == "dot":
            face = '<span class="dot" aria-hidden="true"></span>'
        elif img:
            face = f'<img src="{p}{c["dir"]}/img/{img}" alt="" width="271" height="271" loading="lazy">'
        else:
            face = '<span class="dot ghost" aria-hidden="true"></span>'
        byline = f'<span class="by">{by}</span>' if by else ""
        rows.append(f'<li><a href="{p}{c["dir"]}/#{anchor}">{face}<span class="t"><span class="tt">{title}</span>{byline}</span>'
                    f'<span class="pg">p.&nbsp;{pg}</span></a></li>')
    return f"""<section class="feature" aria-labelledby="feature-t">
  <a class="feature__face" href="{p}{c["dir"]}/" tabindex="-1" aria-hidden="true">
    <img src="{p}{c["photo"]}" alt="" width="1000" height="1508" fetchpriority="high">
    <span class="mastblock">
      <span>Institute for<br>Christian Studies</span>
      <span>{c["label"]}<br>Volume {c["volume"]}&nbsp;&nbsp;•&nbsp;&nbsp;Number {c["number"]}</span>
      <span>Read <em>Perspective</em> online:<br>icscanada.edu/perspective</span>
    </span>
    <span class="feature__pin">
      <span class="wordmark"><span>PER</span><span>SPEC</span><span>TIVE</span></span>
      {edition_logo()}
    </span>
  </a>
  <div class="feature__text">
    <h1 id="feature-t"><span class="vh">Perspective, </span>{c["label"]}: essays on {c["theme"]}</h1>
    <p class="feature__issue">Volume {c["volume"]}, Number {c["number"]} · The magazine of the Institute for Christian Studies</p>
    <ol class="toc" aria-label="In this issue">
{chr(10).join(rows)}
    </ol>
    <p class="feature__note">Page numbers refer to the print edition.</p>
    <div class="feature__acts">
      <a class="btn" href="{p}{c["dir"]}/">Read the {c["label"]} issue {ARROW}</a>
      <a class="btn btn--line" href="{p}subscribe/">Get it in print</a>
    </div>
  </div>
</section>
<section class="intro" aria-label="From the introduction">
  <div class="wrap">
    <blockquote class="intro__q">
      <p>{c["lede"]}</p>
      <cite>{c["lede_by"]}</cite>
    </blockquote>
    <a class="intro__more" href="{p}{c["dir"]}/#about">Read the introduction {ARROW}</a>
  </div>
</section>
"""


def issue_tile(i, p):
    vh = f'Perspective volume {i["volume"]}, '
    if i["online"]:
        href, tail, note = p + i["pdf"], "", "Read online"
    else:
        mb = i["pdf_kb"] / 1024
        size = f"{mb:.1f} MB" if mb >= 1 else f'{i["pdf_kb"]} KB'
        # Most PDFs open from the Repository; one not yet there is hosted with the site
        pdf = i["pdf"] if i["pdf"].startswith("http") else p + i["pdf"]
        href, tail, note = pdf, f" (PDF, {size})", i["label"]
    cls = "issue issue--online" if i["online"] else "issue"
    return (f'<li><a class="{cls}" data-slug="{i["slug"]}" href="{href}">'
            f'<span class="issue__cover"><img src="{p}{i["cover"]}" alt="" width="{i["w"]}" height="{i["h"]}" loading="lazy" decoding="async"></span>'
            f'<span class="issue__meta"><span class="vh">{vh}</span><b>No. {i["number"]}</b> '
            f'<i>{E(note)}</i><span class="vh">{tail}</span></span></a></li>')


def gap_row(v, tag):
    # A volume the Repository doesn't have yet: marked, never filled with invented issues
    return (f'    <div class="vol vol--gap" id="v{v}">\n'
            f'      <{tag} class="vol__t"><span class="v">Vol.</span><span class="n">{v}</span></{tag}>\n'
            f'      <p>Not yet in the ICS Institutional Repository.</p>\n    </div>')


def ledger(issues, p, heading_tag="h2", head_id="archive-t"):
    issues = [i for i in issues if not i["online"]]
    tree = ledger_tree(issues)
    have = {i["volume"] for i in issues}
    gaps = {v for v in range(min(have), max(have)) if v not in have}
    dt, vt = ("h2", "h3") if heading_tag == "h1" else ("h3", "h4")
    in_ir = [i for i in issues if not i["online"]]
    first, last = in_ir[0], in_ir[-1]
    here = [i for i in in_ir if not i["pdf"].startswith("http")]
    still = (f' Volume {here[0]["volume"]} ({here[0]["label"]}) is hosted on this site until it joins the Repository.'
             if len(here) == 1 else "")
    rail = "\n".join(
        f'      <li><a href="#d{d}">{d}s <span>{sum(len(v) for v in vols.values())}</span></a></li>'
        for d, vols in tree.items())
    body = []
    for d, vols in tree.items():
        n = sum(len(v) for v in vols.values())
        body.append(f'  <section class="decade" id="d{d}" aria-labelledby="d{d}-t">\n'
                    f'    <{dt} class="decade__t" id="d{d}-t"><b>{d}s</b> <span>{n} issue{"s" if n != 1 else ""}</span></{dt}>')
        for v, its in vols.items():
            if v + 1 in gaps:
                body.append(gap_row(v + 1, vt))
            years = sorted({i["year"] for i in its})
            yr = str(years[0]) if len(years) == 1 else f"{years[0]}–{str(years[-1])[-2:]}"
            tiles = "\n".join("      " + issue_tile(i, p) for i in its)
            body.append(f'    <div class="vol" id="v{v}">\n'
                        f'      <{vt} class="vol__t"><span class="v">Vol.</span><span class="n">{v}</span><span class="y">{yr}</span></{vt}>\n'
                        f'      <ol class="vol__issues">\n{tiles}\n      </ol>\n    </div>')
        body.append("  </section>")
    total = len(in_ir)
    return f"""<section class="archive" id="archive" aria-labelledby="{head_id}">
  <div class="wrap">
    <div class="archive__head">
      <{heading_tag} id="{head_id}">Sixty years of <em>Perspective</em></{heading_tag}>
      <div>
        <p><em>Perspective</em> has come out since {first["label"]}: six times a year in its early decades, twice a year now, in spring and in the autumn. Every past issue is here, newest first; choose a cover to open it as a PDF.{still}</p>
        <p class="meta">{total} issues, {first["label"]} to {last["label"]}, kept in the <a href="{IR}">ICS Institutional Repository</a>{" and here" if here else ""}.</p>
      </div>
    </div>
    <div class="archive__body">
      <nav class="decades" aria-label="Jump to a decade">
        <ol>
{rail}
        </ol>
        <p class="ir">PDFs open from the <a href="{IR}">ICS Institutional Repository</a>, where each issue is also catalogued{", apart from Volume " + str(here[0]["volume"]) + ", hosted here for now" if len(here) == 1 else ""}.</p>
      </nav>
      <div class="ledger">
{chr(10).join(body)}
      </div>
    </div>
  </div>
</section>
"""


def print_band(p):
    return f"""<section class="print" aria-labelledby="print-t">
  <div class="wrap print__in">
    <h2 id="print-t"><em>Perspective</em> in your mailbox</h2>
    <div>
      <p>Each new issue is printed and mailed twice a year. Give us your address and we will send it to you.</p>
      <p class="small">Letters to the editor: <a href="mailto:perspective-editor@icscanada.edu">perspective-editor@icscanada.edu</a></p>
    </div>
    <div class="print__acts"><a class="btn" href="{p}subscribe/">Subscribe to the print edition</a></div>
  </div>
</section>
"""


# ── pages ───────────────────────────────────────────────────────────────

def page_option_a(issues):
    """The earlier home page (the issue's cover spread, then the archive), kept for comparison."""
    p = "../"
    desc = (f"Perspective, the magazine of the Institute for Christian Studies: read the {CURRENT['label']} issue "
            f"on {CURRENT['theme']}, browse every issue since 1967, or subscribe to the print edition.")
    return (head("Option A · Perspective · The magazine of the Institute for Christian Studies", desc, p,
                 robots='<meta name="robots" content="noindex">\n')
            + '<body>\n<a class="skip" href="#main">Skip to content</a>\n'
            + masthead(p, "")
            + '<main id="main">\n' + feature(p) + ledger(issues, p) + print_band(p) + "</main>\n"
            + footer(p) + "</body>\n</html>\n")


def page_archive(issues):
    p = "../"
    desc = "Every past issue of Perspective, the magazine of the Institute for Christian Studies, since 1967, each one a PDF."
    return (head("Archive · Perspective", desc, p)
            + '<body>\n<a class="skip" href="#main">Skip to content</a>\n'
            + masthead(p, "archive")
            + '<main id="main">\n' + ledger(issues, p, "h1", "archive-t") + print_band(p) + "</main>\n"
            + footer(p) + "</body>\n</html>\n")


def redirect(to, title, text):
    """A page that has moved; old links land on its new home."""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title} · Perspective</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{to}">
<meta http-equiv="refresh" content="0; url={to}">
<script>location.replace('{to}');</script>
</head>
<body>
<p>{text} <a href="{to}">Go there now</a>.</p>
</body>
</html>
"""


def page_subscribe(issues):
    p = "../"
    by_slug = {i["slug"]: i for i in issues}
    recent = [i for i in sorted(issues, key=lambda x: x["issued"], reverse=True)][:3]
    figs = "\n".join(
        f'      <figure><img src="{p}{i["cover"]}" alt="Cover of Perspective, {E(i["label"])}" width="{i["w"]}" height="{i["h"]}"><figcaption>{E(i["label"])}</figcaption></figure>'
        for i in recent)
    desc = "Ask for the print edition of Perspective, the magazine of the Institute for Christian Studies, mailed twice a year."
    tpl = (ROOT / "_scripts/subscribe.html").read_text()
    main = tpl.replace("{{covers}}", figs).replace("{{gform}}", GFORM).replace("{{current_dir}}", CURRENT["dir"]).replace("{{current_label}}", CURRENT["label"]).replace("{{p}}", p)
    return (head("Subscribe to the print edition · Perspective", desc, p)
            + '<body>\n<a class="skip" href="#main">Skip to the form</a>\n'
            + masthead(p, "subscribe")
            + main + footer(p) + "</body>\n</html>\n")


# The edition's cover fills the viewport; with the masthead above it, it fills what is left.
EDITION_FIT = """<style>
  :root { --mast: 69px; }
  @media (min-width: 1201px) { :root { --mast: 100px; } }
  @media (min-width: 52rem) {
    .cover, .cover .face { min-height: calc(100svh - var(--mast)); }
    .cover h1 { font-size: clamp(3rem, min(15.5vw, (100svh - var(--mast) - 14rem) / 2.4), 15rem); }
  }
</style>
"""

MARK = ("<!-- site:{0} -->", "<!-- /site:{0} -->")


def put_between(s, name, content, anchor_re, after=True):
    """Insert or replace a marked block, so rebuilding is idempotent."""
    a, b = MARK[0].format(name), MARK[1].format(name)
    block = f"{a}\n{content}{b}\n"
    if a in s:
        return re.sub(re.escape(a) + r".*?" + re.escape(b) + r"\n", lambda m: block, s, flags=re.S)
    m = re.search(anchor_re, s)
    if not m:
        raise SystemExit(f"anchor for {name} not found")
    at = m.end() if after else m.start()
    return s[:at] + block + s[at:]


def wrap_edition(src, p, active, teaser="", robots=""):
    s = src
    extra = f'<link rel="stylesheet" href="{p}assets/teaser.css">\n' if teaser else ""
    s = put_between(s, "head",
                    f'{robots}<link rel="stylesheet" href="{p}assets/chrome.css">\n{extra}<script src="{p}assets/js/site.js" defer></script>\n{EDITION_FIT}',
                    r"</head>", after=False)
    s = put_between(s, "masthead", masthead(p, active), r'<a class="skip"[^>]*>[^<]*</a>\n')
    s = put_between(s, "footer", teaser + footer(p), r"</body>", after=False)
    return s


def from_archive(issues, p):
    recent = sorted([i for i in issues if not i["online"]], key=lambda x: x["issued"], reverse=True)[:8]
    tiles = "\n".join("    " + issue_tile(i, p) for i in recent)
    total = len([i for i in issues if not i["online"]])
    return f"""<section class="from-archive" aria-labelledby="from-archive-t">
  <div class="wrap">
    <div class="from-archive__head">
      <div>
        <h2 id="from-archive-t">Earlier issues</h2>
        <p>{total} issues of <em>Perspective</em> since 1967, each one a PDF. These are the most recent.</p>
      </div>
      <a class="btn btn--line" href="{p}archive/">Browse every issue {ARROW}</a>
    </div>
    <ol>
{tiles}
    </ol>
  </div>
</section>
"""


def main():
    issues = load_issues()
    out = {
        "archive/index.html": page_archive(issues),
        "subscribe/index.html": page_subscribe(issues),
        "option-a/index.html": page_option_a(issues),
        "option-b/index.html": redirect("../", "Moved", "Option B is now the Perspective home page."),
    }
    ed_path = ROOT / CURRENT["dir"] / "index.html"
    edition = ed_path.read_text()
    out[f'{CURRENT["dir"]}/index.html'] = wrap_edition(edition, "../", "current")

    # The home page is the current edition itself, its paths pointed into its folder,
    # with the most recent past issues after it.
    pristine = re.sub(r"<!-- site:(\w+) -->.*?<!-- /site:\1 -->\n", "", edition, flags=re.S)
    home = re.sub(r'((?:src|href)=")(img|fonts)/', rf'\1{CURRENT["dir"]}/\2/', pristine)
    out["index.html"] = wrap_edition(home, "", "current", teaser=from_archive(issues, ""))
    for rel, text in out.items():
        f = ROOT / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text)
        print("wrote", rel, len(text) // 1024, "KB")


if __name__ == "__main__":
    main()
