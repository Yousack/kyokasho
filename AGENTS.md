# AGENTS.md

## Project goal

This repository is an interactive, web-first mathematics textbook. The website is the canonical output; Markdown/MDX is its authoring format rather than the final product.

## Content structure

- Organize content conceptually as part → chapter → section.
- Implement reader-facing routes as MDX under `src/pages/`.
- A part or chapter may have its own introductory MDX page.
- Begin each section with the learning objectives or questions the reader should be able to answer.
- Add narrower `AGENTS.md` files when a part or chapter needs additional conventions.

## Architecture

- Use Astro as the static-site framework.
- Use Astro layouts and components for reusable structure.
- Put interactive explanations in `src/components/`, using TypeScript with SVG or Canvas by default.
- Keep the site fully static and deployable to GitHub Pages.
- Do not add server APIs, databases, authentication, or runtime secrets without first documenting why static hosting is insufficient.
- The production base path is `/kyokasho`; use `import.meta.env.BASE_URL` rather than hard-coded root-relative URLs.

## Authoring principles

- Begin from an action, transformation, concrete question, or visual intuition before formalizing a definition.
- Treat interactivity as part of the explanation, not decoration.
- Give every interactive element a learning objective and a useful textual explanation.
- Ensure controls work with keyboard input, use semantic HTML, and respect reduced-motion preferences.
- Write reader-facing prose in Japanese unless the material explicitly requires another language.

## Development

- Install dependencies with `npm install`.
- Run locally with `npm run dev`.
- Verify production output with `npm run build`.
- Deployment is defined in `.github/workflows/deploy-pages.yml`.
- Do not commit `node_modules/`, `dist/`, or `.astro/`.
- Keep components small and add dependencies only when they materially improve the textbook.
- Update README.md when build, deployment, or authoring conventions change.
