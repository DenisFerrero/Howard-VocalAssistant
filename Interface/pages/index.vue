<template>
  <b-container class="mb-3">
    <b-row align-v="center">
      <b-col cols="12 pt-3">
        <b-row cols="12" class="border p-3 bg-light">
          <!-- Title -->
          <b-col cols="12" class="text-center mb-2">
            <h3>
              {{ $t('Vocal Assistant configuration', { before: 'Howard -' }) }}
            </h3>
            <!-- Language switch component -->
            <span class="pull-right">
              <LangToggle />
            </span>
          </b-col>
          <!-- Connection property listing -->
          <b-col cols="12" md="6">
            <SocketStatus :status="socketStatus" />
          </b-col>
          <b-col cols="12" md="6" class="text-center mt-2 mt-md-0">
            <!-- Button to create a new record on the db -->
            <!-- Disabled if socket is not connected and hide if assistant already saved on DB -->
            <b-button
              v-if="!assistantConfigInfo.isSaved"
              variant="danger"
              size="lg"
              :disabled="!connInfo.isSocketConnected"
            >
              {{ $t('Bind to server') }}
            </b-button>
            <!-- Info to register the assistant on the platform -->
            <b-card
              v-if="
                assistantConfigInfo.isSaved && !assistantConfigInfo.isRegistered
              "
            >
              <b-card-text>
                <small>{{ $t('Code to register the assistant') }}</small>
                <div class="font-weight-bold">
                  {{ assistantConfigInfo.uuid }}
                </div>
              </b-card-text>
            </b-card>
            <b-card
              v-if="
                assistantConfigInfo.isSaved && assistantConfigInfo.isRegistered
              "
            >
              <b-card-text class="font-weight-bold">
                {{ $t('Assistant already registered to the service') }}
              </b-card-text>
            </b-card>
            <!-- Assistant server info -->
            <i18n path="Assistant server connection" tag="p">
              <template #server>
                <a :href="assistantConfigInfo.server" target="_blank">{{
                  assistantConfigInfo.server
                }}</a>
              </template>
            </i18n>
          </b-col>
          <b-col cols="12" md="6" class="mt-3 mt-md-0">
            <UsageChart
              :chart-data="usageCPU"
              :options="chartOptions"
              :height="200"
            />
          </b-col>
          <b-col cols="12" md="6">
            <UsageChart
              :chart-data="usageRAM"
              :options="chartOptions"
              :height="200"
            />
          </b-col>
        </b-row>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  data() {
    return {
      chartOptions: {},
    }
  },
  computed: {
    ...mapGetters({
      usageRAM: 'assistant/deviceCPU',
      usageCPU: 'assistant/deviceRAM',
      connInfo: 'assistant/connectionInfo',
      assistantConfigInfo: 'assistant/assistantConfigInfo',
    }),
  },
  mounted() {
    // Before running clear all Intervals
    // (need to do this cause when changing language will be added a new Interval)
    // https://gist.github.com/mcenirm/4165198
    ;(function (w) {
      w = w || window
      let i = w.setInterval(function () {}, 100000)
      while (i >= 0) {
        w.clearInterval(i--)
      }
    })(/* window */)

    setInterval(() => {
      this.saveDeviceStats([Math.random() * 10, Math.random() * 10])
    }, 1000)
    // this.socket = this.$nuxtSocket({
    //   name: 'Assistant',
    //   channel: '/assistant',
    // })
  },
  methods: {
    ...mapActions({
      saveDeviceStats: 'assistant/parseDeviceStats',
    }),
    fromKeyToName(key) {
      switch (key) {
        case 'isOnline': {
          return 'Online'
        }
        case 'hasServerConnection': {
          return 'Server connection'
        }
        case 'isSocketConnected': {
          return 'Socket connection'
        }
        default: {
          return key
        }
      }
    },
  },
}
</script>
