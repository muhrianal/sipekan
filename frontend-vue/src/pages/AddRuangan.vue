<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page" style="font-weight: 500;">Tambah Ruangan</h3>
            <hr class="line-header">
        </div>

        <div class="formulir m-3">
            <form>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputJenisRuangan">Jenis Ruangan<label style="color:red">*</label>:</label>
                        <select class="form-control" id="jenis_ruang" v-model="jenis_ruang">
                            <option value="1">Ruang Pertemuan</option>
                            <option value="2">Ruang Kelas</option>
                            <option value="3">Ruang Rapat</option>
                            <option value="4">Selasar</option>
                        </select>
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputFasilitas">Fasilitas<label>:</label></label>
                        <input type="text" class="form-control" id="fasilitas" placeholder="e.g. AC, proyektor, sound system, white board, sofa"
                        v-model="fasilitas">
                    </div>
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputNamaRuangan">Nama Ruangan<label style="color:red">*</label>:</label>
                        <input name="fname" type="text" class="form-control" id="nama" placeholder="e.g. Auditorium" v-model="nama">
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputKapasitas">Kapasitas<label style="color:red">*</label>:</label>
                        <input type="number" class="form-control" id="kapasitas" placeholder="e.g. 350" v-model="kapasitas">
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputLokasi">Lokasi<label style="color:red">*</label>:</label>
                        <input type="text" class="form-control" id="lokasi" placeholder="e.g. Gedung Dekanat Lantai 1" v-model="lokasi">
                    </div>
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputKeterangan">Informasi Tambahan<label>:</label></label>
                        <input type="text" class="form-control" placeholder="peminjaman ruangan maksimal dilakukan h-3 kegiatan"
                        v-model="informasi_tambahan">
                    </div>
                </div>
                <div class="form-row d-flex">
                    <div class="col-12 col-md-3 px-4 py-2">
                        <label for="input">Waktu Tersedia Mulai<label style="color:red">*</label>:</label>
                        <select class="form-control"  id="waktu_available_mulai" v-model="waktu_available_mulai">
                            <option value="" selected disabled>Pilih...</option>
                            <template v-for="option in option_waktu" v-bind:key="option">
                                <option v-bind:value="option.value">{{option.text}}</option>
                            </template>
                        </select>
                    </div>
                    <div class="col-12 col-md-3 px-4 py-2">
                        <label for="input">Waktu Tersedia Akhir<label style="color:red">*</label>:</label>
                            <select class="form-control" id="waktu_available_akhir"  v-model="waktu_available_akhir">
                                <option selected disabled value="">Pilih...</option>
                                    <template v-for="option in option_waktu" v-bind:key="option">
                                        <option v-bind:value="option.value">{{option.text}}
                                </option>
                                    </template>
                            </select>
                    </div>

                </div>

        </form>
                        <div class="d-flex" style="margin-top:100px">
                            <div class="mr-auto"> </div>
                                <div class="p-2">
                                    <a href="/ruangan" class="btn batal" style="padding:3px 20px;font-size:16px;"> Batal</a>
                                </div>
                            <div class="p-2 pr-4">

                                <button class="btn simpan" id="btnValidate" style="padding:3px 20px;font-size:16px;"
                                        v-on:click="postCreateRuangan"
                                        > Simpan</button>
                            </div>
                        </div>

<!-- Modal -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Berhasil</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        Ruangan Berhasil Disimpan
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary batal" data-dismiss="modal">Close</button>
        <button type="button" class="btn simpan">Ok</button>
      </div>
    </div>
  </div>
</div>

        </div>


        </div>

</template>

<script>
import UserService from '../services/user.service';
export default {
    name: 'AddRuangan',
    data() {
        return {
            ruangan: [],
            error_messase: "",
            option_waktu : [],
        }
    },
    created(){
        console.log("masuk created daftar")
        UserService.getAllRuangan().then(
            response => {
                this.ruangan = response.data;
            },
            error => {
                this.error_message = (error.response && error.response.data) || error.message || error.toString();
            }
        )
    },
    mounted(){
        console.log(this.ruangan);
        console.log(this.error_message);
                let option_waktu_made = [];
                    let i;
                    for (i = 0; i < 24; i++){
                        if (i < 10 ){
                            option_waktu_made.push({
                                value: "2021-01-01T0" + i + ":00" +":00+07:00",
                                text: "0" + i + ":00"
                            });
                            option_waktu_made.push({
                                value: "2021-01-01T0" + i + ":30" +":00+07:00",
                                text: "0" + i + ":30"
                            });
                        } else {
                            option_waktu_made.push({
                                value: "2021-01-01T" + i + ":00" +":00+07:00",
                                text:  i + ":00"
                            });
                            option_waktu_made.push({
                                value: "2021-01-01T" + i + ":30" +":00+07:00",
                                text: i + ":30"
                            });
                        }
                    }
                    this.option_waktu = option_waktu_made;
    },
    methods: {
        postCreateRuangan() {
            console.log("masuk post ruangan")
            console.log(this.waktu_available_akhir)

            const data_post = {
                jenis_ruang: this.jenis_ruang,
                nama: this.nama,
                kapasitas: this.kapasitas,
                fasilitas: this.fasilitas,
                lokasi: this.lokasi,
                informasi_tambahan: this.informasi_tambahan,
                waktu_available_mulai: this.waktu_available_mulai,
                waktu_available_akhir: this.waktu_available_akhir,
                status: 1,
            };
            console.log(data_post);
            UserService.postRuangan(data_post).then(
                response => {
                    console.log(response.data);
                    $('#myModal').modal('toggle')
                },
                error => {
                    alert("Bagian berbintang harus diisi");
                    window.location.href='/ruangan/add';
                }
        );
        },

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
}
.line-header {
    background-color: #BDBDBD ;
}
input, select{
    border-radius: 10px !important;
}
</style>