<template>
  <div class="app">
    <div class="wrapper">
      <Nuxt />
    </div>
    <!-- Social link is required having http/https  -->
    <SocialFooter
      class="bg-light"
      :instagram="social.instagram"
      :git="social.git"
      :linkedin="social.linkedin"
      :company="company"
    />
  </div>
</template>
<script>
export default {
  data() {
    return {
      social: {
        instagram: process.env.SOCIAL_INSTAGRAM || '',
        git: process.env.SOCIAL_GIT || '',
        linkedin: process.env.SOCIAL_LINKEDIN || '',
      },
      company: process.env.COMPANY_NAME || '',
    }
  },
}
</script>
<style>
.app {
  height: 100vh;
}

.wrapper {
  min-height: calc(100% - 80px);
}

footer {
  height: 80px;
  position: relative;
  left: 0;
  bottom: 0;
  width: 100%;
}
</style>
