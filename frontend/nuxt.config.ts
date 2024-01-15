// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@pinia/nuxt'],
  css: ['~/assets/scss/styles.scss'],
  ssr: false,
  runtimeConfig: {
    public: {
      apiBase: process.env.API_BASE,
    },
  },
});
