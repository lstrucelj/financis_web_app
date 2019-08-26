<template>
    <div>
        <div>
            <b-form class="registracija">
                <b-form-group>
                    <b-form-input id="input1" v-model="korisnik.ime" type="text" required placeholder="Unesite ime:">

                    </b-form-input>
                    <b-form-input id="input2" v-model="korisnik.prezime" type="text" required placeholder="Unesite prezime:">

                    </b-form-input>
                    <b-form-input id="input3" v-model="korisnik.email" type="text" required placeholder="Unesite e-mail:">

                    </b-form-input>
                    <b-form-input id="input4" v-model="korisnik.lozinka" type="password" required placeholder="Unesite lozinku:">

                    </b-form-input>
                </b-form-group>
            </b-form>
            <b-button @click="submit" variant="warning">
                Registriraj se
            </b-button>
            <div>
                <h4 class="row-1"> Imate račun? </h4>
                <router-link to="prijava">PRIJAVI SE</router-link>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "registracija",
        data(){
            return {
                korisnik: {
                    ime: "",
                    prezime: "",
                    email: "",
                    lozinka: ""
                }
            }
        },
        mounted(){
            document.querySelector("body").style.backgroundImage=this.pozadina;
        },
        computed: {
            pozadina() {
                return "url('" + require('../assets/pozadina11.png') + "')";
            }
        },
        methods: {
            submit: function(){
                console.log('cdscssc');
                var noviKorisnik = {

                    ime: this.korisnik.ime,
                    prezime: this.korisnik.prezime,
                    email: this.korisnik.email,
                    lozinka: this.korisnik.lozinka
                };
                axios.post("/registracija", noviKorisnik)
                    .then((response)=>{console.log("uspjesno!")})
                    .catch((error)=>{console.log("OVDJJCFDJM", error)})
            }
        }
    }
</script>

<style>
    .registracija{
        margin: 15% auto 2% auto;
        width: 30%;
    }
    .row-1{
        display: inline-block;
        margin-right: 0.5%;
        margin-top: 1%;
    }
    #input1, #input2, #input3 {
        margin-bottom: 2%;
    }
</style>