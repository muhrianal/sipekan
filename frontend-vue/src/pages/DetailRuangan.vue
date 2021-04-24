<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page" style="font-weight: 500;">{{ ruangan.nama }}</h3>
            <hr class="line-header">
        </div>


        <div class="formulir m-3">
            <form>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Jenis Ruangan:</label>
                        <input type="text" class="form-control" v-if="ruangan.jenis_ruang==1" placeholder="Ruang Pertemuan" readonly>
                        <input type="text" class="form-control" v-if="ruangan.jenis_ruang==2" placeholder="Ruang Kelas" readonly>
                        <input type="text" class="form-control" v-if="ruangan.jenis_ruang==3" placeholder="Ruang Rapat" readonly>
                        <input type="text" class="form-control" v-if="ruangan.jenis_ruang==4" placeholder="Ruang Selasar" readonly>

                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Fasilitas:</label>

                        <input type="text" class="form-control" :placeholder="ruangan.fasilitas" readonly>
                    </div>

                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Nama Ruangan:</label>
                        <input type="text" class="form-control" :placeholder="ruangan.nama" readonly>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Keterangan:</label>
                        <input type="text" class="form-control" :placeholder="ruangan.informasi_tambahan" readonly>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Lokasi:</label>
                        <input type="text" class="form-control" :placeholder="ruangan.lokasi" readonly>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Status:</label>
                        <input type="text" class="form-control" v-if="ruangan.status==1" placeholder="Aktif" readonly>
                        <input type="text" class="form-control" v-if="ruangan.status==2" placeholder="Nonaktif" readonly>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Kapasitas:</label>
                        <input type="text" class="form-control" :placeholder="ruangan.kapasitas" readonly>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                    </div>
                </div>


            </form>
        </div>
        <div class="d-flex" style="margin-top:100px">
                <div class="mr-auto">

                </div>
               <div class="p-2">
                    <button href="/ruangan" class="btn hapus" v-on:click="hapusRuangan" style="padding:3px 20px;font-size:16px;"> Hapus</button>
               </div>
              <div class="p-2 pr-4">
              <a :href="'/ruangan/ubah/'+ ruangan.id" class="btn ubah" style="padding:3px 20px;font-size:16px;"> Ubah</a>
              </div>
            </div>

    </div>
</template>

<script>
import UserService from '../services/user.service';
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
    methods: {
        hapusRuangan() {
            UserService.deleteRuangan(this.$route.params.id).then(
                response => {
                    console.log(response.data);
                    console.log("ruangan berhasil dihapus");
                },
                error => {
                    console.log(error.message);
                }
            );
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