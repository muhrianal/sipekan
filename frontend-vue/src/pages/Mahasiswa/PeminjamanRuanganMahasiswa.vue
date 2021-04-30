<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page">Buat Perizinan<span style="color:grey"> >> Ruangan</span></h3>
            <hr class="line-header line-title">
        </div>
        <div class="formulir">
            <form v-on:submit.prevent="submitPost">
                <div v-for="peminjaman in number_of_peminjaman" v-bind:key="peminjaman">
                <hr v-if="peminjaman>1" >
                <div class="text-right">
                    <button type="button" class="btn btn-outline-danger" id="button-hapus" @click="deleteRow(peminjaman - 1)" v-if="peminjaman > 1">Hapus</button>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputSubkegiatan">Nama Subkegiatan<span class="asterisk">*</span></label>
                        <input type="text" class="form-control" placeholder="e.g. Administrasi Bisnis - B" v-model="list_peminjaman_ruangan[peminjaman-1].judul_peminjaman" required>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputJumlahPeserta">Jumlah Peserta<span class="asterisk">*</span></label>
                        <input type="number" class="form-control" placeholder="e.g. 120" v-model="list_peminjaman_ruangan[peminjaman-1].jumlah_peserta" required>
                    </div>  
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="waktuMulaiPeminjaman">Waktu mulai<span class="asterisk">*</span></label>
                        <select class="form-control" id="waktuMulaiPeminjaman" v-model="list_peminjaman_ruangan[peminjaman-1].waktu_mulai" required>
                            <option selected disabled value="">Pilih...</option>
                                <option v-for="option in option_waktu" v-bind:key="option" v-bind:value="option.value">{{option.text}}</option>
                        </select>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="waktuAkhirPeminjaman">Waktu akhir<span class="asterisk">*</span></label>
                        <select class="form-control" id="waktuAkhirPeminjaman" v-model="list_peminjaman_ruangan[peminjaman-1].waktu_akhir" required>
                            <option selected disabled value="">Pilih...</option>
                                <option v-for="option in option_waktu" v-bind:key="option" v-bind:value="option.value">{{option.text}}</option>
                        </select>
                    </div>  
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="ruangan">Ruangan<span class="asterisk">*</span></label>
                        <select class="form-control" id="daftar-ruangan" v-model="list_peminjaman_ruangan[peminjaman-1].ruangan" required>
                            <option selected disabled value="">Pilih...</option>
                            <option v-for="pilihan_ruangan in list_ruangan" v-bind:key="pilihan_ruangan.id" :value="pilihan_ruangan.id">{{pilihan_ruangan.nama}}</option>
                        </select>
                        <p class="note-ruangan note-form text-right">Lihat daftar ruangan <a href="#">disini</a> </p>
                        <label for="perulangan">Perulangan<span class="asterisk">*</span></label>
                        <select class="form-control" id="perulangan" v-model="list_perulangan[peminjaman-1].jenjang" required>
                            <option selected disabled value="">Pilih...</option>
                            <option value=1>SEKALI PAKAI</option>
                            <option value=2>HARIAN</option>
                            <option value=3>MINGGUAN</option>
                            <option value=4>BULANAN</option>
                        </select>
                    </div>

                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="keterangan">Keterangan</label>
                        <textarea class="form-control" id="textarea-keterangan" rows="4" v-model="list_peminjaman_ruangan[peminjaman-1].catatan" placeholder="e.g. Fasilitas yang akan digunakan"></textarea>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="tanggalMulaiPelaksanaan">Tanggal Mulai Pelaksanaan<span class="asterisk">*</span></label>
                        <input type="date" class="form-control" v-model="list_perulangan[peminjaman -1].tanggal_mulai" required>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" v-model="list_peminjaman_ruangan[peminjaman-1].terbuka_untuk_umum" id="checkbox-terbuka-untuk-umum">
                            <label class="form-check-label" for="flexCheckDefault">
                                Terbuka untuk umum
                            </label>
                        </div>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="tanggalAkhirPelaksanaan">Tanggal Akhir Pelaksanaan<span class="asterisk">*</span></label>
                        <input type="date" class="form-control" v-model="list_perulangan[peminjaman -1].tanggal_akhir" required>
                        <p class="note-form">isi dengan tanggal yang sama dengan tanggal mulai pelaksanaan jika memilih "sekali pakai"</p>
                    </div>  
                </div>
                    </div>
                    <div class="text-center">
                        <button @click="addRow" type="button" class="btn tambah-ruangan btn-outline-secondary">Tambah Ruangan</button>
                    </div> 
                <div class="text-right">
                    <button  type="button" class="btn btn-outline-danger rounded" @Click="batalPeminjaman" id="button-batal"> Batal Mengajukan Peminjaman</button>
                    <input class="btn btn-success btn-simpan" type=submit value="Simpan">
                </div>
            </form>
                </div>
        <!-- Modal: Notif Sukses -->
        <div class="modal fade" id="notification-success" tabindex="-1" role="dialog" aria-labelledby="sukses-setuju-modal" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">
                <div class="modal-body">
                    <div class="text-center">
                        <img src="../../assets/images/icon_ceklis.png" alt="icon-sukses">
                    <h2 style="margin:20px 0px 15px 0px">Sukses</h2>
                    <p style="margin:0px 0px -15px 0px">{{pesan_body}}</p>
                    </div>
                </div>
                <div class="modal-footer">
                    <div class="text-center">
                        <router-link :to="{path:this.path_selanjutnya, name:this.nama_path,params:this.params_path}" ><button  @click="onCloseModal('#notification-success')" id="button-modal" type="button" class="text-center btn btn-success">{{this.pesan_button}}</button></router-link>
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
                    <p style="margin:0px 0px -15px 0px">{{error_message}}</p>
                    </div>
                </div>
                <div class="modal-footer">
                    <div class="text-center">
                        <button type="button" @click="onCloseModal" class="btn btn-success" data-dismiss="modal" style="width:80px; height:36px;">OK</button>
                    </div>
                </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import Perulangan from '../../models/perulangan';
