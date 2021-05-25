
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
            <td class="text-center">-</td>            
            <td class="text-center">-</td>           
            <td class="text-center"><a href="/" class="btn simpan mr-2" style="padding:3px 6px;font-size:14px;">Ubah</a>
            <a href="/" class="btn batal" style="padding:3px 6px;font-size:14px;">Hapus</a>
            </td>
        </tr>

      </tbody>
    </table>
    </div>
    </div>
</template>


<script>
import UserService from '../../services/user.service';


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