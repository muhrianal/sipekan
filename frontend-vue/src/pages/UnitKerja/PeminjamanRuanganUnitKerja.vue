<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page">Buat Perizinan Ruangan</h3>
            <hr class="line-header">
        </div>
        
        <div class="formulir">
            <form>
                <div class="form-row">
                    <div class="col-12 col-md-6">
                        <label for="inputNamaKegiatan">Nama Kegiatan*:</label>
                        <input type="text" class="form-control" placeholder="e.g. Kelas Administrasi Bisnis">
                    </div>
                    <div class="col-12 col-md-6">
                        <label for="inputOrganisasi">Organisasi/Divisi*:</label>
                        <input type="text" class="form-control" placeholder="e.g. Akademik FEB UI">
                    </div>
                    
                </div>
                <hr class="line-header">
                <div class="form-row">
                    <div class="col-12 col-md-6">
                        <label for="inputNamaKegiatan">Nama Subkegiatan*:</label>
                        <input type="text" class="form-control" placeholder="e.g. Administrasi Bisnis - B">
                    </div>
                    <div class="col-12 col-md-6">
                        <label for="inputOrganisasi">Jumlah Peserta*:</label>
                        <input type="number" class="form-control" placeholder="e.g. 120">
                    </div>  
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6">
                        <label for="exampleFormControlSelect1">Waktu mulai*:</label>
                        <select class="form-control" id="exampleFormControlSelect1" v-model="waktu_mulai">
                            <option selected disabled value="">Pilih...</option>
                            <template v-for="n in 24" v-bind:key="n">
                                <template v-for="m in 2" v-bind:key="m">
                                    <template v-if="n < 11">
                                        <option v-if="m == 1">0{{n-1}}:00</option>
                                        <option v-if="m == 2">0{{n-1}}:30</option>
                                    </template>
                                    <template v-else>
                                        <option v-if="m == 1">{{n-1}}:00</option>
                                        <option v-if="m == 2">{{n-1}}:30</option>
                                    </template>
                                </template>
                            </template>
                        </select>
                    </div>
                    <div class="col-12 col-md-6">
                        <label for="exampleFormControlSelect1">Waktu akhir*:</label>
                        <select class="form-control" id="exampleFormControlSelect1" v-model="waktu_akhir">
                            <option selected disabled value="">Pilih...</option>
                            <template v-for="n in 24" v-bind:key="n">
                                <template v-for="m in 2" v-bind:key="m">
                                    <template v-if="n < 11">
                                        <option v-if="m == 1">0{{n-1}}:00</option>
                                        <option v-if="m == 2">0{{n-1}}:30</option>
                                    </template>
                                    <template v-else>
                                        <option v-if="m == 1">{{n-1}}:00</option>
                                        <option v-if="m == 2">{{n-1}}:30</option>
                                    </template>
                                </template>
                            </template>
                        </select>
                    </div>  
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6">
                        <label for="exampleFormControlSelect1">Ruangan*:</label>
                        <select class="form-control" id="exampleFormControlSelect1" v-model="ruangan">
                            <option selected disabled value="">Pilih...</option>
                            <option>Ruangan A</option>
                        </select>
                        <p class="note-ruangan note-form text-right">Lihat daftar ruangan disini</p>
                        <label for="exampleFormControlSelect1">Perulangan*:</label>
                        <select class="form-control" id="exampleFormControlSelect1" v-model="perulangan">
                            <option selected disabled value="">Pilih...</option>
                            <option>Sekali Pakai</option>
                            <option>Harian</option>
                            <option>Mingguan</option>
                            <option>Bulanan</option>
                        </select>

                    </div>

                    <div class="col-12 col-md-6">
                        <label for="exampleFormControlTextarea1">Keterangan:</label>
                        <textarea class="form-control" id="exampleFormControlTextarea1" rows="4" v-model="keterangan" placeholder="e.g. Fasilitas yang akan digunakan"></textarea>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6">
                        <label for="inputNamaKegiatan">Tanggal Mulai Pelaksanaan*:</label>
                        <input type="date" class="form-control">
                    </div>
                    <div class="col-12 col-md-6">
                        <label for="inputOrganisasi">Tanggal Akhir Pelaksanaan*:</label>
                        <input type="date" class="form-control">
                        <p class="note-form">isi dengan tanggal yang sama dengan tanggal mulai pelaksanaan jika memilih "sekali pakai"</p>
                    </div>  
                </div>
            </form>
        </div>

    </div>
</template>

<script>
export default {
    name: 'PeminjamanRuanganUnitKerja',
    data() {
        return {
            waktu_mulai : '',
            waktu_akhir : '',
            ruangan : '',
            perulangan : '',
            keterangan : '',

        } 
    },
    
}
</script>

<style>
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

.line-header {
    background-color: #BDBDBD ;
}

.note-form{
    font-size: 12px;
}

.note-ruangan{
    margin-bottom: -16px;
}
</style>