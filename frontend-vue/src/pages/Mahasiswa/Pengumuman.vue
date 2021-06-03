<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page">Pengumuman</h3>
            <hr class="line-header">
        </div>
        
        <div class="formulir">
            <form>
                <div class="form-row">
                    <div class="col-12 col-md-8">
                        <br>
                        <div>
                            <div>
                                <div class="form-row">
                                    <div class="search-container">
                                        <form action="">
                                        <input type="text" placeholder="Search.." name="search">
                                        <button type="submit"><i class="fa fa-search"></i></button>
                                        </form>
                                    </div>
                                </div>
                            </div>
                            <br>
                            <div>
                                <textarea />
                            </div>
                        </div>
                        

                    </div>
                   
                    <div class="col-12 col-md-4 overflow-auto">
                        <div>
                            <h6 class="header-page2">Kegiatan Yang Akan Datang</h6>
                            <hr class="line-header">
                        </div>
                        <br>
                        <div class="search-container">
                            <form action="">
                            <input type="text" placeholder="Search.." name="search">
                            <button type="submit"><i class="fa fa-search"></i></button>
                            </form>
                        </div>
                        <div class="table-responsive">
                            <table class="table table-striped">
                            <thead>
                                <tr>
                                <th scope="col" class="text-center" > Tanggal</th>
                                <th scope="col" class="text-center">Kegiatan</th>
                                </tr>
                            </thead>
                            <tbody id="app">
                                <tr v-for="(kegiatan) in kegiatan_disetujui" v-bind:key="kegiatan.id">
                                    <th scope="row" class="text-center" >{{ index+1+"." }} </th>
                                    <td>{{ kegiatan.waktu_mulai }}</td>
                                    <!-- keterangan waktu gaada di model kegiatan, adanya di detail tapi kayaknya masih belum bisa ditembak API ya? -->
                                    <td>{{ kegiatan.nama_kegiatan }}</td>
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

export default {
		name: 'Pengumuman',
        
		data: function() {
		
        return {
            kegiatan_disetujui: [],
            }
        },

        created(){
                UserService.getAllPerizinan().then (
                response => {
                    var tmp = response.data;
                    for (let i = 0; i < tmp.length; i++){
                        if (tmp[i].status_perizinan_kegiatan == 2){
                            this.kegiatan_disetujui.push(tmp[i]);
                            console.log(tmp[i]);                        
                        }
                    }

                },
                error => {
                    this.error_message = (error.response && error.response.data) || error.message || error.toString();
                }
            );
        }

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
    padding: 20px 20px 20px 20px ;
}

label {
    font-size: 14px;
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