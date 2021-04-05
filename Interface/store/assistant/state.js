import dayjs from 'dayjs'

export default () => {
  return {
    DEVICE_USAGE: 'Stable',
    isSocketConnected: false,
    assistantStatus: {
      isOnline: false,
      hasServerConnection: false,
    },
    deviceStats: {
      // CPU usage info for the chart
      usageCPU: {
        labels: [],
        datasets: [{ label: 'CPU', backgroundColor: '#f87979', data: [] }],
      },
      // RAM usage info for the chart
      usageRAM: {
        labels: [],
        datasets: [{ label: 'RAM', backgroundColor: '#c0f571', data: [] }],
      },
      deviceUpTime: dayjs().format('hh:mm:ss A'),
    },
  }
}
