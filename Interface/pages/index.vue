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
              v-if="!assistantConfig.isSaved"
              variant="danger"
              size="lg"
              :disabled="!(socketStatus.status === 'OK')"
            >
              {{ $t('Bind to server') }}
            </b-button>
            <!-- Info to register the assistant on the platform -->
            <b-card
              v-if="assistantConfig.isSaved && !assistantConfig.isRegistered"
            >
              <b-card-text>
                <small>{{ $t('Code to register the assistant') }}</small>
                <div class="font-weight-bold">
                  {{ assistantConfig.uuid }}
                </div>
              </b-card-text>
            </b-card>
            <b-card
              v-if="assistantConfig.isSaved && assistantConfig.isRegistered"
            >
              <b-card-text class="font-weight-bold">
                {{ $t('Assistant already registered to the service') }}
              </b-card-text>
            </b-card>
            <!-- Assistant server info -->
            <i18n path="Assistant server connection" tag="p">
              <template #server>
                <a :href="assistantConfig.server" target="_blank">{{
                  assistantConfig.server
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
import { mapGetters } from 'vuex'

export default {
  name: 'Index',
  data() {
    return {
      chartOptions: {
        layout: {
          padding: 20,
        },
        scales: {
          yAxes: [
            {
              ticks: {
                min: 0,
                max: 100,
                stepSize: 20,
              },
            },
          ],
        },
      },
      socketStatus: {},
    }
  },
  computed: {
    ...mapGetters({
      usageRAM: 'assistant/RamUsage',
      usageCPU: 'assistant/CpuUsage',
      assistantConfig: 'assistant/assistantConfig',
    }),
  },
  mounted() {
    this.socket = this.$nuxtSocket({
      name: 'Assistant',
      channel: '/assistant',
      persist: true,
      // Keep the socket persistent, this way will kept active when changing language
    })
  },
  methods: {
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
