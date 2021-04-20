import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'http://localhost:8080/';

class UserService {
    getPublicContent() {
        return axios.get(API_URL + 'peminjaman-ruangan/unit-kerja/');
    }
}

export default new UserService();