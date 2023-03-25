<template>
    <div>
            
                
                <v-chip outlined color = "success"><v-icon left>mdi-account-check</v-icon>Participantes activos</v-chip>

                <v-data-table
                :headers = "headers"
                :items = "this.activeParticipants"
                :search = "search">

                <template v-slot:top>
        
                    <v-text-field
                      v-model="search"
                      label="Ingrese un nombre"
                      class="my-4 px-5"
                      flat
                      prepend-icon = "mdi-account"
                    ></v-text-field>
                </template>


                <template v-slot:item.wrongQuestion = "{item}">
                    <v-btn color = "error" @click = 'alert = true; downvote(item["_id"]["$oid"],
                    item.name); '>X</v-btn>
                   
                </template>
               

                </v-data-table>
                <v-snackbar 
                v-model = "alert"
                app
                color = "error"
                class = "font-weight-bold"
                >Acabas de calificar la respuesta de {{ name }} como incorrecta
                </v-snackbar>
                

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
            fields: ["name","questions_failed","downgrade"],
            headers: [ 
                {text: 'Nombre',
                value: 'name'},
                {text: 'Resp. incorrectas',
            value: 'wrongQuestions'},
            {text: 'Seccional',
            value: 'seccional'},{
                text: 'Calificar resp. como incorrecta',
                value: 'wrongQuestion'
            }
            ],
            alert: false,
            name: '',
            search: ''

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
                console.log(this.alert)
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