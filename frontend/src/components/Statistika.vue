<template>
  <div>
    <div class="d-flex justify-content-center" style="height: 200px">

    </div>
    <div class="d-flex justify-content-center" style="height: 420px; background-color: #86989B">
      <div>
        <div>
          <b-tabs content-class="mt-3" style="width: 1110px">
            <b-tab title="Korisnik" active style="justify-content: center">
              <p>Statistika po korisniku</p>
              <br>
                <b-container class="" style="width: 700px">
                  <b-row>
                    <b-col style="width: 600px">
                      <div id="chart">
                        <apexchart type=pie width=300 :options="chartOptions" :series="series" />
                      </div>
                    </b-col>

                    <b-col style="width: 600px; margin-left: 100px">
                      <p class="lead"><img src="../assets/auto.png" style="width: 30px"> {{ trosak_po_kategoriji_korisnik[0] | filterValuta}}</p>
                      <p class="lead"><img src="../assets/hrana.png" style="width: 30px"> {{ trosak_po_kategoriji_korisnik[1] | filterValuta}}</p>
                      <p class="lead"><img src="../assets/kuća.png" style="width: 30px"> {{ trosak_po_kategoriji_korisnik[2] | filterValuta}}</p>
                      <p class="lead"><img src="../assets/mob.png" style="width: 30px"> {{ trosak_po_kategoriji_korisnik[3] | filterValuta}}</p>
                      <p class="lead"><img src="../assets/roba.png" style="width: 30px"> {{ trosak_po_kategoriji_korisnik[4] | filterValuta}}</p>
                      <p class="lead"><img src="../assets/shop.png" style="width: 30px"> {{ trosak_po_kategoriji_korisnik[5] | filterValuta}}</p>
                      <p class="lead"><img src="../assets/sport.png" style="width: 30px"> {{ trosak_po_kategoriji_korisnik[6] | filterValuta}}</p>
                      <p class="lead"><img src="../assets/zdravlje.png" style="width: 30px"> {{ trosak_po_kategoriji_korisnik[7] | filterValuta}}</p>
                    </b-col>

                  </b-row>
                </b-container>

            </b-tab>

            <b-tab title="Grupa" active style="justify-content: center">
              <p>Statistika po grupi</p>
              <br>

              <b-container class="" style="width: 700px">
                <b-row style="margin-top: -20px">
                  <b-col style="width: 600px; float: left; margin-left: -200px"  >
                    <b-form-group id="form-grupa"
                                  label="Grupa korisnika:"
                                  label-for="form-grupa-input">
                      <b-form-select v-model="imeGrupe" :options="options" style="width: 150px"></b-form-select>
                      <b-button type="submit" variant="primary" v-on:click="getTroskoviPoKorisnicimaGrupe(imeGrupe)">Prikaži</b-button>
                    </b-form-group>

                  </b-col>

                  <b-col style="width: 600px">

                    <apexchart type=line width=450 :options="chartOptions" :series="groupseries" />

                  </b-col>

                </b-row>
              </b-container>

            </b-tab>

          </b-tabs>
        </div>
      </div>
        <!--
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

        <mdb-pie-chart :data="pieChartData" :options="pieChartOptions" :width="600" :height="300"></mdb-pie-chart>

      </div>
      -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mdbPieChart, mdbContainer } from 'mdbvue'
import VueApexCharts from 'vue-apexcharts'
import Vue from 'vue'
import jwtDecode from 'jwt-decode'
require('jwt-decode')
Vue.component('apexchart', VueApexCharts)

Vue.filter('filterValuta', function (value) {
  return value + ' kn'
})

export default {
  data () {
    return {
      options: [],
      groupseries: [],
      firstGroup: '',
      imeGrupe: '',
      emailKorisnika: '',
      korisnikgrupa: '',

      grupe: [],
      trosak_po_kategoriji_korisnik: [],
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
    getGrupeKorisnika () {
      const path = 'http://localhost:5000/korisnik/grupe'
      const req = {
        email: this.emailKorisnika
      }
      axios.post(path, req)
        .then((response) => {
          this.options = response.data.options
          console.log(this.options)
          this.firstGroup = this.options[0].value
          console.log(this.firstGroup)
          this.imeGrupe = this.firstGroup
          this.getTroskoviPoKorisnicimaGrupe(this.firstGroup)
        })
        .catch((error) => {
          console.error(error)
          this.getGrupeKorisnika()
        })
    },

    getTroskoviPoKorisnicimaGrupe (imeGrupe) {
      const path = 'http://localhost:5000/grupa/korisnici'
      const req = {
        ime: imeGrupe
      }
      axios.post(path, req)
        .then((response) => {
          this.groupseries = response.data.series
        })
        .catch((error) => {
          console.error(error)
          this.getTroskoviPoKorisnicimaGrupe(imeGrupe)
        })
    },
    getTroskoviPoKategoriji () {
      const path = 'http://localhost:5000/troskovi/korisnik'
      const req = {
        email: this.emailKorisnika
      }
      axios.post(path, req)
        .then((response) => {
          var newData = []
          newData = [response.data.troskovi['auto'], response.data.troskovi['hrana'], response.data.troskovi['kuca'],
            response.data.troskovi['mobitel'], response.data.troskovi['roba'], response.data.troskovi['shop'],
            response.data.troskovi['sport'], response.data.troskovi['zdravlje']]

          console.log(newData)
          this.series = newData

          this.trosak_po_kategoriji_korisnik = newData

          console.log(this.trosak_po_kategoriji_korisnik)
        })
        .catch((error) => {
          console.error(error)
          this.getTroskoviPoKategoriji()
        })
    }
  },
  created () {
    const token = localStorage.usertoken
    console.log(token)
    if (token) {
      const decoded = jwtDecode(token)
      this.emailKorisnika = decoded.identity.email
      console.log(this.emailKorisnika)
    }

    this.getGrupeKorisnika()
    this.getTroskoviPoKategoriji()
    this.getTroskoviPoKorisnicimaGrupe(this.firstGroup)
  }
}
</script>

<style>
  .lead {
    font-family: 'Lucida Grande', 'Lucida Sans Unicode', 'Geneva', 'Verdana', sans-serif;
    font-size: medium;
    margin-bottom: 5px;
    text-align: left;
  }
</style>
