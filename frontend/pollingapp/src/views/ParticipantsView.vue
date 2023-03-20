<template>
    <div>
            
                
                <v-chip outlined color = "success"><v-icon left>mdi-account-check</v-icon>Participantes activos</v-chip>
                <Participant class = "mt-5 font-bold-weight" v-for = "elem in this.activeParticipants" 
                :name ="elem.name" 
                :city = "elem['seccional']"
                :wrongQuestions = "elem.wrongQuestions" 
                :id = "elem['_id']['$oid']" 
                :lastName = "elem['lastName']"
                :active = true
                :round = 1
                :key = "elem['_id']['$oid']"
                >

                </Participant>

        <v-divider></v-divider>
        <v-chip outlined color = "error"><v-icon left>mdi-cancel</v-icon>Participantes descalificados</v-chip>
        <Participant class = "mt-5" v-for = "elem in this.desqualifiedParticipants"
            :name ="elem.name" 
            :city = "elem['seccional']"
            :wrongQuestions = "elem.wrongQuestions" 
            :id = "elem['_id']['$oid']" 
            :active = false
            :round = 1
            :key = "elem['_id']['$oid']"
            >

        </Participant>



    
    </div>
</template>
<script>

import LoginService  from '@/services/LoginService';
import {userData} from '../stores/user'
import {mapState} from 'pinia'
import Participant from '@/components/Participant.vue';
export default{
    name: "Participants",
    components:{
        Participant
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

            return this.participants.filter( obj => obj.wrongQuestions < 3)
            
        },
        desqualifiedParticipants(){
            return this.participants.filter(obj => obj.wrongQuestions >= 3)
        },
        ...mapState(userData,['round'])

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


</style>