import dayjs from 'dayjs'
// Number of data to show in the chart
const dataChartLimit = parseInt(process.env.DATA_CHART_LIMIT) || 10

export default {
  parseDeviceUsage({ commit, state }, data) {
    commit('setDeviceUsageState', 'Updating')
    // Check if the variable are OK to be managed
    if (Array.isArray(data) && data.length > 0) {
      // If the first element is a number
      if (typeof data[0] === 'number') {
        data[0] = parseUsageData(state, 'usageCPU', data[0])
      }
      // If the element element is a number
      if (typeof data[1] === 'number') {
        data[1] = parseUsageData(state, 'usageRAM', data[1])
      }
    }
    commit('setDeviceUsage', data)
    commit('setDeviceUsageState', 'Stable')
    // By incrementing socketEmitCount will be triggered the emit event
    setTimeout(() => {
      commit('setSocketEmitCount')
    }, 1000)
  },
}

function parseUsageData(accessor, params, value) {
  // Duplicate current labels and dataset's data
  const labels = [...accessor.deviceUsage[params].labels]
  const currData = [...accessor.deviceUsage[params].datasets[0].data]
  if (labels && currData) {
    // Remove element if has reached the limit
    if (currData.length >= dataChartLimit) {
      labels.shift()
      currData.shift()
    }
    // Push new value
    labels.push(dayjs().format('hh:mm:ss'))
    currData.push(value)
    // Return the updated values
    const tmpData = { ...accessor.deviceUsage[params].datasets[0] }
    tmpData.data = currData
    return { labels, datasets: [tmpData] }
  }
}
