<template>
    <div class ="admin-div">
    <h1>Panel de administrador</h1>
    <div class = "round-handler">
        <b-badge  pill variant = "primary">Ronda {{round}}</b-badge>
        <div class = "round-buttons">
            <b-button variant = "success" pill size="sm" @click = "nextRound">Siguiente</b-button>
            <b-button variant = "danger" pill size="sm" @click = "decreaseRound">Revertir</b-button>
        </div>
    </div>
    <h5>Número de participantes por jurado: </h5>
    <b-button @click = "assignParticipants" pill variant = "primary">Asignar participantes</b-button>
    <b-card v-for = "juror in jurors" :header = "juror.name+' '+juror.lastName">
        <h5>Upb id: {{juror.upb_id}}</h5>
        <div class = "participants-container">
            <b-button v-for = "participant in juror.participants">{{participant.name}}</b-button>
        </div>

    </b-card>
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

    },
    mounted(){
        LoginService.jurorsParticipants().then((response => {
            this.jurors = response.data
        }))
        

    },
    data(){
        return {
        jurors: []
        }
    },
    methods:{
        assignParticipants(){
            LoginService.assign().then((response => {
                this.$bvToast.toast(`Participantes asignados exitosamente`,{
                    title: 'Notificación',
                    variant: 'success',
                    solid: true,
                })
                LoginService.jurorsParticipants().then((response => {
            this.jurors = response.data
        }))

            }))

        },
        nextRound(){
            let store = userData()
            store.increaseRound()
            
        },
        decreaseRound(){
            let store = userData()
            store.decreaseRound()
        },
        

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