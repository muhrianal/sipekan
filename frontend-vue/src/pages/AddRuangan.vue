<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page" style="font-weight: 500;">Tambah Ruangan</h3>
            <hr class="line-header">
        </div>

        <div class="formulir m-3">
            <form v-on:submit.prevent="postCreateRuangan">
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputJenisRuangan">Jenis Ruangan<label style="color:red">*</label>:</label>
                        <select class="form-control" id="exampleFormControlSelect1" v-model="jenis_ruang">
                            <option value="1">Ruang Pertemuan</option>
                            <option value="2">Ruang Kelas</option>
                            <option value="3">Ruang Rapat</option>
                            <option value="4">Selasar</option>
                        </select>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputFasilitas">Fasilitas<label>:</label></label>
                        <input type="text" class="form-control" placeholder="e.g. AC, proyektor, sound system, white board, sofa"
                        v-model="fasilitas">
                    </div>
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputNamaRuangan">Nama Ruangan<label style="color:red">*</label>:</label>
                        <input type="text" class="form-control" placeholder="e.g. Auditorium" v-model="nama">
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputKapasitas">Kapasitas<label style="color:red">*</label>:</label>
                        <input type="number" class="form-control" placeholder="e.g. 350" v-model="kapasitas">
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputLokasi">Lokasi<label style="color:red">*</label>:</label>
                        <input type="text" class="form-control" placeholder="e.g. Gedung Dekanat Lantai 1" v-model="lokasi">
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputKeterangan">Informasi Tambahan<label>:</label></label>
                        <input type="text" class="form-control" placeholder="peminjaman ruangan maksimal dilakukan h-3 kegiatan"
                        v-model="informasi_tambahan">
                    </div>
                </div>
                <div class="d-flex" style="margin-top:100px">
                            <div class="mr-auto"> </div>
                            <div class="p-2">
                                <a href="/ruangan" class="btn batal" style="padding:3px 20px;font-size:16px;"> Batal</a>
                            </div>
                            <div class="p-2 pr-4">
                            <a href="/ruangan">
                                <button class="btn simpan" style="padding:3px 20px;font-size:16px;"
                                v-on:click="postCreateRuangan"
                                > Simpan</button>
                            </a>
                            </div>

                            </div>
        </form>


        </div>


        </div>

</template>

<script>
import UserService from '../services/user.service';
export default {
    name: 'AddRuangan',
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
    methods: {
        postCreateRuangan() {
            console.log("masuk post ruangan")

            const data_post = {
                jenis_ruang: this.jenis_ruang,
                nama: this.nama,
                kapasitas: this.kapasitas,
                fasilitas: this.fasilitas,
                lokasi: this.lokasi,
                informasi_tambahan: this.informasi_tambahan,
                waktu_available_mulai: "2021-04-21T21:50:41+07:00",
                waktu_available_akhir: "2022-04-21T21:50:48+07:00",
                status: "1",
            };
            UserService.postRuangan(data_post).then(
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
}
.line-header {
    background-color: #BDBDBD ;
}
input, select{
    border-radius: 10px !important;
}
</style>