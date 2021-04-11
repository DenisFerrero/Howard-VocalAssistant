<template>
  <footer>
    <div class="socialLink">
      <template v-for="(account, key) in accounts">
        <a
          v-if="validateInfo(account, regex[key])"
          :key="key"
          :href="account"
          target="_blank"
        >
          <FaLayer class="fa-lg">
            <FaIcon icon="circle"></FaIcon>
            <FaIcon
              class="icon-content"
              :icon="['fab', getIconClass(key, account)]"
              transform="shrink-6"
            />
          </FaLayer>
        </a>
      </template>
    </div>
    <div class="copyright">
      <span v-if="company.length > 0"
        >{{ company }} - {{ currentYear }} -
      </span>
      <span>
        {{ softwareVersion }}
      </span>
    </div>
  </footer>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import dayjs from 'dayjs'
import { version } from '~/package.json'

export default {
  name: 'SocialFooter',
  props: {
    accounts: {
      type: Object,
      validator(value) {
        const defaultAccount = [
          'facebook',
          'git',
          'instagram',
          'linkedin',
          'twitter',
        ]
        Object.keys(value).forEach((key) => {
          const found = defaultAccount.find(
            (accountType) => key === accountType
          )
          if (!found) return null
        })
        return true
      },
      default: () => {
        return {
          facebook: null,
          git: null,
          instagram: null,
          linkedin: null,
          twitter: null,
        }
      },
    },
    company: {
      type: String,
      default: '',
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
    currentYear() {
      return dayjs().format('YYYY')
    },
    softwareVersion() {
      return `v${version || '0.0.0'}`
    },
  },
  methods: {
    // Get class for icon
    getIconClass(type, value) {
      // If match git category
      if (value.match(/git\w*\.com/)) {
        // Evaluate if it's github
        if (value.match('github.com')) return 'github'
        // Gitlab
        else if (value.match('gitlab.com')) return 'gitlab'
        // Else return standard git icon
        else return 'git'
      }
      // Other type is easier it's just the key name
      else return type
    },
    // General function for validation props
    validateInfo(info, regex) {
      return info && info.length > 0 && info.match(regex)
    },
  },
}
</script>

<style scoped>
/* Edited the style given by https://epicbootstrap.com/snippets/footer-basic  */
footer {
  padding: 10px 0;
  background-color: #ffe;
  border-top: 1px solid black;
  color: #4b4c4d;
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
