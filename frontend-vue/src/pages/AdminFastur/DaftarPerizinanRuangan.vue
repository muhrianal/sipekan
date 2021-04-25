<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page">Daftar Perizinan</h3>
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
                    <template v-for="perizinan in list_perizinan" v-bind:key="perizinan.id">
                        <tr v-if="perizinan.peminjaman_ruangan.length != 0">
                            <td class="nama-kegiatan">{{perizinan.nama_kegiatan}}</td>
                            <td>{{perizinan.organisasi}}</td>
                            <td>{{perizinan.user.profile.role}} a.n. {{perizinan.user.profile.nama}}</td>
                            <td><a href="/izin-kegiatan/detail">Detail</a></td>
                        </tr>
                    </template>
                </tbody>
            </table>
        </div>
    </div>
    {{list_perizinan}}
</template>


<script>
import UserService from '../../services/user.service';

export default{
    name: 'DaftarPerizinanRuangan',
    data(){
        return {
            list_perizinan : ''

        }
    },
    created(){
        UserService.getListPerizinanFastur().then(
            response => {
                this.list_perizinan = response.data
            },
            error => {
                console.log(error.message) // untuk sementara, nanti handle ini
            }
        )
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
}

.content-perizinan {
    margin: -16px -20px 0px -20px;
}
</style>