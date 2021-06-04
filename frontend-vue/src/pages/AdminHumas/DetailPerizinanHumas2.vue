<template>
    <div class="root-class">
         <div class="header">
            <h3 class="header-page" style="font-weight: bold;">Verfikasi Perizinan Kegiatan</h3>
            <hr class="line-header">
        </div>
        <div>{{this.id_izin_kegiatan}}</div>
        <div>{{this.list_permintaan_souvenir}}</div>
        <!-- <template v-for="permintaan in list_permintaan_souvenir" v-bind:key="permintaan">
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
                    <button class="btn tolak" v-if="permintaan.status_permintaan_souvenir == 1" v-on:click="popUpAlasanPenolakan(permintaan.id)" style="padding:3px 20px;font-size:16px;">Tolak</button>
                </div>
                <div class="p-2 pr-4">
                    <button class="btn setuju" data-toggle="modal" v-if="ppermintaan.status_permintaan_souvenir ==1 " v-on:click="putSetuju(permintaan.id)" style="padding:3px 20px;font-size:16px;">Setuju</button>
                </div>
            </div>
        </div>
        <hr class="line-header">
        </template> -->
    </div>
</template>
<script>
import UserService from '../../services/user.service';
// import moment from 'moment';
// import $ from 'jquery';

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
            error_message : '',
            success_message: '',

        }
    },
    mounted(){
        this.id_izin_kegiatan = this.$route.params.id;
        UserService.getPerizinanHumasByIdIzinKegiatan(this.id_izin_kegiatan).then(
            response => {
                this.id_izin_kegiatan = 10;
                this.list_permintaan_souvenir = response.data.permintaan_souvenir;
                this.permintaan_protokoler = response.data.permintaan_protokoler;
                console.log(this.id_izin_kegiatan)
                console.log( this.list_permintaan_souvenir)
                console.log(this.permintaan_protokoler)
            },
            error => {
                console.log(error.message);
                // do something when error
            }
        )
    },
    
    }
</script>