export default class PeminjamanRuangan {
    constructor(judul_peminjaman, jumlah_peserta, waktu_mulai, waktu_akhir, catatan, ruangan, terbuka_untuk_umum) {
        this.judul_peminjaman = judul_peminjaman;
        this.jumlah_peserta = jumlah_peserta;
        this.waktu_mulai = waktu_mulai;
        this.waktu_akhir = waktu_akhir;
        this.catatan = catatan;
        this.ruangan = ruangan;

        this.alasan_penolakan = null;
        this.status_peminjaman_ruangan = 1; //menunggu persetujuan
        this.perulangan = null;
        this.terbuka_untuk_umum = terbuka_untuk_umum
    }
    setPerulangan(perulangan){
        this.perulangan = perulangan;
    }
}