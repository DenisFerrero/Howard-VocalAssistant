import Vue from 'vue'
import Vuex from 'vuex'
import AssistantStore from '~/store/assistant/index'

Vue.use(Vuex)

// eslint-disable-next-line no-unused-vars
const Store = new Vuex.Store({
  modules: {
    assistant: AssistantStore,
  },
})
