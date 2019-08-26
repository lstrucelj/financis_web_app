<template>
  <nav class="navbar navbar-expand-lg rounded">
    <button class="navbar-toggler" type="button" data-toggle="collapse" aria-controls="navbar1" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div style="justify-self: right; float: right; width: 200px" id="navbar1">
      <ul class="navbar-nav">
        <!--
        <li class="nav-item">
          <router-link class="nav-link" to="/">HOME</router-link>k
        </li>

        <li v-if="auth==''" class="nav-item">
          <router-link class="nav-link" to="/login">LOGIN</router-link>
        </li>

        <li v-if="auth==''" class="nav-item">
          <router-link class="nav-link" to="/registration">REGISTER</router-link>
        </li>

        <li v-if="auth=='loggedin'" class="nav-item">
          <router-link class="nav-link" to="/profile">PROFILE</router-link>
        </li>
        -->
        <li v-if="auth==='loggedin'" class="nav-item">
          <a class="nav-link" style="justify-self: right" href="" v-on:click="logout">Logout</a>
        </li>

      </ul>
    </div>
  </nav>

</template>

<script>
import EventBus from './EventBus'

EventBus.$on('logged-in', test => {
  console.log(test)
})

export default {
  data () {
    return {
      auth: '',
      user: ''
    }
  },
  methods: {
    logout () {
      localStorage.removeItem('usertoken')
    }
  },
  mounted () {
    EventBus.$on('logged-in', status => {
      this.auth = status
    })
  }
}
</script>
