<template>
    <div class = "container register-container">
    <b-form  @submit="onSubmit">
      <b-form-group
        id="input-group-1"
        label="Email address:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model = "user.email"
          type="email"
          placeholder="Ingresa tu email"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Nombre:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model = "user.name"
          placeholder="Ingresa tu nombre"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Apellidos:" label-for="input-3">
        <b-form-input
        id = "input-3"
        v-model = "user.lastName"
        placeholder = "Ingresa tus apellidos"
        required>

        </b-form-input>
      </b-form-group>
      <b-form-group id="input-group-4" label="UPB ID:" label-for="input-3">
        <b-form-input
        id = "input-3"
        v-model = "user.upb_id"
        placeholder = "Ingresa tu ID"
        required>

        </b-form-input>
      </b-form-group>
      <b-form-group id="input-group-3" label="Contraseña:" label-for="input-3">
        <b-form-input
        id = "input-3"
        placeholder = "Ingresa tu contraseña"
        v-model = "user.password"
        type = "password"
        required>

        </b-form-input>
      </b-form-group>

      

      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
    </div>
</template>
<script>
import {BForm,BFormGroup,BFormInput} from 'bootstrap-vue'

import LoginService from '@/services/LoginService'
export default{
    name: 'Register',
    components:{
        BForm,
        BFormGroup,
        BFormInput,
    },
    data(){
        return{
            user: {
                email: "",
                password: "",
                upb_id: "",
                name: "",
                lastName: "",

            }
           

        }
    },
    methods:{
        onSubmit(event){
            event.preventDefault()
            console.log(this.user)
            LoginService.register(this.user).then(response => {
                console.log(response)
            })
        }
    }
}</script>
<style>
.register-container{
    display:flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    margin:auto;
    margin-top:50px;
    width:300px;
    padding: 10px;
}</style>