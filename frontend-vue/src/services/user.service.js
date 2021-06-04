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

    // postIzinKegiatanHeader(data){
    //     return axios.post(API_URL + 'api/ruangan/', data)
    // }

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

    // putPeminjamanRuangan(id,data) {
    //     return axios.get(API_URL + 'peminjaman-ruangan/update/'+id+'/',data)
    // }

    getAllSouvenir() {
        return axios.get(API_URL + 'perizinan-humas/list-souvenir')
    }

    postSouvenir(data) {
        return axios.post(API_URL + 'souvenir/', data)
    }

    getSouvenir(id) {
        return axios.get(API_URL + 'souvenir/' +id)
    }

    deleteSouvenir(id) {
        return axios.delete(API_URL + 'souvenir/' +id)
    }

    putSouvenir(id, data) {
        return axios.put(API_URL + 'souvenir/' + id +'/', data)
    }

    putPermintaanProtokoler(id, data) {
        return axios.put(API_URL + 'permintaan-protokoler/' + id+'/', data)
    }

    putPermintaanSouvenir(id, data) {
        return axios.put(API_URL + 'permintaan-souvenir/' + id+'/', data)
    }

    putPeminjamanRuangan(id, data) {
        return axios.put(API_URL + 'peminjaman-ruangan/' + id+'/', data)
    }

    putIzinKegiatanHeader(id, data){
        return axios.put(API_URL + 'detail-kegiatan/' + id +'/', data)
    }

    putIzinKegiatanDetail(id, data){
        return axios.put(API_URL + 'izin-kegiatan-detail/' + id +'/', data,{
            headers:{
            'Content-Type': 'multipart/form-data'
        }})
    }


    putPerulangan(id, data) {
        return axios.put(API_URL + 'perulangan/' + id +'/', data)
    }

    putDetailIzinKegiatan(id, data) {
        return axios.put(API_URL + 'izin-kegiatan/' + id+'/', data)
    }

    getJenisPublikasi() {
        return axios.get(API_URL + 'perizinan-humas/jenis-publikasi');
    }
    getListSouvenir(){
        return axios.get(API_URL + 'perizinan-humas/list-souvenir');
    }
    postIzinKegiatanHeader(data){
        return axios.post(API_URL + 'perizinan-kegiatan-header/',data)
    }
    postIzinKegiatanDetail(data){
        return axios.post(API_URL + 'perizinan-kegiatan-detail/', data,{
            headers:{
            'Content-Type': 'multipart/form-data'
        }})
    }
    postPeminjamanRuanganMahasiswa(id,data){
        return axios.post(API_URL + 'peminjaman-ruangan/mahasiswa/' + id + '/' , data)
    }
    postPermohonanHumas(id,data){
        return axios.post(API_URL + 'perizinan-humas/'+ id +'/',data)
    }
    postPerizinanPublikasi(data){
        return axios.post(API_URL+ 'perizinan-humas-publikasi/', data ,{
            headers:{
            'Content-Type': 'multipart/form-data'
        }})
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

    putPerizinanPublikasi(id, data) {
        return axios.put(API_URL + 'perizinan-publikasi/' + id , data ,{
            headers:{
            'Content-Type': 'multipart/form-data'
        }})
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