<template>
  <div>
    <div class="loginheader">
      <br><br><br><br>
      <h1 style="color: whitesmoke">LOGIN ON FINANCIS</h1>
    </div>
    <obavijest :message="message" v-if="showMessage"></obavijest>
  <div class="inputFormStyle">
    <br><br>
    <b-form @submit="onSubmit" v-if="show" class="loginform">
      <b-form-group
        id="input-group-1"
        label="Email:"
        label-for="input-1"
        description="We'll never share your email with anyone else."
      >
        <b-form-input
          id="input-1"
          v-model="loginForm.email"
          type="email"
          required
          placeholder="Enter email"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Password:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="loginForm.lozinka"
          type="password"
          required
          placeholder="Enter password"
        ></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary" style="background-color: khaki; color: black; padding: 5px 20px; margin-left: 100px">Log in</b-button>
      <br><br>
      <span style="color: whitesmoke">Don't have an account?</span><router-link to="/registration"> SIGN UP</router-link>
    </b-form>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
import Obavijest from './Obavijest.vue'
import EventBus from './EventBus'
import router from '../router'

export default {
  data () {
    return {
      access_token: '',
      loginForm: {
        email: '',
        lozinka: ''
      },
      show: true,
      showMessage: false
    }
  },
  components: {
    obavijest: Obavijest
  },
  methods: {
    prijavaKorisnika (prijavaKorisnik) {
      const path = 'http://localhost:5000/prijava'
      axios.post(path, prijavaKorisnik)
        .then((res) => {
          console.log(res.data)
          if (res.data.status === 'success') {
            localStorage.setItem('usertoken', res.data.access_token)
            console.log(res.data.access_token)
            this.loginForm.email = ''
            this.loginForm.lozinka = ''

            this.emitMethod()
            router.push({name: 'Profile'})
          }
          // if (res.status === 'success') {
          //   localStorage.setItem('usertoken', res.data)
          //   this.loginForm.email = ''
          //   this.loginForm.lozinka = ''
          //   this.showMessage = true
          //   router.push({name: 'Profile'})
          // }

          // this.message = 'Korisnik prijavljen!'
          // console.log('Korisnik prijavljen!')
          // this.showMessage = true
          // this.push('/troskovi')
        })
        .catch((error) => {
          this.message = 'Pogresno upisan email ili lozinka!'
          this.showMessage = true
          console.log(error)
        })
    },
    emitMethod () {
      EventBus.$emit('logged-in', 'loggedin')
    },
    onSubmit (evt) {
      evt.preventDefault()
      const prijavaKorisnik = {
        email: this.loginForm.email,
        lozinka: this.loginForm.lozinka
      }
      this.prijavaKorisnika(prijavaKorisnik)
      // window.location = '/'
      // TODO: redirect to home
    }
  },
  created () {

  }
}
</script>

<style>
  .inputFormStyle{
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
  .loginform{
    width: 300px;
    margin: auto;
  }
</style>
