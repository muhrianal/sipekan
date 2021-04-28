import axios from 'axios';
// import authHeader from './auth-header';

const API_URL = 'http://localhost:8000/';

class UserService {
    // getA() {
    //     return axios.get(API_URL + 'peminjaman-ruangan/unit-kerja/', {headers : authHeader()});
    // }
    getAllRuangan() {
        return axios.get(API_URL + 'api/ruangan/')
    }

    getRuangan(id){
        return axios.get(API_URL + 'api/ruangan/' + id)
    }

    postRuangan(data){
        return axios.post(API_URL + 'api/ruangan/', data);
    }

    postIzinKegiatanHeader(data){
        return axios.post(API_URL + 'api/ruangan/', data)
    }

    putRuangan(id, data) {
        return axios.put(API_URL + 'api/ruangan/' + id, data)
    }
    

    //rian's code
    postPerizinanRuanganUnitKerja(data){
        return axios.post(API_URL + 'peminjaman-ruangan/unit-kerja/', data)
    }

    getListPerizinanFastur(){
        return axios.get(API_URL + 'peminjaman-ruangan/verifikasi-fastur/')
    }

    getPeminjamanRuanganByIdIzinKegiatan(id){
        return axios.get(API_URL + 'peminjaman-ruangan/verifikasi-fastur/' + id + '/')
    }


    putUpdateStatusDanAlasanPenolakanPeminjamanRuangan(data, id){
        return axios.put(API_URL + 'peminjaman-ruangan/update-status/' + id + '/', data)
    }
}

export default new UserService();