# rcbowlin1.github.io

Personal site for Ryan Bowlin — product manager who builds and ships production AI.

Built with [Eleventy](https://www.11ty.dev/) (static site generator). Deployed to GitHub Pages
via GitHub Actions on every push to `main`.

## Local development

```bash
npm install        # once
npm run serve      # live preview at http://localhost:8080
npm run build      # build to _site/
```

## Publishing a new post

1. Create a Markdown file in `src/posts/`, e.g. `src/posts/my-title.md`:

   ```markdown
   ---
   title: "My post title"
   date: 2026-09-22
   ---

   Write the post in Markdown here.
   ```
2. `git commit` and `git push` to `main`.
3. The GitHub Action rebuilds and deploys. Live in about a minute — no other steps.

## Structure

- `src/index.njk` — landing page (hub)
- `src/work.njk` — Work (cited proof + teardown)
- `src/thoughts.njk` — Thoughts index (lists posts)
- `src/posts/` — blog posts (Markdown); `posts.json` applies the post layout + tag
- `src/about.njk` — About (contact lives in the footer on every page)
- `src/_includes/base.njk` — shared layout (header nav + footer contact)
- `src/_includes/post.njk` — post layout
- `src/css/styles.css` — self-contained styles
- `.github/workflows/deploy.yml` — build + deploy to Pages
