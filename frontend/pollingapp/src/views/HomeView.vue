<template>
  <div>
    <v-card class = "mx-auto">
      <v-card-text class = "font-weight-bold">
        <h1>{{name}}</h1>
        <p><v-icon>mdi-account</v-icon>Nombre: {{name}}</p>
        <p><v-icon>mdi-account</v-icon>Email: {{email}}</p>
        <p><v-icon>mdi-bookshelf</v-icon>UPB id: {{upbid}}</p>
        <p><v-icon>mdi-city</v-icon>Seccional: {{seccional}}</p>
      </v-card-text>

    </v-card>
  </div>
</template>

<script>
  import HelloWorld from '../components/HelloWorld'
  import Participant from '@/components/Participant.vue';
  import {userData} from '../stores/user'
  import { useRouter, useRoute } from 'vue-router'


  export default {
    name: 'Home',

    components: {
      HelloWorld,
      Participant
    },
    setup(props,context){
      let store = userData()
      let router = context.root.$router
       if(!store.isAuthenticated){
        router.push("/login")
       }
      console.log(store)
      let name = store['name']
      let upbid = store['id']
      let seccional = store['seccional']
      let email = store['email']

      return {
        name,
        upbid,
        seccional,
        email
      }
      }
     
    }
  
</script>
