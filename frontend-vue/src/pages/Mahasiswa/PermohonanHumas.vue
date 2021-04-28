<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page">Buat Perizinan<span style="color:grey"> >> Humas</span></h3>
            <hr class="line-header">
        </div>
        
        <div class="formulir">
            <form>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputPublikasiLuarRuangan">Publkasi Luar Ruangan</label>
                        <hr noshade >
                        <!-- <input type="text" class="form-control" placeholder="e.g. Open House FEB UI" required> -->
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputPublikasi">Publikasi</label>
                         <hr noshade >
                        <!-- <input type="text" class="form-control" placeholder="e.g. Akademik FEB UI" required> -->
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputTanggalMulai">Tanggal Mulai:</label>
                        <input type="date" class="form-control" >                   
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2 ">
                        <label for="inputTanggalAkhir">Tanggal Akhir:</label>
                        <input type="date" class="form-control" >
                    </div>                        
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputMateriKegiatan">Materi Kegiatan / Press Release:<span class="text-keterangan">  (Dapat diunggah dalam format zip)</span> </label>
                        <input type="file" class="form-control-file">
                    </div>   
                      <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputFlyerPengumuman">Flyer Pengumuman / Poster Kegiatan:<span class="text-keterangan">  (jika ada)</span></label>
                        <input type="file" class="form-control-file">
                    </div>                       
                </div>

                 <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">            
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputKeterangan">Keterangan: <span class="text-keterangan">  (jika memilih jenis Lainnya, silahkan isi spesifikasi publikasi disini)</span></label>
                        <textarea type="text" class="form-control" placeholder="e.g. Baliho di Depan Gedung x ukuran (axb)"></textarea>
                    </div>                    
                </div>
                
                <div class="col-12col-md-6 px-4"> 
                    <label> Souvenir</label>
                     <hr>
                </div>  

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputNamaPenerima">Nama Penerima:</label>
                        <input type="text" class="form-control" placeholder="e.g. Akhmad">
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputJabatanPenerima">Jabatan Penerima:</label>
                        <input type="text" class="form-control" placeholder="e.g. Menteri" >
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputKelas">Kelas:</label>
                        <select class="form-control" id="exampleFormControlSelect1">
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                        </select>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputRegion">Region:</label>
                          <select class="form-control" id="exampleFormControlSelect1">
                            <option value="1">Dalam Negeri</option>
                            <option value="2">Luar Negeri</option>
                        </select>
                    </div>                    
                </div>

                 <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputPilihanSouvenir">Pilihan Souvenir:</label>
                        <!-- select -->
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputJumlah">Jumlah:</label>
                        <input type="number" class="form-control" placeholder="e.g. 1">
                    </div>                    
                </div>

                <div class="row-12 row-md-6  px-4 py-2"> 
                    <hr>
                    <div style="display: flex;justify-content: center;">
                        <button type="button" class="btn tambah-souvenir"> Tambah Souvenir </button>
                    </div>
                     <hr>
                </div>  

                <div class="col-12col-md-6 px-4"> 
                    <label> Protokoler</label>
                     <hr>
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">   
                        <label for="inputDeskripsiKebutuhan">Deskripsi Kebutuhan: <span class="text-keterangan" id="text-keterangan-small">  (contoh: nama penerima, jumlah pendamping dibutuhkan)</span></label>
                        <textarea type="text" class="form-control" placeholder="e.g. Menteri x, jumlah: 2"></textarea>         
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
input, textarea, select {
    border-radius: 10px !important;
}

.text-keterangan{
  font-size: x-small;
  color: gray
}
#text-keterangan-small{
    font-size: xx-small  !important;
}
hr{
    margin-top: 1px;
    margin-bottom: 3px;
}
.tambah-souvenir{
    margin-top: 4px;
    margin-bottom: 4px;
    font-size: 14px;
    border-radius: 10px !important;
    border-color: rgb(202, 202, 202);

}
</style>