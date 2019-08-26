<template>
    <div>
        <div>
            <b-form class="prijava">
                <b-form-group>
                    <b-form-input id="input1" v-model="korisnik.email" type="text" required placeholder="Unesite e-mail:">

                    </b-form-input>
                    <b-form-input id="input2" v-model="korisnik.lozinka" type="text" required placeholder="Unesite lozinku:">

                    </b-form-input>
                </b-form-group>
            </b-form>
            <b-button @click="submit" variant="warning">
                Prijavi se
            </b-button>
            <div>
                <h4 class="row-1"> Nemate račun? </h4>
                <router-link to="registracija">REGISTRIRAJ SE</router-link>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "prijava",
        data(){
            return{
                korisnik: {
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
            submit: function() {
                var prijavaKorisnik = {
                    email: this.korisnik.email,
                    lozinka: this.korisnik.lozinka
                };
                axios.post("http://127.0.0.1:5000/prijava", prijavaKorisnik)
                    .then((response)=>{
                        console.log("uspjesno!");
                        this.$store.state.korisnik=response.data.korisnik;
                        console.log(this.$store.state.korisnik);
                        this.emitReplaceToRouter();
                    })
                    .catch((error)=>{console.log(error)})
            },
            emitReplaceToRouter(){
                this.$emit("prijava", true);
                this.$router.replace({name: "glavna"})
            }
        }
    }
</script>

<style>
    .prijava{
        margin: 15% auto 2% auto;
        width: 30%;
    }
    #input1{
        margin-bottom: 2%;
    }
    .row-1{
        display: inline-block;
        margin-right: 0.5%;
        margin-top: 1%;
    }

</style>