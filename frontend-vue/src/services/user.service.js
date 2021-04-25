import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'http://localhost:8000/';

class UserService {
    getPublicContent() {
        return axios.get(API_URL + 'peminjaman-ruangan/unit-kerja/', {headers : authHeader()});
    }
    // postTestApi(data){
    //     return axios.post(API_URL + 'test/', data)
    // }

    getPhotos(){
        return axios.get("https://jsonplaceholder.typicode.com/posts");
    }

    getAllRuanganKalender(){
        return axios.get(API_URL + 'api/ruangan');
    }
}

export default new UserService();