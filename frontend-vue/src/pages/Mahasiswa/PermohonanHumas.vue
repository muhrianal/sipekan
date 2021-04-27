<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page">Buat Perizinan<span style="color:grey"> >> Humas</span></h3>
            <hr class="line-header line-title">
        </div>
        
        <div class="formulir">
            <form>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputPublikasiLuarRuangan">Publkasi Luar Ruangan</label>
                        <hr noshade >
                        <span v-for="publikasi in publikasi_luar_ruangan" v-bind:key="publikasi.id">
                            <input v-model="jenis_publikasi" type="checkbox" :value="publikasi"> <span class="checkbox-label">{{publikasi.deskripsi_publikasi}}</span><br>
                        </span>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputPublikasi">Publikasi</label>
                         <hr noshade >
                         <span v-for="publikasi in publikasi" v-bind:key="publikasi.id">
                            <input v-model="jenis_publikasi" type="checkbox" :value="publikasi"> <span class="checkbox-label">{{publikasi.deskripsi_publikasi}}</span><br>
                        </span>
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputTanggalMulai">Tanggal Mulai:</label>
                        <input v-model="tanggal_mulai" type="date" class="form-control" >                   
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2 ">
                        <label for="inputTanggalAkhir">Tanggal Akhir:</label>
                        <input v-model="tanggal_akhir" type="date" class="form-control" >
                    </div>                        
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputMateriKegiatan">Materi Kegiatan / Press Release:<span class="text-keterangan">  (Dapat diunggah dalam format zip)</span> </label>
                        <input type="file" class="form-control-file">
                    </div>   
                      <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputFlyerPengumuman">Flyer Pengumuman / Poster Kegiatan:<span class="text-keterangan">  (jika ada)</span></label>
                        <input type="file" class="form-control-file">
                    </div>                       
                </div>

                 <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">            
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputKeterangan">Keterangan: <span class="text-keterangan">  (jika memilih jenis Lainnya, silahkan isi spesifikasi publikasi disini)</span></label>
                        <textarea type="text" v-model="keterangan" class="form-control" placeholder="e.g. Baliho di Depan Gedung x ukuran (axb)"></textarea>
                    </div>                    
                </div>
                
                <div class="col-12col-md-6 px-4"> 
                    <label> Souvenir</label>                 
                </div>  

                <template v-for="peminjaman in number_of_permintaan_souvenir" v-bind:key="peminjaman">
                <!-- <hr class="line-header"> -->
                <hr>
                <div class="text-right">
                    <button type="button" class="btn btn-outline-danger" id="button-hapus" @click="deleteRow(peminjaman - 1)" v-if="peminjaman > 1">Hapus</button>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputNamaPenerima">Nama Penerima:</label>
                        <input type="text" v-model="list_permintaan_souvenir[peminjaman-1].nama_penerima_souvenir" class="form-control" placeholder="e.g. Akhmad">
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputJabatanPenerima">Jabatan Penerima:</label>
                        <input type="text" v-model="list_permintaan_souvenir[peminjaman-1].jabatan_penerima_souvenir" class="form-control" placeholder="e.g. Menteri" >
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputKelas">Kelas:</label>
                        <select v-model="list_permintaan_souvenir[peminjaman-1].kelas_penerima_souvenir" class="form-control" id="exampleFormControlSelect1">
                            <option selected disabled value="">Pilih...</option>
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                        </select>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputRegion">Region:</label>
                          <select v-model="list_permintaan_souvenir[peminjaman-1].region_penerima_souvenir" class="form-control" id="exampleFormControlSelect1">
                            <option selected disabled value="">Pilih...</option>
                            <option value="1">Dalam Negeri</option>
                            <option value="2">Luar Negeri</option>
                        </select>
                    </div>                    
                </div>

                 <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputPilihanSouvenir">Pilihan Souvenir:</label>
                       <!-- <select v-model="list_souvenir[peminjaman-1]" class="form-control" id="exampleFormControlSelect1"> -->
                        <select v-model="list_permintaan_souvenir[peminjaman-1].souvenir" class="form-control" id="exampleFormControlSelect1">        
                            <option v-for="pilihan_souvenir in souvenir_data" v-bind:key="pilihan_souvenir.id" :value="pilihan_souvenir.id">{{pilihan_souvenir.nama_souvenir}}</option>
                            <!-- <option selected disabled value="">Pilih...</option> -->
                        </select>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputJumlah">Jumlah:</label>
                        <input v-model="list_permintaan_souvenir[peminjaman-1].jumlah" type="number" class="form-control" placeholder="e.g. 1">
                    </div>                    
                </div>
                 </template>

                <div class="row-12 row-md-6  px-4 py-2"> 
                    <hr>
                     <div class="text-center">
                        <button @click="addRow" type="button" class="btn tambah-souvenir btn-outline-secondary">Tambah Souvenir</button>
                    </div> 
                </div>  

                <div class="col-12col-md-6 px-4"> 
                    <label> Protokoler</label>
                     <hr>
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">   
                        <label for="inputDeskripsiKebutuhan">Deskripsi Kebutuhan: <span class="text-keterangan" id="text-keterangan-small">  (contoh: nama penerima, jumlah pendamping dibutuhkan)</span></label>
                        <textarea v-model="deskripsi_kebutuhan" type="text" class="form-control" placeholder="e.g. Menteri x, jumlah pendamping yang dibutuhkan: 2"></textarea>         
                    </div>                    
                </div>
            </form>
            <div class="d-flex" style="margin-top:10px">
            <div class="mr-auto"> </div>
            <!-- <div class="p-2">
                    <button type="button" class="btn btn-outline-danger" id="button-batal">Batal</button>
            </div>
            <div class="p-2 pr-4">
                    <button @click="postPermohonanHumas" type="button" class="btn btn-success" id="button-setuju">Simpan</button>
            </div> -->
             <div class="text-right">
                <button @click="postPermohonanHumas" class="btn btn-success btn-simpan">Simpan</button>
            </div>
        </div>
        </div>
    </div>
