<template>
  <div>
    <b-dropdown variant="light">
      <template #button-content>
        {{ currentLocale }}
        <country-flag :country="getRegionByCode(currentLocale)"></country-flag>
      </template>
      <NuxtLink
        v-for="locale in availableLocales"
        :key="locale.code"
        class="dropdown-item"
        :to="switchLocalePath(locale.code)"
        @click.prevent.stop="$i18n.setLocale(locale.code)"
      >
        {{ locale.iso }}
        <!-- Show the flag -->
        <country-flag :country="getRegionByCode(locale.code)"></country-flag>
      </NuxtLink>
    </b-dropdown>
  </div>
</template>

<script>
import CountryFlag from 'vue-country-flag'

export default {
  name: 'LangToggle',
  components: {
    CountryFlag,
  },
  computed: {
    availableLocales() {
      return this.$i18n.locales.filter((i) => i.code !== this.$i18n.locale)
    },
    currentLocale() {
      return this.$i18n.locale
    },
  },
  methods: {
    getRegionByCode(code) {
      return code.split('-')[1]
    },
  },
}
</script>
