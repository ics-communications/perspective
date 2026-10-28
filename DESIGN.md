---
name: Perspective
description: The ICS magazine since 1967, its newest edition at the front and every volume ruled behind it like a contents page.
colors:
  red: "#D2232A"
  red-deep: "#A8161C"
  cream: "#FFF4DB"
  ink: "#111111"
  paper: "#FFFFFF"
  grey: "#5A5650"
  hair: "color-mix(in srgb, #111111 18%, transparent)"
  stroke: "color-mix(in srgb, #111111 45%, transparent)"
typography:
  display:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(2.3rem, 1.6rem + 2.6vw, 3.4rem)"
    fontWeight: 500
    lineHeight: 1.02
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(1.9rem, 1.5rem + 1.5vw, 2.7rem)"
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: "-0.015em"
  title:
    fontFamily: "Avenir Next Condensed, Arial Narrow, sans-serif"
    fontSize: "clamp(1.9rem, 1.5rem + 1.4vw, 2.7rem)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "-0.005em"
  numeral:
    fontFamily: "Avenir Next Condensed, Arial Narrow, sans-serif"
    fontSize: "3.2rem"
    fontWeight: 300
    lineHeight: 1
    letterSpacing: "-0.02em"
    fontFeature: "lnum"
  body:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "1.06rem"
    fontWeight: 400
    lineHeight: 1.62
  lede:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "1.12rem"
    fontWeight: 400
    lineHeight: 1.45
  label:
    fontFamily: "Avenir Next Condensed, Arial Narrow, sans-serif"
    fontSize: "1.04rem"
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: "0.005em"
  figure:
    fontFamily: "Avenir Next, system-ui, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 500
    lineHeight: 1.3
    fontFeature: "lnum"
  button:
    fontFamily: "Avenir Next, system-ui, sans-serif"
    fontSize: "0.82rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.05em"
rounded:
  none: "0"
  portrait: "50%"
spacing:
  gutter: "clamp(1rem, 5vw, 4.5rem)"
  wrap: "82rem"
  measure: "34em"
  acts: "0.75rem"
  field: "1.1rem"
  section: "clamp(3rem, 6vw, 5rem)"
  sticky-top: "1.5rem"
components:
  button-primary:
    backgroundColor: "{colors.red}"
    textColor: "{colors.paper}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: "0.7rem 1.25rem"
    height: "2.9rem"
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
  button-line:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: "0.7rem 1.25rem"
    height: "2.9rem"
  button-line-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
  input:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "0.6rem 0.75rem"
    height: "2.9rem"
  choice:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "0.5rem 1rem 0.5rem 0.8rem"
    height: "2.9rem"
  form-error:
    backgroundColor: "color-mix(in srgb, #D2232A 6%, #FFFFFF)"
    textColor: "{colors.red-deep}"
    rounded: "{rounded.none}"
    padding: "0.8rem 1rem"
  issue-cover:
    backgroundColor: "{colors.cream}"
    rounded: "{rounded.none}"
  issue-flag:
    backgroundColor: "{colors.red}"
    textColor: "{colors.paper}"
    rounded: "{rounded.none}"
    padding: "0.25rem 0.55rem 0.25rem 0.45rem"
  decade-chip-current:
    backgroundColor: "{colors.red}"
    textColor: "{colors.paper}"
    rounded: "{rounded.none}"
    padding: "0.55rem 0.8rem"
    height: "2.75rem"
  volume-gap:
    backgroundColor: "{colors.cream}"
    textColor: "{colors.grey}"
    padding: "1rem 1.2rem"
  print-band:
    backgroundColor: "{colors.cream}"
    textColor: "{colors.ink}"
    padding: "clamp(3rem, 6vw, 5rem) 0"
  toc-portrait:
    rounded: "{rounded.portrait}"
    size: "2.25rem"
---

# Design System: Perspective

## Overview

**Creative North Star: "The Contents Page, Sixty Years Long"**

The site is the magazine's own contents page scaled to its whole run. Every page is set on white paper in ink, ruled with 1px hairlines and red rules, and reads in the order a reader of the printed magazine would expect: the newest issue's cover and its "In this issue" list first, then every volume as one ruled row, numbered in large light condensed numerals, carrying its real covers. Nothing is decorated that is not already in the print edition; the covers, sixty years of mastheads, are the content and the ornament.

