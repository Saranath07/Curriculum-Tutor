// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    "@nuxtjs/tailwindcss",
    "@pinia/nuxt",
    "@nuxt/content"
  ],
  content: {
    highlight: {
      // Theme used in all color schemes.
      theme: 'monokai',
      preload: ['python']
    }
  }
})
