<script>
import { Line, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  name: 'UsageChart',
  extends: Line,
  mixins: [reactiveProp],
  mounted() {
    this.renderChart(this.chartData, this.options)
  },
}
</script>
