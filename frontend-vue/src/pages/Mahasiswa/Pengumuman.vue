<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page">Pengumuman</h3>
            <hr class="line-header">
        </div>
        
        <div class="container-fluid">

            <form>
                <div class="form-row">
                    <div class="col-12 col-md-8">
                        <br>
                        <div>          
                                <div class="input-group rounded">
                                    <input type="search" class="form-control rounded" placeholder="Search" aria-label="Search"
                                        aria-describedby="search-addon" />
                                    <span class="input-group-text border-0" id="search-addon">
                                        <i class="fas fa-search"></i>
                                    </span>
                                </div>
                            
                            <br>
                            <!-- Nanti for loop disini sesui length pengumuman -->
                            <div class="card w-100">
                                <div class="card-body">
                                    <h5 class="card-title">Judul</h5>
                                    <p class="card-text">isinya Lorem Ipsum apa yak gitu dah</p>
                                    <a href="#">link download file</a>
                                </div>
                            </div>
                            <br>
                            <div class="card w-100">
                                <div class="card-body">
                                    <h5 class="card-title">Judul</h5>
                                    <p class="card-text">isinya Lorem Ipsum apa yak gitu dah</p>
                                    <a href="#">link download file</a>
                                </div>
                            </div>
                            <br>
                            <div class="pagination">               
                                <ul class="pagination">
                                    <li class="page-item">
                                    <a class="page-link" href="#" aria-label="Previous">
                                        <span aria-hidden="true">&laquo;</span>
                                        <span class="sr-only">Previous</span>
                                    </a>
                                    </li>
                                    <li class="page-item"><a class="page-link" href="#">1</a></li>
                                    <li class="page-item"><a class="page-link" href="#">2</a></li>
                                    <li class="page-item">
                                    <a class="page-link" href="#" aria-label="Next">
                                        <span aria-hidden="true">&raquo;</span>
                                        <span class="sr-only">Next</span>
                                    </a>
                                    </li>
                                </ul>

                            </div>
                        </div>
                        

                    </div>
                   

                    <div class="col-12 col-md-4 border" id="kegiatanacc">
                        <div>
                            <h6 class="header-page2">Kegiatan Yang Akan Datang</h6>
                        
                        </div>
                        <br>
                        <div class="input-group rounded">
                            <input type="search" class="form-control rounded" placeholder="Search" aria-label="Search"
                                aria-describedby="search-addon" />
                            <span class="input-group-text border-0" id="search-addon">
                                <i class="fas fa-search"></i>
                            </span>
                        </div>
                        <br>
                        <div class="table-responsive overflow-auto" id="listkegiatan">
                            <table class="table table-striped table-sm table-bordered">
                            <tbody id="app" class="fsmall mt-2">
                                <tr v-for="(kegiatan) in kegiatan_disetujui" v-bind:key="kegiatan.id">
                                    <td>{{kegiatan.waktu}}</td>
                                    <td>{{ kegiatan.nama_kegiatan }}
                                        <p>{{ kegiatan.organisasi}} </p>

                                    </td>

                                </tr>
                            </tbody>
                            </table>
                        </div>
                        </div>
                    </div>    
               

                <br>
                <br>

            </form>
        </div>

    </div>
    
</template>

<script>
import UserService from "../../services/user.service";
import moment from 'moment';


export default {
		name: 'Pengumuman',
        
		data: function() {
		
        return {
            banyak_pengumuman: 1,
            kegiatan_disetujui: [[]],

            }
        },

        created(){
                UserService.getAllIzinKegiatan().then (

                response => {
                    var tmp = response.data;
                    for (let i = 0; i < tmp.length; i++){
                        if (tmp[i].status_perizinan_kegiatan == 2){
                            var tahun = tmp[i].detail_kegiatan.waktu_tanggal_mulai.slice(0,4);
                            var bulan = tmp[i].detail_kegiatan.waktu_tanggal_mulai.slice(5,7);
                            var tanggal = tmp[i].detail_kegiatan.waktu_tanggal_mulai.slice(8,10);

                            var namaBulan = {"01":"Jan", "02":"Feb", "03":"Mar", "04":"Apr", "05":"May", "06":"Jun", "07":"Jul", "08":"Aug",
                                            "09":"Sep", "10":"Oct", "11":"Nov", "12":"Dec"};
                                
                            
                            var waktu = tanggal + " " + namaBulan[bulan] + " " + tahun;
                            var nama_kegiatan = tmp[i].nama_kegiatan;
                            var organisasi = tmp[i].organisasi;
                            this.kegiatan_disetujui.push({nama_kegiatan, waktu, organisasi});                       
                        }
                    }
                    this.kegiatan_disetujui.shift();


                },
                error => {
                    this.error_message = (error.response && error.response.data) || error.message || error.toString();
                }
            );
        },

        method:{
            getDateDef : function (date) {
                return moment(date, 'YYYY-MM-DDTHH:mm').format('D MMMM YYYY');
            },

        },
        


    }
</script>

<style>
#app {
		font-family: 'Avenir', Helvetica, Arial, sans-serif;
		color: #2c3e50;
		height: 90vh;
		width: 70vw;
		margin-left: auto;
		margin-right: auto;
	}
.root-class {
    background-color: white;
    border-color: #BDBDBD;
    border-style: solid;
    border-width: 1px;
    border-radius: 5px;
    padding: 20px 0px 20px 20px ;
}


#kegiatanacc{
    height:500px;
}

#listkegiatan{
    height:350px;

}

.header-page {
    /* padding: 15px 0px 3px 15px; */
    font-size: 23px;
    color: #FFD505;
    font-weight: 550;
}

.header-page2 {
    /* padding: 15px 0px 3px 15px; */
    margin-top: 10px;
    font-size: 18px;
    color: #FFD505;
    font-weight: 550;
    text-align: center;
}

.line-header {
    background-color: #BDBDBD ;
}

.note-form{
    font-size: 12px;
}


.search-container {
    float: right;
}

input[type=text] {
    padding: 6px;
    margin-top: 8px;
    font-size: 15px;
    border-color: gainsboro;
    }

.search-container button {
    float: right;
    padding: 6px 10px;
    margin-top: 8px;
    margin-right: 16px;
    background: #ddd;
    font-size: 17px;
    border: none;
    cursor: pointer;
}

textarea{
    width:100%;
}

</style>