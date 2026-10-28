---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: ["subscribe/index.html","option-b/index.html"]
---

# Surface brief: Perspective site (home, archive, subscribe)

Mode: Read. Code-led. Covers `index.html` (option A home, with the archive at `#archive`; `archive/` only redirects there), `subscribe/index.html`, `option-b/index.html`, and the site chrome around `fall-2026/index.html`.

Audience and job: ICS supporters arrive to read the new issue; alumni and researchers arrive to find a past issue by year. Success: the new issue is one click from arrival, any of 234 past issues is two clicks from its PDF, and a print subscription takes one short form.

Constraints: nav from the philosophy site masthead (black bar, uppercase white links, ICS red underline); footer copied directly from ics-site (`js/footer.js` and its CSS); the Fall 2026 edition's design untouched; no GitHub Pages and no CNAME; relative URLs throughout.

Unattended run: the decision page was not served because the user asked for no questions overnight; the dealt lead was taken. Unresolved: option A or B for the root; whether to show Volume 59 once it is in the repository.

## Direction contract

THESIS: The site is the magazine's own contents page scaled to sixty years. It refuses the stock "latest posts" blog index and the undifferentiated thumbnail wall: every volume is one ruled row, read like the edition's "In this issue" list.

OWN-WORLD: Perspective red #D2232A as the rule and the mast, white paper, ink #111, cream #FFF4DB for quiet fields; Newsreader for reading and titles, Avenir Next Condensed caps for labels, Avenir Next for figures; 1px red and ink hairlines; real covers as the only imagery; the scalloped red mastblock from the print cover.

STORY: The visitor sees the Fall 2026 cover and its contents, understands Perspective has run since 1967, opens the new issue or drops into the volume ledger, and can ask for print copies.

FIRST VIEWPORT: Black ICS masthead (Home, Fall 2026, Archive, Subscribe; no ICS menu). Below, the edition's own cover spread at its own values: the live fern cover with the scalloped red mastblock and PER/SPEC/TIVE wordmark on the left half, full height; on the right half the issue theme in Avenir Next Condensed Light caps, the issue line, the edition's contents rows with page numbers, then "Read the Fall 2026 issue" and "Get it in print". The introduction's question follows in a cream band, as the edition's standfirst. (Revised 2026-10-28 at the user's request: match the edition's fonts and spacing.)

FORM: Structure 6 of 7 (volume ledger in contents-page grammar, sticky decade rail). seed:0bda44e462f2b812. Raises: equal row anatomy for every volume (from the Art Paul magazine program, declined); a "last opened" flag on the issue the reader last took from the archive (from the cutting-bench select rail, declined).

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
