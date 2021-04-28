<template>
    <div class="card fmed" id="app" style="min-height:600%;">
    <div class="d-flex">
        <div class="mr-auto p-3">
            <h4 class="judul p-1 align-middle" style="font-weight: 500;">Daftar Perizinan</h4>
        </div>
      <div class="p-3">
          <a href="/ruangan/add" class="btn tambah" style="padding:3px 6px;font-size:14px;"> Tambah Perizinan</a>
      </div>
    </div>
    <hr class="line-header" style="margin:0px;">

    <div style="margin:1% 7%;">
    <div class="table-responsive">
    <table class="table table-sm table-bordered" style="border-radius: 10px 10px 0px 0px;">
      <thead class="thead kuning rounded-top" style="border-radius: 10px 10px 0px 0px;">
        <tr style="border-radius: 10px;">
          <th scope="col" colspan="2" class="text-center" style="border-radius: 5px 5px 0px 0px;">Informasi Kegiatan</th>
        </tr>
      </thead>
      <tbody class="fsmall">
        <tr>
          <td>Nama Kegiatan</td>
          <td style="min-height=50%">{{ perizinan.nama_kegiatan }}</td>
        </tr>
        <tr>
          <td>Organisasi Penanggungjawab</td>
          <td>{{ perizinan.organisasi}}</td>
        </tr>
        <tr>
          <td>Nama PIC Kegiatan</td>
          <td>{{  }}</td>
        </tr>
        <tr>
          <td>Status</td>
          <td v-if="perizinan.status_perizinan_kegiatan==1">Menunggu Persetujuan</td>
          <td v-if="perizinan.status_perizinan_kegiatan==2">Disetujui</td>
          <td v-if="perizinan.status_perizinan_kegiatan==3">Ditolak <a :href="'/izin-kegiatan/ubah/'+ perizinan.id">edit</a>
          </td>

        </tr>
      </tbody>
    </table>
    </div>
    </div>

    <div style="margin:1% 7%;">
        <div class="table-responsive">
        <table class="table table-sm table-bordered" style="border-radius: 10px 10px 0px 0px;">
          <thead class="thead kuning rounded-top" style="border-radius: 10px 10px 0px 0px;">
            <tr style="border-radius: 10px;">
              <th scope="col" colspan="6" class="text-center" style="border-radius: 5px 5px 0px 0px;">Informasi Peminjaman Ruangan</th>
            </tr>
          </thead>
          <tbody class="fsmall">
            <tr>
              <td class="text-center abu2">Nama Kegiatan</td>
              <td class="text-center abu2">Nama Ruang</td>
              <td class="text-center abu2">Tanggal</td>
              <td class="text-center abu2">Waktu</td>
              <td class="text-center abu2">Pengulangan</td>
              <td class="text-center abu2">Status</td>
            </tr>
            <tr v-for="pinjam in perizinan.peminjaman_ruangan" v-bind:key="pinjam.id">
              <td class="text-center">{{pinjam.judul_peminjaman}} </td>
              <td class="text-center">{{pinjam.ruangan}}</td>
              <td class="text-center">{{getDateDef(pinjam.waktu_mulai)}}</td>
              <td class="text-center">{{getHour(pinjam.waktu_mulai)}} - {{getHour(pinjam.waktu_akhir)}}</td>
              <td></td>
              <td class="text-center" v-if="pinjam.status_peminjaman_ruangan==1">Menunggu Persetujuan</td>
              <td class="text-center" v-if="pinjam.status_peminjaman_ruangan==2">Disetujui</td>
              <td class="text-center" v-if="pinjam.status_peminjaman_ruangan==3">Ditolak <a :href="'/peminjaman-ruangan/ubah/'+ pinjam.id">edit</a></td>

            </tr>

          </tbody>
        </table>
        </div>
        </div>

        <div style="margin:1% 7%;">
        <div class="table-responsive">
        <table class="table table-sm table-bordered" style="border-radius: 10px 10px 0px 0px;">
          <thead class="thead kuning rounded-top" style="border-radius: 10px 10px 0px 0px;">
            <tr style="border-radius: 10px;">
              <th scope="col" colspan="6" class="text-center" style="border-radius: 5px 5px 0px 0px;">Informasi Publikasi, Souvenir, dan Protokoler</th>
            </tr>
          </thead>
        </table>
        <div class="fmed font-weight-bold abu3">Publikasi </div>
        <table v-if="perizinan.perizinan_publikasi==null" class="table table-sm table-bordered mt-2 fsmall" style="border-radius: 10px 10px 0px 0px;">
            <tr>
              <td class="text-center abu2">Jenis Publikasi Luar Ruangan</td>
              <td class="text-center abu2">Jenis Publikasi</td>
              <td class="text-center abu2">Lokasi</td>
              <td class="text-center abu2">Tanggal Mulai</td>
              <td class="text-center abu2">Tanggal Akhir</td>
              <td class="text-center abu2">Status</td>
            </tr>
            <tr>
              <td class="text-center">-</td>
              <td class="text-center">-</td>
              <td class="text-center ">-</td>
              <td class="text-center ">-</td>
              <td class="text-center ">-</td>
              <td class="text-center ">-</td>
            </tr>
        </table>
        <table v-if="perizinan.perizinan_publikasi!=null" class="table table-sm table-bordered mt-2 fsmall" style="border-radius: 10px 10px 0px 0px;">
            <tr>
              <td class="text-center abu2">Jenis Publikasi Luar Ruangan</td>
              <td class="text-center abu2">Jenis Publikasi</td>
              <td class="text-center abu2">Lokasi</td>
              <td class="text-center abu2">Tanggal Mulai</td>
              <td class="text-center abu2">Tanggal Akhir</td>
              <td class="text-center abu2">Status</td>
            </tr>
            <tr>
            <td></td>
            <td></td>
            <td></td>
            <td>{{getDateDef(perizinan.perizinan_publikasi.tanggal_mulai)}}</td>
            <td>{{getDateDef(perizinan.perizinan_publikasi.tanggal_akhir)}}</td>
            <td class="text-center" v-if="perizinan.perizinan_publikasi.status_perizinan_publikasi==1">Menunggu Persetujuan</td>
            <td class="text-center" v-if="perizinan.perizinan_publikasi.status_perizinan_publikasi==2">Disetujui</td>
            <td class="text-center" v-if="perizinan.perizinan_publikasi.status_perizinan_publikasi==3">Ditolak <a href="/ruangan/add">edit</a></td>

            </tr>
        </table>
        </div>
        <div class="fmed font-weight-bold abu3">Souvenir </div>
        <div class="table-responsive">
        <table v-if="perizinan.permintaan_protokoler==null" class="table table-sm table-bordered mt-2 fsmall" style="border-radius: 10px 10px 0px 0px;">
            <tr>
              <td class="text-center abu2">Nama Pembicara</td>
              <td class="text-center abu2">Jabatan Pembicara</td>
              <td class="text-center abu2">Kelas</td>
              <td class="text-center abu2">Souvenir</td>
              <td class="text-center abu2">Kuantitas</td>
              <td class="text-center abu2">Status</td>
            </tr>
            <tr>
              <td class="text-center">-</td>
              <td class="text-center">-</td>
              <td class="text-center ">-</td>
              <td class="text-center ">-</td>
              <td class="text-center ">-</td>
              <td class="text-center ">-</td>
            </tr>
         </table>
        <table v-if="perizinan.permintaan_protokoler!=null" class="table table-sm table-bordered mt-2 fsmall" style="border-radius: 10px 10px 0px 0px;">
            <tr>
              <td class="text-center abu2">Nama Pembicara</td>
              <td class="text-center abu2">Jabatan Pembicara</td>
              <td class="text-center abu2">Kelas</td>
              <td class="text-center abu2">Souvenir</td>
              <td class="text-center abu2">Kuantitas</td>
              <td class="text-center abu2">Status</td>

            </tr>
            <tr v-for="souvenir in perizinan.permintaan_souvenir" v-bind:key="souvenir.id">
            <td>{{souvenir.nama_penerima_souvenir}}</td>
            <td>{{souvenir.jabatan_penerima_souvenir}}</td>
            <td>{{souvenir.kelas}}</td>
            <td>{{souvenir.souvenir}}</td>
            <td>{{souvenir.jumlah}}</td>
            <td class="text-center" v-if="souvenir.status_permintaan_souvenir==1">Menunggu Persetujuan</td>
            <td class="text-center" v-if="souvenir.status_permintaan_souvenir==2">Disetujui</td>
            <td class="text-center" v-if="souvenir.status_permintaan_souvenir==3">Ditolak <a href="/ruangan/add">edit</a></td>
            </tr>
        </table>
        </div>
        <div class="fmed font-weight-bold abu3">Protokoler </div>
        <div class="table-responsive">
        <table v-if="perizinan.permintaan_protokoler==null" class="table table-sm table-bordered mt-2 fsmall" style="border-radius: 10px 10px 0px 0px;">
            <tr>
              <td class="text-center abu2">Deskripsi Kebutuhan</td>
              <td class="text-center abu2">Status</td>
            </tr>
            <tr>
              <td class="text-center ">-</td>
              <td class="text-center ">-</td>
            </tr>
        </table>
        <table v-if="perizinan.permintaan_protokoler!=null" class="table table-sm table-bordered mt-2 fsmall" style="border-radius: 10px 10px 0px 0px;">
            <tr>
              <td class="text-center abu2">Deskripsi Kebutuhan</td>
              <td class="text-center abu2">Status</td>

            </tr>
            <tr>
                <td>{{perizinan.permintaan_protokoler.deskripsi_kebutuhan}}</td>
                <td class="text-center" v-if="perizinan.permintaan_protokoler.status_permintaan_protokoler==1">Menunggu Persetujuan</td>
                <td class="text-center" v-if="perizinan.permintaan_protokoler.status_permintaan_protokoler==2">Disetujui</td>
                <td class="text-center" v-if="perizinan.permintaan_protokoler.status_permintaan_protokoler==3">Ditolak <a href="/ruangan/add">edit</a></td>

            </tr>
        </table>
        </div>
        <div class="fmed font-weight-bold abu3">Komentar </div>
            <div v-for="pinjam in perizinan.peminjaman_ruangan" v-bind:key="pinjam.id">
                <div v-if="pinjam.alasan_penolakan!=null" class="d-flex mb-2">
                    <div class="pt-1"> Admin Fastur </div>
                    <div class="label abu2 ml-4 pl-2 pt-1 komentar align-middle">{{pinjam.alasan_penolakan}}</div>

                </div>
            </div>
            <div v-for="souvenir in perizinan.permintaan_souvenir" v-bind:key="souvenir.id">
                <div v-if="souvenir.alasan_penolakan!=null" class="d-flex mb-2">
                    <div class="pt-1">Admin Humas </div>
                    <div class="label abu2 pl-2 pt-1 komentar align-middle">{{souvenir.alasan_penolakan}}</div>
                </div>
            </div>
        </div>


    </div>

