<template>
  <div class="home">
    <div>
      <router-link to="prijava">
        <b-button id="gumbSI" size="sm" class="my-2 my-sm-0">Sign in</b-button>
      </router-link>
      <h1>
        TAKE CONTROL OF YOUR MONEY
      </h1>
    </div>

    <div>
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
</template>

<script>
// @ is an alias to /src


export default {
  name: 'home',
  data(){
    return {
      props:{
        height: 85, width: 85
      }
    }
  },
  mounted(){
    document.querySelector("body").style.backgroundImage=this.pozadina;
  },
  computed: {
    pozadina(){
      return "url('"+require('../assets/pozadina11.png')+"')";
    },
    auto(){
      return require('../assets/auto.png');
    },
    hrana(){
      return require('../assets/hrana.png');
    },
    kuca(){
      return require('../assets/kuća.png');
    },
    mob(){
      return require('../assets/mob.png');
    },
    roba(){
      return require('../assets/roba.png');
    },
    shop(){
      return require('../assets/shop.png');
    },
    sport(){
      return require('../assets/sport.png');
    },
    zdravlje(){
      return require('../assets/zdravlje.png');
    }
  }

}
</script>
<style>
  #gumbSI{
    margin-right: 70px;
    top: 10px;
    float: right;
  }
</style>