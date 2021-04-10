<template>
  <no-ssr v-if="status.connectUrl">
    <b-card :title="$t(title)">
      <b-card-text v-for="entry in statusTbl" :key="entry.item">
        <b-row cols="12">
          <b-col cols="6" class="font-weight-bold">
            <!-- Property name -->
            {{ entry.key }}
          </b-col>
          <b-col cols="6">
            <!-- Conditional icon -->
            {{ entry.value }}
          </b-col>
        </b-row>
      </b-card-text>
    </b-card>
  </no-ssr>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default() {
        return 'Socket status'
      },
    },
    status: {
      type: Object,
      default() {
        return {}
      },
    },
  },
  computed: {
    statusTbl() {
      const { status } = this
      let err
      const items = []
      Object.keys(status).forEach((key) => {
        const value = status[key]
        if (key !== 'connectUrl' && value !== undefined && value !== '') {
          if (key.match(/Error|Failed/)) err = true
          items.push({ key, value })
        }
      })
      if (!err) {
        items.unshift({ key: 'status', value: 'OK' })
      }
      return items
    },
  },
}
</script>
