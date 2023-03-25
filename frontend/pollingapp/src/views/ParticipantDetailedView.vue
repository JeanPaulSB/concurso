<template>
    <v-card class = "mx-auto">
        <v-card-text class = "font-weight-bold">
            <p><v-icon>mdi-account</v-icon>{{name}}</p>
            <p><v-icon>mdi-bookshelf</v-icon>Respuestas incorrectas: {{wrongQuestions}}</p>
            <p><v-icon>mdi-city</v-icon>{{seccional}}</p>
            <p>UPB id: {{upb_id}}</p>
            <v-divider></v-divider>
            <v-text class = "h5-text">Jurado Responsable</v-text>
            <p><v-icon>mdi-account</v-icon>{{juror_email}}</p>
            <p><v-icon>mdi-city</v-icon>{{juror_seccional}}</p>
            <p><v-icon>mdi-bookshelf</v-icon>{{juror_upb_id}}</p>
            <v-divider></v-divider>
            
            <v-text class = "h5-text">Historial de votaciones</v-text>
            
            <div v-for = "record in history">
                
                    <v-chip color = "primary" outlined><v-icon left>mdi-clock</v-icon>{{record.time}}</v-chip>
                    <v-chip color = "error" @click = "revert(record['participant_id'],record['time'])" class = "my-2 ml-2">Revertir</v-chip>
            
            </div>

        </v-card-text>

    </v-card>


</template>
<script>
import { ref,watch} from "vue";
import LoginService from '@/services/LoginService'
export default{
    name: 'DetailedView',
    props: ['id'],
    setup(props){
        
        let name = ref('s')
        let row_id = ref(0)
        let wrongQuestions = ref(0)
        let upb_id = ref(0)
        let seccional = ref('s')

        let juror_email = ref('n/a')
        let juror_upb_id = ref('n/a')
        let juror_seccional = ref('n/a')

        let history = ref([])



        let participant_id = props.id

        LoginService.participant(participant_id).then((response =>{
            let data = response.data
            console.log(data)
            name.value = data['name']
            upb_id.value = data['upb_id']
            row_id.value = data['row_id']
            seccional.value = data['seccional']
            wrongQuestions.value = data['wrongQuestions']
        }))


        LoginService.getJuror(props.id).then((response => {
            let data = response.data
            juror_email.value =  data['email']
            juror_upb_id.value = data['upb_id']
            juror_seccional.value = data['seccional']
        }))

        LoginService.participantHistory(props.id).then((response =>{
            let data = response.data
            history.value = response.data
            console.log(data)
        })).catch(error => {
            console.log(error)
        })
            

        function revert(id,time){
            console.log("something wrong")
            LoginService.revert(id,time).then((response =>{
                console.log(response.data)
                    LoginService.participantHistory(props.id).then((response =>{
                let data = response.data
                history.value = response.data
                console.log(data)
            })).catch(error => {
                console.log(error)
            })
            
            }))
        }
        



        return {
            name,
            row_id,
            upb_id,
            wrongQuestions,
            seccional,
            juror_email,
            juror_seccional,
            juror_upb_id,
            history,
            revert
        }
    }
}
</script>