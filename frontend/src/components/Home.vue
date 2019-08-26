<template>
<div>
<!--

  <p>Random number from backend: {{ randomNumber }}</p>
  <button @click="getRandom">New random number</button>
  <br>
  <br>
  <button type="button" class="btn btn-danger btn-sm" @click="moveToTroskovi()">Pregled troskova</button>
    link to /troskovi
      <router-link to="/troskovi">Test</router-link>
  -->
  <div>

    <div class="signin">
      <router-link to="/login">Sign in</router-link>
    </div>
    <div class="main">
      <h1 style="color: whitesmoke; margin-top: 190px; font-size: 50px">
        TAKE CONTROL OF YOUR MONEY
      </h1>

      <div class="imagelist">
        <b-img v-bind="props" :src="auto" alt="auto"></b-img>
        <b-img v-bind="props" :src="hrana" alt="hrana"></b-img>
        <b-img v-bind="props" :src="kuca" alt="kuća"></b-img>
        <b-img v-bind="props" :src="mob" alt="mob"></b-img>
        <b-img v-bind="props" :src="roba" alt="roba"></b-img>
        <b-img v-bind="props" :src="shop" alt="shop"></b-img>
        <b-img v-bind="props" :src="sport" alt="sport"></b-img>
        <b-img v-bind="props" :src="zdravlje" alt="zdravlje"></b-img>
      </div>
    </div>

  </div>
</div>
</template>

<script>
import axios from 'axios'
import router from '../router'

export default {
  name: 'home',
  data () {
    return {
      randomNumber: 0,
      props: {
        height: 85, width: 85
      }
    }
  },
  computed: {
    auto () {
      return require('../assets/auto.png')
    },
    hrana () {
      return require('../assets/hrana.png')
    },
    kuca () {
      return require('../assets/kuća.png')
    },
    mob () {
      return require('../assets/mob.png')
    },
    roba () {
      return require('../assets/roba.png')
    },
    shop () {
      return require('../assets/shop.png')
    },
    sport () {
      return require('../assets/sport.png')
    },
    zdravlje () {
      return require('../assets/zdravlje.png')
    }
  },

  methods: {
    getRandom () {
      // this.randomNumber = this.getRandomInt(1, 100)
      this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend () {
      const path = `http://localhost:5000/api/random`
      axios.get(path)
        .then(response => {
          this.randomNumber = response.data.randomNumber
        })
        .catch(error => {
          console.log(error)
        })
    },
    moveToTroskovi () {
      router.push('/troskovi')
    }
  },
  created () {
    this.getRandom()
  }
}
</script>

<style>

  .signin{
    width: 100px;
    justify-self: right;
    float: right;
    margin-right: 50px;
    margin-top: 25px;
    font-size: 20px;
    color: whitesmoke;
  }
  .header {
       float: left;
       width: 100%;
       height: 80px;
     }

  .main {
    float: left;
    width: 100%;
    height: 500px;
  }
  .imagelist{
    margin-top: 120px;
  }
  img{
    margin-left: 25px;
  }
</style>
