<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page" style="font-weight: 500;">Ubah Ruangan</h3>
            <hr class="line-header">
        </div>

        <div class="formulir m-3">
            <form>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Jenis Ruangan:</label>
                        <select class="form-control" id="exampleFormControlSelect1">
                            <option>Ruang Pertemuan</option>
                            <option>Ruang Kelas</option>
                            <option>Ruang Rapat</option>
                            <option>Selasar</option>
                        </select>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Fasilitas:</label>
                        <input type="text" class="form-control" placeholder="e.g. AC, proyektor, sound system, white board, sofa">
                    </div>

                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Nama Ruangan:</label>
                        <input type="text" class="form-control" placeholder="e.g. Auditorium">
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Keterangan:</label>
                        <input type="text" class="form-control" placeholder="e.g. Gedung Dekanat Lantai 1">
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Lokasi:</label>
                        <input type="text" class="form-control" placeholder="e.g. Kelas Administrasi Bisnis">
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Status:</label>
                        <select class="form-control" id="exampleFormControlSelect1">
                            <option value="1">Aktif</option>
                            <option value="2">Nonaktif</option>
                        </select>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Kapasitas:</label>
                        <input type="text" class="form-control" placeholder="e.g. Kelas Administrasi Bisnis">
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                    </div>
                </div>


            </form>
        </div>
        <div class="d-flex" style="margin-top:100px">
            <div class="mr-auto">

            </div>
            <div class="p-2">
                <a href="/ruangan/detail" class="btn batal" style="padding:3px 20px;font-size:16px;"> Batal</a>
            </div>
            <div class="p-2 pr-4">
                <a href="/ruangan" class="btn simpan" style="padding:3px 20px;font-size:16px;"> Simpan</a>
            </div>

            </div>

    </div>
</template>

<script>

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
.simpan {
    color: white;
    border-color: #27AE60;
    background-color: #27AE60 !important;
    border-radius: 10px !important;
}
.simpan:hover {
    color: #27AE60;
    border-color: #27AE60;
    background-color: white !important;
    border-radius: 10px !important;
}

.batal {
    color: red;
    border-color: red;
    background-color: white!important;
    border-radius: 10px !important;
}
.batal:hover {
    color: white;
    border-color: red;
    background-color: red!important;
}
input, select{
    border-radius: 10px !important;
}
</style>