<template>
    <div class="card fmed"  style="min-height:600%;">
    <div class="d-flex">
        <div class="mr-auto p-3">
            <h4 class="judul p-1 align-middle" style="font-weight: 500;">Daftar Perizinan</h4>
        </div>
      <div class="p-3">
          <a href="/ruangan/add" class="btn tambah" style="padding:3px 6px;font-size:14px;"> Tambah Perizinan</a>
      </div>
    </div>
    <hr class="line-header" style="margin:0px;">

    <div style="margin:1% 7%;">
    <div class="table-responsive">
    <table class="table table-sm table-bordered" style="border-radius: 10px 10px 0px 0px;">
      <thead class="thead kuning rounded-top" style="border-radius: 10px 10px 0px 0px;">
        <tr style="border-radius: 10px;">
          <th scope="col" colspan="2" class="text-center" style="border-radius: 5px 5px 0px 0px;">Informasi Kegiatan</th>
        </tr>
      </thead>
      <tbody class="fsmall">
        <tr>
          <td>Nama Kegiatan</td>
          <td style="min-height=50%">{{ perizinan.nama_kegiatan }}</td>
        </tr>
        <tr>
          <td>Organisasi Penanggungjawab</td>
          <td>{{ perizinan.organisasi}}</td>
        </tr>
        <template v-if="perizinan.detail_kegiatan!=null">
        <tr>
          <td>Nama PIC Kegiatan</td>
          <td>{{ perizinan.detail_kegiatan.nama_pic }}</td>
        </tr>
        </template>
        <tr>
          <td>Status</td>
          <td v-if="perizinan.status_perizinan_kegiatan==1">Menunggu Persetujuan</td>
          <td v-if="perizinan.status_perizinan_kegiatan==2">Disetujui</td>
          <td v-if="perizinan.status_perizinan_kegiatan==3">Ditolak <a data-toggle="modal" data-target="#popup-izin-kegiatan">edit</a>
          </td>
          <!-- Modal: Popup Edit izin_kegiatan -->
                  <template v-if="perizinan.detail_kegiatan!=null">
                <div class="modal fade bd-example-modal-lg" id="popup-izin-kegiatan" tabindex="-1" role="dialog" aria-labelledby="popup-protokoler" aria-hidden="true">
                    <div class="modal-dialog modal-lg" role="document">
                        <div class="modal-content">
                        <form>
                        <div class="form-row">
                    <div class="col-12 col-md-6 px-4 py-2">
                        <label for="inputNamaKegiatan">Nama Kegiatan<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. Open House FEB UI" required :value="perizinan.nama_kegiatan"
                        @input="nama_kegiatan = $event.target.value">
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputTempatPelaksanaan">Tempat Pelaksanaan<span class="text-danger">*</span>: <span class="text-keterangan">  (jika kegiatan online, isi: "Online")</span></label>
                        <template v-if="perizinan.detail_kegiatan!=null">

                        <input type="text" class="form-control" placeholder="e.g. FEB UI"  :value="perizinan.detail_kegiatan.tempat_pelaksanaan" @input="tempat_pelaksanaan = $event.target.value" required>
                        </template>

                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputTanggalMulai">Tanggal Mulai<span class="text-danger">*</span>:</label>
                        <input type=datetime-local class=form-control    v-model="waktu_tanggal_mulai"  required>
                    </div>

                    <div class="col-12 col-md-6  px-4 py-2 ">
                        <label for="inputTanggalAkhir">Tanggal Akhir<span class="text-danger">*</span>:</label>
                        <input type=datetime-local class=form-control v-model="waktu_tanggal_akhir" required>
                    </div>  
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputOrganisasi">Organisasi Penanggungjawab<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. BEM FEB UI"  :value="perizinan.organisasi" @input="organisasi= $event.target.value" required>
                    </div>                         
                </div>

                 <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputKetuaOrganisasi">Nama Ketua Organisasi<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. Yobelio"  :value="perizinan.detail_kegiatan.nama_ketua_organisasi" @input="nama_ketua_organisasi= $event.target.value" required>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputNpmKetuaOrganisasi">NPM Ketua Organisasi<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. 1806123456" :value="perizinan.detail_kegiatan.npm_ketua_organisasi" @input="npm_ketua_organisasi= $event.target.value"  required>
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputPicKegiatan">Nama PIC Kegiatan<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. Akhmad"  :value="perizinan.detail_kegiatan.nama_pic" @input="nama_pic = $event.target.value" required> 
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputNpmPic">NPM PIC<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. 1806123456" :value="perizinan.detail_kegiatan.npm_pic" @input="npm_pic = $event.target.value"  required>
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputEmailPic">Email PIC<span class="text-danger">*</span>:</label>
                        <input type="email" class="form-control" placeholder="e.g. akhmad@ui.ac.id" :value="perizinan.detail_kegiatan.email_pic" @input="email_pic = $event.target.value" required>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputHpPic">HP PIC<span class="text-danger">*</span>:</label>
                        <input type="text" pattern="^[0-9]+$" class="form-control" placeholder="e.g. 08151234567" :value="perizinan.detail_kegiatan.hp_pic" @input="hp_pic = $event.target.value"  required>
                    </div>                    
                </div>

                 <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputSumberPendanaan">Sumber Pendanaan<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. Sponsor"  :value="perizinan.detail_kegiatan.sumber_pendanaan" @input="sumber_pendanaan= $event.target.value" required>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputUploadDokumen">Upload Dokumen<span class="text-danger">*</span>:<span class="text-keterangan">  (contoh: TOR-JGTC.pdf; Dokumen-JGTC.zip)</span></label>
                        <input id="file_info" class="form-control-file" type="file" ref="file" @change="onFileChange" required>
                        <p v-if="this.file_info_kegiatan !=null" class="text-right note-form" @Click="deleteFileInfo()">Hapus File</p>
                    </div>                    
                </div>

                        </form>
                        <div class="modal-footer">
                                <div class="text-center">
                                    <button class="btn btn-outline-secondary" data-dismiss="modal" style="width:80px; height:36px;">Batal</button>
                                </div>
                                <div class="text-center">
                                    <button class="btn btn-success" type="submit" style="width:80px; height:36px;" v-on:click="editIzinKegiatan(perizinan.id);editDetailIzinKegiatan(perizinan.detail_kegiatan.id)">Simpan {{perizinan.id}}</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                </template>
        </tr>
      </tbody>
    </table>
    </div>
    </div>

    <div style="margin:1% 7%;">
        <div class="table-responsive">
        <table class="table table-sm table-bordered" style="border-radius: 10px 10px 0px 0px;">
          <thead class="thead kuning rounded-top" style="border-radius: 10px 10px 0px 0px;">
            <tr style="border-radius: 10px;">
              <th scope="col" colspan="6" class="text-center" style="border-radius: 5px 5px 0px 0px;">Informasi Peminjaman Ruangan</th>
            </tr>
          </thead>
          <tbody class="fsmall">
            <tr>
              <td class="text-center abu2">Nama Kegiatan</td>
              <td class="text-center abu2">Nama Ruang</td>
              <td class="text-center abu2">Tanggal</td>
              <td class="text-center abu2">Waktu</td>
              <td class="text-center abu2">Pengulangan</td>
              <td class="text-center abu2">Status</td>
            </tr>
            <template v-for="pinjam in perizinan.peminjaman_ruangan" v-bind:key="pinjam.id"> 
            <tr>
              <td class="text-center">{{pinjam.judul_peminjaman}} </td>
              <td class="text-center">{{pinjam.ruangan}}</td>
              <template v-if="pinjam.perulangan!=null">
              <td class="text-center">{{getDateDef(pinjam.perulangan.tanggal_mulai)}}</td>
              </template>

              <td class="text-center">{{getHour(pinjam.waktu_mulai)}} - {{getHour(pinjam.waktu_akhir)}}</td>                
              

              <template v-if="pinjam.perulangan!=null">
                <template v-if="pinjam.perulangan.jenjang==1">
                <td class="text-center" > Sekali Pakai </td>
                </template>
                <template  v-if="pinjam.perulangan.jenjang==2">
                <td class="text-center"> Harian </td>
                </template>
                <template  v-if="pinjam.perulangan.jenjang==3">
                <td class="text-center"> Mingguan </td>
                </template>
                <template v-if="pinjam.perulangan.jenjang==4">
                <td class="text-center"> Bulanan </td>  
                </template>             
              </template>
              <template v-if="pinjam.perulangan==null">
                <td class="text-center"> - </td>
              </template>
              <td class="text-center" v-if="pinjam.status_peminjaman_ruangan==1">Menunggu Persetujuan</td>
              <td class="text-center" v-if="pinjam.status_peminjaman_ruangan==2">Disetujui</td>
              <td class="text-center" v-if="pinjam.status_peminjaman_ruangan==3">Ditolak <button  data-toggle="modal" data-target="#popup-peminjaman-ruangan" >edit</button>
              <!-- Modal: Popup Edit Peminjaman Ruangan -->
              <div class="modal fade" id="popup-peminjaman-ruangan" tabindex="-1" role="dialog" aria-labelledby="popup-penolakan" aria-hidden="true" :no-enforce-focus="true">
                    <div class="modal-dialog modal-dialog-centered" role="document">
                        <div class="modal-content">
                      <form>             
                
                      <div class="form-row">
                          <div class="col-12 col-md-6 px-4 py-2">
                              <label for="inputSubkegiatan">Nama Subkegiatan<span class="asterisk">*</span></label>
                              <input type="text" class="form-control" placeholder="e.g. Administrasi Bisnis - B"  v-model="judul_peminjaman">
                          </div>
                          <div class="col-12 col-md-6 px-4 py-2">
                              <label for="inputJumlahPeserta">Jumlah Peserta<span class="asterisk">*</span></label>
                              <input type="number" class="form-control" placeholder="e.g. 120" v-model="jumlah_peserta">
                          </div>  
                      </div>
                      <div class="form-row">
                          <div class="col-12 col-md-6 px-4 py-2">
                              <label for="waktuMulaiPeminjaman">Waktu mulai<span class="asterisk">*</span></label>
                              <select class="form-control" id="waktuMulaiPeminjaman" v-model="waktu_mulai">
                                  <option selected disabled value="">Pilih...</option>
                                  <option v-for="option in option_waktu" v-bind:key="option" v-bind:value="option.value">{{option.text}}</option>
                              </select>
                          </div>
                          <div class="col-12 col-md-6 px-4 py-2">
                              <label for="waktuAkhirPeminjaman">Waktu akhir<span class="asterisk">*</span></label>
                              <select class="form-control" id="waktuAkhirPeminjaman" v-model="waktu_akhir">
                                  <option selected disabled value="">Pilih...</option>
                                  <option v-for="option in option_waktu" v-bind:key="option" v-bind:value="option.value">{{option.text}}</option>
                              </select>
                          </div>  
                      </div>
                      <div class="form-row">
                          <div class="col-12 col-md-6 px-4 py-2">
                              <label for="ruangan">Ruangan<span class="asterisk">*</span></label>
                              <select class="form-control" id="daftar-ruangan" v-model="ruangan">
                                  <option selected disabled value="">Pilih...</option>
                                  <option v-for="pilihan_ruangan in list_ruangan" v-bind:key="pilihan_ruangan.id" :value="pilihan_ruangan.id">{{pilihan_ruangan.nama}}</option>
                              </select>
                              <p class="note-ruangan note-form text-right">Lihat daftar ruangan <a href="#">disini</a> </p>
                              <label for="perulangan">Perulangan<span class="asterisk">*</span></label>
                              <select class="form-control" id="perulangan" v-model="jenjang">
                                  <option selected disabled value="">Pilih...</option>
                                  <option value=1>SEKALI PAKAI</option>
                                  <option value=2>HARIAN</option>
                                  <option value=3>MINGGUAN</option>
                                  <option value=4>BULANAN</option>
                              </select>
                          </div>
                          <div class="col-12 col-md-6 px-4 py-2">
                              <label for="keterangan">Keterangan</label>
                              <textarea class="form-control" id="textarea-keterangan" rows="4" v-model="catatan" placeholder="e.g. Fasilitas yang akan digunakan"></textarea>
                          </div>
                      </div>
                      <div class="form-row">
                          <div class="col-12 col-md-6 px-4 py-2">
                              <label for="tanggalMulaiPelaksanaan">Tanggal Mulai Pelaksanaan<span class="asterisk">*</span></label>
                              <input type="date" class="form-control" v-model="tanggal_mulai">
                              <div class="form-check">
                                  <input class="form-check-input" type="checkbox" v-model="terbuka_untuk_umum" id="checkbox-terbuka-untuk-umum">
                                  <label class="form-check-label" for="flexCheckDefault">
                                      Terbuka untuk umum
                                  </label>
                              </div>
                          </div>
                          <div class="col-12 col-md-6 px-4 py-2">
                              <label for="tanggalAkhirPelaksanaan">Tanggal Akhir Pelaksanaan<span class="asterisk">*</span></label>
                              <input type="date" class="form-control" v-model="tanggal_akhir">
                              <p class="note-form">isi dengan tanggal yang sama dengan tanggal mulai pelaksanaan jika memilih "sekali pakai"</p>
                          </div>  
                      </div>
                                                       
                    </form>
                        <div class="modal-footer">
                                <div class="text-center">
                                    <button class="btn btn-outline-secondary" data-dismiss="modal" style="width:80px; height:36px;">Batal</button>
                                </div>
                                <div class="text-center">
                                    <button class="btn btn-success" type="submit" style="width:80px; height:36px;" v-on:click="editPeminjamanRuangan(pinjam.id);editPerulangan(pinjam.perulangan.id);">Simpan</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
              </td>
            </tr>
            </template>

          </tbody>
        </table>
        </div>
        </div>

        <div style="margin:1% 7%;">
        <div class="table-responsive">
        <table class="table table-sm table-bordered" style="border-radius: 10px 10px 0px 0px;">
          <thead class="thead kuning rounded-top" style="border-radius: 10px 10px 0px 0px;">
            <tr style="border-radius: 10px;">
              <th scope="col" colspan="6" class="text-center" style="border-radius: 5px 5px 0px 0px;">Informasi Publikasi, Souvenir, dan Protokoler</th>
            </tr>
          </thead>
        </table>
        <div class="fmed font-weight-bold abu3">Publikasi </div>
        <table v-if="perizinan.perizinan_publikasi==null" class="table table-sm table-bordered mt-2 fsmall" style="border-radius: 10px 10px 0px 0px;">
            <tr>
              <td class="text-center abu2">Jenis Publikasi Luar Ruangan</td>
              <td class="text-center abu2">Jenis Publikasi</td>
              <td class="text-center abu2">Lokasi</td>
              <td class="text-center abu2">Tanggal Mulai</td>
              <td class="text-center abu2">Tanggal Akhir</td>
              <td class="text-center abu2">Status</td>
            </tr>
            <tr>
              <td class="text-center">-</td>
              <td class="text-center">-</td>
              <td class="text-center ">-</td>
              <td class="text-center ">-</td>
              <td class="text-center ">-</td>
              <td class="text-center ">-</td>
            </tr>
        </table>
        <table v-if="perizinan.perizinan_publikasi!=null" class="table table-sm table-bordered mt-2 fsmall" style="border-radius: 10px 10px 0px 0px;">
            <tr>
              <td class="text-center abu2">Jenis Publikasi Luar Ruangan</td>
              <td class="text-center abu2">Jenis Publikasi</td>
              <td class="text-center abu2">Lokasi</td>
              <td class="text-center abu2">Tanggal Mulai</td>
              <td class="text-center abu2">Tanggal Akhir</td>
              <td class="text-center abu2">Status</td>
            </tr>
            <tr>
            <td></td>
            <td></td>
            <td></td>
            <td>{{getDateDef(perizinan.perizinan_publikasi.tanggal_mulai)}}</td>
            <td>{{getDateDef(perizinan.perizinan_publikasi.tanggal_akhir)}}</td>
            <td class="text-center" v-if="perizinan.perizinan_publikasi.status_perizinan_publikasi==1">Menunggu Persetujuan</td>
            <td class="text-center" v-if="perizinan.perizinan_publikasi.status_perizinan_publikasi==2">Disetujui</td>
            <td class="text-center" v-if="perizinan.perizinan_publikasi.status_perizinan_publikasi==3">Ditolak <a href="/ruangan/add">edit</a></td>

            </tr>
        </table>
        </div>
        <div class="fmed font-weight-bold abu3">Souvenir </div>
        <div class="table-responsive">
        <table v-if="perizinan.permintaan_protokoler==null" class="table table-sm table-bordered mt-2 fsmall" style="border-radius: 10px 10px 0px 0px;">
            <tr>
              <td class="text-center abu2">Nama Pembicara</td>
              <td class="text-center abu2">Jabatan Pembicara</td>
              <td class="text-center abu2">Kelas</td>
              <td class="text-center abu2">Souvenir</td>
              <td class="text-center abu2">Kuantitas</td>
              <td class="text-center abu2">Status</td>
            </tr>
            <tr>
              <td class="text-center">-</td>
              <td class="text-center">-</td>
              <td class="text-center ">-</td>
              <td class="text-center ">-</td>
              <td class="text-center ">-</td>
              <td class="text-center ">-</td>
            </tr>
         </table>
        <table v-if="perizinan.permintaan_protokoler!=null" class="table table-sm table-bordered mt-2 fsmall" style="border-radius: 10px 10px 0px 0px;">
            <tr>
              <td class="text-center abu2">Nama Pembicara</td>
              <td class="text-center abu2">Jabatan Pembicara</td>
              <td class="text-center abu2">Kelas</td>
              <td class="text-center abu2">Souvenir</td>
              <td class="text-center abu2">Kuantitas</td>
              <td class="text-center abu2">Status</td>

            </tr>
            <template v-for="souv in perizinan.permintaan_souvenir" v-bind:key="souv.id">
            <tr>
            <td>{{souv.nama_penerima_souvenir}}</td>
            <td>{{souv.jabatan_penerima_souvenir}}</td>
            <td>{{souv.kelas_penerima_souvenir}}</td>
            <td>{{souv.souvenir}}</td>
            <td>{{souv.jumlah}}</td>
            <td class="text-center" v-if="souv.status_permintaan_souvenir==1">Menunggu Persetujuan</td>
            <td class="text-center" v-if="souv.status_permintaan_souvenir==2">Disetujui</td>
            <td class="text-center" v-if="souv.status_permintaan_souvenir==3">Ditolak <a data-toggle="modal" data-target="#popup-permintaan-souvenir">edit</a>
            <!-- Modal: Popup Edit Permintaan Souvenir -->
            <div class="modal fade" id="popup-permintaan-souvenir" tabindex="-1" role="dialog" aria-labelledby="popup-penolakan" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered" role="document">
                        <div class="modal-content">
                        <form>
                            <div class="modal-body">
                            <div class="form-row">
                            <div class="col-12 px-4"> 
                              <label> Souvenir<span class="text-keterangan"> (semua field wajib diisi jika mengajukan permintaan souvenir)</span></label>    
                              <hr >  
                            </div>  
                              <hr v-if="peminjaman>1" >
                              
                              <div class="form-row">
                                  <div class="col-12 col-md-6  px-4 py-2">
                                      <label for="inputNamaPenerima">Nama Penerima:<span class="text-danger">*</span></label>
                                      <input pattern="[A-Za-z]" id="input_nama_penerima" type="text" v-bind:value="souv.nama_penerima_souvenir" v-on:input="nama_penerima_souvenir = $event.target.value" class="form-control" placeholder="e.g. Akhmad">
                                  </div>
                                  <div class="col-12 col-md-6  px-4 py-2">
                                      <label for="inputJabatanPenerima">Jabatan Penerima:<span class="text-danger">*</span></label>
                                      <input id="input_jabatan_penerima" type="text" v-bind:value="souv.jabatan_penerima_souvenir" v-on:input="jabatan_penerima_souvenir = $event.target.value" class="form-control = $event.target.value" placeholder="e.g. Menteri" >
                                  </div>                    
                              </div>
                              <div class="col-12 col-md-6  px-4 py-2">
                                  <label for="inputKelas">Kelas:<span class="text-danger">*</span></label>
                                  <select id="input_kelas" @change="onKelasChange()"  v-model="kelas_penerima_souvenir" class="form-control">
                                      <option disabled selected value="">Pilih...</option>
                                      <option value="1">1</option>
                                      <option value="2">2</option>
                                      <option value="3">3</option>
                                  </select> 

                              </div>
                              <div class="col-12 col-md-6  px-4 py-2">
                                  <label for="inputRegion">Region:<span class="text-danger">*</span></label>
                                  <select id="input_region" @change="onRegionChange()" v-model="region_penerima_souvenir"  class="form-control" >
                                      <option disabled selected value="">Pilih...</option>
                                      <option value="1">Dalam Negeri</option>
                                      <option value="2">Luar Negeri</option>
                                  </select>
                              </div>                    
                            </div>
                            <div class="form-row">
                            <div class="col-12 col-md-6  px-4 py-2">
                                <label for="inputPilihanSouvenir">Pilihan Souvenir:<span class="text-danger">*</span></label>
                                <select id="input_souvenir" v-bind:value="souv.souvenir" v-on:input="souvenir = $event.target.value" class="form-control">        
                                    <option selected disabled value="">Pilih...</option>
                                    <option v-for="pilihan_souvenir in souvenir_data_filtered" v-bind:key="pilihan_souvenir.id" :value="pilihan_souvenir.id">{{pilihan_souvenir.nama_souvenir}}</option>
                                </select>
                            </div>
                            <div class="col-12 col-md-6  px-4 py-2">
                                <label for="inputJumlah">Jumlah:<span class="text-danger">*</span></label>
                                <input id="input_jumlah" v-bind:value="souv.jumlah" v-on:input="jumlah = $event.target.value" type="number" min="1" class="form-control" placeholder="e.g. 1">
                            </div>                    
                            </div>
                            
                              
                          </div>                       
                        </form>
                        <div class="modal-footer">
                                <div class="text-center">
                                    <button class="btn btn-outline-secondary" data-dismiss="modal" style="width:80px; height:36px;">Batal</button>
                                </div>
                                <div class="text-center">
                                    <button class="btn btn-success" type="submit" style="width:80px; height:36px;" v-on:click="editPermintaanSouvenir(souv.id)">Simpan {{souv.id}}</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </td>       
            </tr>
            </template>
        </table>
        </div>
        <div class="fmed font-weight-bold abu3">Protokoler </div>
        <div class="table-responsive">
        <table v-if="perizinan.permintaan_protokoler==null" class="table table-sm table-bordered mt-2 fsmall" style="border-radius: 10px 10px 0px 0px;">
            <tr>
              <td class="text-center abu2">Deskripsi Kebutuhan</td>
              <td class="text-center abu2">Status</td>
            </tr>
            <tr>
              <td class="text-center ">-</td>
              <td class="text-center ">-</td>
            </tr>
        </table>
        <table v-if="perizinan.permintaan_protokoler!=null" class="table table-sm table-bordered mt-2 fsmall" style="border-radius: 10px 10px 0px 0px;">
            <tr>
              <td class="text-center abu2">Deskripsi Kebutuhan</td>
            
              <td class="text-center abu2">Status</td>

            </tr>
            <tr>
                <td>{{perizinan.permintaan_protokoler.deskripsi_kebutuhan}}</td>
                <td class="text-center" v-if="perizinan.permintaan_protokoler.status_permintaan_protokoler==1">Menunggu Persetujuan</td>
                <td class="text-center" v-if="perizinan.permintaan_protokoler.status_permintaan_protokoler==2">Disetujui</td>
                <td class="text-center" v-if="perizinan.permintaan_protokoler.status_permintaan_protokoler==3">Ditolak <button data-toggle="modal" data-target="#popup-permintaan-protokoler" >edit</button></td>
                <!-- Modal: Popup Edit Permintaan Protokoler -->
                <div class="modal fade" id="popup-permintaan-protokoler" tabindex="-1" role="dialog" aria-labelledby="popup-protokoler" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered" role="document">
                        <div class="modal-content">
                        <form>
                            <div class="modal-body">
                                <label>Deskripsi Kebutuhan<span style="color:#EB5757;">*</span></label>
                                <textarea class="form-control" id="textarea-keterangan" rows="6" :value="perizinan.permintaan_protokoler.deskripsi_kebutuhan" @input="deskripsi_kebutuhan = $event.target.value" placeholder="e.g. Waktu terlalu dekat"></textarea>
                            </div>                       
                        </form>
                        <div class="modal-footer">
                                <div class="text-center">
                                    <button class="btn btn-outline-secondary" data-dismiss="modal" style="width:80px; height:36px;">Batal</button>
                                </div>
                                <div class="text-center">
                                    <button class="btn btn-success" type="submit" style="width:80px; height:36px;" v-on:click="editPermintaanProtokoler(perizinan.permintaan_protokoler.id)">Simpan</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </tr>
        </table>
        </div>
        <div class="fmed font-weight-bold abu3">Komentar </div>
          <template v-if="perizinan.peminjaman_ruangan.length!=0">

            <template v-for="pinjam in perizinan.peminjaman_ruangan" v-bind:key="pinjam.id">
                <template v-if="pinjam.alasan_penolakan!=null" class="d-flex mb-2">
                    <div class="pt-1"> Admin Fastur </div>
                    <div class="label abu2 ml-4 pl-2 pt-1 komentar align-middle">{{pinjam.alasan_penolakan}}</div>
                </template>
            </template>
          </template>
          
            <template v-if="perizinan.permintaan_souvenir.length!=0">
              <template v-for="souvenir in perizinan.permintaan_souvenir" v-bind:key="souvenir.id">
                <template v-if="souvenir.alasan_penolakan!=null" class="d-flex mb-2">
                    <div class="pt-1">Admin Humas </div>
                    <div class="label abu2 pl-2 pt-1 komentar align-middle">{{souvenir.alasan_penolakan}}</div>
                </template>
              </template>
            </template>
                <template v-if="perizinan.permintaan_protokoler.alasan_penolakan!=null" class="d-flex mb-2">
                    <div class="pt-1">Admin Humas </div>
                    <div class="label abu2 pl-2 pt-1 komentar align-middle">{{perizinan.permintaan_protokoler.alasan_penolakan}}</div>
                </template>
        </div>



    </div>
 <!-- Modal: Notif Sukses -->
    <div class="modal fade" id="ubahModal" tabindex="-1" role="dialog" aria-labelledby="sukses-setuju-modal" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">

            <div class="modal-body">
                <div class="text-center">
                    <img src="../assets/images/icon_ceklis.png" alt="icon-sukses">
                <h2 style="margin:20px 0px 15px 0px">Sukses</h2>
                <p style="margin:0px 0px -15px 0px">Perubahan berhasil disimpan</p>
                </div>
            </div>
            <div class="modal-footer">
                <div class="text-center">
                    <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="ubahDone" style="width:80px; height:36px;">OK</button>
                </div>
            </div>
            </div>
        </div>
    </div>
    <!-- Modal: Notif Gagal -->
    <div class="modal fade" id="notification-failed" tabindex="-1" role="dialog" aria-labelledby="gagal-submit-modal" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">

            <div class="modal-body">
                <div class="text-center">
                    <img src="../assets/images/icon_silang.png" alt="icon-error">
                <h2 style="margin:20px 0px 15px 0px">Error</h2>
                <p style="margin:0px 0px -15px 0px">{{ error_message }}</p>
                </div>
            </div>
            <div class="modal-footer">
                <div class="text-center">
                    <button type="button" class="btn btn-success" data-dismiss="modal" style="width:80px; height:36px;">OK</button>
                </div>
            </div>
            </div>
        </div>
    </div>
