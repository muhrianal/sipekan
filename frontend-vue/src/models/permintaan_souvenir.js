export default class PermintaanSouvenir {
    constructor(alasan_penolakan_souvenir,jumlah,nama_penerima_souvenir,jabatan_penerima_souvenir,kelas_penerima_souvenir, region_penerima_souvenir,souvenir) {
        this.alasan_penolakan_souvenir = alasan_penolakan_souvenir;
        this.status_permintaan_souvenir =1;
        this.jumlah = jumlah;
        this.nama_penerima_souvenir =  nama_penerima_souvenir;
        this.jabatan_penerima_souvenir =  jabatan_penerima_souvenir;
        this.kelas_penerima_souvenir =  kelas_penerima_souvenir;
        this.region_penerima_souvenir =  region_penerima_souvenir;           
        this.souvenir = souvenir;
    }
    setSouvenir(souvenir){
        this.souvenir = souvenir
    }


}