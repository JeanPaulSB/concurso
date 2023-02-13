<template>
    <div class = "form-container">
        <b-form @submit = "onSubmit" class = "mt-3">
            <b-form-group
            label = "Email">
            
            <b-form-input
            placeholder = "Ingresa tu email"
            required
            v-model = "email"
            type = "email"
            >
            </b-form-input>
            </b-form-group>
            <b-form-group
            label = "Contraseña">
            <b-form-input
            type = "password"
            v-model = "password"
            placeholder = "Ingresa tu contraseña"
            required
            >
            </b-form-input>
            </b-form-group>
            <b-button type = "submit" variant = "success">Ingresar</b-button>
        </b-form>
        <b-alert :show="alert" variant="danger" class = "mt-5">{{ message }}</b-alert>

    </div>
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
        }
    },
    methods:{
        onSubmit(event){
            event.preventDefault()
            // making api call to our backend
            LoginService.login(this.email,this.password).then(response =>{
                let data = response.data.data
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
            console.log("hola jeejej")
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