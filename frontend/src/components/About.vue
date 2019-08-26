<template>
  <div class="container">
    <div class="main">
      <div class="mainform">
        <div class="prijava">
          <b-form>
            <b-form-group>
              <b-form-input id="input1" type="text" required placeholder="Unesite e-mail:">

              </b-form-input>
              <b-form-input id="input2" type="text" required placeholder="Unesite lozinku:">

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
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {

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
  .main{
    width: 100%;
    height: 800px;
    margin: auto;
  }
  .prijava{
    width: 300px;
    height: 100%;
    margin: auto;
    margin-top: 50px;
  }
  .mainform{
    width: 800px;
    height: 400px;
    background-color: #86989B;
    margin: auto;
    margin-top: 150px;
  }

</style>
