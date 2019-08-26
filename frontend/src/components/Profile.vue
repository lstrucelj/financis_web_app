<template>
  <div class="container">
    <div class="jumbotron mt-5">
      <div class="col-sm-8 mx-auto">
        <h1 class="text-center">PROFILE</h1>
      </div>
      <table class="table col-md6 mx-auto">
        <tbody>
          <tr>
            <td>IME</td>
            <td> {{ ime }}</td>
          </tr>
          <tr>
            <td>PREZIME</td>
            <td> {{ prezime }}</td>
          </tr>
          <tr>
            <td>EMAIL</td>
            <td> {{ email }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import jwtDecode from 'jwt-decode'
require('jwt-decode')

export default {
  data () {
    const token = localStorage.userToken
    const decoded = jwtDecode(token, {header: true})

    return {
      ime: decoded.identity.ime,
      prezime: decoded.identity.prezime,
      email: decoded.identity.email
    }
  },
  created () {
    this.ime = ''
    this.prezime = ''
    this.email = ''
  }

}
</script>
