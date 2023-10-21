// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    "@nuxtjs/tailwindcss",
    "@pinia/nuxt",
    "@nuxtjs/mdc"
  ],
  app: {
    head: {
      link: [
        {
          rel: "stylesheet", href: "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css"

        }
      ]
    }
  },
  mdc: {
    rehypePlugins: {
      'rehype-katex': {
        options:
        {
          output: 'html'
        }
      },
    },
    remarkPlugins:  {
      'remark-math': {},
    }
  }
})
