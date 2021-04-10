export default {
  setSocketEmitCount(state) {
    state.socketEmitCount++
  },

  setDeviceUsageState(state, data) {
    state.deviceUsageState = data
  },
  setAssistantConfig(state, data) {
    if (Array.isArray(data) && data.length > 0) {
      if (typeof data[0] === 'string') state.assistantConfig.server = data[0]
      if (typeof data[1] === 'string') state.assistantConfig.uuid = data[1]
      if (typeof data[2] === 'boolean') state.assistantConfig.isSaved = data[2]
      if (typeof data[3] === 'boolean')
        state.assistantConfig.isRegistered = data[3]
    }
  },
  setDeviceUsage(state, data) {
    const newData = {
      usageCPU: state.deviceUsage.usageCPU,
      usageRAM: state.deviceUsage.usageRAM,
    }
    if (Array.isArray(data) && data.length > 0) {
      if (typeof data[0] === 'object') newData.usageCPU = data[0]
      if (typeof data[1] === 'object') newData.usageRAM = data[1]
    }
    // Need to assign this way to make sure to have triggered the update of the content
    state.deviceUsage = Object.assign(newData)
  },
}
