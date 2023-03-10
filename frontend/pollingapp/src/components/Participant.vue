<template>
    <v-card class = "mx-auto">
        <v-card-text class = "font-weight-bold">
            <p><v-icon>mdi-account</v-icon>{{name}}</p>
            <p><v-icon>mdi-bookshelf</v-icon>Respuestas incorrectas: {{wrongQuestions}}</p>
            <p><v-icon>mdi-city</v-icon>{{city}}</p>
            <p>id: {{id}}</p>
        </v-card-text>
        <v-card-actions>
            <v-btn
            :disabled = "!active"
            @click = "alert = true; downvote()"
            color = "error"
            class = "mx-auto mb-5"
             >
             ❌
            </v-btn>
        </v-card-actions>
        <v-snackbar 
        v-model = "alert"
        app
        color = "error"
        class = "font-weight-bold"
        >Calificaste la respuesta de {{name}} como incorrecta!</v-snackbar>
        
    </v-card>
</template>
<script>
import { ref,watch} from "vue";
import {userData} from '../stores/user'
import LoginService  from '@/services/LoginService';


export default {
    'name':'Participant',
    
    
    props: ['name','wrongQuestions','city','id','lastName','round','active'],
    setup(props){

        

    /*
    let name = ref('Jean Paul')
    let wrongQuestions = ref(2)
    let city = ref("Medellin")
    */
    let store = userData()
    let user = store.getUser
    let alert = ref(false)
    
        function downvote(){
            const date = new Date()
     
            console.log(alert)
            let obj = {
                'juror':user.id,
                'participant_id':props.id,
                'participant_name': props.name,
                'participant_lastName':props.lastName,
                'round':props.round,
                'time': date.toString()
            }
            
            this.$socket.emit("downvote",obj)
        }

      
    

    return {
        alert,
        downvote
    }
   

    

    
}
}


</script>