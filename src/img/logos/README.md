# Logo drop folder

Put company logos here for the homepage "Where I've worked" marquee.

- **Format:** SVG preferred (crisp at any size); PNG with transparent background is fine.
- **Color:** don't worry about color — the site normalizes every logo to a single flat (white) tone for a consistent look, so the original color/format doesn't matter.
- **Naming:** lowercase, hyphenated, e.g. `amazon.svg`, `heineken.svg`, `henkel.svg`, `advantage.svg`.
- Logos rarely change, so the marquee list is hardcoded in `src/index.njk` — no build/data step. Adding one = drop the file, add one `<img>` line.
