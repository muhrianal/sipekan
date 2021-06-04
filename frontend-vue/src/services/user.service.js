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

    getWaitingPKM(id,data) {
        return axios.get(API_URL + 'izin-kegiatan-waiting/',data)
    }

    getVerifiedPKM(id,data) {
        return axios.get(API_URL + 'izin-kegiatan-disetujui/',data)
    }
    getRuanganDetailed(){
        return axios.get(API_URL + 'izin-kegiatan-detailed/')
    }
    getChartDisetujui(){
        return axios.get(API_URL + 'chart/kegiatan-disetujui/')
    }
    getChartDitolak(){
        return axios.get(API_URL + 'chart/kegiatan-ditolak/')
    }
    getChartMenunggu(){
        return axios.get(API_URL + 'chart/kegiatan-menunggu/')
    }
    getWaitingHumas(){
        return axios.get(API_URL + 'perizinan-humas-disetujui/')
    }
    getStokSouvenir(){
        return axios.get(API_URL + 'stok-souvenir/')
    }
}
export default new UserService();