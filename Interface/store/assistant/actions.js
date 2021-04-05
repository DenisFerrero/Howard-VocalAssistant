import dayjs from 'dayjs'
// Number of data to show in the chart
const dataChartLimit = process.env.DATA_CHART_LIMIT || 10

export default {
  parseDeviceStats({ commit, state }, data) {
    // Update the Device state
    commit('SET_DEVICE_USAGE', 'Updating')
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
      // If the third element is a number
      if (typeof data[2] === 'number')
        // Parse the hour of device uptime
        data[2] = dayjs().startOf('day').second(data[2]).format('hh:mm:ss A')
    }
    // Update the Device state
    commit('SET_DEVICE_USAGE', 'Stable')
    commit('SET_DEVICE_STATS', data)
  },
}

function parseUsageData(accessor, params, value) {
  // Duplicate current labels and dataset's data
  const labels = [...accessor.deviceStats[params].labels]
  const currData = [...accessor.deviceStats[params].datasets[0].data]
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
    const tmpData = { ...accessor.deviceStats[params].datasets[0] }
    tmpData.data = currData
    return { labels, datasets: [tmpData] }
  }
}
