import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";

export default defineConfig({
  site: "https://yousack.github.io",
  base: "/kyokasho",
  integrations: [mdx()],
});
