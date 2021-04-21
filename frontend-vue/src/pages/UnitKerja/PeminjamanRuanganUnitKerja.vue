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
                        <input type="text" class="form-control" placeholder="e.g. Kelas Administrasi Bisnis">
                    </div>
                    <div class="col-12 col-md-6">
                        <label for="inputOrganisasi">Organisasi/Divisi*:</label>
                        <input type="number" class="form-control" placeholder="e.g. Akademik FEB UI">
                    </div>  
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6">
                        <label for="exampleFormControlSelect1">Waktu mulai*:</label>
                        <select class="form-control" id="exampleFormControlSelect1">
                            <template v-for="n in 23" v-bind:key="n">
                                <template v-for="m in 2" v-bind:key="m">
                                    <template v-if="n < 10">
                                        <option v-if="m == 1">0{{n}}:00</option>
                                        <option v-if="m == 2">0{{n}}:30</option>
                                    </template>
                                    <template v-else>
                                        <option v-if="m == 1">{{n}}:00</option>
                                        <option v-if="m == 2">{{n}}:30</option>
                                    </template>
                                </template>
                            </template>
                            

                        </select>
                    </div>
                    <div class="col-12 col-md-6">
                        <label for="exampleFormControlSelect1">Waktu akhir*:</label>
                            <select class="form-control" id="exampleFormControlSelect1">
                            <option>1</option>
                            <option>2</option>
                            <option>3</option>
                            <option>4</option>
                            <option>5</option>
                        </select>

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
            selectHours : [
                '00:00',
                '00:30',
                '01:00',
                '01:30',
                '02:00',
                '02:30',
                '03:00',
                '03:30',
                '04:00',
                '04:30',
                '05:00',
                '05:30',
                '06:00',
                '06:30',
                '07:00',
                '07:30',
            ]
        } 
    }
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
</style>