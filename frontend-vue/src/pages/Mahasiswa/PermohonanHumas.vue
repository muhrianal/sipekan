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
                        <label for="inputPublikasiLuarRuangan">Publikasi Luar Ruangan</label>
                        <hr noshade >
                        <span v-for="publikasi in publikasi_luar_ruangan" v-bind:key="publikasi.id">
                            <input id="input_publikasi" v-model="jenis_publikasi" type="checkbox" :value="publikasi"> <span class="checkbox-label">{{publikasi.deskripsi_publikasi}}</span><br>
                        </span>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputPublikasi">Publikasi</label>
                         <hr noshade >
                         <span v-for="publikasi in publikasi" v-bind:key="publikasi.id">
                            <input id="input_publikasi" v-model="jenis_publikasi" type="checkbox" :value="publikasi"> <span class="checkbox-label">{{publikasi.deskripsi_publikasi}}</span><br>
                        </span>
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputTanggalMulai">Tanggal Mulai:<span class="text-danger">*</span><span class="text-keterangan">  (wajib disi jika mengajukan permintaan publikasi)</span></label>
                        <input id="input_tanggal_mulai" v-model="tanggal_mulai" type="date" class="form-control" >                   
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2 ">
                        <label for="inputTanggalAkhir">Tanggal Akhir:<span class="text-danger">*</span><span class="text-keterangan">  (wajib disi jika mengajukan permintaan publikasi)</span></label>
                        <input id="input_tanggal_akhir" v-model="tanggal_akhir" type="date" class="form-control" >
                    </div>                        
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputMateriKegiatan">Materi Kegiatan / Press Release:<span class="text-keterangan">  (Dapat diunggah dalam format zip)</span> </label>
                        <input id= "file_materi" type="file" ref="fileMateri" @change="onFileMateriChange" class="form-control-file">
                        <p v-if="this.file_materi_kegiatan !=null" class="text-right note-form" @Click="deleteFileMateri()">Hapus File</p>
                    </div>   
                      <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputFlyerPengumuman">Flyer Pengumuman / Poster Kegiatan:<span class="text-keterangan">  (jika ada)</span></label>
                        <input id= "file_flyer" type="file" ref="fileFlyer" @change="onFileFlyerChange" class="form-control-file">
                        <p v-if="this.file_flyer_pengumuman !=null" class="text-right note-form" @Click="deleteFileFlyer()">Hapus File</p>
                    </div>                       
                </div>

                 <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">            
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputKeterangan">Keterangan: <span class="text-keterangan">  (jika memilih jenis Lainnya, silahkan isi spesifikasi publikasi disini)</span></label>
                        <textarea id="input_keterangan" type="text" v-model="keterangan" class="form-control" placeholder="e.g. Baliho di Depan Gedung x ukuran (axb)"></textarea>
                    </div>                    
                </div>
                 <div class="text-right">
                        <button type="button" class="btn btn-outline-danger" id="button-reset" @click="resetPublikasi" >Reset Formulir Publikasi</button>
                </div>
               
               <div class="col-12 px-4"> 
                    <label> Souvenir<span class="text-keterangan"> (semua field wajib diisi jika mengajukan permintaan souvenir)</span></label>    
                    <hr >  
                </div>  
                <template v-for="peminjaman in number_of_permintaan_souvenir" v-bind:key="peminjaman">
                    <hr v-if="peminjaman>1" >
                    <div class="text-right">
                        <button type="button" class="btn btn-outline-danger" id="button-hapus" @click="deleteRow(peminjaman - 1)" v-if="peminjaman > 1">Hapus</button>
                    </div>
                    <div class="form-row">
                        <div class="col-12 col-md-6  px-4 py-2">
                            <label for="inputNamaPenerima">Nama Penerima:<span class="text-danger">*</span></label>
                            <input pattern="[A-Za-z]" id="input_nama_penerima" type="text" v-model="list_permintaan_souvenir[peminjaman-1].nama_penerima_souvenir" class="form-control" placeholder="e.g. Akhmad">
                        </div>
                        <div class="col-12 col-md-6  px-4 py-2">
                            <label for="inputJabatanPenerima">Jabatan Penerima:<span class="text-danger">*</span></label>
                            <input id="input_jabatan_penerima" type="text" v-model="list_permintaan_souvenir[peminjaman-1].jabatan_penerima_souvenir" class="form-control" placeholder="e.g. Menteri" >
                        </div>                    
                    </div>

                    <div class="form-row">
                        <div class="col-12 col-md-6  px-4 py-2">
                            <label for="inputKelas">Kelas:<span class="text-danger">*</span></label>
                            <select id="input_kelas" @change="onKelasChange(peminjaman-1)" v-model="list_permintaan_souvenir[peminjaman-1].kelas_penerima_souvenir" class="form-control">
                                <option disabled selected value="">Pilih...</option>
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                            </select> 
                            <p class="text-right note-form" @Click="onModalKelas()">Lihat Klasifikasi Kelas</p>

                        </div>
                        <div class="col-12 col-md-6  px-4 py-2">
                            <label for="inputRegion">Region:<span class="text-danger">*</span></label>
                            <select id="input_region" @change="onRegionChange(peminjaman-1)" v-model="list_permintaan_souvenir[peminjaman-1].region_penerima_souvenir" class="form-control" >
                                <option disabled selected value="">Pilih...</option>
                                <option value="1">Dalam Negeri</option>
                                <option value="2">Luar Negeri</option>
                            </select>
                        </div>                    
                    </div>

                    <div class="form-row">
                        <div class="col-12 col-md-6  px-4 py-2">
                            <label for="inputPilihanSouvenir">Pilihan Souvenir:<span class="text-danger">*</span></label>
                            <select id="input_souvenir" v-model="list_permintaan_souvenir[peminjaman-1].souvenir" class="form-control">        
                                <option selected disabled value="">Pilih...</option>
                                    <option v-for="pilihan_souvenir in list_souvenir_data_filtered[peminjaman-1]" v-bind:key="pilihan_souvenir.id" :value="pilihan_souvenir.id">{{pilihan_souvenir.nama_souvenir}}</option>
                            </select>
                        </div>
                        <div class="col-12 col-md-6  px-4 py-2">
                            <label for="inputJumlah">Jumlah:<span class="text-danger">*</span></label>
                            <input id="input_jumlah"  v-model="list_permintaan_souvenir[peminjaman-1].jumlah" type="number" min="1" class="form-control" placeholder="e.g. 1">
                        </div>                    
                    </div>
                    <div class="text-right">
                            <button v-if="this.number_of_permintaan_souvenir < 2" type="button" class="btn btn-outline-danger" id="button-reset" @click="resetSouvenir(peminjaman-1)" >Reset Formulir Souvenir</button>
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
                        <textarea id="input_deskripsi_kebutuhan" v-model="deskripsi_kebutuhan" type="text" class="form-control" placeholder="e.g. Menteri x, jumlah pendamping yang dibutuhkan: 2"></textarea>         
                    </div>                    
                </div>
                <div class="text-right">
                        <button type="button" class="btn btn-outline-danger" id="button-reset" @click="resetProtokoler" >Reset Formulir Protokoler</button>
                </div>
            </form>
            <div class="d-flex" style="margin-top:10px">
            <div class="mr-auto"> </div>
             <div class="text-right">
                <button  type="button" class="btn btn-outline-danger rounded" @Click="batalPermohonan" id="button-batal"> Batal Mengajukan Permohonan</button>
                <button @click="postPermohonanHumas" class="btn btn-success btn-simpan">Simpan</button>
            </div>
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
                    <p style="margin:0px 0px -15px 0px">{{pesan_body}}</p>
                    </div>
                </div>
                <div class="modal-footer">
                    <div class="text-center">                
                                <button  @click="refreshPage" id="button-modal" type="button" class="text-center btn btn-success">
                                    OK
                                </button>
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
                        <button type="button" @click="onCloseModal('#notification-failed')" class="btn btn-success" data-dismiss="modal" style="width:80px; height:36px;">OK</button>
                    </div>
                </div>
                </div>
            </div>
        </div>
        <!-- Modal: Spesifikasi Kelas -->
        <div class="modal fade" id="spesifikasi-kelas" tabindex="-1" role="dialog" aria-labelledby="gagal-submit-modal" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">  
                <div class="modal-header"><h5 class="text-center">Klasifikasi Kelas</h5></div>                    
                <div class="modal-body">
                   
                    <table class="table table-bordered">
                         <thead>
                            <tr>
                                <th scope="col" class="text-center">Kelas</th>
                                <th scope="col" class="text-center">Penerima Souvenir</th>          
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="text-center">I</td>
                                <td>Presiden/ Menteri/ Rektor/ Dekan/ Sederajat</td>
                            </tr>
                            <tr>
                                <td class="text-center">II</td>
                                <td>Pembicara Kuliah Tamu/ Seminar/ Profesional/ CEO/ Partner dari luar</td>
                            </tr>
                            <tr>
                                <td class="text-center">III</td>
                                <td>Penerima bersifat masal (contoh: keperluan seminar, kunjungan mahasiswa)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="modal-footer">
                    <div class="text-center">
                        <button type="button" @click="onCloseModal('#spesifikasi-kelas')" class="btn btn-secondary" data-dismiss="modal" style="width:80px; height:36px;">Close</button>
                    </div>
                </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import IzinMahasiswaService from '../../services/izinMahasiswa.service';
