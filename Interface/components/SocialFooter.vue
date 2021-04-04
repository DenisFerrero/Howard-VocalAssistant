<template>
  <footer>
    <div class="socialLink">
      <!-- Github or Gitlab link -->
      <a v-if="validateInfo(git, regex.git)" :href="git">
        <FaLayer class="fa-lg">
          <FaIcon icon="circle" />
          <FaIcon
            class="icon-content"
            :icon="['fab', gitIconClass]"
            transform="shrink-6"
          />
        </FaLayer>
      </a>
      <!-- Instagram link -->
      <a v-if="validateInfo(instagram, regex.instagram)" :href="instagram">
        <FaLayer class="fa-lg">
          <FaIcon icon="circle" />
          <FaIcon
            class="icon-content"
            :icon="['fab', 'instagram']"
            transform="shrink-6"
          />
        </FaLayer>
      </a>
      <!-- Linkedin link -->
      <a v-if="validateInfo(linkedin, regex.linkedin)" :href="linkedin">
        <FaLayer class="fa-lg">
          <FaIcon icon="circle" />
          <FaIcon
            class="icon-content"
            :icon="['fab', 'linkedin']"
            transform="shrink-6"
          />
        </FaLayer>
      </a>
    </div>
    <div
      v-if="typeof company === 'string' && company.length > 0"
      class="copyright"
    >
      {{ company }} - {{ currentYear }}
    </div>
  </footer>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import dayjs from 'dayjs'

export default {
  name: 'SocialFooter',
  props: {
    git: {
      type: String,
      default: null,
    },
    instagram: {
      type: String,
      default: null,
    },
    linkedin: {
      type: String,
      default: null,
    },
    company: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      // Regex to match Github/Gitlab, Instagram and Linkedin user link
      regex: {
        git: /ht{2}ps:\/{2}(w{3}\.)?git(hub|lab)\.com\/[\w.@:/~]+\/?/,
        instagram: /ht{2}ps?:\/{2}(w{3}\.)?instagram\.com\/\w+\/?/,
        linkedin: /ht{2}ps?:\/{2}((w{3}|\w{2})\.)?linkedin\.com\/.*$/,
      },
    }
  },
  computed: {
    gitIconClass() {
      // Icon class of Git property
      if (this.git && this.git.length > 0) {
        // Check if it's github
        if (this.git.match('github.com')) return 'github'
        // Check if it's gitlab
        else if (this.git.match('gitlab.com')) return 'gitlab'
      }
      // By default return git icon
      return 'git'
    },
    currentYear() {
      return dayjs().format('YYYY')
    },
  },
  methods: {
    // General function for validation props
    validateInfo(info, regex) {
      return info && info.length > 0 && info.match(regex)
    },
  },
}
</script>

<style scoped>
/* Edited by the style given by https://epicbootstrap.com/snippets/footer-basic  */
footer {
  padding: 10px 0;
  background-color: #ffe;
  border-top: 1px solid black;
  color: #4b4c4d;
}

footer ul {
  padding: 0;
  list-style: none;
  text-align: center;
  font-size: 18px;
  line-height: 1.6;
  margin-bottom: 0;
}

footer li {
  padding: 0 10px;
}

footer ul a {
  color: inherit;
  text-decoration: none;
  opacity: 0.8;
}

footer ul a:hover {
  opacity: 1;
}

footer .socialLink {
  text-align: center;
}

footer .socialLink > a {
  font-size: 24px;
  width: 38px;
  height: 38px;
  text-align: center;
  margin: 0 8px;
  color: inherit;
  opacity: 0.75;
}

footer .socialLink > a:hover {
  opacity: 0.9;
}

footer .copyright {
  text-align: center;
  font-size: 13px;
  color: #aaa;
  margin-bottom: 0;
}

.icon-content {
  color: #fff;
}
</style>
