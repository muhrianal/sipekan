<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page" style="font-weight: bold;">Verfikasi Perizinan Kegiatan</h3>
            <hr class="line-header">
        </div>
        <div v-if="this.list_permintaan_souvenir.length > 0" class="header-perizinan col-12 px-2"> 
            Souvenir
            <hr noshade>
        </div>   
        <div v-for="permintaan in list_permintaan_souvenir" v-bind:key="permintaan">
        <div class="formulir m-3">    
            <form>
                <div class="form-row">
                    <div class="col-6 col-md-6">
                        <label v-if="permintaan.status_permintaan_souvenir==1" class="status">Status Sekarang: <span class="status-span" style="color: #828282;">Menunggu Persetujuan</span></label>
                        <label v-if="permintaan.status_permintaan_souvenir==2" class="status">Status Sekarang: <span class="status-span" style="color: #27AE60;">Disetujui</span></label>
                        <label v-if="permintaan.status_permintaan_souvenir==3" class="status">Status Sekarang: <span class="status-span" style="color: #EB5757;">Ditolak</span></label>
                    </div>
                    <div class="col-6 col-md-6 px-4 d-flex justify-content-end">
                        <label class="status">Dibuat: {{getDate(permintaan.created_at)}}</label>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-6 col-md-6"></div>
                    <div class="col-6 col-md-6 px-4 d-flex justify-content-end">
                    <label class="status">Disunting: {{getDate(permintaan.updated_at)}}</label>
                    </div>
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputNamaPenerima">Nama Penerima</label>
                        <input class="form-control readonly-form" :placeholder="permintaan.nama_penerima_souvenir" readonly>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputJabatanPenerima">Jabatan Penerima</label>
                        <input class="form-control readonly-form" :placeholder="permintaan.jabatan_penerima_souvenir" readonly>
                    </div>                             
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputKelas">Kelas</label>
                        <input v-if="permintaan.kelas_penerima_souvenir == 1" type="text" class="form-control readonly-form" placeholder="Presiden/ Menteri/ Rektor/ Dekan/ Sederajat" readonly>
                        <input v-if="permintaan.kelas_penerima_souvenir == 2" type="text" class="form-control readonly-form" placeholder="Pembicara Kuliah Tamu/ Seminar/ Profesional/ CEO/ Partner dari luar" readonly>
                        <input v-if="permintaan.kelas_penerima_souvenir == 3" type="text" class="form-control readonly-form" placeholder="Penerima bersifat masal" readonly>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputRegion">Region</label>
                        <input v-if="permintaan.region_penerima_souvenir == 1" type="text" class="form-control readonly-form" placeholder="Dalam Negeri" readonly>
                        <input v-if="permintaan.region_penerima_souvenir == 2" type="text" class="form-control readonly-form" placeholder="Luar Negeri" readonly>
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputPilihanSouvenir">Pilihan Souvenir</label>
                        <input class="form-control readonly-form" :placeholder="permintaan.souvenir.nama_souvenir" readonly>                
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputJumlah">Jumlah</label>
                        <input id="input_jumlah" class="form-control readonly-form" :placeholder="permintaan.jumlah">
                    </div>                    
                </div>
            </form>
             <div class="d-flex" style="margin-top:10px">
                <div class="mr-auto"></div>
                <div class="p-2">
                    <button class="btn tolak" v-if="permintaan.status_permintaan_souvenir == 1" v-on:click="popUpAlasanPenolakan(permintaan.id,'souvenir')" style="padding:3px 20px;font-size:16px;">Tolak</button>
                </div>
                <div class="p-2 pr-4">
                    <button class="btn setuju" data-toggle="modal" v-if="permintaan.status_permintaan_souvenir ==1 " v-on:click="putSetujuSouvenir(permintaan.id)" style="padding:3px 20px;font-size:16px;">Setuju</button>
                </div>
            </div>
        </div>
        <hr>
        </div>
         <div v-if="this.permintaan_protokoler!=null" class="header-perizinan col-12 px-2"> 
            Protokoler
            <hr class="line-header">        
        </div>  
        <div v-if="this.permintaan_protokoler!=null" class="formulir m-3">  
            <form>
                 <div class="form-row">
                    <div class="col-6 col-md-6">
                        <label v-if="this.permintaan_protokoler.status_permintaan_protokoler==1" class="status">Status Sekarang: <span class="status-span" style="color: #828282;">Menunggu Persetujuan</span></label>
                        <label v-if="this.permintaan_protokoler.status_permintaan_protokoler==2" class="status">Status Sekarang: <span class="status-span" style="color: #27AE60;">Disetujui</span></label>
                        <label v-if="this.permintaan_protokoler.status_permintaan_protokoler==3" class="status">Status Sekarang: <span class="status-span" style="color: #EB5757;">Ditolak</span></label>
                    </div>
                    <div class="col-6 col-md-6 px-4 d-flex justify-content-end">
                        <label class="status">Dibuat: {{getDate(this.permintaan_protokoler.created_at)}}</label>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-6 col-md-6"></div>
                    <div class="col-6 col-md-6 px-4 d-flex justify-content-end">
                    <label class="status">Disunting: {{getDate(this.permintaan_protokoler.updated_at)}}</label>
                    </div>
                </div>
               <div class="form-row">
                    <div class="col-12 col-md-12  px-4 py-2">   
                        <label for="inputDeskripsiKebutuhan">Deskripsi Kebutuhan: <span class="text-keterangan" id="text-keterangan-small">  (contoh: nama penerima, jumlah pendamping dibutuhkan)</span></label>
                        <textarea  class="form-control readonly-form" :placeholder="this.permintaan_protokoler.deskripsi_kebutuhan" readonly></textarea>         
                    </div>                    
                </div>   
            </form>
            <div  v-if="this.permintaan_protokoler!=null" class="d-flex" style="margin-top:10px">
                <div class="mr-auto"></div>
                <div class="p-2">
                    <button class="btn tolak" v-if="this.permintaan_protokoler.status_permintaan_protokoler == 1" v-on:click="popUpAlasanPenolakan(this.permintaan_protokoler.id,'protokoler')" style="padding:3px 20px;font-size:16px;">Tolak</button>
                </div>
                <div class="p-2 pr-4">
                    <button class="btn setuju" data-toggle="modal" v-if="this.permintaan_protokoler.status_permintaan_protokoler ==1 " v-on:click="putSetujuProtokoler(this.permintaan_protokoler.id)" style="padding:3px 20px;font-size:16px;">Setuju</button>
                </div>
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
                <p style="margin:0px 0px -15px 0px">{{success_message}}</p>
                </div>
            </div>
            <div class="modal-footer">
                <div class="text-center">
                    <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="refreshPage" style="width:80px; height:36px;">OK</button>
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

    <!-- Modal: Popup Alasan Penolakan -->
    <div class="modal fade" id="popup-penolakan" tabindex="-1" role="dialog" aria-labelledby="popup-penolakan" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">

            <form v-on:submit.prevent="putTolak">
                <div class="modal-body">
                    <label for="keterangan">Tambah alasan penolakan<span class="asterisk">*</span></label>
                    <textarea class="form-control" id="textarea-keterangan" rows="6" v-model="alasan_penolakan" placeholder="e.g. Pilih pilihan humas yang lain" required></textarea>
                </div>
                <div class="modal-footer">
                    <div class="text-center">
                        <button class="btn btn-outline-secondary" data-dismiss="modal" style="width:80px; height:36px;">Batal</button>
                    </div>
                    <div class="text-center">
                        <button class="btn btn-success" type="submit" style="width:80px; height:36px;">Selesai</button>
                    </div>
                </div>
            </form>
            </div>
        </div>
    </div>

