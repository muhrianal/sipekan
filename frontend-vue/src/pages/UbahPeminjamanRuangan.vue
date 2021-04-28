<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page" style="font-weight: 500;">Ubah Ruangan</h3>
            <hr class="line-header">
        </div>

        <div class="formulir m-3">
            <form>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Jenis Ruangan:</label>
                        <select class="form-control" id="exampleFormControlSelect1" v-model="jenis_ruang">
                            <option value="1">Ruang Pertemuan</option>
                            <option value="2">Ruang Kelas</option>
                            <option value="3">Ruang Rapat</option>
                            <option value="4">Selasar</option>
                        </select>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Fasilitas:</label>
                        <input type="text" class="form-control" v-model="fasilitas" :placeholder="ruangan.fasilitas" onfocus="this.placeholder=''">
                    </div>

                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Nama Ruangan:</label>
                        <input type="text" class="form-control" v-model="nama" :placeholder="ruangan.nama" onfocus="this.placeholder=''">
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Informasi Tambahan:</label>
                        <input type="text" class="form-control" v-model="informasi_tambahan" :placeholder="ruangan.informasi_tambahan" onfocus="this.placeholder=''">
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Lokasi:</label>
                        <input type="text" class="form-control" v-model="lokasi" :placeholder="ruangan.lokasi" onfocus="this.placeholder=''">
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Status:</label>
                        <select class="form-control" id="exampleFormControlSelect1" v-model="status">
                            <option value="1">Aktif</option>
                            <option value="2">Nonaktif</option>
                        </select>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Kapasitas:</label>
                        <input type="text" class="form-control" v-model="kapasitas" :placeholder="ruangan.kapasitas" onfocus="this.placeholder=''">
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                    </div>
                </div>


            </form>
            <div class="d-flex" style="margin-top:100px">
                        <div class="mr-auto">

                        </div>
                        <div class="p-2">
                            <a href="/ruangan/detail" class="btn batal" style="padding:3px 20px;font-size:16px;"> Batal</a>
                        </div>
                        <div class="p-2 pr-4">
                            <button href="/ruangan" class="btn simpan" v-on:click="putEditRuangan" style="padding:3px 20px;font-size:16px;"> Simpan</button>
                        </div>

                        </div>
        </div>


    </div>
</template>

<script>
import UserService from '../services/user.service';
export default {
    name: 'EditRuangan',
    data() {
        return {
            ruangan: [],
            error_messase: "",
            jenis_ruang: "",
            nama: "",
            kapasitas: "",
            fasilitas: "",
            lokasi: "",
            informasi_tambahan: "",
            waktu_available_mulai: "",
            waktu_available_akhir: "",
            status:"",
        }
    },
    created(){
        console.log("masuk created daftar")
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
        putEditRuangan() {
            console.log("masuk put ruangan");
            console.log(this.$route.params.id);

            const data_put = {
                id: this.$route.params.id,
                jenis_ruang: this.jenis_ruang,
                nama: this.nama,
                kapasitas: this.kapasitas,
                fasilitas: this.fasilitas,
                lokasi: this.lokasi,
                informasi_tambahan: this.informasi_tambahan,
                waktu_available_mulai: "2021-04-21T21:50:41+07:00",
                waktu_available_akhir: "2022-04-21T21:50:48+07:00",
                status: this.status,
            };
            console.log(data_put);
            UserService.putRuangan(this.$route.params.id, data_put).then(
                response => {
                    console.log(response.data);
                },
                error => {
                    console.log(error.message);
                }
        );
        }
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
.simpan {
    color: white;
    border-color: #27AE60;
    background-color: #27AE60 !important;
    border-radius: 10px !important;
}
.simpan:hover {
    color: #27AE60;
    border-color: #27AE60;
    background-color: white !important;
    border-radius: 10px !important;
}

.batal {
    color: red;
    border-color: red;
    background-color: white!important;
    border-radius: 10px !important;
}
.batal:hover {
    color: white;
    border-color: red;
    background-color: red!important;
}
input, select{
    border-radius: 10px !important;
}
</style>