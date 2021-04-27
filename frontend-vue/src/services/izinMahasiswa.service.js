import axios from 'axios';

const API_URL = 'http://localhost:8000/';

class IzinMahasiswaService {
    getJenisPublikasi() {
        return axios.get(API_URL + 'perizinan-humas/jenis-publikasi');
    }
    getListSouvenir(){
        return axios.get(API_URL + 'perizinan-humas/list-souvenir');
    }
    postIzinKegiatan(data){
        return axios.post(API_URL + 'perizinan-kegiatan-mahasiswa/' , data) 
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
    // postTestApi(data){
    //     return axios.post(API_URL + 'test/', data)
    // }
}

export default new IzinMahasiswaService();