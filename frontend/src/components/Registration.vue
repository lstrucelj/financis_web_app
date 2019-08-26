<template>
  <div>
    <div class="loginheader">
      <br><br><br><br>
      <h1 style="color: whitesmoke">CREATE YOUR ACCOUNT</h1>
    </div>
    <obavijest :message="message" v-if="showMessage"></obavijest>
    <div class="inputFormStyleReg">

      <br>
      <b-form @submit="onSubmit" class="form">

        <b-container>
          <b-row>
            <b-col>
        <b-form-group
          id="input-group-1"
          label="First name:"
          label-for="input-1"
        >
          <b-form-input
            id="input-q"
            v-model="registrationForm.ime"
            type="text"
            required
            placeholder="Enter first name"
          ></b-form-input>
        </b-form-group>
            </b-col>

            <b-col>
        <b-form-group
          id="input-group-1"
          label="Last name:"
          label-for="input-1"
        >
          <b-form-input
            id="input-w"
            v-model="registrationForm.prezime"
            type="text"
            required
            placeholder="Enter last name"
          ></b-form-input>
        </b-form-group>
              </b-col>
          </b-row>
        </b-container>

        <b-form-group id="input-group-2" label="Email:" label-for="input-2">
          <b-form-input
            id="input-e"
            v-model="registrationForm.email"
            type="email"
            required
            placeholder="Enter email"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="Password:" label-for="input-2">
          <b-form-input
            id="input-r"
            v-model="registrationForm.lozinka"
            type="password"
            required
            placeholder="Enter password"
          ></b-form-input>
        </b-form-group>
        <br>
        <b-button type="submit" variant="primary" style="background-color: khaki; color: black; padding: 5px 10px; margin-left: 200px">Create your account</b-button>
        <br>
        <span style="color: whitesmoke; margin-left: 190px; margin-top: 15px">Have an account?</span><router-link to="/login"> SIGN IN</router-link>
      </b-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Obavijest from './Obavijest.vue'
import router from '../router'

export default {
  data () {
    return {
      registrationForm: {
        ime: '',
        prezime: '',
        email: '',
        lozinka: ''
      },
      message: '',
      showMessage: false
    }
  },
  components: {
    obavijest: Obavijest
  },
  methods: {
    dodajKorisnika (noviKorisnik) {
      const path = 'http://localhost:5000/korisnici'
      axios.post(path, noviKorisnik)
        .then((res) => {
          router.push({ name: 'Login' })
          this.message = res.data.message
          this.showMessage = true
          // this.$router.push('/login')
          // this.$router.go()
        })
        .catch((error) => {
          this.message = 'Korisnik nije kreiran - error!'
          this.showMessage = true
          console.log(error)
        })
    },
    onSubmit (evt) {
      evt.preventDefault()
      const noviKorisnik = {
        ime: this.registrationForm.ime,
        prezime: this.registrationForm.prezime,
        email: this.registrationForm.email,
        lozinka: this.registrationForm.lozinka
      }
      this.dodajKorisnika(noviKorisnik)
      // window.location = '/login'
      // TODO: redirect to login
    }
  }

}
</script>

<style>
  .inputFormStyleReg{
    margin: auto;
    width: 700px;
    height: 400px;
    background-color: #86989B;
    text-align: left;
  }
  .loginheader{
    width: 700px;
    height: 200px;
    margin: auto;
  }
  .form{
    width: 600px;
    margin: auto;
  }
  .container{
    padding: 0px;
  }
</style>
