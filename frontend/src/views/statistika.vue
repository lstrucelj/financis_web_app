<template>
    <div id="statistika">
        <div style="z-index: 99; position: absolute; margin: 60px auto 0 40%">
            <b-button-group>
                <b-button @click="toggle(1)" variant="info">
                    KATEGORIJE
                </b-button>
                <b-button @click="toggle(2)" variant="info">
                    KORISNICI
                </b-button>
            </b-button-group>
        </div>

        <div id="korisnici" v-bind:style="{'width':(korisniciShow ? '30%' : '0') }">
            <ul style="list-style-type: none; padding: 0; margin-top: 2%">
                <li>
                    <b-img v-bind="props" :src="roba" alt="roba"></b-img>
                    <h4 class="item">3412,33kn</h4>
                </li>
                <!--
                <li v-for="(korisnik, index) in korisnici" key="index">
                  <h2>
                      korisnik.ime
                  </h2>
                    <h4>
                        korisnik.iznos
                    </h4>

                </li>
                -->
            </ul>
        </div>

        <div id="kategorije" v-bind:style="{'width':(kategorijeShow ? '30%' : '0') }">
            <ul style="list-style-type: none; padding: 0; margin-top: 2%">
                <li>
                    <b-img v-bind="props" :src="auto" alt="auto"></b-img>
                    <h4 class="item">312,33kn</h4>
                </li>
                <li>
                    <b-img v-bind="props" :src="hrana" alt="hrana"></b-img>
                    <h4 class="item">312,33kn</h4>
                </li>
                <li>
                    <b-img v-bind="props" :src="kuca" alt="kuća"></b-img>
                    <h4 class="item">312,33kn</h4>
                </li>
                <li>
                    <b-img v-bind="props" :src="mob" alt="mob"></b-img>
                    <h4 class="item">3412,33kn</h4>
                </li>
                <li>
                    <b-img v-bind="props" :src="roba" alt="roba"></b-img>
                    <h4 class="item">3412,33kn</h4>
                </li>
                <li>
                    <b-img v-bind="props" :src="shop" alt="shop"></b-img>
                    <h4 class="item">3142,33kn</h4>
                </li>
                <li>
                    <b-img v-bind="props" :src="sport" alt="sport"></b-img>
                    <h4 class="item">3312,33kn</h4>
                </li>
                <li>
                    <b-img v-bind="props" :src="zdravlje" alt="zdravlje"></b-img>
                    <h4 class="item">313,33kn</h4>
                </li>
            </ul>


        </div>
    </div>
</template>

<script>
    export default {
        name: "statistika",
        data(){
            return{
                kategorijeShow: false,
                korisniciShow: false,
                korisnici: [],
                props:{
                    height: 85, width: 85, class:"item img"
                }

            }
        },
        methods: {
            toggle: function(e) {
                if(e===1){
                    this.kategorijeShow = true;
                    this.korisniciShow = false;
                }
                if(e===2){
                    this.kategorijeShow = false;
                    this.korisniciShow = true;
                }

            }
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
    #kategorije {
        background-color: cadetblue;
        height: 100%;
        width: 0;
        margin: 0;
        padding: 10px 0;
        transition: .5s ease;
        float: right;
        overflow: hidden;
    }

    ul li{
        margin-bottom: 5px;
    }

    #statistika{
        position: relative;
        margin: 0;
        padding: 0;
    }

    #korisnici{
        background-color: aqua;
        height: 100%;
        width: 0;
        margin: 0;
        padding: 10px;
        transition: .5s ease;
        float: right;
        overflow: hidden;
    }

    .item{
        display: inline-block;
        margin-right: 20%;
    }
</style>