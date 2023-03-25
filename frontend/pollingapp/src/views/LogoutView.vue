<template>
    <v-alert sucess = "danger">
        Has cerrado sesión
    </v-alert>
</template>
<script>
import {userData} from '../stores/user'
const store = userData()
export default{
    name:'LogoutView',
mounted(){
    localStorage.clear()
    store.$reset()
}
}</script>