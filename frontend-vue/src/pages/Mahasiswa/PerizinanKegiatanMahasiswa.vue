<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page">Buat Perizinan<span style="color:grey"> >> Kegiatan</span></h3>
            <hr class="line-header line-title">
        </div>
        <div class="formulir">
            <div v-if="this.respon_kegiatan != null & this.kebutuhan.length>0">
                    <router-link  v-if="this.kebutuhan[0] == 'ruangan'" :to="{path: '/buat-perizinan/form-ruangan-mahasiswa/', name:'Form Peminjaman Ruangan Mahasiswa',params:{id_izin_kegiatan:this.respon_kegiatan.id, kebutuhan: this.kebutuhan}}" > <button class="btn btn-primary">RUANGAN</button> </router-link>
                    <router-link v-if="this.kebutuhan[0] == 'humas'" :to="{path: '/buat-perizinan/form-humas/', name:'Form Permohonan Humas Mahasiswa',params:{id_izin_kegiatan:this.respon_kegiatan.id, kebutuhan: this.kebutuhan}}" > <button class="btn btn-primary">HUMAS</button> </router-link>
            </div>
            <form v-on:submit.prevent="postIzinKegiatan">
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputNamaKegiatan">Nama Kegiatan<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. Open House FEB UI" required v-model="nama_kegiatan">
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputTempatPelaksanaan">Tempat Pelaksanaan<span class="text-danger">*</span>: <span class="text-keterangan">  (jika kegiatan online, isi: "Online")</span></label>
                        <input type="text" class="form-control" placeholder="e.g. FEB UI" required v-model="tempat_pelaksanaan">
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputTanggalMulai">Tanggal Mulai<span class="text-danger">*</span>:</label>
                        <input type=datetime-local class=form-control v-model="waktu_tanggal_mulai" required>
                    </div>

                    <div class="col-12 col-md-6  px-4 py-2 ">
                        <label for="inputTanggalAkhir">Tanggal Akhir<span class="text-danger">*</span>:</label>
                        <input type=datetime-local class=form-control v-model="waktu_tanggal_akhir" required>
                    </div>  
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputOrganisasi">Organisasi Penanggungjawab<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. BEM FEB UI" required v-model="organisasi">
                    </div>                         
                </div>

                 <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputKetuaOrganisasi">Nama Ketua Organisasi<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. Yobelio" required v-model="nama_ketua_organisasi">
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputNpmKetuaOrganisasi">NPM Ketua Organisasi<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. 1806123456" required v-model="npm_ketua_organisasi">
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputPicKegiatan">Nama PIC Kegiatan<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. Akhmad" required v-model="nama_pic"> 
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputNpmPic">NPM PIC<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. 1806123456" required v-model="npm_pic">
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputEmailPic">Email PIC<span class="text-danger">*</span>:</label>
                        <input type="email" class="form-control" placeholder="e.g. akhmad@ui.ac.id" required v-model="email_pic">
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputHpPic">HP PIC<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. 08151234567" required v-model="hp_pic">
                    </div>                    
                </div>

                 <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputSumberPendanaan">Sumber Pendanaan<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. Sponsor" required v-model="sumber_pendanaan">
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputUploadDokumen">Upload Dokumen<span class="text-danger">*</span>:<span class="text-keterangan">  (contoh: TOR-JGTC.pdf; Dokumen-JGTC.zip)</span></label>
                        <input type="file" ref="file" @change="onFileChange">
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputButuhHumas">Apakah anda memerlukan ruangan?</label>
                        <br><input v-model="kebutuhan" type="checkbox" value ="ruangan" id="humas"> <label>Ya</label>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputButuhRuangn">Apakah anda memerlukan humas? <span class="text-keterangan">  (Publikasi, Souvenir, Protokoler)</span> </label>
                        <br><input v-model="kebutuhan" type="checkbox" value ="humas" id="ruangan"> <label>Ya</label>
                    </div>                    
                </div>
                <div>
                    <div class="text-right">
                        <input class="btn btn-success btn-simpan" type=submit value="Simpan">
                    </div>
                </div>
            </form>
            <!-- <div class="text-right">
                <button href="/" @click="postIzinKegiatan" class="btn btn-success btn-simpan">Submit</button>
            </div> -->
            <div class="d-flex" style="margin-top:10px">
            <div class="mr-auto"> </div>
            
        </div>
        </div>

    </div>
</template>

<script>
import IzinMahasiswaService from '../../services/izinMahasiswa.service';

export default{
    name: 'PerizinanKegiatanMahasiswa',
 
    data(){
        return{
            nama_kegiatan: '',
            organisasi: '',
            user: 1, 
            status_perizinan_kegiatan: 1,
            waktu_tanggal_mulai: '',
            waktu_tanggal_akhir: '',
            email_pic: '',
            nama_pic: '',
            hp_pic: '',
            npm_pic:'',
            npm_ketua_organisasi: '',
            nama_ketua_organisasi:'',
            tempat_pelaksanaan: '',
            sumber_pendanaan:'',
            alasan_penolakan:'',
            file_info_kegiatan: null,
            kebutuhan:[],
            respon_kegiatan: null,
            modalOpen:false
        }
    },
    methods: {
        mounted(){
        console.log(this.user);
        console.log(this.error_message);
        },
        onFileChange(){
            this.file_info_kegiatan = this.$refs.file.files[0];
        },
        postIzinKegiatan(){
            const data_kegiatan = {
                nama_kegiatan: this.nama_kegiatan,
                organisasi: this.organisasi,
                user: this.user,
                status_perizinan_kegiatan :this.status_perizinan_kegiatan,
            }
            console.log(this.kebutuhan)
                IzinMahasiswaService.postIzinKegiatanHeader(data_kegiatan).then(
                    response =>{
                        this.respon_kegiatan = response.data;
                        console.log(response.data);
                        let formDataDetail = new FormData()
                        formDataDetail.append("izin_kegiatan",this.respon_kegiatan.id)
                        formDataDetail.append("waktu_tanggal_mulai",this.waktu_tanggal_mulai)
                        formDataDetail.append("waktu_tanggal_akhir",this.waktu_tanggal_akhir)
                        formDataDetail.append("email_pic",this.email_pic)
                        formDataDetail.append("nama_pic",this.nama_pic)
                        formDataDetail.append("hp_pic",this.hp_pic)
                        formDataDetail.append("npm_pic",this.npm_pic)
                        formDataDetail.append("npm_ketua_organisasi",this.npm_ketua_organisasi)
                        formDataDetail.append("nama_ketua_organisasi",this.nama_ketua_organisasi)
                        formDataDetail.append("tempat_pelaksanaan",this.tempat_pelaksanaan)
                        formDataDetail.append("sumber_pendanaan",this.sumber_pendanaan)
                        formDataDetail.append("alasan_penolakan",this.alasan_penolakan)
                        if(this.file_info_kegiatan != null){
                            formDataDetail.append("file_info_kegiatan",this.file_info_kegiatan)
                        }
                        IzinMahasiswaService.postIzinKegiatanDetail(formDataDetail).then(
                            response =>{
                                console.log(response.data);
                            },
                            error =>{
                                console.log(error.message);
                            }
                        )
                        },
                error =>{
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
input {
    border-radius: 10px !important;
}
.form-control-file{
    border-radius: 0px !important;
}
.text-keterangan{
  font-size: x-small;
  color: gray
}
.btn-simpan {
    padding:3px 20px;
    font-size:16px;
    width: 107px;
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
</style>