</template>

<script>
import IzinMahasiswaService from '../../services/izinMahasiswa.service';
import PermintaanSouvenir from '../../models/permintaan_souvenir';
// import Souvenir from '../../models/souvenir';

export default {
    name: 'PermohonanHumas',
    data(){
        return{
            jenis_publikasi_data : [],
            souvenir_data : [],
            //izin_kegiatan dan kebutuhan
            id_izin_kegiatan: '',
            kebutuhan: [],
            // perizinan publikasi
            tanggal_mulai: '',
            tanggal_akhir: '',
            status_perizinan_publikasi: 1,
            alasan_penolakan_publikasi: '',
            keterangan: '',
            jenis_publikasi: [],
            // permintaan souvenir
            list_permintaan_souvenir : [new PermintaanSouvenir("","","","","","",null),],
            // list_souvenir : [new Souvenir (null,"",null,null,null),],
            number_of_permintaan_souvenir: 1,
            // permintaan protokoler
            deskripsi_kebutuhan: '',
            status_permintaan_protokoler:1,
            alasan_penolakan_protokoler: ''
        }
    },
    computed: {
        publikasi_luar_ruangan: function(){
            return this.jenis_publikasi_data.filter(function(u){
                return u.luar_ruangan
            })
        },
        publikasi: function(){
            return this.jenis_publikasi_data.filter(function(u){
                return !u.luar_ruangan
            })
        },
        
    },
    created(){
        this.id_izin_kegiatan =  this.$route.params.id_izin_kegiatan
        this.kebutuhan = this.$route.params.kebutuhan
        console.log(this.id_izin_kegiatan)
        console.log(this.kebutuhan)
        // this.id_izin_kegiatan=7
        // this.kebutuhan = ["ruangan","humas"]
        IzinMahasiswaService.getJenisPublikasi().then(
            response =>{
                this.jenis_publikasi_data = response.data;
            },
            error => {
                this.error_call_api = (error.response && error.response.data) || error.message || error.toString();
            }
        )
        IzinMahasiswaService.getListSouvenir().then(
            response => {
                this.souvenir_data = response.data;
            },
            error => {
                this.error_call_api = (error.response && error.response.data) || error.message || error.toString();
            }
        )
    },
    methods:{
        addRow(){
            // this.list_souvenir.push(new Souvenir(null,"",null,null,null))
            this.list_permintaan_souvenir.push(new PermintaanSouvenir("","","","","","",null));
            this.number_of_permintaan_souvenir++;
            console.log(this.number_of_permintaan_souvenir);

        },
        deleteRow(index){
            this.number_of_permintaan_souvenir--;
            this.list_permintaan_souvenir.splice(index,1);
        },
        cekPublikasi(){
            let terisi_penuh = true
            if(this.jenis.publikasi.length != 0 && (this.tanggal_mulai.length == 0 || this.tanggal_akhir  == 0)){
                terisi_penuh = false
            }
            return terisi_penuh
        },
        postPermohonanHumas(){
            const data = {
                id : this.id_izin_kegiatan
            }
                if(this.jenis_publikasi.length != 0){
                    const perizinan_publikasi_data = {
                        tanggal_mulai: this.tanggal_mulai,
                        tanggal_akhir: this.tanggal_akhir,
                        status_perizinan_publikasi: 1,
                        alasan_penolakan: this.alasan_penolakan_publikasi,
                        keterangan: this.keterangan,
                        jenis_publikasi: this.jenis_publikasi
                    }
                    data["perizinan_publikasi"] = perizinan_publikasi_data
                }
                if(this.list_permintaan_souvenir[0].nama_penerima_souvenir.length !=0){                    
                    // for (let i = 0; i < this.number_of_permintaan_souvenir; i++){
                    //     this.list_permintaan_souvenir[i].setSouvenir(this.list_souvenir[i])
                    // }   
                   data["permintaan_souvenir"] = this.list_permintaan_souvenir
                }
                if(this.deskripsi_kebutuhan.length != 0){
                    const permintaan_protokoler_data = {
                        deskripsi_kebutuhan : this.deskripsi_kebutuhan,
                        status_permintaan_protokoler : this.status_permintaan_protokoler,
                        alasan_penolakan : this.alasan_penolakan_protokoler
                    }
                    data["permintaan_protokoler"] = permintaan_protokoler_data
             
                }
                console.log(data)
            IzinMahasiswaService.postPermohonanHumas(this.id_izin_kegiatan,data).then(
                response => {
                    console.log(response.data);
                },
                error => {
                    console.log(error.message);
                }
            )
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
input, textarea, select {
    border-radius: 10px !important;
}

.text-keterangan{
  font-size: x-small;
  color: gray
}
#text-keterangan-small{
    font-size: xx-small  !important;
}
hr{
    margin-top: 1px;
    margin-bottom: 3px;
}
/* .tambah-souvenir{
    margin-top: 4px;
    margin-bottom: 4px;
    font-size: 14px;
    border-radius: 10px !important;
    border-color: rgb(202, 202, 202);

} */
.checkbox-label{
    font-size: 14px;
}
.tambah-souvenir {
    width: 400px;
}
#button-hapus{
    width: 80px;
    height: 35px;
    font-size: 15px;
}
@media (max-width: 768px) {
    .tambah-souvenir {
        width: 200px;
    }
}
</style>