<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page" style="font-weight: bold;">Verfikasi Perizinan Kegiatan</h3>
            <hr class="line-header">
        </div>

        <template v-for="peminjaman in list_peminjaman" v-bind:key="peminjaman">
        <div class="formulir m-3">    
            <form>
                <div class="form-row">
                    <div class="col-6 col-md-6">
                    <label v-if="peminjaman.status_peminjaman_ruangan==1" class="status">Status Sekarang: <span class="status-span" style="color: #828282;">Menunggu Persetujuan</span></label>
                    <label v-if="peminjaman.status_peminjaman_ruangan==2" class="status">Status Sekarang: <span class="status-span" style="color: #27AE60;">Disetujui</span></label>
                    <label v-if="peminjaman.status_peminjaman_ruangan==3" class="status">Status Sekarang: <span class="status-span" style="color: #EB5757;">Ditolak</span></label>
                    </div>
                    <div class="col-6 col-md-6 px-4 d-flex justify-content-end">
                    <label class="status">Dibuat: {{getDate(peminjaman.created_at)}}</label>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-6 col-md-6"></div>
                    <div class="col-6 col-md-6 px-4 d-flex justify-content-end">
                    <label class="status">Disunting: {{getDate(peminjaman.updated_at)}}</label>
                    </div>
                </div>
                
                <div class="form-row">
                    <div class="col-12 col-md-6">
                        <label for="inputSubkegiatan">Nama Subkegiatan<span class="asterisk">*</span></label>
                        <input type="text" class="form-control readonly-form" :placeholder="peminjaman.judul_peminjaman" readonly>
                    </div>
                    <div class="col-12 col-md-6">
                        <label for="inputJumlahPeserta">Jumlah Peserta<span class="asterisk">*</span></label>
                        <input type="number" class="form-control readonly-form" :placeholder="peminjaman.jumlah_peserta" readonly>
                    </div>  
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6">
                        <label for="waktuMulaiPeminjaman">Waktu mulai<span class="asterisk">*</span></label>
                        <input type="text" class="form-control readonly-form" :placeholder="getHour(peminjaman.waktu_mulai)" readonly>
                        
                    </div>
                    <div class="col-12 col-md-6">
                        <label for="waktuAkhirPeminjaman">Waktu akhir<span class="asterisk">*</span></label>
                        <input type="text" class="form-control readonly-form" :placeholder="getHour(peminjaman.waktu_akhir)" readonly>
                    </div>  
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6">
                        <label for="ruangan">Ruangan<span class="asterisk">*</span></label>
                        <input type="text" class="form-control readonly-form" :placeholder="peminjaman.ruangan" readonly>
                        
                        <p class="note-ruangan note-form text-right">Lihat daftar ruangan <a href="#">disini</a> </p>

                        <label for="perulangan">Perulangan<span class="asterisk">*</span></label>
                        <input v-if="peminjaman.perulangan.jenjang == 1" type="text" class="form-control readonly-form" placeholder="SEKALI PAKAI" readonly>
                        <input v-if="peminjaman.perulangan.jenjang == 2" type="text" class="form-control readonly-form" placeholder="HARIAN" readonly>
                        <input v-if="peminjaman.perulangan.jenjang == 3" type="text" class="form-control readonly-form" placeholder="MINGGUAN" readonly>
                        <input v-if="peminjaman.perulangan.jenjang == 4" type="text" class="form-control readonly-form" placeholder="BULANAN" readonly>
                    </div>

                    <div class="col-12 col-md-6">
                        <label for="keterangan">Keterangan</label>
                        <textarea class="form-control readonly-form" rows="4" id="textarea-keterangan" :placeholder="peminjaman.catatan" readonly></textarea>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6">
                        <label for="tanggalMulaiPelaksanaan">Tanggal Mulai Penggunaan<span class="asterisk">*</span></label>
                        <input type="text" class="form-control readonly-form" :placeholder="getDateOnly(peminjaman.perulangan.tanggal_mulai)" readonly>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" v-model="peminjaman.terbuka_untuk_umum" id="checkbox-terbuka-untuk-umum" disabled>
                            <label class="form-check-label" for="flexCheckDefault">
                                Terbuka untuk umum
                            </label>
                        </div>
                    </div>
                    <div class="col-12 col-md-6">
                        <label for="tanggalAkhirPelaksanaan">Tanggal Akhir Penggunaan<span class="asterisk">*</span></label>
                        <input type="text" class="form-control readonly-form" :placeholder="getDateOnly(peminjaman.perulangan.tanggal_akhir)" readonly>
                        <p class="note-form">isi dengan tanggal yang sama dengan tanggal mulai pelaksanaan jika memilih "sekali pakai"</p>
                    </div>  
                </div>
            </form>
             <div class="d-flex" style="margin-top:10px">
                <div class="mr-auto"></div>
                <div class="p-2">
                    <button class="btn tolak" v-if="peminjaman.status_peminjaman_ruangan == 1" v-on:click="popUpAlasanPenolakan(peminjaman.id)" style="padding:3px 20px;font-size:16px;">Tolak</button>
                </div>
                <div class="p-2 pr-4">
                    <button class="btn setuju" data-toggle="modal" v-if="peminjaman.status_peminjaman_ruangan == 1" v-on:click="putSetuju(peminjaman.id)" style="padding:3px 20px;font-size:16px;">Setuju</button>
                </div>
            </div>
        </div>
        

        <hr class="line-header">
        </template>

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
                        <textarea class="form-control" id="textarea-keterangan" rows="6" v-model="alasan_penolakan" placeholder="e.g. Pilih ruangan lain yang lebih kecil" required></textarea>
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
    </div>

   

</template>

<script>
import UserService from '../../services/user.service';
import moment from 'moment';
import $ from 'jquery';

export default {
    name: 'DetailPerizinanRuangan',
    
    data(){
        return{
            id_izin_kegiatan: -1,
            list_peminjaman: [],

            // for put update status
            alasan_penolakan : null,
            current_id_untuk_ditolak : -1,
            error_message : '',
            success_message: '',

        }
    },
    created(){
        this.id_izin_kegiatan = this.$route.params.id;

        UserService.getPeminjamanRuanganByIdIzinKegiatan(this.id_izin_kegiatan).then(
            response =>{
                this.list_peminjaman = response.data;

            },
            error => {
                console.log(error.message);
                // do something when error
            }
        );
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

        putSetuju(id_peminjaman){
            const data = {
                'status_peminjaman_ruangan' : 2,
                'alasan_penolakan' : null
            }

            UserService.putUpdateStatusDanAlasanPenolakanPeminjamanRuangan(data, id_peminjaman).then(
                response => {
                    this.success_message = 'Peminjaman ruangan berhasil disetujui'
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
                'status_peminjaman_ruangan' : 3,
                'alasan_penolakan' : this.alasan_penolakan
            }

            UserService.putUpdateStatusDanAlasanPenolakanPeminjamanRuangan(data, this.current_id_untuk_ditolak).then(
                response => {
                    this.success_message = 'Peminjaman ruangan berhasil ditolak'
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

        popUpAlasanPenolakan(id_peminjaman){
            this.current_id_untuk_ditolak = id_peminjaman

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