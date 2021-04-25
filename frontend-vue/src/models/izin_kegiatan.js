export default class IzinKegiatan{
    constructor(nama_kegiatan, organisasi, user){
        this.nama_kegiatan = nama_kegiatan;
        this.organisasi = organisasi;
        this.peminjaman_ruangan = null;
        this.user = user;
        this.status_perizinan_kegiatan = 2 // karena unit kerja langsung disetujui
    }
    setPeminjamanRuangan(peminjaman_ruangan){
        this.peminjaman_ruangan = peminjaman_ruangan;
    }

    setUser(id_user){
        this.user = id_user;
    }
}