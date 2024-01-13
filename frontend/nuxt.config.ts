// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@pinia/nuxt', '@pinia-plugin-persistedstate/nuxt'],
  css: ['~/assets/scss/styles.scss'],
  runtimeConfig: {
    public: {
      apiBase: process.env.API_BASE,
    },
  },
});