import PermintaanSouvenir from '../../models/permintaan_souvenir';
import izinMahasiswaService from '../../services/izinMahasiswa.service';
// import Souvenir from '../../models/souvenir';
import $ from 'jquery';

export default {
    name: 'PermohonanHumas',
    data(){
        return{
            jenis_publikasi_data : [],
            souvenir_data : [],
            pesan_body: "Pengajuan humas berhasil",
            // souvenir_data_filtered : [],
            list_souvenir_data_filtered : [],           
            error_message: '',
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
            file_materi_kegiatan: null,
            file_flyer_pengumuman: null,
            // permintaan souvenir
            list_permintaan_souvenir : [new PermintaanSouvenir('','','','','','',null),],
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
                this.list_souvenir_data_filtered[0] = this.souvenir_data;
            },
            error => {
                this.error_call_api = (error.response && error.response.data) || error.message || error.toString();
            }
        )
    },
    methods:{
        addRow(){
            // this.list_souvenir.push(new Souvenir(null,"",null,null,null))
            this.list_permintaan_souvenir.push(new PermintaanSouvenir('','','','','','',null));
            this.number_of_permintaan_souvenir++;
            console.log(this.number_of_permintaan_souvenir);

        },
        deleteRow(index){
            this.number_of_permintaan_souvenir--;
            this.list_permintaan_souvenir.splice(index,1);
        },
         batalPermohonan(){
            this.pesan_body = "Anda telah membatalkan pengajuan permohonan humas" 
             $('#notification-success').modal('show')
        },
        cekPublikasi(){
            let terisi_penuh = true
            if(this.jenis.publikasi.length != 0 && (this.tanggal_mulai.length == 0 || this.tanggal_akhir  == 0)){
                terisi_penuh = false
            }
            return terisi_penuh
        },
        onFileMateriChange(){
            this.file_materi_kegiatan = this.$refs.fileMateri.files[0];
        },
        onFileFlyerChange(){
            this.file_flyer_pengumuman = this.$refs.fileFlyer.files[0];
        },
        refreshPage(){
            location.reload()
        },
        onModalKelas(){
            $('#spesifikasi-kelas').modal('show')
        },
        onKelasChange(index){
            let kelas_souvenir_diminta = this.list_permintaan_souvenir[index].kelas_penerima_souvenir
            let region_souvenir_diminta = this.list_permintaan_souvenir[index].region_penerima_souvenir
            let souvenir_data_filtered = []
                this.souvenir_data.forEach(function(souvenir){
                    if(kelas_souvenir_diminta == 1){            
                        if(souvenir.kelas == 1 || souvenir.kelas == 4 || souvenir.kelas == 5 || souvenir.kelas == 7){             
                            if(region_souvenir_diminta != '' && ((souvenir.region == region_souvenir_diminta || souvenir.region == 3))){
                                souvenir_data_filtered.push(souvenir)
                            }
                            else if (region_souvenir_diminta==''){
                                souvenir_data_filtered.push(souvenir)
                            }
                        }
                    }else if(kelas_souvenir_diminta == 2){
                        console.log("kelas diminta " + kelas_souvenir_diminta)
                        if(souvenir.kelas == 2 || souvenir.kelas == 4 || souvenir.kelas == 6 || souvenir.kelas == 7){
                            console.log("reg diminta " + region_souvenir_diminta)
                            if(region_souvenir_diminta != '' && ((souvenir.region == region_souvenir_diminta || souvenir.region == 3))){                              
                                souvenir_data_filtered.push(souvenir)
                            }
                            else if(region_souvenir_diminta==''){
                               souvenir_data_filtered.push(souvenir)
                            }
                        }
                    }else if(kelas_souvenir_diminta == 3){
                        if(souvenir.kelas == 3 || souvenir.kelas == 5 || souvenir.kelas == 6 || souvenir.kelas == 7){
                            if(region_souvenir_diminta != '' && ((souvenir.region == region_souvenir_diminta || souvenir.region == 3))){
                                souvenir_data_filtered.push(souvenir)
                            }
                            else if (region_souvenir_diminta==''){
                                souvenir_data_filtered.push(souvenir)
                            }
                        }
                    }
                })
                this.list_souvenir_data_filtered[index] = souvenir_data_filtered
                console.log(this.souvenir_data_filtered)
        },
        onRegionChange(index){
            if(this.list_permintaan_souvenir[index].kelas_penerima_souvenir != ''){
                this.onKelasChange(index)
            }else{
                let region_souvenir_diminta = this.list_permintaan_souvenir[index].region_penerima_souvenir
                let souvenir_data_filtered = []
                this.souvenir_data.forEach(function(souvenir){
                    if(souvenir.region == region_souvenir_diminta || souvenir.region == 3){
                        souvenir_data_filtered.push(souvenir)
                    }
                })
                this.list_souvenir_data_filtered[index] = souvenir_data_filtered
            }
            
        },
        onCloseModal(id){
            $(id).modal('hide')
        },
        alertFuntion(message){
            alert(message)
        },
        deleteFileMateri(){            
            document.getElementById("file_materi").value  = null; 
            this.file_materi_kegiatan = null
        },
      
        deleteFileFlyer(){
            document.getElementById("file_flyer").value  = null; 
            this.file_flyer_pengumuman = null
        },
        resetPublikasi(){
            document.getElementById("input_publikasi").checked = false;
            document.getElementById("input_tanggal_mulai").value  = ''; 
            document.getElementById("input_tanggal_akhir").value  = ''; 
            document.getElementById("input_keterangan").value  = ''; 
            document.getElementById("file_flyer").value  = null; 
            document.getElementById("file_materi").value  = null;
            this.tanggal_akhir = '';
            this.tanggal_mulai = '';
            this.keterangan = '';
            this.file_flyer_pengumuman = null;
            this.file_materi_kegiatan = null;
            this.jenis_publikasi = []
        },
        resetSouvenir(index){
            document.getElementById("input_nama_penerima").value = '';
            document.getElementById("input_jabatan_penerima").value = '';
            document.getElementById("input_kelas").selectedIndex = '';
            document.getElementById("input_region").selectedIndex = '';
            document.getElementById("input_souvenir").value = null;
            document.getElementById("input_jumlah").value = '';
            this.list_permintaan_souvenir[index].nama_penerima_souvenir = '';
            this.list_permintaan_souvenir[index].jabatan_penerima_souvenir = '';
            this.list_permintaan_souvenir[index].kelas_penerima_souvenir = '';
            this.list_permintaan_souvenir[index].region_penerima_souvenir = '';
            this.list_permintaan_souvenir[index].souvenir = null;
            this.list_permintaan_souvenir[index].jumlah = '';
            this.souvenir_data_filtered = this.souvenir_data;
        },
        resetProtokoler(){
            document.getElementById("input_deskripsi_kebutuhan").value = '';
            this.deskripsi_kebutuhan = '';
        },
        checkEmpty(){
            let passed = true
            const id_input = ["input_tanggal_mulai","input_tanggal_akhir", "input_keterangan","input_nama_penerima","input_jabatan_penerima","input_jumlah", "file_flyer","file_materi","input_souvenir","input_kelas","input_region"]
            // const id_dropdown = ["input_kelas","input_region"]
            // const id_input_null = []
            for(var id in id_input){
                if(document.getElementById(id).value == '' || document.getElementById(id).value == null || 
                 document.getElementById(id).checked == false || document.getElementById(id).selectedIndex == ''){
                    passed= false 
                }else{
                    passed = true
                }
            }
            if(!passed){
                this.alertFuntion("Anda belum mengisi Form Permohonan Humas")
            }
            return passed
        },
        checkFields(){
            let passed = true
            if(this.jenis_publikasi.length != 0 && (this.tanggal_mulai == '' || this.tanggal_akhir == '')){
                this.alertFuntion("Harap mengisi seluruh field yang wajib, jika Anda ingin mengajukan perizinan publikasi")
                passed = false
            }
            if(this.jenis_publikasi.some(el => el.deskripsi_publikasi === "Lainnya") & this.keterangan == ''){
                this.alertFuntion("Anda memilih jenis publikasi 'Lainnya', harap mengisi spesifikasi di keterangan")
                passed = false
            }
            for(var i=0; i < this.number_of_permintaan_souvenir; i++ ){
                console.log(i)
                let nama = this.list_permintaan_souvenir[i].nama_penerima_souvenir
                let jabatan = this.list_permintaan_souvenir[i].jabatan_penerima_souvenir
                let kelas = this.list_permintaan_souvenir[i].kelas_penerima_souvenir
                let region = this.list_permintaan_souvenir[i].region_penerima_souvenir
                let souvenir = this.list_permintaan_souvenir[i].souvenir
                let jumlah = this.list_permintaan_souvenir[i].jumlah
                if(
                    ( nama!='' && (jabatan=='' || kelas =='' || region == '' || souvenir == null || jumlah == '' ) ) ||                    
                    ( jabatan != '' && (nama=='' || kelas =='' || region == '' || souvenir == null || jumlah == '') ) ||
                    ( kelas !='' && (nama=='' || jabatan =='' || region == '' || souvenir == null || jumlah == '') ) ||
                    ( region !='' && (nama=='' || jabatan =='' || kelas == '' || souvenir == null || jumlah == '') ) ||
                    ( souvenir !=null && (nama=='' || jabatan =='' || kelas == '' || region == '' || jumlah == '')) ||
                    ( jumlah !='' && (nama=='' || jabatan =='' || kelas == '' || region == '' || souvenir == null))              
                    ) {                           
                        this.alertFuntion("Harap mengsi serluruh field yang wajib, jika Anda ingin mengajukan permintaan souvenir")
                        passed = false
                }
            }
            return passed;
        },
        postPermohonanHumas(){
            const data = {
                id : this.id_izin_kegiatan
            }
            if(this.checkFields()){
                if(this.jenis_publikasi.length != 0){
                    console.log(this.jenis_publikasi)
                    let formDataPublikasi = new FormData()
                    formDataPublikasi.append("izin_kegiatan", this.id_izin_kegiatan)
                    formDataPublikasi.append("tanggal_mulai", this.tanggal_mulai)
                    formDataPublikasi.append("tanggal_akhir", this.tanggal_akhir)
                    formDataPublikasi.append("status_perizinan_publikasi", 1) //menunggu persetujuan
                    formDataPublikasi.append("alasan_penolakan", this.alasan_penolakan_publikasi)
                    formDataPublikasi.append("keterangan", this.keterangan)
                    formDataPublikasi.append("jenis_publikasi", this.jenis_publikasi)    
                    if(this.file_materi_kegiatan != null){
                        formDataPublikasi.append("file_materi_kegiatan",this.file_materi_kegiatan)
                    }
                    if(this.file_flyer_pengumuman != null){
                        formDataPublikasi.append("file_flyer_pengumuman", this.file_flyer_pengumuman)
                    }
                    izinMahasiswaService.postPerizinanPublikasi(formDataPublikasi).then( 
                        response => {
                            console.log(response.data);
                            $('#notification-success').modal('show')
                        },
                        error => {
                            console.log(error.message);
                            this.error_message = error.message
                            $('#notification-failed').modal('show')
                        }                     
                    )
                }
                let ada_souvenir_protokoler = false
                if(this.list_permintaan_souvenir[0].nama_penerima_souvenir.length !=0){                    
                    // for (let i = 0; i < this.number_of_permintaan_souvenir; i++){
                    //     this.list_permintaan_souvenir[i].setSouvenir(this.list_souvenir[i])
                    // }   
                    ada_souvenir_protokoler = true
                   data["permintaan_souvenir"] = this.list_permintaan_souvenir
                }
                if(this.deskripsi_kebutuhan.length != 0){
                    const permintaan_protokoler_data = {
                        deskripsi_kebutuhan : this.deskripsi_kebutuhan,
                        status_permintaan_protokoler : this.status_permintaan_protokoler,
                        alasan_penolakan : this.alasan_penolakan_protokoler
                    }
                    ada_souvenir_protokoler = true
                    data["permintaan_protokoler"] = permintaan_protokoler_data        
                }
                if(ada_souvenir_protokoler){
                    IzinMahasiswaService.postPermohonanHumas(this.id_izin_kegiatan,data).then(
                    response => {
                        console.log(response.data);
                        $('#notification-success').modal('show')
                    },
                    error => {
                        console.log(error.message);
                        this.error_message = error.message
                        $('#notification-failed').modal('show')
                    }
                    )
                }    
             
            }
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
.checkbox-label{
    font-size: 14px;
}
.tambah-souvenir {
    width: 400px;
}
#button-reset{
    width: 160px;
    height: 30px;
    font-size: 13px;
    padding: 3px 3px 3px 3px;
    margin-top:2px;
}
.note-form{
    font-size: 12px;
    color: black;
    margin-bottom:0px;
}
.note-form:hover {
    text-decoration: underline;
}
#button-modal{
    display:inline-block;
    text-align: center;
}
#button-batal{
    display:inline-block;
    height: 30px;
    font-size: 13px;
    padding: 3px 3px 3px 3px;
    margin:5px 5px 2px;
}
@media (max-width: 768px) {
    .tambah-souvenir {
        width: 200px;
    }
}
</style>