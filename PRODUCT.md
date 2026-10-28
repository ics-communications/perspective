# Product

<!-- impeccable:product-schema 1 -->

> Written unattended on 2026-10-28 from the user's brief (2026-10-27) and the repository; no interview round ran because the user asked for the overnight rebuild to proceed without questions. Lines marked *(inferred)* are assumptions to confirm.

## Platform

web

## Stack

Static HTML/CSS with a small Python build script (`_scripts/build.py`) that renders the archive from `assets/data/issues.json`, the same shape as the sibling ICS repos. *(inferred: delegated; matches philosophy, ics-site and f2bf)*

## Users

- Readers of *Perspective*: ICS members, donors, alumni, supporters and church communities who receive the print magazine and want to read the latest issue online. *(inferred)*
- People looking back: alumni, researchers and ICS staff searching the 1967-to-present run for a particular issue, article or moment in the Institute's history. *(inferred)*
- New readers who want a printed copy mailed to them twice a year.

## Product Purpose

*Perspective* is the magazine of the Institute for Christian Studies (Toronto), first issued in 1967 and published twice a year (spring and autumn) in print and online. This site at perspective.icscanada.edu showcases the current edition (Fall 2026, Volume 60, Number 1), gives access to every previous edition, and takes print subscriptions.

## Positioning

Sixty years of one Institute's magazine, unbroken: 234 digitised issues (1967 to Spring 2024) live in the ICS Institutional Repository, and this site is the reading room in front of that run.

## Operating Context

- Past issues are PDFs in the ICS Institutional Repository (DSpace), community handle `10756/271894`, collections "1967-1999" and "2000 to Current Year". The site links to them; it does not host the PDFs.
- The current edition is a hand-built web edition in `fall-2026/` with its own design, made from the print InDesign file.
- Print subscriptions go into the existing Google Form "Perspective Print Issue Subscription".
- DNS is handled by the user through EasyDNS; GitHub Pages is not configured by this repo.

## Capabilities and Constraints

- Navigation follows the ICS masthead used on the philosophy site (black bar, white uppercase links, red underline).
- The footer is the shared ics-site footer, copied directly.
- Old Google Site pages (Latest Issue, Recent Issues, Archive, Subscribe) do not need one-for-one recreation.
- Volume 59 (2024-2026) is not in the repository as of this build. *(observed; not to be filled with invented issues)*

## Brand Commitments

- *Perspective* masthead, Perspective red (#D2232A), Newsreader and Avenir Next, as set by the Fall 2026 edition and its print design by Kevin van der Leek Design Inc.
- ICS identity: wine footer, ICS logo.

## Evidence on Hand

- `fall-2026/` web edition and images (`fall-2026/img/SOURCES.txt`).
- 234 cover images rendered from page 1 of each repository PDF (`assets/covers/`), with metadata in `assets/data/issues.json`.
- Old site text in `info/Old-Site/`.

## Product Principles

1. The newest issue is the front door; the archive is the depth behind it.
2. Every issue in the run is one click from its PDF; no dead ends.
3. Show the real covers. The masthead's sixty-year evolution is the archive's best content.
4. Asking for a print copy should take one short form, nothing more.

## Accessibility & Inclusion

WCAG 2.2 AA. Older readers are a large share of the audience *(inferred)*: generous type, strong contrast, 44px targets.
