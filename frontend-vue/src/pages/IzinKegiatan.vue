<template>
    <div class="card">
    <div class="d-flex">
        <div class="mr-auto p-3">
            <h4 class="judul p-1 align-middle mb-0" style="font-weight: bold;">Daftar Perizinan</h4>
        </div>
    </div>
    <table class="table table-striped">
            <thead> 
                <tr>
                    <th scope="col" class="text-left"><span class="ml-3">Nama Kegiatan</span></th>
                    <th scope="col" class="text-left">Tanggal Mulai</th>
                    <th scope="col" class="text-left">Organisasi</th>
                    <th scope="col" class="text-left">Pemohon</th>
                    <th scope="col" class="text-center">Status</th>
                    <th scope="col"></th>
                </tr>
            </thead>
            <tbody id="app">
                <!-- <tr >
                    <th scope="row" class="text-left">Jazz Goes To Campus</th>
                    <td>20 Agustus 2019</td>
                    <td>BEM FEB UI</td>
                    <td>akhmad.diponegoro</td>
                    <td class="text-left"><span class="badge badge-pill badge-secondary">Menunggu <br> Persetujuan</span></td>
                    <td><a href="/izin-kegiatan/detail">Detail</a></td>
                </tr>
                <tr>
                    <th scope="row" class="text-left">Jazz Goes To Campus</th>
                    <td>20 Agustus 2019</td>
                    <td>BEM FEB UI</td>
                    <td>akhmad.diponegoro</td>
                    <td class="text-left"><span class="badge badge-pill badge-success">Disetujui</span></td>
                    <td><a href="/izin-kegiatan/detail">Detail</a></td>
                </tr>
                <tr>
                    <th scope="row" class="text-left">Jazz Goes To Campus</th>
                    <td>20 Agustus 2019</td>
                    <td>BEM FEB UI</td>
                    <td>akhmad.diponegoro</td>
                    <td class="text-left"><span class="badge badge-pill badge-danger">Ditolak</span></td>
                    <td><a href="/izin-kegiatan/detail">Detail</a></td>
                </tr> -->
                <tr v-for="izin_kegiatan in list_izin_kegiatan" v-bind:key="izin_kegiatan.id">
                    <th scope="row" class="text-left"><span class="ml-3">{{izin_kegiatan.nama_kegiatan}}</span></th>
                    <td>{{getDateDef(izin_kegiatan.detail_kegiatan.waktu_tanggal_mulai)}}</td>
                    <td>{{izin_kegiatan.organisasi}}</td>
                    <td>{{izin_kegiatan.user.username}}</td>
                    <td v-if="izin_kegiatan.status_perizinan_kegiatan==1" class="text-center"><span class="badge badge-pill badge-secondary">Menunggu<br>Persetujuan</span></td>
                    <td v-if="izin_kegiatan.status_perizinan_kegiatan==2" class="text-center"><span class="badge badge-pill badge-success">Disetujui</span></td>
                    <td v-if="izin_kegiatan.status_perizinan_kegiatan==3" class="text-center"><span class="badge badge-pill badge-danger">Ditolak</span></td>
                    <td><a :href="'izin-kegiatan/'+izin_kegiatan.id">Detail</a></td>
                </tr>
            </tbody>
    </table>
    </div>
</template>


<script>
import UserService from '../services/user.service';
import moment from 'moment';
export default {
    
    name: 'IzinKegiatan',
    data() {
        return {
            list_izin_kegiatan: [[]],
            error_message: "",
        }
    },
    methods: {
        getDateDef : function (date) {
            return moment(date, 'YYYY-MM-DDTHH:mm').format('D MMMM YYYY');
        },
    },
    created(){
         UserService.getAllIzinKegiatan().then(
            response => {
                this.list_izin_kegiatan = response.data;
                // console.log(this.list_izin_kegiatan)
            },
            error => {
                this.error_message = (error.response && error.response.data) || error.message || error.toString();
                // console.log(this.error_message)
            }
        )
    },
    mounted(){
        // console.log(this.list_izin_kegiatan);
        // console.log(this.error_message);
    },
}
</script>
<style>
.badge-secondary{
    background-color: #bdbdbd;
}
.badge-success{
    background-color: #27AE60;
}
.badge-danger{
    background-color: #EB5757;
}
.badge{
    font-weight: 500;
    
    padding-left: 20px;
    padding-right: 20px;
    font-size: 14px;
}
.judul{
    color: #FFD505;
}
*{
    font-weight: bold !important;
}

</style>