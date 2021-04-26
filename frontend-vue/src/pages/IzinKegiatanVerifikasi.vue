<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page" style="font-weight: 500;">Verfikasi Perizinan Kegiatan</h3>
            <hr class="line-header">
        </div>

        <div class="formulir m-3">
            
            <form>
                <div class="form-row">
                    <div class="col-6 col-md-6 px-4">
                    <label v-if="izin_kegiatan.status_perizinan_kegiatan==1" class="status">Status Sekarang: <span class="status-span" style="color: #828282;">Menunggu Persetujuan</span></label>
                    <label v-if="izin_kegiatan.status_perizinan_kegiatan==2" class="status">Status Sekarang: <span class="status-span" style="color: #27AE60;">Disetujui</span></label>
                    <label v-if="izin_kegiatan.status_perizinan_kegiatan==3" class="status">Status Sekarang: <span class="status-span" style="color: #EB5757;">Ditolak</span></label>
                    </div>
                    <div class="col-6 col-md-6 px-4 d-flex justify-content-end">
                    <label class="status">Dibuat: {{getDate(izin_kegiatan.detail_kegiatan.created_at)}}</label>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-6 col-md-6"></div>
                    <div class="col-6 col-md-6 px-4 d-flex justify-content-end">
                    <label class="status">Disunting: {{getDate(izin_kegiatan.detail_kegiatan.updated_at)}}</label>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Nama Kegiatan:</label>
                        <input type="text" class="form-control" :placeholder="izin_kegiatan.nama_kegiatan" readonly> 

                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Tempat Pelaksanaan:</label>
                        <input type="text" class="form-control" :placeholder="izin_kegiatan.detail_kegiatan.tempat_pelaksanaan" readonly>
                    </div>

                </div>

                <div class="form-row">
                    <div class="col-12 col-md-5 px-4 py-2">
                        <label>Tanggal Mulai:</label>
                        <input type="text" class="form-control" :placeholder="getDateDef(izin_kegiatan.detail_kegiatan.waktu_tanggal_mulai)" readonly>
                    </div>
                    <div class="pukul col-12 col-md-1 pl-2 pr-4">
                        <label></label>
                        <input type="text" class="form-control" :placeholder="getHour(izin_kegiatan.detail_kegiatan.waktu_tanggal_mulai)" readonly>
                    </div>
                    <div class="col-12 col-md-5 px-4 py-2">
                        <label>Tanggal Selesai:</label>
                        <input type="text" class="form-control" :placeholder="getDateDef(izin_kegiatan.detail_kegiatan.waktu_tanggal_akhir)" readonly>
                    </div>
                    <div class="pukul col-12 col-md-1 pl-2 pr-4">
                        <label></label>
                        <input type="text" class="form-control" :placeholder="getHour(izin_kegiatan.detail_kegiatan.waktu_tanggal_akhir)" readonly>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Organisasi Penanggungjawab:</label>
                        <input type="text" class="form-control" :placeholder="izin_kegiatan.organisasi" readonly>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Ketua Organisasi:</label>
                        <input type="text" class="form-control" :placeholder="izin_kegiatan.detail_kegiatan.nama_ketua_organisasi" readonly>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>NPM Ketua Organisasi:</label>
                        <input type="text" class="form-control" :placeholder="izin_kegiatan.detail_kegiatan.npm_ketua_organisasi" readonly>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Nama PIC Kegiatan:</label>
                        <input type="text" class="form-control" :placeholder="izin_kegiatan.detail_kegiatan.nama_pic" readonly>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>NPM PIC:</label>
                        <input type="text" class="form-control" :placeholder="izin_kegiatan.detail_kegiatan.npm_pic" readonly>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Email PIC:</label>
                        <input type="text" class="form-control" :placeholder="izin_kegiatan.detail_kegiatan.email_pic" readonly>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>HP PIC:</label>
                        <input type="text" class="form-control" :placeholder="izin_kegiatan.detail_kegiatan.hp_pic" readonly>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Sumber Pendanaan</label>
                        <input type="text" class="form-control" :placeholder="izin_kegiatan.detail_kegiatan.sumber_pendanaan" readonly>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Dokumen</label>
                        <input type="text" class="form-control" :placeholder="izin_kegiatan.detail_kegiatan.file_info_kegiatan" readonly>
                    </div>
                </div>

            </form>
        </div>
        <div class="d-flex" style="margin-top:100px">
            <div class="mr-auto">

            </div>
            <div class="p-2">
                <button class="btn tolak" v-on:click="putTolak" style="padding:3px 20px;font-size:16px;"> Tolak</button>
            </div>
            <div class="p-2 pr-4">
                <button class="btn setuju" v-on:click="putSetuju" style="padding:3px 20px;font-size:16px;"> Setuju</button>
            </div>
         </div>
    </div>
</template>

<script>
import UserService from '../services/user.service';
import moment from 'moment';
export default {
    
    name: 'IzinKegiatan',
    data() {
        return {
            izin_kegiatan: "",
            error_message: "",
        }
    },
   
    created(){
         UserService.getIzinKegiatan(this.$route.params.id).then(
            response => {
                this.izin_kegiatan = response.data;
            },
            error => {
                this.error_message = (error.response && error.response.data) || error.message || error.toString();
            }
        );
    },
    mounted(){
        console.log(this.error_message);
    },
     methods: {
        getDateDef : function (date) {
            return moment(date, 'YYYY-MM-DDTHH:mm').format('D MMMM YYYY');
        },
        getDate : function (date) {
            return moment(date, 'YYYY-MM-DDTHH:mm').format('HH:mm, D MMMM YYYY');
        },
        getHour : function (date) {
            return moment(date, 'YYYY-MM-DDTHH:mm').format('HH:mm');
        },
        putSetuju() {
            
            console.log("test");
            const data_put = {
                izin_kegiatan: {
                    status_perizinan_kegiatan: 2
                },
            };
            console.log(data_put);
            UserService.putIzinKegiatan(this.$route.params.id, data_put).then(
                response => {
                    console.log(response.data);
                },
                error => {
                    console.log(error.message);
                }
            );
            location.reload();
        },
        putTolak() {
            console.log("test");
            const data_put = {
                izin_kegiatan: {
                    status_perizinan_kegiatan: 3
                },
            };
            console.log(data_put);
            UserService.putIzinKegiatan(this.$route.params.id, data_put).then(
                response => {
                    console.log(response.data);
                },
                error => {
                    console.log(error.message);
                }
            );
            location.reload();
        }
    },
}
</script>

<style>
.pukul{
    padding-top: 14px;
}
.status {
    color: #BDBDBD
}
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
.setuju {
    color: white;
    border-color: #27AE60;
    background-color: #27AE60 !important;
    border-radius: 5px !important;
}
.setuju:hover{
    background-color: #27AE60 !important;
    border-color: #27AE60;
    color: white;
}
.tolak {
    color: #EB5757;
    border-color: #EB5757;
    background-color: white!important;
    border-radius: 5px !important;
}
.tolak:hover {
    color: white;
    border-color: #EB5757;
    background-color:#EB5757!important;
}
input, select{
    border-radius: 10px !important;
}
</style>