The world comes from the hand-built Fall 2026 edition (`fall-2026/index.html`), whose inline stylesheet sets the same tokens the site pages use: Perspective red, cream, ink, warm grey, Newsreader to read, Avenir Next Condensed caps to label, Avenir Next for figures and buttons, the `cubic-bezier(.16, 1, .3, 1)` ease. The site pages (`assets/site.css`) are that world without the edition's essay furniture: square, flat, hairline-ruled, generous at a 17px root for an older readership. The edition's own signatures, the scalloped red mastblock, the scalloped red pull quote, the orange box, the dotted dividers and the .6rem-rounded cards, belong to the edition; on the site pages the mastblock appears only inside the cover raster (`assets/img/fall-2026-cover.webp`, a screenshot of the edition's cover).

Two pieces of chrome are borrowed and keep their own tokens: the ICS masthead (black bar, Helvetica Neue uppercase links, ICS red `#D31145` underline) copied from the philosophy site, and the ICS footer copied from ics-site, recoloured to the masthead's black, white and `#D31145` red, its tokens scoped to `.site-footer`. They frame Perspective; they are not Perspective tokens and must not be pulled into Perspective components. The ICS nav red (`#D31145`) and Perspective red (`#D2232A`) sit a few pixels apart on every page and are not reconciled.

**Key Characteristics:**
- White paper, ink text, one red: the red draws the rules, fills the primary button and marks the current or last-opened thing.
- Ruled, not boxed: rows are separated by 1px ink-18% hairlines under a 1px ink or 3px red head rule.
- Square everywhere on the site; the only curves are circular contributor portraits.
- Real covers and contributor portraits are the only imagery; nothing stock, nothing generated.
- Flat: no elevation shadows. Depth is the sticky cover and the sticky decade rail.
- Type at a 106.25% root (1rem = 17px); every target at least 44px tall, most controls 2.75rem to 2.9rem.

## Colors

One saturated red on white paper and ink, with a warm cream for quiet fields and a warm grey for secondary text.

### Primary
- **Perspective Red** (`{colors.red}`): the print masthead red. Section rules (1px above the print band, 3px over each decade title and the form), the primary button fill, link underlines, focus outlines, the volume year, the issue line under the feature headline, the "Read online" note on the current issue's tile, the "last opened" flag, the current-decade chip on narrow screens, required-field asterisks, and text selection. 5.23:1 on paper, 4.79:1 on cream.
- **Deep Red** (`{colors.red-deep}`): text on the red-tinted error notice only, where Perspective red on a red tint would lose contrast.

### Neutral
- **Ink** (`{colors.ink}`): all running text, the 1px head rule over a ledger or list, the line button's stroke, the hover fill of every button.
- **Paper** (`{colors.paper}`): the page, input fields, text on red.
- **Cream** (`{colors.cream}`): quiet fields. The print band, the missing-volume note, and the empty state behind an issue cover while it loads. Never a page background for reading.
- **Warm Grey** (`{colors.grey}`): bylines, citations, issue labels under covers, counts, hints, fine print. 7.29:1 on paper, 6.67:1 on cream.
- **Hairline** (`{colors.hair}`): the 1px rule between rows and the 1px outline around every cover.
- **Field Stroke** (`{colors.stroke}`): the resting border of inputs and radio choices; hover firms it to ink.

Edition-only: the edition also carries an orange (`#E1905D`) for its boxed standfirst and pull quote. No site page uses it.

### Named Rules
**The One Red Rule.** Perspective red is the only chromatic colour in Perspective's own components; the covers and the borrowed chrome are outside the rule. It rules, it fills the one primary action, and it marks state (current, last opened, invalid). Everything else is ink, grey, cream or paper.

**The Borrowed Chrome Rule.** The masthead's and footer's shared `#000`/`#FFF`/`#D31145` palette stays inside `.ics-header`, `.ics-mobile-menu` and `.site-footer`. Perspective components never reference them, and the chrome never takes Perspective tokens.

## Typography

**Display Font:** Newsreader (with Georgia, serif), self-hosted variable 200 to 800, roman and italic; it stands in for the print edition's Heldane.
**Body Font:** Newsreader (with Georgia, serif)
**Label Font:** Avenir Next Condensed (with Arial Narrow), Light 300, Regular 400 and Demi 600, set in uppercase caps.
**Figure / UI Font:** Avenir Next (with system-ui), 400, 500 and 700, ICS's licensed copy, self-hosted.

**Character:** A bookish text serif for everything a reader reads, condensed grotesque caps for everything a reader scans, and plain Avenir Next for numbers, dates and controls, exactly the division of labour in the printed magazine.

The root is 106.25%, so 1rem is 17px and body text sits at 1.06rem (about 18px).

### Hierarchy
- **Display** (Newsreader 500, clamp(2.3rem, 1.6rem + 2.6vw, 3.4rem), line-height 1.02, -0.02em, balanced): page headlines below the cover spread: the archive's "Sixty years of *Perspective*", the print band and the subscribe page.
- **Cover headline** (Avenir Next Condensed 300, clamp(2.6rem, 6vw, 4.2rem), line-height 0.95, uppercase, 0.005em, balanced): the home page's "Fall 2026: essays on imagination", set exactly as the edition sets "In this issue".
- **Wordmark** (Avenir Next 700, clamp(3rem, min(15.5vw, (100svh − masthead − 14rem) / 2.4), 15rem) from 52rem, line-height 0.8, −0.035em): PER/SPEC/TIVE on the home cover, the edition's own values.
- **Headline** (Newsreader 500, clamp(1.9rem, 1.5rem + 1.5vw, 2.7rem), 1.08, -0.015em): band headings. Print band, "Earlier issues", the confirmation (to 2.5rem).
- **Title** (Avenir Next Condensed 600, clamp(1.9rem, 1.5rem + 1.4vw, 2.7rem), line-height 1, uppercase): decade titles ("1990S"), with the issue count beside them in Avenir Next 0.88rem grey.
- **Numeral** (Avenir Next Condensed 300, 3.2rem; 2.6rem under 40rem, line-height 1, lining figures): the volume number in each ledger row, under a "VOL." label in condensed 600 0.78rem caps at 0.08em, over the year range in Avenir Next 500 0.9rem red.
- **Body** (Newsreader 400, 1.06rem, 1.62): running text, held to a 34em measure.
- **Lede** (Newsreader 400, `--lede` 1.32rem, 1.5rem from 52rem, line-height 1.35, Perspective red): the introduction's question in the cream band under the cover spread, set as the edition's standfirsts. The subscribe introduction stays ink at 1.15rem/1.5.
- **Label** (Avenir Next Condensed 600, 1.12rem, 1.12, uppercase, 0.005em): contents titles in the home cover's contents list, as in the edition; form legends use the same face at 1.25rem. Page numbers and the issue line are Avenir Next 400 at 0.88rem in warm grey.
- **Figure** (Avenir Next 500, 0.9 to 0.95rem, lining figures; tabular in the decade rail): issue lines, counts, dates, form labels, notes. Issue tile labels run at 0.82rem/1.3.
- **Button** (Avenir Next 700, 0.82rem, 1.2, uppercase, 0.05em): every button.

### Named Rules
**The Three Voices Rule.** Read in Newsreader, scan in Avenir Next Condensed caps, count in Avenir Next. Figures that stand alone as data (issue lines, counts, tile labels, volume years) and every control take Avenir Next; numbers inside sentences and headlines stay in the serif. Page and band headlines are Newsreader; decade and contents titles are condensed caps.

**The Italic Title Rule.** The magazine's name is set in italic wherever it appears in running text or headlines, as in print.

## Layout

A single 82rem column (`.wrap`) centred with a fluid gutter of clamp(1rem, 5vw, 4.5rem). Text measure is 34em. The root is generous (17px) and every interactive row or control is at least 44px tall: buttons and fields 2.9rem, decade chips 2.75rem, the wide decade rail's links about 44px.

- **Feature (home):** the edition's cover spread. One column below 52rem: the cover at 92svh, then the contents. From 52rem, two equal columns at least the viewport under the masthead tall. The photo fills the cover column whatever its height; the wordmark and ICS mark sit in a sticky layer the height of that viewport, so they hold the bottom of the screen while the longer contents column scrolls past. Contents rows are the edition's: 2.9rem portraits, 0.72rem vertical padding, page numbers right.
- **Archive:** the head is two columns (5fr / 6fr) from 60rem. Below 64rem the decade rail is a wrapping row of bordered chips above the ledger; from 64rem it becomes an 11rem sticky column (1.5rem from the top) with a red right rule, beside the ledger.
- **Ledger rows:** a numeral column (4.6rem; 6.5rem from 40rem) and an issue grid of auto-fill tiles (min 6.4rem; 7.6rem to 8.6rem from 40rem).
- **Print band:** full-bleed cream; inside the wrap, headline, text and action in three columns (5fr / 4fr / auto) from 60rem.
- **Subscribe:** two columns (4fr / 6fr) from 60rem with the left column sticky; field rows split 1fr 1fr or 2fr 1fr from 40rem.
- **Vertical rhythm:** major sections pad by clamp(3rem, 6vw, 5rem) to clamp(3.5rem, 7vw, 6rem); decades are spaced by clamp(2.5rem, 5vw, 4rem); action groups gap 0.75rem; form rows 1.1rem.
- **Breakpoints:** 40rem, 60rem, 64rem for site pages. The borrowed masthead switches to its burger at 1200px.
- **Print:** the decade rail, print band and feature actions are hidden; the ledger prints as one column.

### Named Rules
**The One Row Per Volume Rule.** Every volume is one ruled row with the same anatomy: numeral, "VOL." label, year, then its covers. A volume the repository lacks keeps its row as a cream note ("Not yet in the ICS Institutional Repository."), never invented issues.

## Elevation & Depth

Flat. No surface casts a shadow. Depth comes from position: the cover's wordmark and the decade rail stay sticky while the page scrolls past, and the masthead sits above everything in black. `box-shadow` appears only as a 1px state ring: the red ring around a focused input (`0 0 0 1px` red) and the inset red ring of a checked radio choice (`inset 0 0 0 1px` red).

### Named Rules
**The Ruled Not Raised Rule.** Separation is a 1px hairline or a red rule, never a shadow or a lifted card.

## Shapes

Square. Buttons, inputs, choices, chips, tiles, the error notice, the flag and the bands all have 0 radius; inputs explicitly reset to `border-radius: 0`. The only curve is the circle: contributor portraits in the contents list (2.25rem, 50%) and the solid red dot that stands in for a missing portrait. Covers sit inside a 1px hairline outline inset by 1px, so a pale cover still has an edge against white paper.

Rules carry the structure: 1px ink over a list or ledger, 1px ink-18% between rows, 3px red over each decade title, the subscribe form and the confirmation, 1px ink over the introduction band and 1px red over the print band.

The edition keeps its own form language (scalloped mastblock and pull-quote edges, dotted dividers, .6rem-rounded cards); site components do not adopt it.

## Components

### Buttons
Square, confident, Avenir Next bold caps, as the edition's Contents button.
- **Shape:** square corners (0), at least 2.9rem tall, padding 0.7rem 1.25rem, a 0.55rem gap before a trailing 1em SVG arrow.
- **Primary (`.btn`):** red fill, 1px red border, paper text. "Read the Fall 2026 issue", "Subscribe to the print edition", "Send my address".
- **Line (`.btn--line`):** transparent with a 1px ink border and ink text. The secondary action beside a primary ("Get it in print") or alone where the action is navigation ("Browse every issue", "Read the Fall 2026 issue now").
- **Hover:** both fill with ink and turn the text paper, over 0.3s on the house ease.
- **Focus:** the global 2px red outline at a 3px offset.
- **Disabled:** 0.55 opacity with a progress cursor; the subscribe button also reads "Sending…".

### Feature (the new issue)
The home page's front door, rebuilt from the edition's own cover (`fall-2026/index.html`, `header.cover`) so the two read as one object. On the left, a live copy of the cover rather than a picture of it: the fern photo (`assets/img/<dir>-fern.webp`), the scalloped red mastblock, the PER/SPEC/TIVE wordmark and the ICS mark (drawn from the edition's own SVG at build time), the whole face a decorative link to the edition. On the right: the cover headline in condensed light caps, the issue line in grey, the edition's "In this issue" contents list with page numbers and the print-edition note, then "Read the Fall 2026 issue" and "Get it in print". Below the spread, a cream band carries the introduction's question in red Newsreader with its attribution and a "Read the introduction" link.

### Volume ledger
The archive, rendered on the home page under `#archive`; the nav's Archive link jumps there from every page, and `archive/` is only a redirect for old links. A head (display headline plus a note on the run and its count, linked to the ICS Institutional Repository), then decades newest first, each opened by a condensed caps decade title over a 3px red rule with its issue count on the right. Within a decade, one ledger row per volume (see the Layout rule): numeral column, then an ordered grid of issue tiles, a hairline under each row.

### Decade rail
Navigation through the ledger, each entry a decade and its issue count ("1990s 44").
- **Under 64rem:** a wrapping row of square chips, 1px hairline border, Avenir Next 500 0.95rem with the count in 0.8rem grey; hover turns the border red; the decade in view is a red chip with paper text.
- **From 64rem:** a sticky 11rem column with a red right rule, the list ruled in hairlines under a 1px ink head rule, grey links that turn red on hover; the decade in view is set in bold ink. A small grey note about the Repository follows the list.
- `site.js` sets `aria-current="true"` on the decade in view with an IntersectionObserver; without JavaScript the rail is a plain jump list.

### Issue tile
A real cover above two lines of label. The cover sits at 17:22 on a cream ground inside the inset hairline outline, cropped from the top. Below: "No. 3" in Avenir Next 700 and the issue's date label in grey; the current issue's tile (`.issue--online`) reads "Read online" in red and links to the edition rather than a PDF. Visually hidden text gives the volume and the PDF size. Hover lifts the cover image 2% and scales it 3% over 0.6s, rings the cover with a 2px red outline and turns the number red; keyboard focus shows the same ring.
- **"Last opened" flag:** when a reader opens an issue, `site.js` stores its slug in `localStorage` (`perspective:last-issue`) and pins a red tab to the cover's left edge, 0.55rem from the top: "LAST OPENED" in Avenir Next 700 caps, 0.76rem, 0.06em, paper on red. One flag at a time; the page is whole without it. At 0.76rem (about 11px) the flag is the smallest text on the site; it is recorded as built, not as a step of the type scale.

### Volume gap row
A ledger row for a volume the Repository does not have (today, Volume 59). The numeral column shows "VOL." and the number without a year; the issue column is a cream panel stretched to the row's height with the note "Not yet in the ICS Institutional Repository." in Avenir Next 0.9rem grey.

### Print band
The closing invitation on the home page. A full-width cream band under a 1px red rule: the headline "*Perspective* in your mailbox", a short paragraph with the editor's address in grey Avenir Next, and the primary "Subscribe to the print edition" button.

### Subscribe form
One short form posting to the existing Google Form.
- **Structure:** under a 3px red rule, three fieldsets ("Your name", "Mailing address", "And by email?") with condensed caps legends at 1.25rem. Labels are Avenir Next 500 0.9rem above the field; required fields carry a red asterisk, optional ones a grey "(optional)" or "(if any)".
- **Inputs:** square, paper, 1px field stroke, 2.9rem tall, 1.02rem text, red caret. Hover firms the border to ink; focus turns it red and adds a 1px red ring.
- **Radio choices:** the e-news question is a pair of bordered square choices with red native radios; the checked choice gets a red border and an inset red ring, and keyboard focus a 2px red outline.
- **Invalid:** on submit, empty required fields get a red border and a 5% red tint and `aria-invalid="true"`; an unanswered choice group turns both choice borders red. Typing or choosing clears the state.
- **Error notice:** a square panel with a 1px red border and a 6% red tint, deep-red Avenir Next 0.92rem text, `role="alert"`, focused when shown: "Please fill in the 2 highlighted fields." or, on a network failure, a message with a link to the Google Form.
- **Confirmation:** the form hides and a confirmation panel takes its place under the same 3px red rule, a headline-size thank you, a line about the next issue, and a line button back to the current issue; it takes focus.
- **Fallback:** a grey note under the form links the Google Form directly.

### "Earlier issues" teaser (Option B)
On Option B (`option-b/`, noindex) the edition itself is the home page, and a scoped band (`assets/teaser.css`, everything under `.from-archive`) closes it: a 1px red top rule, the headline "Earlier issues" with a count line, a line button "Browse every issue", and the eight most recent repository issues as issue tiles. It reproduces the site's issue tile and line button inside the edition, which keeps its own stylesheet.

### Navigation (borrowed)
The ICS masthead, unchanged from the philosophy site: a black bar 100px tall (69px under 1200px) with the white-and-red ICS logo, then Helvetica Neue 600 0.8rem uppercase links at 0.14em tracking; hover and the current page take a 1.5px ICS-red underline at a 6px offset. Under 1200px a three-bar asymmetric burger opens a full-screen black overlay. Items: Home, the current edition's label, Archive (a jump to the home page's archive), Subscribe. There is no ICS menu; the ICS logo and the footer carry the Institute's links. The ICS footer (Libre Baskerville and Outfit, recoloured to the masthead: black ground, white text, a 2px ICS-red top rule and red hover underlines) is injected by `assets/js/footer.js` and is otherwise borrowed as is.

### Adding a new edition
The edition on the front door is the `CURRENT` record in `_scripts/build.py`. To ship the next one:
1. Put the hand-built edition in its own folder (e.g. `spring-2027/index.html`) with `img/` and `fonts/` beside it, a `<a class="skip">` link (the masthead is inserted after it) and a `<title>` beginning "Perspective · ". Its cover markup should use `.cover` / `.cover .face` and `.cover h1` so the build's viewport fit applies.
2. Add its cover tile as `assets/covers/<slug>.webp` (440×569) and the cover photo as `assets/img/<dir>-<name>.webp` (1000px wide, WebP q60), with its provenance `.json` sidecar.
3. Change `CURRENT` in `_scripts/build.py`: `dir`, `label`, `volume`, `number`, `slug`, `cover`, `photo`, `theme`, `lede`, `lede_by`, and the `contents` rows (anchor, title, author or `None`, portrait file, `"dot"` for the red dot or `None` for none, print page).
4. Add the outgoing edition (Fall 2026) as a record in `assets/data/issues.json` once its PDF is in the Repository; otherwise it drops out of the ledger when `CURRENT` moves.
5. Check the values the build still hardcodes: `load_issues()` sets the current issue's `year: 2026`, `issued: "2026-10"` and 440×569; `_scripts/subscribe.html` links "Read the Fall 2026 issue now" to `fall-2026/`; the archive head says "Sixty years" and "Volume 59 is still to be added."
6. Run `python3 _scripts/build.py`.

## Do's and Don'ts

### Do:
- **Do** take every colour from the six Perspective tokens: red `#D2232A`, deep red `#A8161C` (error text only), cream `#FFF4DB`, ink `#111111`, paper `#FFFFFF`, grey `#5A5650`, with hairlines at ink 18%.
- **Do** separate rows with a 1px hairline and open lists with a 1px ink rule; open a major block (decade, form, confirmation) with a 3px red rule.
- **Do** keep every site component square; reserve the circle for contributor portraits.
- **Do** show real covers at 17:22 inside the 1px inset hairline outline, cropped from the top.
- **Do** set labels in Avenir Next Condensed caps, figures and controls in Avenir Next with lining numerals, and reading text in Newsreader at a 34em measure.
- **Do** keep interactive targets at least 44px tall (buttons and fields 2.9rem) and use the 2px red focus outline at a 3px offset.
- **Do** mark a missing volume with the cream gap row rather than hiding it or filling it.
- **Do** keep the ICS masthead as borrowed and the footer in the masthead's colours, with their own tokens in their own scopes.

### Don't:
- **Don't** add shadows for elevation; `box-shadow` is used only as a 1px state ring on inputs and choices.
- **Don't** use stock or generated imagery; covers and contributor portraits are the only pictures.
- **Don't** use the ICS nav red `#D31145` or the chrome's black palette in Perspective components.
- **Don't** add a second accent colour to site pages; the edition's orange stays in the edition.
- **Don't** set standalone figures (issue lines, counts, dates under covers) or controls in Newsreader.
- **Don't** invent issues, covers or volumes to close a gap in the run.
