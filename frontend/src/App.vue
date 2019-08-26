<template>
  <div id="app">
    <nav-bar></nav-bar>
    <mdb-container>
      <!-- Content here -->
      <router-view/>

    </mdb-container>
  </div>
</template>

<script>
import NavBar from './components/NavBar'
import {mdbContainer} from 'mdbvue'
export default {
  name: 'App',
  components: {
    mdbContainer,
    'NavBar': NavBar
  },
  mounted () {
    document.querySelector('body').style.backgroundImage = this.pozadina
  },
  computed: {
    pozadina () {
      return "url('" + require('./assets/pozadina11.png') + "')"
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  height: 100%;
  min-height: 800px;
}
</style>
