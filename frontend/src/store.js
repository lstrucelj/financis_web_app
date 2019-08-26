import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    korisnik: {},
    ukupanTrosak: 0,
    autoTrosak: null,
    hranaTrosak: null,
    kucaTrosak: null,
    mobTrosak: null,
    robaTrosak: null,
    shopTrosak: null,
    sportTrosak: null,
    zdravljeTrosak: null
  },
  mutations: {
    izracun (state, noviIznos){
      state.ukupanTrosak = parseInt(state.ukupanTrosak) + parseInt(noviIznos);
    },
    izracunKategorije (state, noviIznos, value){
      if(value===1){
        state.autoTrosak = parseInt(state.autoTrosak) + parseInt(noviIznos);
      }
      else if(value===2){
        state.hranaTrosak = parseInt(state.hranaTrosak) + parseInt(noviIznos);
      }
      else if(value===3){
        state.kucaTrosak = parseInt(state.kucaTrosak) + parseInt(noviIznos);      }
      else if(value===4){
        state.mobTrosak = parseInt(state.mobTrosak) + parseInt(noviIznos);      }
      else if(value===5){
        state.robaTrosak = parseInt(state.robaTrosak) + parseInt(noviIznos);      }
      else if(value===6){
        state.shopTrosak = parseInt(state.shopTrosak) + parseInt(noviIznos);      }
      else if(value===7){
        state.sportTrosak = parseInt(state.sportTrosak) + parseInt(noviIznos);      }
      else{
        state.zdravljeTrosak = parseInt(state.zdravljeTrosak) + parseInt(noviIznos);      }
    }
  },
  actions: {
    noviIzracun ({commit}, noviIznos){
      commit("izracun", noviIznos)
  },
    trosakKategorije({commit}, noviIznos, value){
      commit("izracunKategorije", noviIznos, value)
    }
  }
})
