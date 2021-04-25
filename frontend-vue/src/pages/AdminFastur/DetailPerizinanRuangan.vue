<template>
    <div>
        {{list_peminjaman}}
    </div>
</template>

<script>
import UserService from '../../services/user.service';


export default {
    name: 'DetailPerizinanRuangan',
    data(){
        return{
            id_izin_kegiatan: -1,
            list_peminjaman: []

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
    }
}
</script>