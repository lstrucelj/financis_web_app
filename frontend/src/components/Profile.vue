<template>
  <div>

    <div style="width: 200px; height: 200px; position: fixed; text-align: center; left: 0px; top:580px">
      <b-button type="button" style="background-color: transparent;" href="#/statistika"><img src="../assets/stat.png" alt="" style="margin-left: 0px"></b-button>
    </div>

    <div style="width: 200px; height: 400px; position: fixed; text-align: center; right: 0px; top: 270px">

      <button type="button" class="btn btn-success btn-circle btn-xl " v-b-modal.grupa-modal style="border-color: navy;color: navy;">Kreiraj grupu</button>
      <button type="button" class="btn btn-success btn-circle btn-xl" v-b-modal.dodajkorisnika-modal style="border-color: goldenrod;color: darkgoldenrod;">Dodaj korisnika u grupu</button>
      <button type="button" class="btn btn-success btn-circle btn-xl" v-b-modal.kreirajtrosak-modal>Kreiraj trosak</button>

    </div>
    <div class="col-sm-10" style="margin-left: 85px">
      <obavijest :message="message" v-if="showMessage"></obavijest>
    </div>

    <div class="" >
      <div class="" >
        <div class="" style="position: fixed; text-align: center; left: -50px; top:220px; background-color: #86989B; margin-left: 85px; width: 200px; font-size: 10px; " >
          <br><br>
          <h4>Moje grupe</h4>
          <br>

          <div>
            <b-table striped hover :items="popisgrupa" :fields="fieldsGrupe"></b-table>
          </div>
        </div>
      </div>
    </div>
    <br><br><br><br>
  <div class="container">

    <div class="row">
      <div class="col-sm-10" style="background-color: #86989B; margin-left: 85px">

        <br><br>
        <h1>Ispis svih troškova</h1>
        <br>

        <table class="table table-hover">
          <thead>
          <tr>
            <th scope="col">Naziv</th>
            <th scope="col">Kategorija</th>
            <th scope="col">Iznos</th>
            <th></th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(trosak, index) in troskovi" :key="index">
            <td>{{ trosak.naziv }}</td>
            <td>{{ trosak.kategorija | filterKategorija }}</td>
            <td>{{ trosak.iznos | filterValuta }}</td>
            <td>
              <div class="btn-group" role="group">

                <button type="button" class="btn btn-danger btn-sm" @click="onIzbrisiTrosak(trosak)">Delete</button>
              </div>
            </td>
          </tr>
          </tbody>
        </table>

<!--
        <div>
          <b-table striped hover :items="troskovi" :fields="fields"></b-table>
        </div>

        -->

      </div>
    </div>

    <b-modal class="" ref="kreirajGrupu"
             id="grupa-modal"
             title="Kreiraj novu grupu"
             hide-footer>
      <b-form @submit="onSubmitKreirajGrupu" @reset="onResetKreirajGrupu" class="w-100">
        <b-form-group id="form-naziv-group"
                      label="Ime grupe:"
                      label-for="form-naziv-input">
          <b-form-input id="form-naziv-input"
                        type="text"
                        v-model="kreirajGrupu.ime"
                        required
                        placeholder="Unesi naziv">
          </b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

    <b-modal class="" ref="dodajKorisnikaUGrupu"
             id="dodajkorisnika-modal"
             title="Dodaj korisnika u grupu"
             hide-footer>
      <b-form @submit="onSubmitDodajKorUGrupu" @reset="onResetDodajKorUGrupu" class="w-100">
        <b-form-group id="form-naziv-dodajkorisnika-email"
                      label="Email korisnika:"
                      label-for="form-naziv-input">
          <b-form-input id="form-naziv-dodajkorisnika-input"
                        type="email"
                        v-model="dodajKorisnikaUGrupu.email"
                        required
                        placeholder="Unesi email korisnika">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-naziv-dodajkorisnika-grupa"
                      label="Naziv grupe:"
                      label-for="form-naziv-grupe-input">
          <b-form-input id="form-naziv-dodajkorisnika-email-input"
                        type="text"
                        v-model="dodajKorisnikaUGrupu.imeGrupe"
                        required
                        placeholder="Unesi ime grupe">
          </b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

    <b-modal class="" ref="kreirajTrosak"
             id="kreirajtrosak-modal"
             title="Kreiraj novi trosak"
             hide-footer>
      <b-form @submit="onSubmitKreirajTrosak" @reset="onResetKreirajTrosak" class="w-100">
        <b-form-group id="form-naziv-trosak-group"
                      label="Ime troska:"
                      label-for="form-naziv-trosak-input">
          <b-form-input id="form-naziv-trosak-input"
                        type="text"
                        v-model="kreirajTrosak.naziv"
                        required
                        placeholder="Unesi ime troska">
          </b-form-input>
        </b-form-group>

        <b-form-group id="form-naziv-iznos-group"
                      label="Iznos troska:"
                      label-for="form-iznos-trosak-input">
          <b-form-input id="form-iznos-trosak-input"
                        type="number"
                        v-model="kreirajTrosak.iznos"
                        required
                        placeholder="Unesi iznos troska">
          </b-form-input>
        </b-form-group>

        <b-form-group id="form-kategorija-trosak-group"
                      label="Kategorija troska:"
                      label-for="form-kategorija-trosak-input">

          <b-form-select v-model="kreirajTrosak.kategorija" :options="options"></b-form-select>

        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

  </div>
  </div>
