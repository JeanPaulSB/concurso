<template>
    <div>
        
    <v-alert class = "mx-auto my-auto" type = "error" v-if = "!isAdmin"> Lo sentimos pero no tienes los privilegios para acceder a esta sección.</v-alert>
    <v-card class = "py-10" v-if = "isAdmin">
    
    <span class = "text-h5">Controles de ronda</span>
    <div class ="buttons">
        <v-btn outlined color ="success" class = "mr-2" @click = "nextRound">Siguiente</v-btn>
        <v-btn outlined color = "error" @click = "decreaseRound">Revertir</v-btn>
    </div>
    <div>
    <v-chip outlined class = "mt-5 font-bold-weight" label color = "primary">Ronda actual: {{round}}</v-chip>
    </div>
    <v-btn  depressed color = "success" class = "mt-5" @click = "settings = true"><v-icon left>mdi-account-group</v-icon>Asignar participantes</v-btn>
    <v-dialog
    width = "500"
    v-model = "settings">

    <v-card>
        <v-card-title>Ajustes</v-card-title>
        <v-card-text>
        <v-text-field v-model = "MEDnumber" label = "Participantes por jurado Medellín"></v-text-field>
        <v-text-field v-model = "BGAnumber" label = "Participantes por jurado Bucaramanga"></v-text-field>
        <v-btn color = "success" @click = "assignParticipants()">Asignar</v-btn>
    </v-card-text>
    </v-card>


    </v-dialog>
    <div>
    <div>
    <a download = "resultados.xlsx" href = "https://www.concursoupb.com/api/report"><v-btn class = "mt-2 green lighten-4" ><v-icon left>mdi-file-excel</v-icon>Generar reporte en excel</v-btn></a>
    </div>
    <v-btn color = "primary" class = "mt-2" @click = "dialog = true"><v-icon left>mdi-list-box</v-icon>Registrar participantes</v-btn>
    <v-dialog 
    persistent
    max-width = "600px"
    v-model = "dialog"
    > 
        <v-card>
            <v-card-title><span class = "text-h5">Registro de participantes</span></v-card-title>
            <v-card-text>
                Ingresa el archivo de excel que contiene la información de los participantes a registrar
                <v-file-input
                chips
                label = "Archivo de excel"
                v-model = "currentFile"
                >

                </v-file-input>
            </v-card-text>
            <v-card-actions>
                <v-btn @click = "handleFile">Subir</v-btn>
                <v-btn
                @click = "dialog = false"
                >Cerrar</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
    <v-snackbar color = "success" v-if = "this.message == 'success'" v-model = "alert"><v-icon left>mdi-account-group</v-icon>Se registaron {{ registeredUsers }} participantes de forma exitosa. </v-snackbar>
    </div>
    <v-data-table
    :headers = "headers"
    :items = "participants"
    item-key = "name"
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
    <template v-slot:item.name = "{item}">

        <router-link :to="{name : 'DetailedView' ,params: { id: item['_id']['$oid']}}">
   
            {{ item.name }}
        </router-link>
       
    </template>
    <template v-slot:item.wrongQuestions="{item}">
        <v-chip class = "mx-auto" 
            dark
            :color = "getColor(item.wrongQuestions)" >
            {{ item.wrongQuestions }}
        </v-chip>
    </template>

    </v-data-table>
    </v-card>
   
    </div>



</template>

<script>
import LoginService from '@/services/LoginService';
import {BButton,BToast,BBadge, BCard} from 'bootstrap-vue'
import {userData} from '../stores/user'
import {mapState} from 'pinia'
export default{
    name:'admin',
    components:{
        BButton,
        BToast,
        BCard,
        BBadge,
    },
    
    computed:{
        ...mapState(userData,['round']),
        ...mapState(userData,['isAdmin'])

    },
    mounted(){

        if(this.isAdmin){
            this.$socket.emit("admin")
            LoginService.jurorsParticipants().then((response => {
            this.jurors = response.data
            
            }))

            LoginService.participantsList().then((response => {
            this.participants = response.data
            }))
        
            }
        

    },
    data(){
        return {
        jurors: [],
        dialog: false,
        currentFile: '',
        MEDnumber: 0,
        BGAnumber: 0,
        error: false,
        assignsettings: false,
        registeredUsers: 0,
        settings: false,
        MEDnumber: 0,
        BGAnumber: 0,
        status: '',
        alert: false,
        message: '',
        participants:  [],
        search: '',
        headers: [
            {
                text: 'Id',
                align: 'start',
                sortable: true,
                value: 'row_id'
            },
            {'text':'Nombres', value: 'name'},
            {'text': 'Seccional',value: 'seccional'},
            {'text':'Respuestas incorrectas',value: 'wrongQuestions'},
            {'text':'ID UPB',value: 'upb_id'}

        ]
        }
        
        
    },
    methods:{
        assignParticipants(){
            LoginService.assign(this.MEDnumber,this.BGAnumber).then((response => {
                this.settings = false;
                LoginService.jurorsParticipants().then((response => {
                this.jurors = response.data
                console.log(this.jurors)
        }))

            }))
        }
        
        ,
        nextRound(){
            let store = userData()
            store.increaseRound()
            console.log(store)
            
        },
        decreaseRound(){
            let store = userData()
            store.decreaseRound()
        },
        handleFile(){
            if (this.currentFile){
                LoginService.sendFile(this.currentFile).then((response => {
                    let data = response.data.data
                    this.registeredUsers = data.registered_users
                    this.message = "success"
                    this.alert = true

                    LoginService.participantsList.then((response => {
                        this.participants = response.data
                    }))
                    
                }))
            }

        },
        getColor(value){
            if( value == 3) return 'red'
            else if(value == 2) return 'orange'
            else return 'green'

        },

        

    },
    sockets:{
        results(data){
            this.participants = data
        }
    }
}
</script>
<style>
.admin-div{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap:30px;
}
.participants-container{
    display: flex;
    flex-direction: column;
    gap: 20px;
}
</style>