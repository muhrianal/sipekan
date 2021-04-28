<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page">Buat Perizinan<span style="color:grey"> >> Kegiatan</span></h3>
            <hr class="line-header">
        </div>
        
        <div class="formulir">
            <form>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputNamaKegiatan">Nama Kegiatan<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. Open House FEB UI" required>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputTempatPelaksanaan">Tempat Pelaksanaan<span class="text-danger">*</span>: <span class="text-keterangan">  (jika kegiatan online, isi: "Online")</span></label>
                        <input type="text" class="form-control" placeholder="e.g. Akademik FEB UI" required>
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputTanggalMulai">Tanggal Mulai<span class="text-danger">*</span>:</label>
                        <div class="form-row">
                          <div class="col-8 md 4">
                             <input type="date" class="form-control" required>
                          </div>
                          <div class="col-4 md 2">
                             <input type="time" class="form-control" required>
                          </div>
                        </div>  
                    </div>

                    <div class="col-12 col-md-6  px-4 py-2 ">
                        <label for="inputTanggalAkhir">Tanggal Akhir<span class="text-danger">*</span>:</label>
                        <div class="form-row">
                          <div class="col-8 md 4">
                             <input type="date" class="form-control" required>
                          </div>
                          <div class="col-4 md 2">
                             <input type="time" class="form-control" required>
                          </div>
                        </div>  
                    </div>  
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputOrganisasi">Organisasi Penanggungjawab<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. FEB UI" required>
                    </div>                         
                </div>

                 <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputKetuaOrganisasi">Nama Ketua Organisasi<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. Yobelio" required>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputNpmKetuaOrganisasi">NPM Ketua Organisasi<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. 1806123456" required>
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputPicKegiatan">Nama PIC Kegiatan<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. Akhmad" required>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputNpmPic">NPM PIC<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. 1806123456" required>
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputEmailPic">Email PIC<span class="text-danger">*</span>:</label>
                        <input type="email" class="form-control" placeholder="e.g. akhmad@ui.ac.id" required>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputHpPic">HP PIC<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. 08151234567" required>
                    </div>                    
                </div>

                 <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputSumberPendanaan">Sumber Pendanaan<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. Sponsor" required>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputUploadDokumen">Upload Dokumen<span class="text-danger">*</span>:<span class="text-keterangan">  (contoh: TOR-JGTC.pdf; Dokumen-JGTC.zip)</span></label>
                        <input type="file" class="form-control-file" required>
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputButuhHumas">Apakah anda memerlukan humas?<span class="text-keterangan">  (Publikasi, Souvenir, Protokoler)</span></label>
                        <br><input type="checkbox" value ="humas" id="humas"> <label>Ya</label>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputButuhRuangn">Apakah anda memerlukan ruangan?</label>
                        <br><input type="checkbox" value ="ruangan" id="ruangan"> <label>Ya</label>
                    </div>                    
                </div>
            </form>
            <div class="d-flex" style="margin-top:10px">
            <div class="mr-auto"> </div>
            <div class="p-2">
                    <button type="button" class="btn btn-outline-danger" id="button-batal">Batal</button>
                <!-- <a href="/" class="btn btn-outline-danger" id="button-batal" style="padding:3px 20px;font-size:16px;"> Batal</a> -->
            </div>
            <div class="p-2 pr-4">
                    <button type="button" class="btn btn-success" id="button-setuju">Simpan</button>
                <!-- <a class="btn simpan" style="padding:3px 20px;font-size:16px;"> Simpan</a> -->
            </div>
        </div>
        </div>

    </div>
</template>

<script>
// export default {
//     name: 'PeminjamanRuanganUnitKerja',
//     data() {
//         return {
//             selectHours : [
//             ]
//         } 
//     }
// }
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
input {
    border-radius: 10px !important;
}
.form-control-file{
    border-radius: 0px !important;
}
.text-keterangan{
  font-size: x-small;
  color: gray
}
</style>