<template>
    <div class="card">
    <div class="d-flex">
        <div class="mr-auto p-3">
            <h4 class="judul p-1 align-middle" style="font-weight: 500;">Daftar Ruangan</h4>
        </div>
      <div class="p-3">
          <a href="/ruangan/add" class="btn tambah" style="padding:3px 6px;font-size:14px;"> Tambah Ruangan</a>
      </div>
    </div>
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col" class="text-center" > No.</th>
          <th scope="col" class="text-center">Nama Ruangan</th>
          <th scope="col" class="text-center">Jenis Ruangan</th>
          <th scope="col" class="text-center">Lokasi</th>
          <th scope="col" class="text-center">Kapasitas</th>
          <th scope="col"></th>

        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row" class="text-center" >1.</th>
          <td>Auditorium</td>
          <td>Ruang Pertemuan</td>
          <td>Gedung Dekanat Lantai 1</td>
          <td class="text-center">350</td>
          <td><a href="/ruangan/detail">Detail</a></td>
        </tr>
        <tr>
            <th scope="row" class="text-center">2.</th>
            <td>Aula Student Center</td>
            <td>Ruang Pertemuan</td>
            <td>Gedung Student Center Lantai 2</td>
            <td class="text-center">170</td>
            <td><a href="/">Detail</a></td>
        </tr>
        <tr>
            <th scope="row" class="text-center">3.</th>
            <td>B. 301</td>
            <td>Ruang Kelas</td>
            <td>Gedung Soenaryo Kolopaking Lantai 1</td>
            <td class="text-center">40</td>
            <td><a href="/">Detail</a></td>
        </tr>
      </tbody>
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
h4{
    margin-bottom:0px;
}
.tambah {
    color: #FFD505;
    border-color: #FFD505;
    border-width: 2px;
}
th{
    font-weight: normal;
}
.tambah:hover{
    background-color: #FFD505 !important;
    border-color: #FFD505;
    color: white;
}
</style>