</template>

<script>
import UserService from '../../services/user.service';
import moment from 'moment';
import $ from 'jquery';

export default {
    name: 'DetailPerizinanHumas',
    
    data(){
        return{
            id_izin_kegiatan: null,
            list_permintaan_souvenir: [],
            permintaan_protokoler:null,

            // for put update status
            alasan_penolakan : null,
            current_id_untuk_ditolak : -1,
            current_permintaan_untuk_ditolak: '',
            error_message : '',
            success_message: '',

        }
    },
    created(){
        this.id_izin_kegiatan = this.$route.params.id;

        UserService.getPerizinanHumasByIdIzinKegiatan(this.id_izin_kegiatan).then(
            response => {
                this.permintaan_protokoler = response.data.permintaan_protokoler;
                this.list_permintaan_souvenir = response.data.permintaan_souvenir;
                console.log(this.permintaan_protokoler)
            },
            error => {
                console.log(error.message);
                // do something when error
            }
        )
    },
    methods: {
        getDate : function (date) {
            return moment(date, 'YYYY-MM-DDTHH:mm').format('HH:mm, D MMMM YYYY');
        },
        getDateOnly : function (date) {
            return moment(date, 'YYYY-MM-DDTHH:mm').format('D MMMM YYYY');
        },
        getHour : function (date) {
            return moment(date, 'YYYY-MM-DDTHH:mm').format('HH:mm');
        },
        putSetujuSouvenir(id_permintaan){
            const data = {
                'status_permintaan_souvenir' : 2,
                'alasan_penolakan' : null
            }

            UserService.putUpdateStatusDanAlasanPermintaanSouvenir(data, id_permintaan).then(
                response => {
                    this.success_message = 'Permintaan humas berhasil disetujui'
                    $('#notification-success').modal('show')
                    console.log(response.data);
                },
                error => {
                    this.error_message = error.message
                    

                    $('#notification-failed').modal('show')
                    console.log(error.message);
                }
            )
        },
        putSetujuProtokoler(id_permintaan){
            const data = {
                'status_permintaan_protokoler' : 2,
                'alasan_penolakan' : null
            }

            UserService.putUpdateStatusDanAlasanPermintaanProtokoler(data, id_permintaan).then(
                response => {
                    this.success_message = 'Permintaan humas berhasil disetujui'
                    $('#notification-success').modal('show')
                    console.log(response.data);
                },
                error => {
                    this.error_message = error.message
                    

                    $('#notification-failed').modal('show')
                    console.log(error.message);
                }
            )
        },
        putTolak(){
            $('#popup-penolakan').modal('hide')
                const data = {
                    'alasan_penolakan' : this.alasan_penolakan
                }
            if(this.current_permintaan_untuk_ditolak=='souvenir'){
                data["status_permintaan_souvenir"] = 3
                UserService.putUpdateStatusDanAlasanPermintaanSouvenir(data, this.current_id_untuk_ditolak).then(
                response => {
                    this.success_message = 'Permintaan humas berhasil ditolak'
                    $('#notification-success').modal('show')
                    console.log(response.data);
                },
                error => {
                    this.error_message = error.message
                    

                    $('#notification-failed').modal('show')
                    console.log(error.message);
                }
            )
            }
            if(this.current_permintaan_untuk_ditolak=='protokoler'){
                data["status_permintaan_protokoler"] = 3
                UserService.putUpdateStatusDanAlasanPermintaanProtokoler(data, this.current_id_untuk_ditolak).then(
                response => {
                    this.success_message = 'Permintaan humas berhasil ditolak'
                    $('#notification-success').modal('show')
                    console.log(response.data);
                },
                error => {
                    this.error_message = error.message
                    

                    $('#notification-failed').modal('show')
                    console.log(error.message);
                }
            )

            }

            
        },
        popUpAlasanPenolakan(id_permintaan,jenisPermintaan){
            this.current_id_untuk_ditolak = id_permintaan
            this.current_permintaan_untuk_ditolak = jenisPermintaan

            $('#popup-penolakan').modal('show')

        },

        refreshPage(){
            location.reload()
        }
    }
}
</script>

<style>

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

/* ::placeholder {
    color:  #5f5f5f;
} */

.readonly-form::placeholder {
    color: #5f5f5f !important;
}
</style>