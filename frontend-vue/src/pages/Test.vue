<template>
    <div>
        Test
    </div>

    <button v-on:click="postCreateRuangan">Post API Ruangan</button>
</template>


<script>
import UserService from '../services/user.service';


export default {
    name: 'Test',
    data() {
        return {
            ruangan : [],
            error_message : "",

            nama : "1102",
            kapasitas : 100,
            lokasi : "Lokasi nya cuy",
            waktu_available_mulai : "2021-04-12T08:00:00",
            waktu_available_akhir : "2021-04-12T15:00:00",
            informasi_tambahan : "nothing",
            

        }
    },
    created(){
        console.log("masuk created")
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
        postCreateRuangan() {
            const detail_kegiatan_data =
            [
                            {
                waktu_tanggal_mulai : "XXX"
            }


            ]


            const header_kegiatan = {
                nama_kegiatan : "Pameran",
                detail_kegiatan : detail_kegiatan_data
                
            };

            UserService.postRuangan(header_kegiatan).then(
                response => {
                    console.log(response.data);
                },
                error => {
                    console.log(error.message);
                }
            );


        },

        // putEditRuangan(){
        //     UserService.putRuangan(5,)
        // }
    }

    

    
    
}
</script>
