
<template>
    <div class="card">
    <div class="d-flex">
        <div class="mr-auto p-3">
            <h4 class="judul p-1 align-middle" style="font-weight: bold;">Daftar Souvenir</h4>
        </div>
      <div class="p-3" v-if="isLoggedIn && currentUser.role == 'ADMIN HUMAS'" v-bind:class="{active : isInHomePage}" >
          <a href="/souvenir/add" class="btn tambah adminfastur" style="padding:3px 6px;font-size:14px;"> Tambah Souvenir</a>
      </div>
    </div>
    <div class="table-responsive">
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col" class="text-center" > No.</th>
          <th scope="col" class="text-center">Nama Souvenir</th>       
          <th scope="col" class="text-center">Stok</th>
          <th scope="col" class="text-center">Tanggal Masuk</th>
          <th scope="col" class="text-center">Keterangan</th>          
          <th scope="col" class="text-center">Aksi</th>

        </tr>
      </thead>
      <tbody id="app" style="font-weight=300;">
        <tr v-for="(souv, index) in souvenir" v-bind:key="souv.id">
            <th scope="row" class="text-center" >{{ index+1+"." }} </th>
            <td>{{ souv.nama_souvenir }}</td>
            <td class="text-center">{{ souv.stok }}</td>
            <td class="text-center">{{ souv.tanggal_masuk }}</td>            
            <td class="text-center">{{ souv.keterangan }}</td>           
            <td class="text-center"><a :href="'/souvenir/ubah/'+souv.id" class="btn simpan mr-2" style="padding:3px 6px;font-size:14px;">Ubah</a>
            <a href="/" class="btn batal" data-toggle="modal" data-target="#deleteModal" style="padding:3px 6px;font-size:14px;">Hapus</a>
            </td>
            <!-- Modal: Konfirmasi Hapus -->
    <div class="modal fade" id="deleteModal" tabindex="-1" role="dialog" aria-labelledby="sukses-setuju-modal" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">

            <div class="modal-body">
                <div class="text-center d-flex ml-5">
                 <img src="../../assets/images/icon_ceklis.png" alt="icon-sukses" class="my-4" style="width:7%;height:7%;margin-right:2%;">
                <p class="my-4">Ingin menghapus Souvenir?</p>
                </div>
            </div>
            <div class="modal-footer">

                        <button type="button" class="btn batal" data-dismiss="modal">Batal</button>
                        <button type="button" class="btn simpan" v-on:click="hapusSouvenir(souv.id)">Hapus</button>

            </div>
            </div>
        </div>
    </div>
    <!-- Modal: Notif Berhasil Dihapus -->
    <div class="modal fade" id="deleteSuksesModal" tabindex="-1" role="dialog" aria-labelledby="gagal-submit-modal" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">

            <div class="modal-body">
                <div class="text-center">
                    <img src="../../assets/images/icon_ceklis.png" alt="icon-error">
                <p class="my-2">Souvenir {{ souv.nama_souvenir }} berhasil dihapus</p>
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
        </tr>

      </tbody>
    </table>
    </div>
    </div>
    
</template>


<script>
import UserService from '../../services/user.service';
import $ from 'jquery';


export default {
    name: 'Souvenir',
    data() {
        return {
            souvenir: [],
        }
    },
    created(){
        console.log("masuk created daftar")
        UserService.getAllSouvenir().then(
            response => {
                this.souvenir = response.data;
            },
            error => {
                this.error_message = (error.response && error.response.data) || error.message || error.toString();
            }
        )
    },
    mounted(){
        console.log(this.souvenir);
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
        methods:{

            // getting a var from child to get to know that it is the active one
            isInLoginPageFunc(value){
                this.isInLoginPage = value;
            },
            isInHomePageFunc(value){
                this.isInHomePage = value;
            },
            hapusSouvenir(id) {
            UserService.deleteSouvenir(id).then(
                response => {
                    console.log(response.data);
                    console.log("souvenir berhasil dihapus");
                    $('#deleteSuksesModal').modal('show')
                },
                error => {
                    console.log(error.message);
                }
            );
        },
        deleteDone() {
            window.location.href='/souvenir';
        },
        },

}
</script>


<style>

.judul{
    color: #FFD505;
}
*{
    font-weight: bold !important;
}
h4{
    margin-bottom:0px;
}
.tambah {
    color: #FFD505;
    border-color: #FFD505;
    border-width: 2px;
}

.tambah:hover{
    background-color: #FFD505 !important;
    border-color: #FFD505;
    color: white;
}
</style>