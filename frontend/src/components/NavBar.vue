<template>
<div>
  <b-navbar toggleable="lg">

    <li class="nav-item" style="width: 200px; height: 200px; position: absolute; top: 10px; list-style-type: none">
      <router-link class="nav-link" style="width: 100%; height: 100%" to="/"><img src="../assets/logo.png" alt="" style="margin-left: 0px; width: 150px"></router-link>
    </li>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav style="margin-left: 150px">
      <b-navbar-nav>

        <li  v-if="auth=='loggedin'" class="nav-item" style="margin-left: 50px">
          <router-link class="nav-link" to="/profile">Profil: </router-link>
        </li>

        <li v-if="auth=='loggedin'" class="nav-item" style="margin-left: 10px; margin-top: 7px">
          {{ ime }}
        </li>
        <li v-if="auth=='loggedin'" class="nav-item" style="margin-left: 10px; margin-top: 7px">
          {{ prezime }}
        </li>
        <li v-if="auth=='loggedin'" class="nav-item" style="margin-left: 50px; margin-top: 7px">
          email: {{ email }}
        </li>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <li v-if="auth==''" class="nav-item">
            <router-link class="nav-link" to="/login">Sign in</router-link>
          </li>
          <li v-if="auth==='loggedin'" class="nav-item">
            <a class="nav-link" href="" style="color: whitesmoke" v-on:click="logout">Logout</a>
          </li>
        </b-nav-form>

      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
<!--
  <nav class="navbar navbar-expand-rg">
    <button class="navbar-toggler" type="button" data-toggle="" aria-controls="navbar1" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div style="width: 200px" id="navbar1">
      <ul class="navbar-nav">

        <li class="nav-item">
          <router-link class="nav-link" to="/">HOME</router-link>k
        </li>

        <li v-if="auth==''" class="nav-item">
          <router-link class="nav-link" to="/login">LOGIN</router-link>
        </li>

        <li v-if="auth==''" class="nav-item">
          <router-link class="nav-link" to="/registration">REGISTER</router-link>
        </li>

        <li v-if="auth==''" class="nav-item">
          <router-link class="nav-link" to="/login">Sign in</router-link>
        </li>

        <li v-if="auth=='loggedin'" class="nav-item">
          PROFILE:
        </li>

        <li v-if="auth=='loggedin'" class="nav-item">
          Ime: {{ ime }}
        </li>
        <li v-if="auth=='loggedin'" class="nav-item">
          Prezime: {{ prezime }}
        </li>
        <li v-if="auth=='loggedin'" class="nav-item">
          Email: {{ email }}
        </li>

        <li v-if="auth==='loggedin'" class="nav-item">
          <a class="nav-link" href="" v-on:click="logout">Logout</a>
        </li>

      </ul>
    </div>
  </nav>
  -->
</div>
</template>

<script>
import EventBus from './EventBus'
import jwtDecode from 'jwt-decode'
require('jwt-decode')

EventBus.$on('logged-in', test => {
  console.log(test)
})

export default {
  data () {
    return {
      auth: '',
      user: '',
      ime: '',
      prezime: '',
      email: ''
    }
  },
  methods: {
    logout () {
      localStorage.removeItem('usertoken')
    },
    init () {
      const token = localStorage.usertoken
      console.log(token)

      if (token) {
        const decoded = jwtDecode(token)

        console.log(decoded.identity.ime)
        console.log(decoded.identity.prezime)
        console.log(decoded.identity.email)

        this.ime = decoded.identity.ime
        this.prezime = decoded.identity.prezime
        this.email = decoded.identity.email
      }

      EventBus.$on('logged-in', status => {
        this.auth = status
        this.init()
      })
    }
  },
  mounted () {
    EventBus.$on('logged-in', status => {
      this.auth = status
      this.init()
    })
  },
  created () {
    this.init()
  }
}
</script>

<style>
  .nav-item {
    color: whitesmoke;
  }
  .navbar-light .navbar-nav .nav-link {
    color: whitesmoke;
  }
</style>
