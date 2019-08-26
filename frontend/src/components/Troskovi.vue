<template>
  <div class="container">

    <div class="row">
      <div class="col-sm-10">
        <h1>Troskovi</h1>
        <hr>
        <br><br>

        <obavijest :message="message" v-if="showMessage"></obavijest>

        <button type="button" class="btn btn-success btn-sm" v-b-modal.trosak-modal>Dodaj Trosak</button>

        <br><br>
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
            <td>{{ trosak.naziv}}</td>
            <td>{{ trosak.kategorija}}</td>
            <td>{{ trosak.iznos | valuta}}</td>
            <td>
              <div class="btn-group" role="group">

                <button type="button" class="btn btn-warning btn-sm" v-b-modal.izmjena-modal @click="promjenaTroska(trosak)">Update</button>

                <button type="button" class="btn btn-danger btn-sm" @click="onIzbrisiTrosak(trosak)">Delete</button>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>

    <b-modal class="formaUnos" ref="dodajTrosakModal"
             id="trosak-modal"
             title="Dodaj novi trosak"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-naziv-group"
                      label="Naziv:"
                      label-for="form-naziv-input">
          <b-form-input id="form-naziv-input"
                        type="text"
                        v-model="dodajTrosakForm.naziv"
                        required
                        placeholder="Unesi naziv">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-kategorija-group"
                      label="Kategorija:"
                      label-for="form-kategorija-input">
          <b-form-input id="form-kategorija-input"
                        type="text"
                        v-model="dodajTrosakForm.kategorija"
                        required
                        placeholder="Unesi kategoriju">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-iznos-group"
                      label="Iznos:"
                      label-for="form-iznos-input">
          <b-form-input id="form-iznos-input"
                        type="number"
                        v-model="dodajTrosakForm.iznos"
                        required
                        placeholder="Unesi iznos">
          </b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

    <b-modal ref="izmjTroskaModal"
             id="izmjena-modal"
             title="Izmjena troska"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-title-edit-group"
                      label="Naziv:"
                      label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="izmjTrosakForm.naziv"
                        required
                        placeholder="Unesi novi naziv">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-edit-group"
                      label="Kategorija:"
                      label-for="form-author-edit-input">
          <b-form-input id="form-author-edit-input"
                        type="text"
                        v-model="izmjTrosakForm.kategorija"
                        required
                        placeholder="Unesi novu kategoriju">
          </b-form-input>
        </b-form-group>

        <b-form-group id="form-author-edit-group"
                      label="Iznos:"
                      label-for="form-author-edit-input">
          <b-form-input id="form-author-edit-input"
                        type="text"
                        v-model="izmjTrosakForm.iznos"
                        required
                        placeholder="Unesi novi iznos">
          </b-form-input>
        </b-form-group>

        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>

  </div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'
import Obavijest from './Obavijest.vue'

Vue.filter('valuta', function (value) {
  return value.toFixed(2) + 'HRK'
})

export default {
  data () {
    return {
      troskovi: [],
      dodajTrosakForm: {
        naziv: '',
        kategorija: '',
        iznos: 0
      },
      message: '',
      showMessage: false,
      izmjTrosakForm: {
        id: '',
        naziv: '',
        kategorija: '',
        iznos: 0
      }
    }
  },
  components: {
    obavijest: Obavijest
  },
  methods: {
    dohvatiTroskove () {
      const path = 'http://localhost:5000/troskovi'
      axios.get(path)
        .then((response) => {
          this.troskovi = response.data.troskovi
        })
        .catch((error) => {
          console.error(error)
        })
    },
    dodajTrosak (noviTrosak) {
      const path = 'http://localhost:5000/troskovi'
      axios.post(path, noviTrosak)
        .then(() => {
          this.dohvatiTroskove()
          this.message = 'Dodan trosak'
          this.showMessage = true
        })
        .catch((error) => {
          console.log(error)
          this.dohvatiTroskove()
        })
    },

    promjenaTroska (trosak) {
      this.izmjTrosakForm = trosak
      this.izmjTrosakForm.id = trosak.id
    },

    initForm () {
      this.dodajTrosakForm.naziv = ''
      this.dodajTrosakForm.kategorija = ''
      this.dodajTrosakForm.iznos = ''
      this.izmjTrosakForm.id = ''
      this.izmjTrosakForm.naziv = ''
      this.izmjTrosakForm.kategorija = ''
      this.izmjTrosakForm.iznos = ''
    },
    onSubmit (evt) {
      evt.preventDefault()
      this.$refs.dodajTrosakModal.hide()
      const noviTrosak = {
        naziv: this.dodajTrosakForm.naziv,
        kategorija: this.dodajTrosakForm.kategorija,
        iznos: this.dodajTrosakForm.iznos
      }
      this.dodajTrosak(noviTrosak)
      this.initForm()
    },
    onReset (evt) {
      evt.preventDefault()
      this.$refs.dodajTrosakModal.hide()
      this.initForm()
    },

    onSubmitUpdate (evt) {
      evt.preventDefault()
      this.$refs.izmjTroskaModal.hide()
      const noviTrosak = {
        id: this.izmjTrosakForm.id,
        naziv: this.izmjTrosakForm.naziv,
        kategorija: this.izmjTrosakForm.kategorija,
        iznos: this.izmjTrosakForm.iznos
      }
      this.zamjeniTrosak(noviTrosak, this.izmjTrosakForm.id)
    },

    onResetUpdate (evt) {
      evt.preventDefault()
      this.$refs.izmjTroskaModal.hide()
      this.initForm()
      this.dohvatiTroskove() // why?
    },

    zamjeniTrosak (noviTrosak, trosakID) {
      const path = `http://localhost:5000/troskovi/${trosakID}`
      axios.put(path, noviTrosak)
        .then(() => {
          this.dohvatiTroskove()
          this.message = 'Trosak izmijenjen'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
          this.dohvatiTroskove()
        })
    },

    izbrisiTrosak (trosakID) {
      const path = `http://localhost:5000/troskovi/${trosakID}`
      axios.delete(path)
        .then(() => {
          this.dohvatiTroskove()
          this.message = 'Trosak izbrisan!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
          this.dohvatiTroskove()
        })
    },
    onIzbrisiTrosak (trosak) {
      this.izbrisiTrosak(trosak.id)
    }
  },
  created () {
    this.dohvatiTroskove()
  }
}
</script>

<style>
  .container{
    text-align: left;
  }
  .formaUnos{
    text-align: left;
  }
</style>
