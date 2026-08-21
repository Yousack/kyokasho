# AGENTS.md

## Project goal

This repository is an interactive, web-first mathematics textbook. The website is the canonical output; Markdown/MDX is its authoring format rather than the final product.

## Content structure

- Organize the textbook conceptually as part → chapter → section, but use **one primary Markdown/MDX source file per chapter**.
- Do not split ordinary sections or subsections into separate Markdown files. Inside a chapter file, represent them with `##` and `###` headings.
- Split a chapter into multiple source files only when there is a concrete technical reason, such as a genuinely independent interactive application or an unusually large generated/reference artifact. Do not split merely because the chapter has many sections.
- Keep chapter prose continuous so definitions, examples, motivation, and transitions can be edited and read in context.
- Use directories primarily for parts, assets, figures, and chapter-specific interactive components rather than for one-file-per-section prose.
- Implement reader-facing routes under `src/pages/`. Prefer one reader-facing route per chapter; use in-page anchors for sections.
- A part may have its own introductory page when it provides meaningful orientation rather than merely repeating the table of contents.
- At the beginning of each chapter, state the chapter's learning objectives or central questions. Individual sections need separate objectives only when useful.
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
- When several kinds of objects or operations could answer the opening question, explain why the chapter selects the one it studies. Do not present linearity, orthogonality, invertibility, or another restriction as arbitrary; state what structure it preserves and what that preservation lets the reader reconstruct or calculate.
- In the opening development of linear algebra, proceed from a concrete input-output problem to a rule that acts on every input, then distinguish linear transformations from other possible rules. Introduce matrices only after showing that linearity makes the images of basis vectors sufficient to determine every output.
- Distinguish an operation chosen separately for one input from a fixed transformation applied uniformly to all inputs. A single correspondence such as $\mathbf u\mapsto\mathbf v$ does not determine a transformation; make any resulting non-uniqueness explicit.
- Optimize chapter structure for conceptual continuity rather than for small files. A section boundary should mark a genuine change of topic, not merely keep files short.
- Introduce notation and terminology close to where they become necessary; avoid creating isolated micro-sections for definitions that are better explained in context.
- Use explicit transitions between sections when one idea motivates the next.
- Treat interactivity as part of the explanation, not decoration.
- Give every interactive element a learning objective and a useful textual explanation.
- Ensure controls work with keyboard input, use semantic HTML, and respect reduced-motion preferences.
- Write reader-facing prose in Japanese unless the material explicitly requires another language.
- Set definitions, theorems, and supplementary notes apart from the surrounding prose with a Markdown blockquote. Begin the block with a bold label such as `**定義（一次結合）**`, `**定理（階数・退化次数の定理）**`, or `**補足**`. Keep motivation and examples outside the box so the box contains the statement readers will want to find again.

## Development

- Install dependencies with `npm install`.
- Run locally with `npm run dev`.
- Verify production output with `npm run build`.
- Deployment is defined in `.github/workflows/deploy-pages.yml`.
- Do not commit `node_modules/`, `dist/`, or `.astro/`.
- Keep components small and add dependencies only when they materially improve the textbook.
- Update README.md when build, deployment, or authoring conventions change.
