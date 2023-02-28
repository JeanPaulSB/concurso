import axios from 'axios'


const apiClient = axios.create({
    baseURL:"https://www.concursoupb.com/api",
    headers:{
        Accept: 'application/json',
        "Content-Type": "multipart/form-data",
    }

})

export default{
    login(email,password){
        let form = new FormData()
        form.append('email',email)
        form.append('password',password)
        return apiClient.post("/login",form)
    },
    jurorParticipants(id){
        return apiClient.get("/jurors/"+id)
    },
    participant(id){
        return apiClient.get("/participant/"+id)
    },
    register(obj){
        let form = new FormData()
        form.append("name",obj.name)
        form.append("lastName",obj.lastName)
        form.append("email",obj.name)
        form.append("upb_id",obj.upb_id)
        form.append("password",obj.password)
        
        return apiClient.post("/juror/register",form)
    },
    history(id){
        let form = new FormData()
        form.append('upb_id',id)
        return apiClient.post("/jurors/history",form)
    },
    revert(id){
        let form = new FormData();
        form.append('participant_id',id)
        return apiClient.post("/jurors/revert",form)
    },
    assign(){
        return apiClient.get("/participants/assign")
    },
    jurors(){
        return apiClient.get("/jurors/list")
    },
    jurorsParticipants(){
        return apiClient.get("/jurors/participants_normalized")
    }
}