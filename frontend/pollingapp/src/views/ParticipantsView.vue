<template>
    <div class="participants-container">
        <b-card>
            <b-card v-for="elem in activeParticipants"
            border-variant = "primary"
            :header = 'elem["_id"]["$oid"]'
            header-bg-variant = "primary"
            header-text-variant = "white"
            align = "center"
            class = "mt-5" 
            
            >
            <b-card-text>Nombre: {{ elem["name"] }} {{ elem["lastName"] }}</br>
            Respuestas incorrectas: {{ elem["questions_failed"] }} </br>
            <b-button class = "mt-2" variant = "danger" @click="downvote(elem['_id']['$oid'])">❌</b-button>
            
            </b-card-text>
                
            </b-card>
        </b-card>
    
    </div>
</template>
<script>

import LoginService  from '@/services/LoginService';
import {userData} from '../stores/user'
import {BCard,BCardText,BTable,BButton,BCardGroup,BBadge,BToast} from 'bootstrap-vue'

export default{
    name: "Participants",
    components:{
        BCard,
        BCardText,
        BTable,
        BButton,
        BCardGroup,
        BBadge,
        BToast,
    },
    data(){
        return {
            ids: [],
            participants: [],
            fields: ["name","questions_failed","downgrade"]

        }
    },
    computed: {
        // getting active participants
        activeParticipants(){
            this.participants.filter((obj) => obj.questions_failed < 3)
        }
    },
    mounted(){
        let store = userData()

        if(store.isAuthenticated){
            let user = store.getUser
            this.$socket.emit('join',{'room':user.id})
        }
        else{
            this.$router.push("/login")
        }
        },
        methods:{
            downvote(id){
                let store = userData()
                let user = store.getUser

                const participant = this.participants.filter( user => user['_id']['$oid'] == id)[0]
                
                const date = new Date()
                
                let obj = {
                    'juror':user.id,
                    'participant_id':id,
                    'participant_name': participant.name,
                    'participant_lastName': participant.lastName,
                    'time':date.toString()
                }

                this.$socket.emit("downvote",obj)
                
               
                
                this.$bvToast.toast(`Acabas de calificar la respuesta de ${participant.name} ${participant.lastName} como incorrecta!`,{
                    title: 'Notificación',
                    variant: 'danger',
                    solid: true,
                })
                
                
            }
        },
        sockets:{
            participants(data){
                console.log(data)
                this.participants = data
            }

        },
        beforeDestroy(){
            let store = userData()
            let user = store.getUser

            this.$socket.emit("leave",{'room':user.id})
        }


    }

</script>
<style>
.participants-container{
    display:flex;
    width: 100vw;
    justify-content: center;
    align-items: center;
    margin-top: 50px;
}
.individual-participant{
    display: flex;
    gap: 50px;
}


</style>