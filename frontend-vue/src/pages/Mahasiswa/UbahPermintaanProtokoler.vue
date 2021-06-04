<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page" style="font-weight: bold;">Ubah Souvenir</h3>
            <hr class="line-header">
        </div>

        <div class="formulir m-3">
            <form>
                

                <div class="form-row">
                    <div class="col-12 col-md-6 px-3">
                        <label >Deskripsi Kebutuhan<label style="color:red">*</label>:</label>
                        <input name="fname" type="text" class="form-control" id="nama" placeholder="e.g. Pulpen" v-model="deskripsi_kebutuhan">
                    </div>
                    <div class="col-12 col-md-6 px-3">
                        
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
                                        v-on:click="putPermintaanProtokoler"
                                        > Simpan</button>
                            </div>
                        </div>
 <!-- Modal: Notif Sukses -->
    <div class="modal fade" id="ubahModal" tabindex="-1" role="dialog" aria-labelledby="sukses-setuju-modal" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">

            <div class="modal-body">
                <div class="text-center">
                    <img src="../../assets/images/icon_ceklis.png" alt="icon-sukses">
                <h2 style="margin:20px 0px 15px 0px">Sukses</h2>
                <p style="margin:0px 0px -15px 0px">Permintaan protokoler berhasil disimpan</p>
                </div>
            </div>
            <div class="modal-footer">
                <div class="text-center">
                    <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="ubahDone" style="width:80px; height:36px;">OK</button>
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
                <p style="margin:0px 0px -15px 0px">{{ error_message }}</p>
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
    name: 'EditPermintaanProtokoler',
    data() {
        return {
            izin_kegiatan: "",
            error_messase: "",
            
        }
    },
    created(){
        
    },
    mounted(){
        console.log(this.izin_kegiatan);
        console.log(this.error_message);
                
    },
    methods: {
        putPermintaanProtokoler() {
            console.log("masuk put permintaan_protokoler");
            console.log(this.$route.params.id);

            const data_put = {                                     
                id:this.$route.params.id,         
                permintaan_protokoler: {id:1, deskripsi_kebutuhan: this.deskripsi_kebutuhan, status_permintaan_protokoler:1}
                
            };
            console.log(data_put);
            UserService.putPerizinan(this.$route.params.id, data_put).then(
                response => {
                    console.log(response.data);
                    $('#ubahModal').modal('toggle')

                },
                error => {
                    console.log("masuk put permintaan_protokoler");
                    console.log(this.$route.params.id);
                    console.log(error.message);
                    $('#notification-failed').modal('show')
                }
        );
        },
        ubahDone() {
            window.location.href="/perizinan/";
        }
    }
}
</script>