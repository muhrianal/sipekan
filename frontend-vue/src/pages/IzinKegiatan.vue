<template>
    <div class="card">
    <div class="d-flex">
        <div class="mr-auto p-3">
            <h4 class="judul p-1 align-middle mb-0" style="font-weight: 500;">Daftar Perizinan</h4>
        </div>
    </div>
    <table class="table table-striped">
        <div class="ml-3">
            <thead>
                <tr>
                    <th scope="col" class="text-left">Nama Kegiatan</th>
                    <th scope="col" class="text-left">Tanggal Mulai</th>
                    <th scope="col" class="text-left">Organisasi</th>
                    <th scope="col" class="text-left">Pemohon</th>
                    <th scope="col" class="text-left">Status</th>
                    <th scope="col"></th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th scope="row" class="text-left">Jazz Goes To Campus</th>
                    <td>20 Agustus 2019</td>
                    <td>BEM FEB UI</td>
                    <td>akhmad.diponegoro</td>
                    <td class="text-left"><span class="badge badge-pill badge-secondary">Menunggu <br> Persetujuan</span></td>
                    <td><a href="/izin-kegiatan/detail">Detail</a></td>
                </tr>
                <tr>
                    <th scope="row" class="text-left">Jazz Goes To Campus</th>
                    <td>20 Agustus 2019</td>
                    <td>BEM FEB UI</td>
                    <td>akhmad.diponegoro</td>
                    <td class="text-left"><span class="badge badge-pill badge-success">Disetujui</span></td>
                    <td><a href="/izin-kegiatan/detail">Detail</a></td>
                </tr>
                <tr>
                    <th scope="row" class="text-left">Jazz Goes To Campus</th>
                    <td>20 Agustus 2019</td>
                    <td>BEM FEB UI</td>
                    <td>akhmad.diponegoro</td>
                    <td class="text-left"><span class="badge badge-pill badge-danger">Ditolak</span></td>
                    <td><a href="/izin-kegiatan/detail">Detail</a></td>
                </tr>
            </tbody>
        </div>
    </table>
    </div>
</template>


<script>
</script>
<style>
.judul{
    color: #FFD505;
}
*{
    @import url('https://fonts.googleapis.com/css2?family=Mulish:wght@200&display=swap');
    font-family: 'Mulish', sans-serif;
}

tbody{
    font-weight: lighter;
}
th{
    font-weight: normal;
}
</style>