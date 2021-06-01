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

    putUpdateStatusDanAlasanPenolakanPeminjamanRuangan(data, id){
        return axios.put(API_URL + 'peminjaman-ruangan/update-status/' + id + '/', data)
    }

    getAllRuanganKalender(){
        return axios.get(API_URL + 'api/ruangan');
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
    getListPerizinanHumas(){
        return axios.get(API_URL + 'perizinan-humas/verifikasi-humas')
    }
    getPerizinanHumasByIdIzinKegiatan(id){
        return axios.get(API_URL + 'perizinan-humas/verifikasi-humas/' + id+'/')
    }
    putUpdateStatusDanAlasanPermintaanSouvenir(data,id){
        return axios.put(API_URL + 'perizinan-humas/update-status-souvenir/'+id+'/',data)
    }
    putUpdateStatusDanAlasanPermintaanProtokoler(data,id){
        return axios.put(API_URL + 'perizinan-humas/update-status-protokoler/'+id+'/',data)
    }
    putUpdateStatusDanAlasanJenisPerizinanPublikasi(data,id){
        return axios.put(API_URL + 'perizinan-humas/update-status-jenis-izin-publikasi/' + id +'/',data)
    }
}

export default new UserService();