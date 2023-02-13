import {defineStore} from 'pinia'

export const userData  = defineStore('user',{
    state: () =>({
        name: '',
        id:'',
        lastName:'',
        email:'',
        isAdmin: false,
    }),
    actions:{
        loadData(obj){
            this.name = obj.name
            this.id = obj.id
            this.email = obj.email

        }
    },
    getters:{
        getUser(state){
            return {
                name: state.name,
                id: state.id,
                lastName: state.lastName,
                email: state.email,
                isAdmin: state.isAdmin
            }
        }
    }
})