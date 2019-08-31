<template>
  <div>
    <div class="d-flex justify-content-center" style="height: 200px">

    </div>
    <div class="d-flex justify-content-center" style="height: 400px; background-color: #86989B">
      <div>
        <b-container class="bv-example-row">
          <b-row>
            <b-col>
              <div id="chart">
                <apexchart type=pie width=380 :options="chartOptions" :series="series" />
              </div>
            </b-col>

            <b-col>2 of 3</b-col>
            <b-col>3 of 3</b-col>
          </b-row>
        </b-container>

      <br><br>

        <!--<mdb-pie-chart :data="pieChartData" :options="pieChartOptions" :width="600" :height="300"></mdb-pie-chart>
-->
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mdbPieChart, mdbContainer } from 'mdbvue'
import VueApexCharts from 'vue-apexcharts'
import Vue from 'vue'
Vue.component('apexchart', VueApexCharts)

export default {
  data () {
    return {
      series: [],
      chartOptions: {
        labels: ['Auto', 'Hrana', 'Kuca', 'Mobitel', 'Roba', 'Shop', 'Sport', 'Zdravlje'],
        colors: ['#43994e', '#da4b2f', '#23527b', '#4fdef3', '#8507b6', '#b67bd2', '#a64084', '#dcf3c9'],
        responsive: [{
          breakpoint: 480,
          options: {
            chart: {
              width: 200
            },
            legend: {
              position: 'bottom'
            }
          }
        }]
      }
    }
  },
  components: {
    mdbPieChart,
    mdbContainer,
    VueApexCharts
  },
  methods: {
    getTroskoviPoKategoriji () {
      const path = 'http://localhost:5000/troskovi/korisnik'
      axios.get(path)
        .then((response) => {
          var newData = []
          newData = [response.data.troskovi['auto'], response.data.troskovi['hrana'], response.data.troskovi['kuca'],
            response.data.troskovi['mobitel'], response.data.troskovi['roba'], response.data.troskovi['shop'],
            response.data.troskovi['sport'], response.data.troskovi['zdravlje']]

          console.log(newData)
          this.series = newData
        })
        .catch((error) => {
          console.error(error)
          this.getTroskoviPoKategoriji()
        })
    }
  },
  created () {
    this.getTroskoviPoKategoriji()
  }
}
</script>
