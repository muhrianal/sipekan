<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page" style="font-weight: 500;">{{ ruangan.nama }}</h3>
            <hr class="line-header">
        </div>


        <div class="formulir m-3">
            <form>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-3">
                        <label>Jenis Ruangan:</label>
                        <input type="text" class="form-control" v-if="ruangan.jenis_ruang==1" placeholder="Ruang Pertemuan" readonly>
                        <input type="text" class="form-control" v-if="ruangan.jenis_ruang==2" placeholder="Ruang Kelas" readonly>
                        <input type="text" class="form-control" v-if="ruangan.jenis_ruang==3" placeholder="Ruang Rapat" readonly>
                        <input type="text" class="form-control" v-if="ruangan.jenis_ruang==4" placeholder="Ruang Selasar" readonly>

                    </div>
                    <div class="col-12 col-md-6 px-3">
                        <label>Fasilitas:</label>

                        <input type="text" class="form-control" :placeholder="ruangan.fasilitas" readonly>
                    </div>

                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6 px-3">
                        <label>Nama Ruangan:</label>
                        <input type="text" class="form-control" :placeholder="ruangan.nama" readonly>
                    </div>
                    <div class="col-12 col-md-6 px-3">
                        <label>Kapasitas:</label>
                            <input type="text" class="form-control" :placeholder="ruangan.kapasitas" readonly>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-3">
                        <label>Lokasi:</label>
                        <input type="text" class="form-control" :placeholder="ruangan.lokasi" readonly>
                    </div>
                    <div class="col-12 col-md-6 px-3">
                        <label>Informasi Tambahan:</label>
                            <input type="text" class="form-control" :placeholder="ruangan.informasi_tambahan" readonly>

                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-3 px-3">
                        <label for="input">Waktu Tersedia Mulai<label style="color:red">*</label>:</label>
                        <input class="form-control"  :placeholder="getHour(ruangan.waktu_available_mulai)" readonly>
                    </div>
                    <div class="col-12 col-md-3 px-3">
                        <label for="input">Waktu Tersedia Akhir<label style="color:red">*</label>:</label>
                            <input class="form-control"  :placeholder="getHour(ruangan.waktu_available_akhir)" readonly>

                    </div>
                    <div class="col-12 col-md-6 px-3">
                    <label>Status:</label>
                        <input type="text" class="form-control" v-if="ruangan.status==1" placeholder="Aktif" readonly>
                        <input type="text" class="form-control" v-if="ruangan.status==2" placeholder="Nonaktif" readonly>
                    </div>
                </div>


            </form>
        </div>
        <div class="d-flex" style="margin-top:100px" v-if="isLoggedIn && currentUser.role == 'ADMIN FASTUR'">
                <div class="mr-auto">

                </div>
               <div class="p-2">
                    <button href="/ruangan" class="btn hapus" data-toggle="modal" data-target="#deleteModal" style="padding:3px 20px;font-size:16px;"> Hapus</button>
               </div>
              <div class="p-2 pr-4">
              <a :href="'/ruangan/ubah/'+ ruangan.id" class="btn ubah" style="padding:3px 20px;font-size:16px;"> Ubah</a>
              </div>
            </div>

<!-- Modal: Notif Sukses -->
    <div class="modal fade" id="deleteModal" tabindex="-1" role="dialog" aria-labelledby="sukses-setuju-modal" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">

            <div class="modal-body">
                <div class="text-center d-flex ml-5">
                 <img src="../../assets/images/icon_ceklis.png" alt="icon-sukses" class="my-4" style="width:7%;height:7%;margin-right:2%;">
                <p class="my-4">Ingin menghapus Ruangan?</p>
                </div>
            </div>
            <div class="modal-footer">

                        <button type="button" class="btn batal" data-dismiss="modal">Batal</button>
                        <button type="button" class="btn simpan" v-on:click="hapusRuangan">Hapus</button>

            </div>
            </div>
        </div>
    </div>
    <!-- Modal: Notif Gagal -->
    <div class="modal fade" id="deleteSuksesModal" tabindex="-1" role="dialog" aria-labelledby="gagal-submit-modal" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">

            <div class="modal-body">
                <div class="text-center">
                    <img src="../../assets/images/icon_ceklis.png" alt="icon-error">
                <p class="my-2">Ruangan {{ruangan.nama}} berhasil dihapus</p>
                </div>
            </div>
            <div class="modal-footer">
                <div class="text-center">
                    <button type="button" class="btn simpan" data-dismiss="modal" v-on:click="deleteDone" style="width:80px; height:36px;">OK</button>
                </div>
            </div>
            </div>
        </div>
    </div>
<!-- Modal -->


    </div>
</template>

<script>
import UserService from '../../services/user.service';
import moment from 'moment';
import $ from 'jquery';


export default {
    name: 'DetailRuangan',
    data() {
        return {
            ruangan: "",
            error_message : "",
        }
    },
    created(){
        console.log("masuk created detail")
        console.log(this.$route.params.id)
        UserService.getRuangan(this.$route.params.id).then(
            response => {
                this.ruangan = response.data;
            },
            error => {
                this.error_message = (error.response && error.response.data) || error.message || error.toString();
            }
        )
    },
    mounted(){
        console.log(this.ruangan);
        console.log(this.error_message);
    },
        computed: {
                    isLoggedIn() {
                        return this.$store.state.auth.status.loggedIn;
                    },
                    currentUser() {
                        return this.$store.state.auth.user;
                    }
                },
    methods: {
                        // getting a var from child to get to know that it is the active one
                        isInLoginPageFunc(value){
                            this.isInLoginPage = value;
                        },
                        isInHomePageFunc(value){
                            this.isInHomePage = value;
                        },
        hapusRuangan() {
            UserService.deleteRuangan(this.$route.params.id).then(
                response => {
                    console.log(response.data);
                    console.log("ruangan berhasil dihapus");
                    $('#deleteSuksesModal').modal('show')
                },
                error => {
                    console.log(error.message);
                }
            );
        },
        deleteDone() {
            window.location.href='/ruangan';
        },
        getDateDef : function (date) {
            return moment(date, 'YYYY-MM-DDTHH:mm').format('D MMMM YYYY');
        },
        getDate : function (date) {
            return moment(date, 'YYYY-MM-DDTHH:mm').format('HH:mm, D MMMM YYYY');
        },
        getHour : function (date) {
            return moment(date, 'YYYY-MM-DDTHH:mm').format('HH:mm');
        },
    }
}
</script>

<style>
.root-class {
    background-color: white;
    border-color: #BDBDBD;
    border-style: solid;
    border-width: 1px;
    border-radius: 5px;
    padding: 20px 20px 20px 20px ;
}
label {
    font-size: 14px;
}
.header-page {
    /* padding: 15px 0px 3px 15px; */
    font-size: 23px;
    color: #FFD505;
    font-weight: 550;
}
.line-header {
    background-color: #BDBDBD ;
}
.ubah {
    color: white;
    border-color: #FFD505;
    background-color: #FFD505 !important;
    border-radius: 10px !important;

}
.ubah:hover{
    background-color: #FFD505 !important;
    border-color: #FFD505;
    color: white;
}
.hapus {
    color: red;
    border-color: red;
    background-color: white!important;
    border-radius: 10px !important;
}
.hapus:hover {
    color: white;
    border-color: red;
    background-color: red!important;
}
input, select{
    border-radius: 10px !important;
}
</style>