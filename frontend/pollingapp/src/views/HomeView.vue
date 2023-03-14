<template>
  <div>
    <v-card>
      <v-card-title>Bienvenido </v-card-title>
      <v-card-text></v-card-text>
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
      }
     
    }
  
</script>
