
<template>
    <div class="card">
    <div class="d-flex">
        <div class="mr-auto p-3">
            <h4 class="judul p-1 align-middle" style="font-weight: bold;">Daftar Ruangan</h4>
        </div>
      <div class="p-3" v-if="isLoggedIn && currentUser.role == 'ADMIN FASTUR'" v-bind:class="{active : isInHomePage}" >
          <a href="/ruangan/add" class="btn tambah adminfastur" style="padding:3px 6px;font-size:14px;"> Tambah Ruangan</a>
      </div>
    </div>
    <div class="table-responsive">
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col" class="text-center" > No.</th>
          <th scope="col" class="text-center">Nama Ruangan</th>
          <th scope="col" class="text-center">Jenis Ruangan</th>
          <th scope="col" class="text-center">Lokasi</th>
          <th scope="col" class="text-center">Kapasitas</th>
          <th scope="col"></th>

        </tr>
      </thead>
      <tbody id="app" style="font-weight=300;">
        <tr v-for="(ruang, index) in ruangan" v-bind:key="ruang.id">
            <th scope="row" class="text-center" >{{ index+1+"." }} </th>
            <td class="text-center">{{ ruang.nama }}</td>
            <td class="text-center" v-if="ruang.jenis_ruang==1">Ruang Pertemuan</td>
            <td class="text-center" v-if="ruang.jenis_ruang==2">Ruang Kelas</td>
            <td class="text-center" v-if="ruang.jenis_ruang==3">Ruang Rapat</td>
            <td class="text-center" v-if="ruang.jenis_ruang==4">Ruang Selasar</td>
            <td class="text-center">{{ ruang.lokasi }}</td>
            <td class="text-center">{{ ruang.kapasitas }}</td>
            <td><a :href="'/ruangan/'+ruang.id">Detail</a></td>
        </tr>

      </tbody>
    </table>
    </div>
    </div>
</template>


<script>
import UserService from '../../services/user.service';


export default {
    name: 'Ruangan',
    data() {
        return {
            ruangan: [],
        }
    },
    created(){
        console.log("masuk created daftar")
        UserService.getAllRuangan().then(
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