<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page">Buat Pengumuman</h3>
            <hr class="line-header line-title">
        </div>
        <div class="form-pengumuman">
            <form v-on:submit.prevent="submitPengumuman">
                <label for="inputJudul">Judul<span class="asterisk">*</span></label>
                <input type="text" class="form-control" v-model="judul" required>

                <label for="inputUploadDokumen">Upload Dokumen<span class="text-keterangan"> (contoh: InfoRuangan.pdf; FormulirPeminjaman.zip)</span></label>
                <input id="file_pengumuman" class="form-control-file" type="file" ref="file" @change="onFileChange">
                <p  v-if="this.file_pengumuman!=null" class="text-left text-danger note-form" @Click="deleteFileInfo()">Hapus File</p>

                <label for="inputDeskripsi">Deskripsi<span class="asterisk">*</span></label>
                <textarea type="text" rows=20 class="form-control" v-model="deskripsi" required></textarea>
                <br>
                <div class="text-right">
                    <button type="submit" class="btn btn-success btn-simpan">Submit</button>
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
                        <p style="margin:0px 0px -15px 0px">Pengumuman berhasil dibuat</p>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <div class="text-center">
                            <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="goToPengumuman" style="width:80px; height:36px;">OK</button>
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
                            <button type="button" class="btn btn-success" data-dismiss="modal" style="width:80px; height:36px;">OK</button>
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
    name: 'BuatPengumuman',
    data() {
        return {
            judul: '',
            file_pengumuman: null,
            deskripsi:'',
            error_message : '',
        
        } 
    },
    computed: {

    },
    created(){

    },
    methods: {
        submitPengumuman(){
            let formData = new FormData()
            formData.append('nama', this.judul)
            formData.append('deskripsi', this.deskripsi)
            formData.append('file_pengumuman', this.file_pengumuman)
            
            UserService.postPengumuman(formData).then(
                response => {
                    $('#notification-success').modal('show')
                    console.log(response.data)
                    
                },
                error => {
                    this.error_message = error.message

                    $('#notification-failed').modal('show')

                    console.log(error.message)
                }
            )
            
        },
        onFileChange(){
            this.file_pengumuman = this.$refs.file.files[0];
        },
        deleteFileInfo(){
            document.getElementById("file_pengumuman").value  = null; 
            this.file_pengumuman = null
        },
        goToPengumuman(){
            this.$router.push('/pengumuman');
        }

    }
}

</script>

<style>

</style>