export default class JenisIzinPublikasi{
    constructor(jenis_publikasi,alasan_penolakan){
        this.jenis_publikasi = jenis_publikasi;
        this.status_perizinan_publikasi = 1; //menunggu persetujuan
        this.alasan_penolakan = alasan_penolakan
    }
}