</template>
<script>
import UserService from '../services/user.service';
import moment from 'moment';

export default {
    name: 'DetailPerizinan',
    data() {
        return {
            perizinan: "",
            error_message : "",
        }
    },
    methods: {
             getDateDef : function (date) {
                 return moment(date, 'YYYY-MM-DDTHH:mm').format('D MMMM YYYY');
             },
             getDate : function (date) {
                 return moment(date, 'YYYY-MM-DDTHH:mm').format('HH:mm, D MMMM YYYY');
             },
             getHour : function (date) {
                 return moment(date, 'YYYY-MM-DDTHH:mm').format('HH:mm');
             },
         },
    created(){
        console.log("masuk detail")
        console.log(this.$route.params.id)
        UserService.getPerizinan(this.$route.params.id).then(
            response => {
                this.perizinan = response.data;
            },
            error => {
                this.error_message = (error.response && error.response.data) || error.message || error.toString();
            }
        )
    },
    mounted(){
        console.log(this.perizinan);
        console.log(this.error_message);
    },

}
</script>
<style>
table-bordered{
    border-radius: 5px !important;
}
.fmed{
    font-size:14px;
}
.abu3{
    color:#777777 !important;
}
.abu2{
    background-color:#E8E8E8 !important;
}
.komentar{
    width:88%;
    height: 30px;
    padding:2px;
    margin-left:2%;
    border-radius: 5px;
}
</style>