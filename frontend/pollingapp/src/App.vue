
<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="#">Polling Software</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item><router-link to = "/">Inicio</router-link></b-nav-item>
        <b-nav-item :disabled="getAuthStatus()"><router-link to = "/login">Ingresar</router-link></b-nav-item>
        <b-nav-item><router-link to = "/register">Regístrate</router-link></b-nav-item>
        <b-nav-item :disabled="!getAuthStatus()"><router-link to = "/participants">Participantes</router-link></b-nav-item>
        <b-nav-item><router-link to = "/admin">Admin</router-link></b-nav-item>
        <b-nav-item :disabled="!getAuthStatus()">Cerrar Sesión</b-nav-item>
        

        
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
  <router-view></router-view>   
  </div>
</template>
<script>
import {BNavbar} from 'bootstrap-vue'
import {userData} from './stores/user'






export default{
  components:{
    BNavbar

  },
  setup(){
    const store = userData()
    
    function getAuthStatus(){
      return store.authStatus
    }

    return{
      getAuthStatus
    }
  }
  }

</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
