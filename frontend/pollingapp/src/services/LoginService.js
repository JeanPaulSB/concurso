import axios from 'axios'


const apiClient = axios.create({
    baseURL:"http://137.184.131.14/api",
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
        return apiClient.get("/api/jurors/"+id)
    },
    participant(id){
        return apiClient.get("/api/participant/"+id)
    },
    register(obj){
        let form = new FormData()
        form.append("name",obj.name)
        form.append("lastName",obj.lastName)
        form.append("email",obj.name)
        form.append("upb_id",obj.upb_id)
        form.append("password",obj.password)
        
        return apiClient.post("/api/juror/register",form)
    }
}