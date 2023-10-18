import type { Config } from "tailwindcss";

import Typography from "@tailwindcss/typography";

export default <Partial<Config>> {
  darkMode: "class",
  theme: {
    extend: {
      typography(theme: any) {
        return {
          dark: {
            css: {
              color: theme("colors.zinc.300"),
              '[class~="lead"]': { color: theme("colors.zinc.400") },
              a: { color: theme("colors.zinc.100") },
              strong: { color: theme("colors.zinc.100") },
              "ul > li::before": { backgroundColor: theme("colors.zinc.700") },
              hr: { borderColor: theme("colors.zinc.800") },
              blockquote: {
                color: theme("colors.zinc.100"),
                borderLeftColor: theme("colors.zinc.800"),
              },
              h1: { color: theme("colors.zinc.100") },
              h2: { color: theme("colors.zinc.100") },
              h3: { color: theme("colors.zinc.100") },
              h4: { color: theme("colors.zinc.100") },
              code: { color: theme("colors.zinc.100") },
              "a code": { color: theme("colors.zinc.100") },
              pre: {
                color: theme("colors.zinc.200"),
                backgroundColor: theme("colors.zinc.800"),
              },
              thead: {
                color: theme("colors.zinc.100"),
                borderBottomColor: theme("colors.zinc.700"),
              },
              "tbody tr": { borderBottomColor: theme("colors.zinc.800") },
            },
          },
          css: {
            maxWidth: "60rem",
          },
        };
      },
    },
  },
  plugins: [
    Typography,
  ],
};