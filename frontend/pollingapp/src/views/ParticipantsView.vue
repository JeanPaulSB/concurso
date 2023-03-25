<template>
    <div>
            
                
                <v-chip outlined color = "success"><v-icon left>mdi-account-check</v-icon>Participantes activos</v-chip>
                <v-card><v-card-title>
                    <v-text-field
                    v-model = "search"
                    single-line
                    hide-details
                    append-icon = "mdi-magnify"
                    label = "Ingresa un nombre">

                    </v-text-field>
                </v-card-title></v-card>
                <v-data-table
                :headers = "headers"
                :items = "activeParticipants"
                :search = "search"
                >

                <template v-slot:item.calificar = "{item}">
                    <v-btn color = "error" @click = "alert = true; downvote(item['_id']['$oid'],item['name'])">X</v-btn>
                </template>


                </v-data-table>
                <v-snackbar color = "error" v-model = "alert">Calificaste la respuesta de {{name}} como incorrecta</v-snackbar>
                

        <v-divider></v-divider>
        <v-chip outlined color = "error"><v-icon left>mdi-cancel</v-icon>Participantes descalificados</v-chip>
        <v-data-table
                :headers = "headersDesq"
                :items = "desqualifiedParticipants"
                >

               

                </v-data-table>
                



    
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
            alert: false,
            search: "",
            name: '',
            fields: ["name","questions_failed","downgrade"],
            headers: [
                {text: 'Nombre',
                value: 'name'},
                {text: 'Seccional',
                value: 'seccional'},{
                    text: 'Resp. incorrectas',
                    value: 'wrongQuestions'
                },
                {text: 'calificar',value:'calificar'}
            ]
            ,
            headersDesq: [
                {text: 'Nombre',
                value: 'name'},
                {text: 'Seccional',
                value: 'seccional'},{
                    text: 'Resp. incorrectas',
                    value: 'wrongQuestions'
                },

            ]

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
            downvote(id,name){
                let store = userData()
                let user = store.getUser

                this.name = name

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