import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";
import rehypeKatex from "rehype-katex";
import remarkMath from "remark-math";

const markdown = {
  remarkPlugins: [remarkMath],
  rehypePlugins: [rehypeKatex],
};

export default defineConfig({
  site: "https://yousack.github.io",
  base: "/kyokasho/",
  markdown,
  integrations: [mdx(markdown)],
});
