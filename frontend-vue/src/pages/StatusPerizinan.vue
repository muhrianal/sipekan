<template>
    <div class="card" id="app" style="min-height:600%;">
    <div class="d-flex">
        <div class="mr-auto p-3">
            <h4 class="judul p-1 align-middle" style="font-weight: 500;">Daftar Perizinan</h4>
        </div>
      <div class="p-3">
          <a href="/ruangan/add" class="btn tambah" style="padding:3px 6px;font-size:14px;"> Tambah Perizinan</a>
      </div>
    </div>
    <hr class="line-header" style="margin:0px;">


    <div class="d-flex flex-row-reverse mr-4 mt-2 ">
      <div class="pl-4 fsmall"><span class="dot abu"></span> Tidak Mengajukan</div>
      <div class="pl-4 fsmall"><span class="dot kuning"></span> Menunggu</div>
      <div class="pl-4 fsmall"><span class="dot merah"></span> Ditolak</div>
      <div class="pl-4 fsmall"><span class="dot hijau"></span> Disetujui</div>
    </div>

    <div class="m-1">
    <div class="card m-2 kotakstatus"  v-for="izin in perizinan" v-bind:key="izin.id">

    <div class="d-flex bd-highlight">
      <div class="p-2 flex-grow-1 bd-highlight">
      <div class="acara font-weight-bold">{{ izin.nama_kegiatan }}</div>
              <div class="organisasi" >{{ izin.organisasi }}</div>
      </div>
      <a class="p-2 pr-3 bd-highlight" style="font-size:13px" :href="'/perizinan/'+izin.id">Lihat Detail &#8594;</a>
    </div>

    <div class="m-2">
       <div class="progress m-2" style="height:8px">
       <template v-if="izin.status_perizinan_kegiatan!=3">
          <div v-if="izin.status_perizinan_kegiatan==1" class="progress-bar kuning" role="progressbar" style="width:20%"  aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"></div>
          <div class="progress-bar hijau" role="progressbar" style="width:20%"  aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"></div>

          <div class="progress-bar putih" role="progressbar" style="width:0.1%"  aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"></div>

          <div v-if="izin.peminjaman_ruangan.length==0" class="progress-bar abu" role="progressbar" style="width:20%"  aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"></div>

          <template v-if="izin.peminjaman_ruangan.length!=0" style="width:20%">
            <template v-for="pinjam in izin.peminjaman_ruangan" v-bind:key=pinjam.id>
                <div v-if="pinjam.status_peminjaman_ruangan==1" class="progress-bar flex-fill kuning p-2 bd-highlight"></div>
                <div v-if="pinjam.status_peminjaman_ruangan==2" class="progress-bar flex-fill hijau p-2 bd-highlight"></div>
                <div v-if="pinjam.status_peminjaman_ruangan==3" class="progress-bar flex-fill merah p-2 bd-highlight"></div>
            </template>
          </template>


           <div class="progress-bar putih" role="progressbar" style="width:0.1%"  aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"></div>

          <template v-if="izin.perizinan_publikasi!=null" style="width:20%">
            <div v-if="izin.perizinan_publikasi.status_perizinan_publikasi==1" class="progress-bar kuning" role="progressbar" style="width: 20%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
            <div v-if="izin.perizinan_publikasi.status_perizinan_publikasi==2" class="progress-bar hijau" role="progressbar" style="width: 20%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
            <div v-if="izin.perizinan_publikasi.status_perizinan_publikasi==3" class="progress-bar merah" role="progressbar" style="width: 20%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
          </template>
          <template v-if="izin.perizinan_publikasi==null">
            <div class="progress-bar abu" role="progressbar" style="width: 20%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
          </template>

          <div class="progress-bar putih" role="progressbar" style="width:0.1%"  aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"></div>

          <template v-if="izin.permintaan_souvenir.length!=0" style="width:20%">
            <template v-for="souvenir in izin.permintaan_souvenir" v-bind:key=souvenir.id>
                <div v-if="souvenir.status_permintaan_souvenir==1" class="progress-bar flex-fill kuning p-2 bd-highlight" ></div>
                <div v-if="souvenir.status_permintaan_souvenir==2" class="progress-bar flex-fill hijau p-2 bd-highlight" ></div>
                <div v-if="souvenir.status_permintaan_souvenir==3" class="progress-bar flex-fill merah p-2 bd-highlight" ></div>
            </template>
          </template>

          <template v-if="izin.permintaan_souvenir.length==0">
            <div class="progress-bar abu" role="progressbar" style="width: 20%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
          </template>

          <div class="progress-bar putih" role="progressbar" style="width:0.1%"  aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"></div>
          <template v-if="izin.permintaan_protokoler!=null" style="width:20%">

            <div v-if="izin.permintaan_protokoler.status_permintaan_protokoler==1" class="progress-bar kuning" role="progressbar" style="width: 20%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
            <div v-if="izin.permintaan_protokoler.status_permintaan_protokoler==2" class="progress-bar hijau" role="progressbar" style="width: 20%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
            <div v-if="izin.permintaan_protokoler.status_permintaan_protokoler==3" class="progress-bar merah" role="progressbar" style="width: 20%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>

          </template>

          <template v-if="izin.permintaan_protokoler==null">
          <div class="progress-bar abu" role="progressbar" style="width: 20%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
          </template>
       </template>
       <template v-if="izin.status_perizinan_kegiatan==3" >
          <div class="progress-bar merah" role="progressbar" style="width:20%"  aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"></div>
       </template>


        </div>

    <div class="d-flex justify-content-around mr-4 mt-2 ">
      <div class="pl-4 fsmall">Kegiatan</div>
      <div class="pl-4 fsmall">Ruangan</div>
      <div class="pl-4 fsmall">Publikasi</div>
      <div class="pl-4 fsmall">Souvenir</div>
      <div class="pl-4 fsmall">Protokoler</div>

    </div>
    </div>
    </div>
    </div>

    </div>
</template>

<script>
import UserService from '../services/user.service';
export default {
    name: 'StatusPerizinan',
    data() {
        return {
            perizinan: [[]],
            peminjaman_ruangan: [],
            error_messase: "",
        }
    },
    created(){
        console.log("masuk created daftar perizinan")
        UserService.getAllPerizinan().then(
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
.putih {
    background-color: white !important;
}
.abu {
    background-color: #BDBDBD !important;
}
.kuning {
    background-color: #FFD505 !important;
}
.merah {
    background-color: #EB5757 !important;
}
.hijau {
    background-color: #27AE60 !important;
}
.dot {
  height: 8px;
  width: 8px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
}
.fsmall{
    font-size:12px;
}
.acara{
    font-size: 24px;
    padding-left: 10px;
}
.organisasi{
    font-size: 14px;
    padding-left:10px;
}
.kotakstatus{
    border-radius:11px;
}

</style>