</template>

<script>
import axios from 'axios'
import Obavijest from './Obavijest.vue'
import Vue from 'vue'
import jwtDecode from 'jwt-decode'
require('jwt-decode')

Vue.filter('filterKategorija', function (value) {
  value = parseInt(value)
  switch (value) {
  case 1: return 'Auto'
  case 2: return 'Hrana'
  case 3: return 'Kuca'
  case 4: return 'Mobitel'
  case 5: return 'Roba'
  case 6: return 'Shop'
  case 7: return 'Sport'
  case 8: return 'Zdravlje'
  }
})

Vue.filter('filterValuta', function (value) {
  return value + ' HRK'
})

export default {
  data () {
    return {
      options: [
        { value: null, text: 'Izaberite kategoriju troska' },
        { value: '1', text: 'Auto' },
        { value: '2', text: 'Hrana' },
        { value: '3', text: 'Kuca' },
        { value: '4', text: 'Mobitel' },
        { value: '5', text: 'Roba' },
        { value: '6', text: 'Shop' },
        { value: '7', text: 'Sport' },
        { value: '8', text: 'Zdravlje' }
      ],
      emailKorisnika: '',
      popisgrupa: [],
      fieldsGrupe: [
        {
          key: 'ime',
          sortable: true,
          thStyle: {
            display: 'none'
          }
        }
      ],
      fields: [
        {
          key: 'naziv',
          sortable: true
        },
        {
          key: 'kategorija',
          sortable: true
        },
        {
          key: 'iznos',
          sortable: true
        }
      ],
      troskovi: [],
      kreirajGrupu: {
        ime: ''
      },
      dodajKorisnikaUGrupu: {
        email: '',
        imeGrupe: ''
      },
      kreirajTrosak: {
        naziv: '',
        iznos: '',
        kategorija: '',
        korisnik: ''
      },
      message: '',
      showMessage: false
    }
  },
  components: {
    obavijest: Obavijest
  },
  methods: {
    getGrupeKorisnika () {
      const path = 'http://localhost:5000/korisnik/grupa'

      const nova = {
        email: this.emailKorisnika
      }

      axios.post(path, nova)
        .then((response) => {
          this.popisgrupa = response.data.grupe
        })
        .catch((error) => {
          console.error(error)
        })
    },
    getTroskovi () {
      const path = 'http://localhost:5000/korisnik/trosak'

      const nova = {
        email: this.emailKorisnika
      }

      axios.post(path, nova)
        .then((response) => {
          this.troskovi = response.data.troskovi
        })
        .catch((error) => {
          console.error(error)
        })
    },
    onSubmitKreirajGrupu (evt) {
      evt.preventDefault()
      this.$refs.kreirajGrupu.hide()

      const token = localStorage.usertoken
      console.log(token)
      if (token) {
        const decoded = jwtDecode(token)
        console.log(decoded)
      }

      const novaGrupa = {
        ime: this.kreirajGrupu.ime
      }

      this.postKreirajGrupu(novaGrupa)
    },
    onResetKreirajGrupu (evt) {
      evt.preventDefault()
      this.$refs.kreirajGrupu.hide()
    },
    postKreirajGrupu (novaGrupa) {
      const path = 'http://localhost:5000/grupa'
      axios.post(path, novaGrupa)
        .then(() => {
          this.message = 'Grupa kreirana'
          this.showMessage = true

          const korUGrupu = {
            email: this.emailKorisnika,
            imeGrupe: this.kreirajGrupu.ime
          }

          this.postDodajKorUGrupu(korUGrupu)
        })
        .catch((error) => {
          console.log(error)
        })
    },

    //
    onSubmitDodajKorUGrupu (evt) {
      evt.preventDefault()
      this.$refs.dodajKorisnikaUGrupu.hide()

      const korUGrupu = {
        email: this.dodajKorisnikaUGrupu.email,
        imeGrupe: this.dodajKorisnikaUGrupu.imeGrupe
      }

      this.postDodajKorUGrupu(korUGrupu)
    },
    onResetDodajKorUGrupu (evt) {
      evt.preventDefault()
      this.$refs.dodajKorisnikaUGrupu.hide()
    },

    postDodajKorUGrupu (korUGrupu) {
      const path = 'http://localhost:5000/grupa/korisnik'
      axios.post(path, korUGrupu)
        .then((res) => {
          this.message = res.data.message
          this.showMessage = true
          this.getGrupeKorisnika()
        })
        .catch((error) => {
          console.log(error)
          this.getGrupeKorisnika()
        })
    },
    //
    onSubmitKreirajTrosak (evt) {
      evt.preventDefault()
      this.$refs.kreirajTrosak.hide()

      const token = localStorage.usertoken
      console.log(token)
      if (token) {
        const decoded = jwtDecode(token)
        console.log(decoded)
        console.log('korisnik email:')
        console.log(decoded.identity.email)

        const noviTrosak = {
          naziv: this.kreirajTrosak.naziv,
          iznos: this.kreirajTrosak.iznos,
          kategorija: this.kreirajTrosak.kategorija,
          korisnik: decoded.identity.email
        }

        this.postKreirajTrosak(noviTrosak)
      }
    },
    onResetKreirajTrosak (evt) {
      evt.preventDefault()
      this.$refs.kreirajTrosak.hide()
    },
    postKreirajTrosak (noviTrosak) {
      const path = 'http://localhost:5000/troskovi'
      axios.post(path, noviTrosak)
        .then(() => {
          this.message = 'Trosak kreiran'
          this.showMessage = true
          this.getTroskovi()
        })
        .catch((error) => {
          console.log(error)
          this.message = 'Pogresan unos!'
          this.getTroskovi()
        })
    },
    onIzbrisiTrosak (trosak) {
      this.izbrisiTrosak(trosak.id)
    },
    izbrisiTrosak (trosakID) {
      const path = `http://localhost:5000/troskovi/${trosakID}`
      axios.delete(path)
        .then(() => {
          this.getTroskovi()
          this.message = 'Trosak izbrisan!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
          this.getTroskovi()
        })
    }
  },
  //
  created () {
    const token = localStorage.usertoken
    console.log(token)
    if (token) {
      const decoded = jwtDecode(token)
      this.emailKorisnika = decoded.identity.email
      console.log(this.emailKorisnika)
    }

    this.getTroskovi()
    this.getGrupeKorisnika()

    this.kreirajTrosak.kategorija = null
  }
}
</script>

<style>
  .btn-circle.btn-xl {
    width: 120px;
    height: 120px;
    padding: 10px 16px;
    border-radius: 50%;
    font-size: 17px;
    line-height: 1.33;
    margin-top: 20px;
    background-color: #cccccc;
    border-color: #9C1A1C;
    border-width: 7px;
    color: darkred;
  }

  .btn-circle {
    width: 30px;
    height: 30px;
    padding: 6px 0px;
    border-radius: 15px;
    text-align: center;
    font-size: 12px;
    line-height: 1.42857;
  }

</style>
