import axios from 'axios'


const apiClient = axios.create({
    baseURL:"http://127.0.0.1:5000",
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
        return apiClient.post("/api/login",form)
    },
    jurorParticipants(id){
        return apiClient.get("/jurors/"+id)
    },
    participant(id){
        return apiClient.get("/participant/"+id)
    }
}