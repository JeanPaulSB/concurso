<template>
  <div class="home">
      <h1>Bienvenido a nuestra aplicación! </h1>
      <p>Nombre: {{ name }}</p>
      <p>Email: {{ email }}</p>
      <p>Id: {{ id }}</p>
  </div>
</template>

<script>
// @ is an alias to /src


import {userData} from '../stores/user'

export default {

  name: 'HomeView',
  components: {

  },
  data(){
    return {
      email: "",
      name: "",
      lastName: "",
      id: "",
    }

  },
  mounted(){
    const store = userData()
    let user = store.getUser
    this.email = user.email
    this.name = user.name
    this.id = user.id
  }
}
</script>
