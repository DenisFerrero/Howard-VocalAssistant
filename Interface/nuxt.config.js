export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'Interface',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  target: 'server',

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ['@fortawesome/fontawesome-svg-core/styles.css'],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: ['~/plugins/fontawesome.js'],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    // https://go.nuxtjs.dev/stylelint
    '@nuxtjs/stylelint-module',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
    'nuxt-i18n',
    'nuxt-socket-io',
  ],

  // i18n configuration
  i18n: {
    langDir: '~/locales/',
    // Default language based on user browser and saved in i18n_language cookie
    detectBrowserLanguage: {
      useCookie: true,
      cookieKey: 'i18n_language',
      // Trigger the language detection only on homepage
      onlyOnRoot: true,
    },
    defaultLocale: 'en-US',
    locales: [
      { code: 'en-US', iso: 'en-US', file: 'en-US.js', dir: 'ltr' },
      { code: 'it-IT', iso: 'it-IT', file: 'it-IT.js', dir: 'ltr' },
    ],
    lazy: true,
  },

  io: {
    sockets: [
      {
        // Assistant communication
        name: 'Assistant',
        // If not found env variable connect locally because the server is available on the same network (dev env)
        url: process.env.ASSISTANT_SOCKET || 'http://localhost:5000',
        default: true,
        vuex: {
          mutations: ['assistant.config.res --> assistant/setAssistantConfig'],
          actions: ['device.usage.res --> assistant/parseDeviceUsage'],
          emitBacks: [{ 'assistant/socketEmitCount': 'device.usage.req' }],
        },
      },
    ],
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},
}
