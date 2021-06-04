<template>
    <div class="root-class">
        <div class="header">
            <div class="row">
                <div class="col-12 col-md-4">
                    <h3 class="header-page" style="font-weight: bold;">Daftar Perizinan</h3>
                </div>
                <div class="col-12 col-md-4">
                    <div class="search-wrapper panel-heading col-sm-12">
                        <input class="form-control" type="text" v-model="searchQuery" placeholder="Search" />
                    </div>                        
                </div>
                <div class="col-12 col-md-4">
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
            <table class="table table-striped table-responsive-sm">
                <thead>
                    <tr>
                        <th scope="col">Nama Kegiatan</th>
                        <th scope="col">Organisasi</th>
                        <th scope="col">Pemohon</th>
                        <th scope="col"></th>
                    </tr>
                </thead>
                <tbody>
                    <template v-for="perizinan in resultQuery" >
                        <tr v-bind:key="perizinan.id" v-if="perizinan.perizinan_publikasi != null | perizinan.permintaan_souvenir.length != 0 | perizinan.permintaan_protokoler != null">
                            <td class="nama-kegiatan">{{perizinan.nama_kegiatan}}</td>
                            <td>{{perizinan.organisasi}}</td>
                            <td>{{perizinan.user.profile.role}}</td>
                            <td>
                                <a :href="'/perizinan-humas/' + perizinan.id">Detail</a>
                            </td>
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
            searchQuery: null

        };
    },
    computed: {
        resultQuery(){
            if(this.searchQuery){
                return this.list_perizinan_filtered.filter((item)=>{
                    return this.searchQuery.toLowerCase().split(' ').every(v => item.nama_kegiatan.toLowerCase().includes(v))
                })
            }else{
                return this.list_perizinan_filtered
            }
        }
    },
    created(){
        UserService.getListPerizinanHumas().then(
            response => {
                console.log(response.data) 
                this.list_perizinan= response.data
                this.list_perizinan_filtered = this.list_perizinan
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
                    let include_perizinan = false
                    if(this.list_perizinan[i].permintaan_protokoler != null){
                        if(this.list_perizinan[i].permintaan_protokoler.status_permintaan_protokoler == this.choice){
                            include_perizinan = true
                        }else{
                           include_perizinan = false;
                        }
                    }
                    if(!include_perizinan && this.list_perizinan[i].perizinan_publikasi != null){
                        let publikasi_found = this.filterPerizinanPublikasi(this.list_perizinan[i].perizinan_publikasi)
                        include_perizinan = publikasi_found
                    }
                    if(!include_perizinan && this.list_perizinan[i].permintaan_souvenir.length >0){
                        let souvenir_found = this.filterPermintaanSouvenir(this.list_perizinan[i].permintaan_souvenir)
                        include_perizinan = souvenir_found
                    }
                    if(include_perizinan){
                        this.list_perizinan_filtered.push(this.list_perizinan[i])
                    }
                }
            }
        },
        filterPerizinanPublikasi(perizinan_publikasi){
            let list_jenis_izin_publikasi = perizinan_publikasi.jenis_izin_publikasi;
            let found = false;
            let index = 0;
            while(!found && index<list_jenis_izin_publikasi.length){
                if(list_jenis_izin_publikasi[index].status_perizinan_publikasi == this.choice){
                    found = true;
                }else{
                    index +=1;
                }
            }
            return found;
        },
        filterPermintaanSouvenir(list_permintaan_souvenir){
            let found = false;
            let index = 0;
            while(!found && index<list_permintaan_souvenir.length){
                if(list_permintaan_souvenir[index].status_permintaan_souvenir == this.choice){
                    found = true;
                }else{
                    index+=1;
                }
            }
            return found;
        },

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