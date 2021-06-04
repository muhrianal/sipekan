<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page" style="font-weight: bold;">Tambah Souvenir</h3>
            <hr class="line-header">
        </div>

        <div class="formulir m-3">
            <form>
                

                <div class="form-row">
                    <div class="col-12 col-md-6 px-3">
                        <label >Nama Souvenir<label style="color:red">*</label>:</label>
                        <input name="fname" type="text" class="form-control" id="nama" placeholder="e.g. Pulpen" v-model="nama_souvenir">
                    </div>
                    <div class="col-12 col-md-6 px-3">
                        <label class="fontg3">Kelas<label style="color:red">*</label>:</label>
                        <select class="form-control" id="jenis_ruang" v-model="kelas">
                            <option value="1">Kelas 1</option>
                            <option value="2">Kelas 2</option>
                            <option value="3">Kelas 3</option>
                            <option value="4">Kelas 1 & Kelas 2</option>
                            <option value="5">Kelas 1 & Kelas 3</option>
                            <option value="6">Kelas 2 & Kelas 3</option>
                            <option value="7">Kelas 1 & Kelas 2 & Kelas 3</option>
                        </select>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-3">
                        <label class="fontg3">Region<label style="color:red">*</label>:</label>
                        <select class="form-control" id="jenis_ruang" v-model="region">
                            <option value="1">Dalam Negeri</option>
                            <option value="2">Luar Negeri</option>
                            <option value="3">Dalam Negeri dan Luar Negeri</option>
                        </select>
                    </div>
                    <div class="col-12 col-md-3 px-3">
                        <label for="inputKeterangan">Stok<label style="color:red">*</label>:</label>
                        <input type="number" class="form-control" placeholder="30"
                        v-model="stok">
                    </div>
                    <div class="col-12 col-md-3 px-3">
                        <label for="inputKeterangan">Stok Minimum<label style="color:red">*</label>:</label>
                        <input type="number" class="form-control" placeholder="30"
                        v-model="stok_minimum">
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-3">
                        <label class="fontg3">Keterangan<label>:</label></label>
                        <input name="fname" type="text" class="form-control" id="nama" placeholder="e.g. Barang dipesan dari vendor oleh xx" v-model="keterangan">

                    </div>
                    <div class="col-12 col-md-6 px-3">
                        <label for="inputKeterangan">Tanggal Masuk Souvenir<label>:</label></label>
                        <input type="date" class="form-control" 
                        v-model="tanggal_masuk">
                    </div>
                </div>
               

        </form>
                        <div class="d-flex" style="margin-top:100px">
                            <div class="mr-auto"> </div>
                                <div class="p-2">
                                    <a href="/souvenir" class="btn batal" style="padding:3px 20px;font-size:16px;"> Batal</a>
                                </div>
                            <div class="p-2 pr-4">

                                <button class="btn simpan" id="btnValidate" style="padding:3px 20px;font-size:16px;"
                                        v-on:click="postCreateSouvenir"
                                        > Simpan</button>
                            </div>
                        </div>
 <!-- Modal: Notif Sukses -->
    <div class="modal fade" id="notification-success" tabindex="-1" role="dialog" aria-labelledby="sukses-setuju-modal" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">

            <div class="modal-body">
                <div class="text-center">
                    <img src="../../assets/images/icon_ceklis.png" alt="icon-sukses">
                <h2 style="margin:20px 0px 15px 0px">Sukses</h2>
                <p style="margin:0px 0px -15px 0px">Souvenir berhasil disimpan</p>
                </div>
            </div>
            <div class="modal-footer">
                <div class="text-center">
                    <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="addDone" style="width:80px; height:36px;">OK</button>
                </div>
            </div>
            </div>
        </div>
    </div>
    <!-- Modal: Notif Gagal -->
    <div class="modal fade" id="notification-failed" tabindex="-1" role="dialog" aria-labelledby="gagal-submit-modal" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">

            <div class="modal-body">
                <div class="text-center">
                    <img src="../../assets/images/icon_silang.png" alt="icon-error">
                <h2 style="margin:20px 0px 15px 0px">Error</h2>
                <p style="margin:0px 0px -15px 0px">Bagian berbintang harus diisi</p>
                </div>
            </div>
            <div class="modal-footer">
                <div class="text-center">
                    <button type="button" class="btn btn-success" data-dismiss="modal" style="width:80px; height:36px;">OK</button>
                </div>
            </div>
            </div>
        </div>
    </div>

        </div>


        </div>

</template>

<script>
import UserService from '../../services/user.service';
import $ from 'jquery';

export default {
    name: 'AddSouvenir',
    data() {
        return {
            souvenir: [],
            error_messase: "",
        }
    },
    created(){
        console.log("masuk created daftar")
        
    },
    mounted(){
        console.log(this.souvenir);
        
    },
    methods: {
        postCreateSouvenir() {
            console.log("masuk post souvenir")
            const souvenir_post = {
                nama_souvenir: this.nama_souvenir,
                region: this.region,
                kelas: this.kelas,
                stok: this.stok,
                stok_minimum: this.stok_minimum,
                tanggal_masuk: this.tanggal_masuk,
                keterangan: this.keterangan,

            };
            console.log(souvenir_post);
            UserService.postSouvenir(souvenir_post).then(
                response => {
                    console.log(response.data);
                    $('#notification-success').modal('show')
                },
                error => {
                    console.log(souvenir_post);
                    this.error_message = error.message
                    $('#notification-failed').modal('show')
                    console.log(error.message);
                }
        );
        },
        addDone() {
            window.location.href='/souvenir';
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
}
.line-header {
    background-color: #BDBDBD ;
}
input, select{
    border-radius: 10px !important;
}
.fontg3{
    color: #828282 !important;
}
</style>