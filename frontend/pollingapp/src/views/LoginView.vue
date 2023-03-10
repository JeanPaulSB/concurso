<template>
        <v-card class = " loading-info grey lighten-5 mx-auto mt-10 w-75 px-6 py-8">
        <v-form @submit.prevent = "onSubmit" v-model = "form" >
            <v-text-field
            v-model = "email"
            :readonly="loading"
            :rules="emailRule"
            class ="mb-2"
            clearable
            label = "Email"
            prepend-icon = "mdi-email"
            >
            </v-text-field>
            <v-text-field
            v-model="password"
            :readonly="loading"
            :rules="passwordRule"
            clearable
            type = "password"
            prepend-icon = "mdi-lock"
            label="Password"
            placeholder="Enter your password"
            ></v-text-field>
            <br>
            <v-btn
            color = "success"
            size = "large"
            type = "submit"
            variant = "elevated"
            
            :loading="loading">
            Ingresar</v-btn>
        </v-form>
        <v-alert
        prominent
        v-if = "this.alert == true"
        type = "error"
        dense
        class = "mt-4"
        >{{message}}</v-alert>
    </v-card>
   
</template>
<script>
import { BForm,BFormInput,BFormGroup,BButton,BAlert} from 'bootstrap-vue';
import LoginService from '@/services/LoginService.js'
import {userData} from '../stores/user'

const store = userData()
export default{
    name:"Login",
    components:{
        BForm,
        BFormInput,
        BFormGroup,
        BButton,
        BAlert
    },
    data(){
        return{
            email:"",
            password:"",
            alert: false,
            message: "",
            emailRule: [ value => { if(value) return true
                return "Ingresa un email"}],
            passwordRule: [ value => {if(value) return true
            return "Ingresa tu contraseña"},
            ]
        }
    },
    methods:{
        onSubmit(event){
            event.preventDefault()
            // making api call to our backend
            LoginService.login(this.email,this.password).then(response =>{
                let data = response.data.data
                console.log(data)
                let msg = data["message"]
                console.log(data)
                if(msg != "success"){
                    this.alert = true;
                    this.message = msg
                }
                else{
                    // successfully logged
                    this.alert = false
                    // updating state
                    store.loadData(data)
                    this.$router.push("/")
                }

                
            })
            
        }
    }

}</script>
<style>
.form-container{
    margin: auto;
    margin-top: 50px;
  
    width: 50%;
    height: 60vh;
    justify-content: center;
    
}
</style>