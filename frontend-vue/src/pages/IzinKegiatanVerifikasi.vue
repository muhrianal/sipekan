<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page" style="font-weight: 500;">Verfikasi Perizinan Kegiatan</h3>
            <hr class="line-header">
        </div>

        <div class="formulir m-3">
            
            <form>
                <div class="form-row">
                    <div class="col-6 col-md-6 px-4">
                    <label class="status">Status Sekarang: <span class="status-span">Menunggu Persetujuan</span></label>
                    </div>
                    <div class="col-6 col-md-6 px-4 d-flex justify-content-end">
                    <label class="status">Dibuat:  17:00, 23 April 2020</label>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-6 col-md-6"></div>
                    <div class="col-6 col-md-6 px-4 d-flex justify-content-end">
                    <label class="status">Disunting:  17:00, 23 April 2020</label>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Nama Kegiatan:</label>
                        <input type="text" class="form-control" readonly>

                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Tempat Pelaksanaan:</label>
                        <input type="text" class="form-control" readonly>
                    </div>

                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Tanggal Mulai:</label>
                        <input type="text" class="form-control" readonly>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Tanggal Selesai:</label>
                        <input type="text" class="form-control" readonly>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Organisasi Penanggungjawab:</label>
                        <input type="text" class="form-control" readonly>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Ketua Organisasi:</label>
                        <input type="text" class="form-control" readonly>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>NPM Ketua Organisasi:</label>
                        <input type="text" class="form-control" readonly>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Nama PIC Kegiatan:</label>
                        <input type="text" class="form-control" readonly>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>NPM PIC:</label>
                        <input type="text" class="form-control" readonly>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Email PIC:</label>
                        <input type="text" class="form-control" readonly>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>HP PIC:</label>
                        <input type="text" class="form-control" readonly>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Sumber Pendanaan</label>
                        <input type="text" class="form-control" readonly>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label>Dokumen</label>
                        <input type="text" class="form-control" readonly>
                    </div>
                </div>

            </form>
        </div>
        <div class="d-flex" style="margin-top:100px">
                <div class="mr-auto">

                </div>
               <div class="p-2">
                    <a href="/ruangan" class="btn hapus" style="padding:3px 20px;font-size:16px;"> Hapus</a>
               </div>
              <div class="p-2 pr-4">
              <a href="/ruangan/ubah" class="btn ubah" style="padding:3px 20px;font-size:16px;"> Ubah</a>
              </div>
            </div>

    </div>
</template>

<script>

</script>

<style>
.status-span{
    color: #828282
}
.status {
    color: #BDBDBD
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
.line-header {
    background-color: #BDBDBD ;
}
.ubah {
    color: white;
    border-color: #FFD505;
    background-color: #FFD505 !important;
    border-radius: 10px !important;
}
.ubah:hover{
    background-color: #FFD505 !important;
    border-color: #FFD505;
    color: white;
}
.hapus {
    color: red;
    border-color: red;
    background-color: white!important;
    border-radius: 10px !important;
}
.hapus:hover {
    color: white;
    border-color: red;
    background-color: red!important;
}
input, select{
    border-radius: 10px !important;
}
</style>