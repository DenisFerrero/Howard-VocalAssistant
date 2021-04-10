import _ from 'lodash'

// IMPORTANT Before export an object (nested or not) clone it!!!
//  By doing spread operator { ...obj } will clone only the first level of key
//  Instead use a custom function or run npm i loadash --save, and use the cloneDeep method
// Solution by https://github.com/nuxt/nuxt.js/issues/1917#issuecomment-370363332

export default {
  CpuUsage: (state) => _.cloneDeep(state.deviceUsage.usageCPU),
  RamUsage: (state) => _.cloneDeep(state.deviceUsage.usageRAM),
  assistantConfig: (state) => _.cloneDeep(state.assistantConfig),
}