import PeminjamanRuangan from '../../models/peminjaman_ruangan';
import IzinMahasiswaService from '../../services/izinMahasiswa.service';
import $ from 'jquery';

export default {
    name: 'PeminjamanRuanganMahasiswa',
    data() {
        return {
            list_ruangan: [],
            terbuka_untuk_umum: false,
            option_waktu : [],
            number_of_peminjaman : 1,
            list_perulangan : [new Perulangan(null, "", "")],
            list_peminjaman_ruangan : [new PeminjamanRuangan("", "", "", "", "", "", false),],
            id_izin_kegiatan: '',
            kebutuhan: [],
            pesan_button: '',
            path_selanjutnya:'',
            nama_path:'',
            params_path : null,
            error_message: '',
            pesan_body:'',
        } 
    },
    created(){
        
        this.id_izin_kegiatan =  this.$route.params.id_izin_kegiatan
        this.kebutuhan = this.$route.params.kebutuhan
        console.log('the response ' + this.$route.params.id_izin_kegiatan)
        console.log('kebutuhan '+ this.$route.params.kebutuhan)
        IzinMahasiswaService.getRuangan().then(
            response =>{
                this.list_ruangan = response.data
            },
            error => {
                this.error_call_api = (error.response && error.response.data) || error.message || error.toString();
            }
        )
    },
    computed: {
        getUserId(){
            return this.$store.state.auth.user.id_user;
        },
    },
    methods: {
        addRow(){
            this.list_perulangan.push(new Perulangan(null, "", ""));
            this.list_peminjaman_ruangan.push(new PeminjamanRuangan("", "", "", "", "", "",false));
            this.number_of_peminjaman++
        },
        deleteRow(index){
            this.number_of_peminjaman--;
            this.list_perulangan.splice(index, 1);
            this.list_peminjaman_ruangan.splice(index, 1);
            
        },
        onCloseModal(id){
            $(id).modal('hide')
        },
        batalPeminjaman(){
            this.pesan_body = "Anda telah membatalkan pengajuan peminjaman ruangan" 
             if(this.kebutuhan.length >1){
                        this.pesan_button = "Ke halaman perizinan humas"
                        this.path_selanjutnya = '/buat-perizinan/form-humas'
                        this.nama_path = 'Form Permohonan Humas Mahasiswa'
                        this.params_path = {id_izin_kegiatan:this.id_izin_kegiatan, kebutuhan: this.kebutuhan}
            }else{
                        this.pesan_button = "OK"
                        this.path_selanjutnya = '/'
            }
             $('#notification-success').modal('show')
        },
        submitPost(){
            // console.log(this.izin_kegiatan)
            console.log(this.list_peminjaman_ruangan)
            console.log(this.list_perulangan)
            let i;
            for (i = 0; i < this.number_of_peminjaman; i++){
                this.list_peminjaman_ruangan[i].setPerulangan(this.list_perulangan[i])
            }
            const data ={
                id : this.id_izin_kegiatan,
                peminjaman_ruangan : this.list_peminjaman_ruangan
            }
            // this.izin_kegiatan.setPeminjamanRuangan(this.list_peminjaman_ruangan)
            // this.izin_kegiatan.setUser(1)
            console.log(data)
            IzinMahasiswaService.postPeminjamanRuanganMahasiswa(this.id_izin_kegiatan,data).then(
                response => {
                    console.log(response.data);
                    if(this.kebutuhan.length>0){
                        this.pesan_button = "Ke halaman perizinan humas"
                        this.path_selanjutnya = '/buat-perizinan/form-humas'
                        this.nama_path = 'Form Permohonan Humas Mahasiswa'
                        this.params_path = {id_izin_kegiatan:this.id_izin_kegiatan, kebutuhan: this.kebutuhan}
                        this.pesan_body = "Peminjaman ruangan berhasil"
                    }else{
                        this.pesan_button = "OK"
                        this.path_selanjutnya = '/'
                        this.pesan_body = "Peminjaman ruangan berhasil"
                    }
                     $('#notification-success').modal('show')
                },
                error => {
                    console.log(error.message);
                    this.error_message = error.message
                    $('#notification-failed').modal('show')
                }
            )
        }
    },
    mounted(){
        //create daftar waktu
        let option_waktu_made = [];
        let i;
        for (i = 0; i < 24; i++){
            if (i < 10 ){
                option_waktu_made.push({
                    value: "2021-01-01T0" + i + ":00",
                    text: "0" + i + ":00"
                });
                option_waktu_made.push({
                    value: "2021-01-01T0" + i + ":30",
                    text: "0" + i + ":30"
                });
            } else {
                option_waktu_made.push({
                    value: "2021-01-01T" + i + ":00",
                    text:  i + ":00"
                });
                option_waktu_made.push({
                    value: "2021-01-01T" + i + ":30",
                    text: i + ":30"
                });
            }
        }
        this.option_waktu = option_waktu_made;
        // ngasih boolean flag buat nandain lagi active di halaman ini
        this.$emit('inPeminjamanRuanganUnitKerjaPage', true);
  
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
.line-title{
    margin-right: -20px !important;
    margin-left: -20px !important;
}
::placeholder {
    color:  #bdbdbd!important;
}
label {
    font-size: 14px;
    color: #828282;
    margin: 10px 0px -5px 0px;
}
label.form-check-label{
    margin: 0px 0px 0px 0px !important; 
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
.note-form{
    font-size: 12px;
}
.note-ruangan{
    margin-bottom: -16px;
}
.tambah-ruangan {
    width: 400px;
}
#button-hapus{
    width: 80px;
    height: 35px;
    font-size: 15px;
}
.btn-simpan {
    width: 107px;
}
.asterisk {
    color: red;
}
#button-batal{
    display:inline-block;
    height: 30px;
    font-size: 13px;
    padding: 3px 3px 3px 3px;
    margin:5px 5px 2px;
}
#button-modal{
    display:inline-block;
    text-align: center;
}
@media (max-width: 768px) {
    .tambah-ruangan {
        width: 200px;
    }
}
</style>