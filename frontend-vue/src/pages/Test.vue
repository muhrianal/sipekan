<template>
    <div>
        Test
    </div>
</template>

<script>
import UserService from '../services/user.service';
export default {
    name: 'EditRuangan',
    data() {
        return {
            ruangan: [],
            error_messase: "",
            jenis_ruang: "",
            nama: "",
            kapasitas: "",
            fasilitas: "",
            lokasi: "",
            informasi_tambahan: "",
            waktu_available_mulai: "",
            waktu_available_akhir: "",
            status:"",
        }
    },
    created(){
        console.log("masuk created daftar")
        UserService.getAllRuangan().then(
            response => {
                this.ruangan = response.data;
            },
            error => {
                this.error_message = (error.response && error.response.data) || error.message || error.toString();
            }
        )
    },
    mounted(){
        console.log(this.ruangan);
        console.log(this.error_message);
    },
    methods: {
        putEditRuangan() {
            console.log("masuk put ruangan")

            const data_put = {
                jenis_ruang: this.jenis_ruang,
                nama: this.nama,
                kapasitas: this.kapasitas,
                fasilitas: this.fasilitas,
                lokasi: this.lokasi,
                informasi_tambahan: this.informasi_tambahan,
                waktu_available_mulai: "2021-04-21T21:50:41+07:00",
                waktu_available_akhir: "2022-04-21T21:50:48+07:00",
                status: "1",
            };
            UserService.putRuangan(this.$route.params.id,data_put).then(
                response => {
                    console.log(response.data);
                },
                error => {
                    console.log(error.message);
                }
        );
        }
    }
}
</script>
