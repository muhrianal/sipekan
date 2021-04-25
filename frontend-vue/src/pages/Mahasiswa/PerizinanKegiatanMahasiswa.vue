<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page">Buat Perizinan<span style="color:grey"> >> Kegiatan</span></h3>
            <hr class="line-header">
        </div>
        
        <div class="formulir">
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
                        <!-- <div class="form-row">
                          <div class="col-8 md 4">
                             <input type="date" class="form-control" required v-model="tanggal_mulai">
                          </div>
                          <div class="col-4 md 2">
                             <input type="time" class="form-control" required>
                          </div>
                        </div>   -->
                    </div>

                    <div class="col-12 col-md-6  px-4 py-2 ">
                        <label for="inputTanggalAkhir">Tanggal Akhir<span class="text-danger">*</span>:</label>
                        <input type=datetime-local class=form-control v-model="waktu_tanggal_akhir" required>
                        <!-- <div class="form-row">
                          <div class="col-8 md 4">
                             <input type="date" class="form-control" required >
                          </div>
                          <div class="col-4 md 2">
                             <input type="time" class="form-control" required>
                          </div>
                        </div>   -->
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
                        <!-- <input v-el="info_kegiatan" type="file" ref="fileInput" @change="onPickFile" class="form-control-file" required > -->
                        <input type="file" ref="file" @change="onFileChange">
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputButuhHumas">Apakah anda memerlukan humas?<span class="text-keterangan">  (Publikasi, Souvenir, Protokoler)</span></label>
                        <br><input v-model="kebutuhan" type="checkbox" value ="humas" id="humas"> <label>Ya</label>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputButuhRuangn">Apakah anda memerlukan ruangan?</label>
                        <br><input v-model="kebutuhan" type="checkbox" value ="ruangan" id="ruangan"> <label>Ya</label>
                    </div>                    
                </div>
                <!-- <div class="p-2">
                    <button type="button" class="btn btn-outline-danger" id="button-batal">Batal</button> -->
                <!-- <a href="/" class="btn btn-outline-danger" id="button-batal" style="padding:3px 20px;font-size:16px;"> Batal</a> -->
                <!-- </div> -->
                <div class="form-row p-2 pr-4">
                    <input type="submit" value ="submit">
                        <!-- <button type="button" class= "btn btn-success" id="button-setuju">Simpan</button> -->
                    <!-- <a class="btn simpan" style="padding:3px 20px;font-size:16px;"> Simpan</a> -->
                </div>
                 <!-- v-on:click="postIzinKegiatan" -->
            </form>
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
            kebutuhan:[]
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
            const detail_kegiatan_data = {
                waktu_tanggal_mulai: this.waktu_tanggal_mulai,
                waktu_tanggal_akhir: this.waktu_tanggal_akhir,
                email_pic: this.email_pic,
                nama_pic: this.email_pic,
                hp_pic: this.hp_pic,
                npm_pic: this.npm_pic,
                npm_ketua_organisasi: this.npm_pic,
                nama_ketua_organisasi: this.nama_ketua_organisasi,
                tempat_pelaksanaan: this.tempat_pelaksanaan,
                sumber_pendanaan: this.sumber_pendanaan,
                alasan_penolakan:'',
                file_info_kegiatan: this.file_info_kegiatan,
            }
            const data_kegiatan = {
                nama_kegiatan: this.nama_kegiatan,
                organisasi: this.organisasi,
                user: this.user,
                status_perizinan_kegiatan :this.status_perizinan_kegiatan,
                detail_kegiatan: detail_kegiatan_data
            }
            // let formData = new FormData()
            // formData.append('file_info_kegiatan', this.file_info_kegiatan)
            // // formData.append('nama_kegiatan',this.nama_kegiatan)
            // // var json = JSON.stringify(formData)
            // // console.log(json)
            // for(var key in data_kegiatan){
            //     formData.append(key,data_kegiatan[key])
            // }
            // const list_kebutuhan = {
            //     kebutuhan: this.kebutuhan
            // }
            
            IzinMahasiswaService.postIzinKegiatan(data_kegiatan).then(
                response =>{
                    console.log(response.data);
                },
                error =>{
                    console.log(error.message);
                }
            );
            // IzinMahasiswaService.postIzinKegiatan(formData).then(
            //     response => {
            //         console.log(formData);
            //         console.log(response.data);
            //     },
            //     error =>{
            //         console.log(error.message);
            //     }
            // );
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
</style>