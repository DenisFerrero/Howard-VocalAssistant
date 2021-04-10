export default () => {
  return {
    // States
    deviceUsageState: 'Stable',
    socketEmitCount: 0,
    // Info related to the configuration
    assistantConfig: {
      // Link has to be with http/https before
      server: '',
      uuid: '',
      isSaved: false,
      isRegistered: false,
    },
    // Device info hardware info
    deviceUsage: {
      // CPU usage info for the chart
      usageCPU: {
        labels: [],
        datasets: [
          {
            label: 'CPU',
            backgroundColor: '#f87979',
            data: [],
          },
        ],
      },
      // RAM usage info for the chart
      usageRAM: {
        labels: [],
        datasets: [
          {
            label: 'RAM',
            backgroundColor: '#c0f571',
            data: [],
          },
        ],
      },
    },
  }
}
