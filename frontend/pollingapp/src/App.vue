<template>
  <v-app>
    <v-navigation-drawer 
    v-model = "drawer"
    class="blue darken-2 white--text"
    app>
      <v-list
        dense
        nav
        rounded
      >
        <v-list-item
          v-for="link in links "
          :key="link.title"
          link
          @click = "clickMe(link.route)"
          color = "success"
        >
          <v-list-item-icon>
            <v-icon color = "white">{{ link.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title  class = "white--text font-weight-bold">{{link.name }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <!-- -->
    </v-navigation-drawer>
  
    <v-app-bar  app>
      <!-- -->
      

      <v-app-bar-nav-icon  @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Concurso UPB</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-chip 
      v-if = "getAuthStatus()"
      color = "blue"
      label
      text-color = "white"
      >
      <v-icon left>mdi-account-circle-outline</v-icon>
      {{getFirstName()}}</v-chip>
    </v-app-bar>
  
    <!-- Sizes your content based upon application components -->
    <v-main>
  
      <!-- Provides the application the proper gutter -->
      <v-container fluid>
  
        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-main>
  
    <v-footer app>
      <!-- -->
    </v-footer>
  </v-app>
</template>
<script>
import {BNavbar} from 'bootstrap-vue'
import {userData} from './stores/user'
import { ref } from "vue";
export default{
  components:{
    BNavbar
  },
  setup(){
    const store = userData()
    let drawer = ref(true)

    const links = [
      {'name':"Login",'route':'/login','icon':'mdi-account'},
      {'name':"Inicio",'route':'/','icon':'mdi-home'},
      {'name':"Participantes",'route':'/participants','icon':'mdi-account-group-outline'},
      {'name':"Admin",'route':'/admin','icon':'mdi-cog'},
      {'name':"Cerrar sesión",'route':'/','icon':'mdi-logout'},

    ]
    
    function getAuthStatus(){
      return store.authStatus
    }
    function getFirstName(){
      return store.name
    }
    function clickMe(route){
     this.$router.push(route)
    }
    return{
      getAuthStatus,
      links,
      drawer,
      clickMe,
      getFirstName
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