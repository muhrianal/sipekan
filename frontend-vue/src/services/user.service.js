import axios from 'axios';
// import authHeader from './auth-header';

const API_URL = 'http://localhost:8000/';

class UserService {
    // path('izin-kegiatan/<int:id_perizinan>/', update_izin_kegiatan_by_id_perizinan),
    // path('izin-kegiatan/', list_izin_kegiatan)
    getAllIzinKegiatan() {
        return axios.get(API_URL + 'izin-kegiatan/')
    }

    getIzinKegiatan(id){
        return axios.get(API_URL + 'izin-kegiatan/' + id)
    }
}

export default new UserService();