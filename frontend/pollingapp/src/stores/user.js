import {defineStore} from 'pinia'

export const userData  = defineStore('user',{
    state: () =>({
        name: '',
        id:'',
        lastName:'',
        email:'',
        isAdmin: false,
        isAuthenticated: false,
        round: 0,
        seccional: '',
    }),
    actions:{
        loadData(obj){
            this.name = obj.name
            this.id = obj.id
            this.email = obj.email
            this.isAuthenticated = true
            this.isAdmin = obj.isAdmin
            this.seccional = obj.seccional
        },
        increaseRound(){
            this.round+=1;
        },
        decreaseRound(){
            
            if(this.round > 0){
             this.round--;
            }
            
        }
    },
    getters:{
        getUser(state){
            return {
                name: state.name,
                id: state.id,
                lastName: state.lastName,
                email: state.email,
                isAdmin: state.isAdmin,
                seccional: state.seccional
            }
        },
        authStatus(state){
            return state.isAuthenticated
        },
        getRound(state){
            return state.round
        }
    }
})