<template>
    <div class="root-class">
        <div class="header">
            <div class="row">
                <div class="col-12 col-md-9">
                    <h3 class="header-page" style="font-weight: bold;">Daftar Perizinan</h3>
                </div>
                <div class="col-12 col-md-3">
                    <select class="form-control" v-model="choice" @change="filterPerizinan">
                        <option selected disabled value=-1>Pilih status</option>
                        <option value=-5>Semua</option>
                        <option value=1>Menunggu Persetujuan</option>
                        <option value=2>Disetujui</option>
                        <option value=3>Ditolak</option>
                    </select>
                </div>
            </div>
            <hr class="line-header line-title">
        </div>
        <div class="content-perizinan">
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th scope="col">Nama Kegiatan</th>
                        <th scope="col">Organisasi</th>
                        <th scope="col">Pemohon</th>
                        <th scope="col"></th>
                    </tr>
                </thead>
                <tbody>
                    <template v-for="perizinan in list_perizinan_filtered" >
                        <tr v-bind:key="perizinan.id" v-if="perizinan.peminjaman_ruangan.length != 0">
                            <td class="nama-kegiatan">{{perizinan.nama_kegiatan}}</td>
                            <td>{{perizinan.organisasi}}</td>
                            <td>{{perizinan.user.profile.role}} a.n. {{perizinan.user.profile.nama}}</td>
                            <td><a :href="'/perizinan-fastur/' + perizinan.id">Detail</a></td>
                        </tr>
                    </template>
                </tbody>
            </table>
        </div>
    </div>
    <!-- {{list_perizinan}} -->
</template>


<script>
import UserService from '../../services/user.service';

export default{
    name: 'DaftarPerizinanRuangan',
    data(){
        return {
            list_perizinan : [],
            choice : -1,
            list_perizinan_filtered : [],

        }
    },
    created(){
        UserService.getListPerizinanFastur().then(
            response => {
                this.list_perizinan = response.data
                this.list_perizinan_filtered = response.data
            },
            error => {
                console.log(error.message) // untuk sementara, nanti handle ini
            }
        )
    },
    methods: {
        filterPerizinan(){
            if (this.choice < 0) {
                this.list_perizinan_filtered = this.list_perizinan;
            }
            else {
                this.list_perizinan_filtered = []
                
                for (let i = 0; i < this.list_perizinan.length; i++){
                    for (let j = 0; j<this.list_perizinan[i].peminjaman_ruangan.length; j++){
                        if (this.list_perizinan[i].peminjaman_ruangan[j].status_peminjaman_ruangan == this.choice){
                            this.list_perizinan_filtered.push(this.list_perizinan[i]);
                            break;
                        }
                    }
                }

            }


        }
    }
}
</script>

<style>

tbody{
    font-weight:200;
}

th{
    font-weight: 500;
    /* padding-bottom: 100px; */
}


td{
    color: black;
}

.nama-kegiatan {
    font-weight: 300;
}

.root-class {
    background-color: white;
    border-color: #BDBDBD;
    border-style: solid;
    border-width: 1px;
    border-radius: 5px;
    padding: 20px 20px 20px 20px ;
}

.line-title{
    margin-right: -20px !important;
    margin-left: -20px !important;
}

.header-page {
    /* padding: 15px 0px 3px 15px; */
    font-size: 23px;
    color: #FFD505;
    font-weight: 550;
}

.line-header {
    background-color: #BDBDBD ;
    margin: 10px 0px 0px 0px;
}

.content-perizinan {
    margin: 0px -20px 0px -20px;
}
</style>