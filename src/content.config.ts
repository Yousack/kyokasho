import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";

const textbook = defineCollection({
  loader: glob({
    base: "./数学",
    pattern: "**/*.md",
    generateId: ({ entry }) => entry.replace(/\.md$/, ""),
  }),
});

export const collections = { textbook };
