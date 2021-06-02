import axios from 'axios';
// import authHeader from './auth-header';

const API_URL = 'http://localhost:8000/';

class UserService {
    getAllIzinKegiatan() {
        return axios.get(API_URL + 'izin-kegiatan/')
    }

    getIzinKegiatan(id){
        return axios.get(API_URL + 'izin-kegiatan/' + id)
    }
    
    putIzinKegiatan(id, data){
        return axios.put(API_URL + 'izin-kegiatan/update/' + id + '/', data )
    }

    getAllRuangan() {
        return axios.get(API_URL + 'api/ruangan/')
    }
    
    postPerizinanRuanganUnitKerja(data){
        return axios.post(API_URL + 'peminjaman-ruangan/unit-kerja/', data)
    }

    getListPerizinanFastur(){
        return axios.get(API_URL + 'peminjaman-ruangan/verifikasi-fastur/')
    }

    getPeminjamanRuanganByIdIzinKegiatan(id){
        return axios.get(API_URL + 'peminjaman-ruangan/verifikasi-fastur/' + id + '/')
    }

    getJadwalPeminjamanRuangan(){
        return axios.get(API_URL + 'peminjaman-ruangan/')
    }

    putUpdateStatusDanAlasanPenolakanPeminjamanRuangan(data, id){
        return axios.put(API_URL + 'peminjaman-ruangan/update-status/' + id + '/', data)
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
        return axios.put(API_URL + 'api/ruangan/' + id +'/', data)
    }

    deleteRuangan(id){
        return axios.delete(API_URL + 'api/ruangan/' + id)
    }

    getAllPerizinan() {
        return axios.get(API_URL + 'api/list-perizinan/')
    }

    getPerizinan(id) {
        return axios.get(API_URL + 'api/perizinan/' + id)
    }

    putPeminjamanRuangan(id,data) {
        return axios.get(API_URL + 'api/peminjaman-ruangan/update/'+id+'/',data)
    }

    postPengumuman(data){
        return axios.post(API_URL + 'pengumuman/create', data)
    }

    getPengumumanById(id){
        return axios.get(API_URL + 'pengumuman/' + id)
    }

    putPengumumanById(id, data){
        return axios.put(API_URL + 'pengumuman/edit/' + id, data)
    }
}

export default new UserService();