export default {
  SET_ASSISTANT_STATE(state, data) {
    if (Array.isArray(data) && data.length > 0) {
      if (typeof data[0] === 'boolean') state.assistantStatus.isOnline = data[0]
      if (typeof data[1] === 'boolean')
        state.assistantStatus.hasServerConnection = data[1]
    }
  },
  SET_DEVICE_STATS(state, data) {
    const newData = {
      usageCPU: state.deviceStats.usageCPU,
      usageRAM: state.deviceStats.usageRAM,
      deviceUpTime: state.deviceStats.deviceUpTime,
    }
    if (Array.isArray(data) && data.length > 0) {
      if (typeof data[0] === 'object') newData.usageCPU = data[0]
      if (typeof data[1] === 'object') newData.usageRAM = data[1]
      if (typeof data[2] === 'string') newData.deviceUpTime = data[2]
    }
    state.deviceStats = Object.assign(newData)
  },
  SET_SOCKET_CONNECTION(state, data) {
    state.isSocketConnected = data
  },
  SET_DEVICE_USAGE(state, data) {
    state.DEVICE_USAGE = data
  },
}