</template>
<script>
import UserService from '../services/user.service';
import IzinMahasiswaService from '../services/izinMahasiswa.service';

import moment from 'moment';
import $ from 'jquery';


export default {
    name: 'DetailPerizinan',
    data() {
        return {
            perizinan: "",
            permintaan_protokoler: "",
            permintaan_souvenir : "",
            souvenir_data : [],
            error_message : "",
            judul_peminjaman: "",
            souvenir_data_filtered: [],
            kelas_penerima_souvenir: "",
            region_penerima_souvenir: "",
            list_ruangan: [],
            peminjaman_ruangan: "",
            perulangan: "",
            detail_kegiatan:"",
            user: this.$store.state.auth.user.id_user, 
            file_info_kegiatan: null,
            respon_kegiatan: null,



        }
    },
    methods: {
             getDateDef : function (date) {
                 return moment(date, 'YYYY-MM-DDTHH:mm').format('D MMMM YYYY');
             },
             getDate : function (date) {
                 return moment(date, 'YYYY-MM-DDTHH:mm').format('HH:mm, D MMMM YYYY');
             },
             getHour : function (date) {
                 return moment(date, 'YYYY-MM-DDTHH:mm').format('HH:mm');
             },

             
            
            editIzinKegiatan(id) {
              console.log("masuk edit kegiatan")
                const data_kegiatan = {
                    id: id,
                    nama_kegiatan: this.nama_kegiatan,
                    organisasi: this.organisasi,
                    user: this.user,
                    status_perizinan_kegiatan :3,
                    detail_kegiatan: id,
                };
                console.log(data_kegiatan)
                    IzinMahasiswaService.putIzinKegiatanHeader(id,data_kegiatan).then(
                        response =>{
                            this.respon_kegiatan = response.data;
                            console.log(response.data);                   
                            },
                        error =>{
                        console.log(error.message);
                        }
                    );            
            },
            editDetailIzinKegiatan(id_detail){
                console.log("masuk edit detail")
                let formDataDetail = new FormData()
                formDataDetail.append("izin_kegiatan",1)
                formDataDetail.append("waktu_tanggal_mulai",this.waktu_tanggal_mulai)
                formDataDetail.append("waktu_tanggal_akhir",this.waktu_tanggal_akhir)
                formDataDetail.append("email_pic",this.email_pic)
                formDataDetail.append("nama_pic",this.nama_pic)
                formDataDetail.append("hp_pic",this.hp_pic)
                formDataDetail.append("npm_pic",this.npm_pic)
                formDataDetail.append("npm_ketua_organisasi",this.npm_ketua_organisasi)
                formDataDetail.append("nama_ketua_organisasi",this.nama_ketua_organisasi)
                formDataDetail.append("tempat_pelaksanaan",this.tempat_pelaksanaan)
                formDataDetail.append("sumber_pendanaan",this.sumber_pendanaan)
                formDataDetail.append("alasan_penolakan","")
                if(this.file_info_kegiatan != null){
                  formDataDetail.append("file_info_kegiatan", this.file_info_kegiatan)
                }
                console.log(formDataDetail)
                for (var value of formDataDetail.values()) {
                console.log(value);
}           
                IzinMahasiswaService.putIzinKegiatanDetail(id_detail,formDataDetail).then(
                    response =>{
                        console.log(response.data);                                                            
                        $('#notification-success').modal('show')
                    },
                    error =>{
                        console.log(error.message);
                        this.error_message = error.message
                        $('#notification-failed').modal('show')
                    }
                )           
            },
            editPeminjamanRuangan(id) {
              console.log("masuk put Perminjaman Ruangan");

              const data_put = {
                  id: id,
                  judul_peminjaman: this.judul_peminjaman,
                  jumlah_peserta: this.jumlah_peserta,
                  status_peminjaman_ruangan: 1,
                  alasan_penolakan: null,
                  waktu_mulai: this.waktu_mulai,
                  waktu_akhir: this.waktu_akhir,
                  catatan: this.catatan,                 
                  ruangan: this.ruangan,
                  terbuka_untuk_umum: this.terbuka_untuk_umum,
                  perulangan: {
                    id: id,
                    jenjang: this.jenjang,
                    tanggal_mulai: this.tanggal_mulai,
                    tanggal_akhir: this.tanggal_akhir
                  }

              };
              console.log(data_put);
              UserService.putPeminjamanRuangan(id, data_put).then(
                  response => {
                      console.log(response.data);


                  },
                  error => {
                      console.log(error.message);

                  }

              );
            },
            editPerulangan(id) {
              console.log("masuk put Perulangan");

              const data_put = {         
                    id: id,
                    jenjang: this.jenjang,
                    tanggal_mulai: this.tanggal_mulai,
                    tanggal_akhir: this.tanggal_akhir
              };
              console.log(data_put);
              UserService.putPerulangan(id, data_put).then(
                  response => {
                      console.log(response.data);
                      $('#ubahModal').modal('toggle')


                  },
                  error => {
                      console.log(error.message);

                  }

              );
            },

            editPermintaanProtokoler(id) {
            console.log("masuk put permintaan_protokoler");

            const data_put = {
                id: id,
                deskripsi_kebutuhan: this.deskripsi_kebutuhan,
                status_permintaan_protokoler: 1,
                alasan_penolakan: null,
            };
            console.log(data_put);
            UserService.putPermintaanProtokoler(id, data_put).then(
                response => {
                    console.log(response.data);
                    $('#ubahModal').modal('toggle')
                    window.location.reload();


                },
                error => {
                    console.log(error.message);
                    window.location.reload();

                }

        );
        },
        editPermintaanSouvenir(id) {
            console.log("masuk put permintaan_souvenir");

            const data_put = {
                id: id,
                alasan_penolakan: null,
                status_permintaan_souvenir: 1,
                jumlah: this.jumlah,
                souvenir: this.souvenir,
                nama_penerima_souvenir:this.nama_penerima_souvenir,
                kelas_penerima_souvenir: this.kelas_penerima_souvenir,
                region_penerima_souvenir: this.region_penerima_souvenir,
                jabatan_penerima_souvenir: this.jabatan_penerima_souvenir,
                

            };
            console.log(data_put);
            UserService.putPermintaanSouvenir(id, data_put).then(
                response => {
                    console.log(response.data);
                    $('#ubahModal').modal('toggle')
                    window.location.reload();
                },
                error => {
                    console.log(error.message);
                    //window.location.reload();
                }

        );
        },
        ubahDone() {
            window.location.href="/perizinan";
        },
        onKelasChange(){
            console.log("masuk onkelaschange")
            let kelas_souvenir_diminta = this.kelas_penerima_souvenir
            let region_souvenir_diminta = this.region_penerima_souvenir
            let souvenir_data_filtered = []
                this.souvenir_data.forEach(function(souvenir){
                    if(kelas_souvenir_diminta == 1){            
                        if(souvenir.kelas == 1 || souvenir.kelas == 4 || souvenir.kelas == 5 || souvenir.kelas == 7){             
                            if(region_souvenir_diminta != '' && ((souvenir.region == region_souvenir_diminta || souvenir.region == 3))){
                                souvenir_data_filtered.push(souvenir)
                            }
                            else if (region_souvenir_diminta==''){
                                souvenir_data_filtered.push(souvenir)
                            }
                        }
                    }else if(kelas_souvenir_diminta == 2){
                        console.log("kelas diminta " + kelas_souvenir_diminta)
                        if(souvenir.kelas == 2 || souvenir.kelas == 4 || souvenir.kelas == 6 || souvenir.kelas == 7){
                            console.log("reg diminta " + region_souvenir_diminta)
                            if(region_souvenir_diminta != '' && ((souvenir.region == region_souvenir_diminta || souvenir.region == 3))){                              
                                souvenir_data_filtered.push(souvenir)
                            }
                            else if(region_souvenir_diminta==''){
                               souvenir_data_filtered.push(souvenir)
                            }
                        }
                    }else if(kelas_souvenir_diminta == 3){
                        if(souvenir.kelas == 3 || souvenir.kelas == 5 || souvenir.kelas == 6 || souvenir.kelas == 7){
                            if(region_souvenir_diminta != '' && ((souvenir.region == region_souvenir_diminta || souvenir.region == 3))){
                                souvenir_data_filtered.push(souvenir)
                            }
                            else if (region_souvenir_diminta==''){
                                souvenir_data_filtered.push(souvenir)
                            }
                        }
                    }
                })
                this.souvenir_data_filtered = souvenir_data_filtered
                console.log(this.souvenir_data_filtered)
        },
        onRegionChange(){
            console.log("masuk onregionchange")
            if(this.kelas_penerima_souvenir != ''){
                this.onKelasChange()
            }else{
                let region_souvenir_diminta = this.permintaan_souvenir.region_penerima_souvenir
                let souvenir_data_filtered = []
                this.souvenir_data.forEach(function(souvenir){
                    if(souvenir.region == region_souvenir_diminta || souvenir.region == 3){
                        souvenir_data_filtered.push(souvenir)
                    }
                })
                this.souvenir_data_filtered = souvenir_data_filtered
                console.log(this.souvenir_data_filtered)
            }
            
        },

         },
    created(){
        console.log("masuk detail")
        console.log(this.$route.params.id)
        UserService.getPerizinan(this.$route.params.id).then(
            response => {
                this.perizinan = response.data;
            },
            error => {
                this.error_message = (error.response && error.response.data) || error.message || error.toString();
            }
        ),
        IzinMahasiswaService.getListSouvenir().then(
            response => {
                this.souvenir_data = response.data;
                this.souvenir_data_filtered = this.souvenir_data;
                console.log(this.souvenir_data_filtered)
            },
            error => {
                this.error_call_api = (error.response && error.response.data) || error.message || error.toString();
            }
        ),
        IzinMahasiswaService.getRuangan().then(
            response =>{
                this.list_ruangan = response.data
            },
            error => {
                this.error_call_api = (error.response && error.response.data) || error.message || error.toString();
            }
        )
    },
    mounted(){
        console.log(this.perizinan);
        console.log(this.error_message);
        //create daftar waktu
        let option_waktu_made = [];
        let i;
        for (i = 0; i < 24; i++){
            if (i < 10 ){
                option_waktu_made.push({
                    value: "2021-01-01T0" + i + ":00",
                    text: "0" + i + ":00"
                });
                option_waktu_made.push({
                    value: "2021-01-01T0" + i + ":30",
                    text: "0" + i + ":30"
                });
            } else {
                option_waktu_made.push({
                    value: "2021-01-01T" + i + ":00",
                    text:  i + ":00"
                });
                option_waktu_made.push({
                    value: "2021-01-01T" + i + ":30",
                    text: i + ":30"
                });
            }
        }
        this.option_waktu = option_waktu_made;

    },

}
</script>
<style>
table-bordered{
    border-radius: 5px !important;
}
.fmed{
    font-size:14px;
}
.abu3{
    color:#777777 !important;
}
.abu2{
    background-color:#E8E8E8 !important;
}
.komentar{
    width:88%;
    height: 30px;
    padding:2px;
    margin-left:2%;
    border-radius: 5px;
}
</style>