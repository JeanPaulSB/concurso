import axios from 'axios'


const apiClient = axios.create({
    baseURL:"https://www.concursoupb.com/api",
    headers:{
        Accept: 'application/json',
        "Content-Type": "multipart/form-data",
        "Authorization": ""
    }

})

export default{
    apiClient,
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
    participantsList(){
        return apiClient.get("/participants/list")
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
    revert(id,time){
        let form = new FormData();
        form.append('participant_id',id)
        form.append('time',time)

        return apiClient.post("/jurors/revert",form)
    },
    assign(med,bga){
        let form = new FormData()

        form.append("med",med)
        form.append("bga",bga)
        return apiClient.post("/participants/assign",form)
    },
    jurors(){
        return apiClient.get("/jurors/list")
    },
    jurorsParticipants(){
        return apiClient.get("/jurors/participants_normalized")
    },
    sendFile(file){
        let form = new FormData();
        form.append("file",file)
        return apiClient.post("/participants/register",form)

    },
    getReport(){
        return apiClient.get("/report")
    },
    getJuror(participant_id){
        let form = new FormData();
        form.append('participant_id',participant_id)
        return apiClient.post("/jurors/participant",form)
        
    },
    participantHistory(participant_id){
        let form = new FormData();
        form.append('participant_id',participant_id)
        return apiClient.post("/participant/history",form)
    }
}