<template>
    <div class="participants-container">
    
    <b-card class = "w-25 mt-2" v-for = "elem in participants" bg-variant = "dark" text-variant = "white" :title="elem.name">
        <b-card-text>{{ elem.name }} {{ elem.lastName }}</b-card-text>
        
    
        
        <b-card-text><a :href ="'http://127.0.0.1:5000/participant/'+elem['$oid']">{{elem["$oid"]}}</a></b-card-text>
    </b-card>
    
</div>
</template>
<script>

import LoginService  from '@/services/LoginService';
import {userData} from '../stores/user'
import {BCard,BCardText} from 'bootstrap-vue'
export default{
    name: "Participants",
    components:{
        BCard,
        BCardText
    },
    data(){
        return {
            ids: [],
            participants: [],

        }
    },
    mounted(){
        let store = userData()
        console.log("we are loading your participants, just wait...")
        LoginService.jurorParticipants(store.getUser.id).then(response => {
            this.ids = response.data[0]['participants']
            console.log(this.ids)
            for(let i = 0; i<this.ids.length;i++){
                LoginService.participant(this.ids[i]["$oid"]).then(response =>{
                    this.participants.push(response.data)
                })
            }
        })

        }


    }

</script>
<style>
.participants-container{
    display:flex;
    width: 100vw;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 50px;
}
</style>