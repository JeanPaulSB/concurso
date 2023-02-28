<template>
  <div class="home">
      
      <h2>Historial de votaciones</h2>
      <b-card class = "w-50" v-for = "record in history" bg-variant = "warning">
        <b-card-text>
          Time: {{record.time}}

        </b-card-text>
        <b-card-text>
        Participante: {{ record.participant_name }} {{ record.participant_lastName }}
      </b-card-text>
      <b-button variant = "success" @click = 'revert(record["participant_id"])'>Revertir </b-button>
      </b-card>


  </div>
  
</template>

<script>
// @ is an alias to /src


import {userData} from '../stores/user'
import LoginService from '@/services/LoginService.js'
import {BTable,BCard,BButton,BToast} from 'bootstrap-vue' 

export default {

  name: 'HomeView',
  components: {
    BTable,
    BCard,
    BButton,

  },
  data(){
    return {
      email: "",
      name: "",
      lastName: "",
      id: "",
      data: "",
      history: [],
    }

  },
  mounted(){
    const store = userData()
    let user = store.getUser

    if (store.isAuthenticated){
      this.email = user.email
      this.name = user.name
      this.id = user.id
      
      LoginService.history(this.id).then( response => {
        this.history = response.data.reverse()
        console.log(this.history)
      })
      
      
    }



    else{
      this.$router.push("/login")
    }
    
  },
  methods:{
    revert(id){
      this.$bvToast.toast(`Acabas de revertir una calificación!`,{
                    title: 'Notificación',
                    variant: 'success',
                    solid: true,
                })
      console.log("reverting")
      console.log(id)
      LoginService.revert(id).then(response => {
        console.log("reverted!")
      })


    }
  },

  sockets:{
    logged(data){
      this.data = data
    }
  }
}
</script>
<style>
.home{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
