// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    "@nuxtjs/tailwindcss",
    "@pinia/nuxt",
    "@nuxt/content"
  ],
  app: {
    head: {
      link: [
        {
          rel:"stylesheet", href:"https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css"
        }
      ]
    }
  },
  content: {
    highlight: {
      // Theme used in all color schemes.
      theme: 'monokai',
      preload: ['python']
    },
    markdown: {
      remarkPlugins: [
        'remark-math'
      ],
      
      rehypePlugins: [
        // this next line here
      ['rehype-katex', { output: 'html' }]

      ]
    }
  }
})
