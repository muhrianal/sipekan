<template>
    <div class="card fmed"  style="min-height:600%;">
    <div class="d-flex">
        <div class="mr-auto p-3">
            <h4 class="judul p-1 align-middle" style="font-weight: 500;">Daftar Perizinan</h4>
        </div>
      <div class="p-3">
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
          <td v-if="perizinan.status_perizinan_kegiatan==3">Ditolak <a data-toggle="modal" class="btn tambah" style="padding:1px 3px;font-size:12px;"  data-target="#popup-izin-kegiatan">edit</a>
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
                        <input type="text" class="form-control" placeholder="e.g. Open House FEB UI" required 
                        v-model="nama_kegiatan">
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputTempatPelaksanaan">Tempat Pelaksanaan<span class="text-danger">*</span>: <span class="text-keterangan">  (jika kegiatan online, isi: "Online")</span></label>
                        <template v-if="perizinan.detail_kegiatan!=null">

                        <input type="text" class="form-control" placeholder="e.g. FEB UI"   v-model="tempat_pelaksanaan" required>
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
                        <input type="text" class="form-control" placeholder="e.g. BEM FEB UI"  v-model="organisasi" required>
                    </div>                         
                </div>

                 <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputKetuaOrganisasi">Nama Ketua Organisasi<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. Yobelio"  v-model="nama_ketua_organisasi" required>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputNpmKetuaOrganisasi">NPM Ketua Organisasi<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. 1806123456" v-model="npm_ketua_organisasi" required>
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputPicKegiatan">Nama PIC Kegiatan<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. Akhmad"  v-model="nama_pic" required> 
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputNpmPic">NPM PIC<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. 1806123456" v-model="npm_pic"  required>
                    </div>                    
                </div>

                <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputEmailPic">Email PIC<span class="text-danger">*</span>:</label>
                        <input type="email" class="form-control" placeholder="e.g. akhmad@ui.ac.id" v-model="email_pic" required>
                    </div>
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputHpPic">HP PIC<span class="text-danger">*</span>:</label>
                        <input type="text" pattern="^[0-9]+$" class="form-control" placeholder="e.g. 08151234567" v-model="hp_pic"  required>
                    </div>                    
                </div>

                 <div class="form-row">
                    <div class="col-12 col-md-6  px-4 py-2">
                        <label for="inputSumberPendanaan">Sumber Pendanaan<span class="text-danger">*</span>:</label>
                        <input type="text" class="form-control" placeholder="e.g. Sponsor"  v-model="sumber_pendanaan" required>
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
                                    <button class="btn btn-success" type="submit" style="width:80px; height:36px;" v-on:click="editIzinKegiatan(perizinan.id);editDetailIzinKegiatan(perizinan.detail_kegiatan.id, perizinan.id)">Simpan {{perizinan.id}}</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                </template>
        </tr>
      </tbody>
    </table>
    <div class="d-flex bd-highlight">
  <div class="p-2 flex-grow-1 bd-highlight"></div>
  <div class="p-2 bd-highlight"></div>
  <div class="p-2 bd-highlight">        <a class="ml-auto" :href="'/detail-kegiatan/' + perizinan.id"> Detail Izin Kegiatan>></a>
</div>
</div>

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
            <template v-for="peminjaman in list_peminjaman_ruangan.length" v-bind:key="peminjaman.id"> 
                <tr>
                    <td class="text-center">{{list_peminjaman_ruangan[peminjaman-1].judul_peminjaman}} </td>   
                    <td class="text-center" >{{list_peminjaman_ruangan[peminjaman-1].ruangan}}</td>
                    <template v-if="peminjaman.perulangan==null">
                        <td class="text-center"> - </td>
                    </template>
                    <template v-if="peminjaman.perulangan!=null">
                        <td class="text-center">{{getDateDef(list_peminjaman_ruangan[peminjaman-1].perulangan.tanggal_mulai)}}</td>
                    </template>       
                    <td class="text-center">{{getHour(list_peminjaman_ruangan[peminjaman-1].waktu_mulai)}} - {{getHour(list_peminjaman_ruangan[peminjaman-1].waktu_akhir)}}</td> 
                        <template v-if="list_peminjaman_ruangan[peminjaman-1].perulangan.jenjang==1">
                        <td class="text-center" > Sekali Pakai </td>
                        </template>
                        <template  v-if="list_peminjaman_ruangan[peminjaman-1].perulangan.jenjang==2">
                        <td class="text-center"> Harian </td>
                        </template>
                        <template  v-if="list_peminjaman_ruangan[peminjaman-1].perulangan.jenjang==3">
                        <td class="text-center"> Mingguan </td>
                        </template>
                        <template v-if="list_peminjaman_ruangan[peminjaman-1].perulangan.jenjang==4">
                        <td class="text-center"> Bulanan </td>  
                        </template>     
                    <td class="text-center" v-if="list_peminjaman_ruangan[peminjaman-1].status_peminjaman_ruangan==1">Menunggu Persetujuan</td>
                    <td class="text-center text-success" v-if="list_peminjaman_ruangan[peminjaman-1].status_peminjaman_ruangan==2">Disetujui</td>
                    <td class="text-center text-danger" v-if="list_peminjaman_ruangan[peminjaman-1].status_peminjaman_ruangan==3">Ditolak <button  class="btn tambah" style="padding:1px 3px;font-size:12px;" @click="openModal(peminjaman-1)" >edit</button></td>
                    
                </tr>

            </template>
            <!-- MODALPEMINJAMANRUANGAN -->
            <div v-if="indexPeminjamanRuangan!=null">

            <div class="modal fade" id="popup-peminjaman-ruangan" tabindex="-1" role="dialog" aria-labelledby="popup-penolakan" aria-hidden="true" :no-enforce-focus="true">
                    <div class="modal-dialog modal-dialog-centered" role="document">
                        <div class="modal-content">
                      <form>             
    
                      <div class="form-row">
                          <div class="col-12 col-md-6 px-4 py-2">
                              <label for="inputSubkegiatan">Nama Subkegiatan<span class="asterisk">*</span></label>
                              <input type="text" class="form-control" placeholder="e.g. Administrasi Bisnis - B" v-model="list_peminjaman_ruangan[indexPeminjamanRuangan].judul_peminjaman">
                          </div>
                          <div class="col-12 col-md-6 px-4 py-2">
                              <label for="inputJumlahPeserta">Jumlah Peserta<span class="asterisk">*</span></label>
                              <input type="number" class="form-control" placeholder="e.g. 120" v-model="list_peminjaman_ruangan[indexPeminjamanRuangan].jumlah_peserta">
                          </div>  
                      </div>
                      <div class="form-row">
                          <div class="col-12 col-md-6 px-4 py-2">
                              <label for="waktuMulaiPeminjaman">Waktu mulai<span class="asterisk">*</span></label>
                              <select class="form-control" id="waktuMulaiPeminjaman" v-model="list_peminjaman_ruangan[indexPeminjamanRuangan].waktu_mulai">
                                  <option selected disabled value="">Pilih...</option>
                                  <option v-for="option in option_waktu" v-bind:key="option" v-bind:value="option.value">{{option.text}}</option>
                              </select>
                          </div>
                          <div class="col-12 col-md-6 px-4 py-2">
                              <label for="waktuAkhirPeminjaman">Waktu akhir<span class="asterisk">*</span></label>
                              <select class="form-control" id="waktuAkhirPeminjaman" v-model="list_peminjaman_ruangan[indexPeminjamanRuangan].waktu_akhir">
                                  <option selected disabled value="">Pilih...</option>
                                  <option v-for="option in option_waktu" v-bind:key="option" v-bind:value="option.value">{{option.text}}</option>
                              </select>
                          </div>  
                      </div>
                      <div class="form-row">
                          <div class="col-12 col-md-6 px-4 py-2">
                              <label for="ruangan">Ruangan<span class="asterisk">*</span></label>
                              <select class="form-control" id="daftar-ruangan" v-model="list_peminjaman_ruangan[indexPeminjamanRuangan].ruangan">
                                  <option selected disabled value="">Pilih...</option>
                                  <option v-for="pilihan_ruangan in list_ruangan" v-bind:key="pilihan_ruangan.id" :value="pilihan_ruangan.id">{{pilihan_ruangan.nama}}</option>
                              </select>
                              <p class="note-ruangan note-form text-right">Lihat daftar ruangan <a href="#">disini</a> </p>
                              <label for="perulangan">Perulangan<span class="asterisk">*</span></label>
                              <select class="form-control" id="perulangan" v-model="list_peminjaman_ruangan[indexPeminjamanRuangan].perulangan.jenjang">
                                  <option selected disabled value="">Pilih...</option>
                                  <option value=1>SEKALI PAKAI</option>
                                  <option value=2>HARIAN</option>
                                  <option value=3>MINGGUAN</option>
                                  <option value=4>BULANAN</option>
                              </select>
                          </div>
                          <div class="col-12 col-md-6 px-4 py-2">
                              <label for="keterangan">Keterangan</label>
                              <textarea class="form-control" id="textarea-keterangan" rows="4" v-model="list_peminjaman_ruangan[indexPeminjamanRuangan].catatan" placeholder="e.g. Fasilitas yang akan digunakan"></textarea>
                          </div>
                      </div>
                      <div class="form-row">
                          <div class="col-12 col-md-6 px-4 py-2">
                              <label for="tanggalMulaiPelaksanaan">Tanggal Mulai Pelaksanaan<span class="asterisk">*</span></label>
                              <input type="date" class="form-control" v-model="list_peminjaman_ruangan[indexPeminjamanRuangan].perulangan.tanggal_mulai">
                              <div class="form-check">
                                  <input class="form-check-input" type="checkbox" v-model="list_peminjaman_ruangan[indexPeminjamanRuangan].terbuka_untuk_umum" id="checkbox-terbuka-untuk-umum">
                                  <label class="form-check-label" for="flexCheckDefault">
                                      Terbuka untuk umum
                                  </label>
                              </div>
                          </div>
                          <div class="col-12 col-md-6 px-4 py-2">
                              <label for="tanggalAkhirPelaksanaan">Tanggal Akhir Pelaksanaan<span class="asterisk">*</span></label>
                              <input type="date" class="form-control"  v-model="list_peminjaman_ruangan[indexPeminjamanRuangan].perulangan.tanggal_akhir">
                              <p class="note-form">isi dengan tanggal yang sama dengan tanggal mulai pelaksanaan jika memilih "sekali pakai"</p>
                          </div>  
                      </div>
                                                       
                    </form>
                        <div class="modal-footer">
                                <div class="text-center">
                                    <button class="btn btn-outline-secondary" data-dismiss="modal" style="width:80px; height:36px;">Batal</button>
                                </div>
                                <div class="text-center">
                                    <button class="btn btn-success" type="submit" style="width:80px; height:36px;" v-on:click="editPeminjamanRuangan(list_peminjaman_ruangan[indexPeminjamanRuangan].id,indexPeminjamanRuangan);editPerulangan(list_peminjaman_ruangan[indexPeminjamanRuangan].perulangan.id,indexPeminjamanRuangan);">Simpan</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

</div>
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
        <div class="d-flex">
          <div>
            <div class="fmed font-weight-bold abu3">Publikasi </div>

          </div>
          <template v-if="perizinan.perizinan_publikasi.jenis_izin_publikasi!=null">
          
          <div class="ml-auto">
            <a data-toggle="modal" class="btn tambah" style="padding:1px 3px;font-size:12px;"  data-target="#popup-perizinan-publikasi">edit</a>
          </div>
          
          </template>
        </div>
        <table v-if="perizinan.perizinan_publikasi==null" class="table table-sm table-bordered mt-2 fsmall" style="border-radius: 10px 10px 0px 0px;">
            <tr>
              <td class="text-center abu2">Tanggal Mulai</td>
              <td class="text-center abu2">Tanggal Akhir</td>
              <td class="text-center abu2">Keterangan</td>
              <td class="text-center abu2">Jenis Publikasi Luar Ruangan</td>
              <td class="text-center abu2">Jenis Publikasi</td>              
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
              <td class="text-center abu2">Tanggal Mulai</td>
              <td class="text-center abu2">Tanggal Akhir</td>
              <td class="text-center abu2">Keterangan</td>
              <td class="text-center abu2">Jenis Publikasi Luar Ruangan</td>
              <td class="text-center abu2">Jenis Publikasi</td>
              <td class="text-center abu2">Status</td>
            </tr>
            <tr>
            <td :rowspan="perizinan.perizinan_publikasi.jenis_izin_publikasi.length+1" class="align-middle text-center">{{getDateDef(perizinan.perizinan_publikasi.tanggal_mulai)}}</td>
            <td :rowspan="perizinan.perizinan_publikasi.jenis_izin_publikasi.length+1" class="align-middle text-center">{{getDateDef(perizinan.perizinan_publikasi.tanggal_akhir)}}</td>
            <td :rowspan="perizinan.perizinan_publikasi.jenis_izin_publikasi.length+1" class="align-middle text-center">{{perizinan.perizinan_publikasi.keterangan}}</td>
            </tr>
            <template  v-for="pub in perizinan.perizinan_publikasi.jenis_izin_publikasi" v-bind:key="pub.id">
            <tr>
            
            <td v-if="pub.jenis_publikasi.luar_ruangan==true"> {{pub.jenis_publikasi.deskripsi_publikasi}}</td>
            <td v-if="pub.jenis_publikasi.luar_ruangan==true"> - </td>

            <td v-if="pub.jenis_publikasi.luar_ruangan==false"> - </td>
            <td v-if="pub.jenis_publikasi.luar_ruangan==false"> {{pub.jenis_publikasi.deskripsi_publikasi}}</td>
            
            <td class="text-center" v-if="pub.status_perizinan_publikasi==1">Menunggu Persetujuan</td>
            <td class="text-center" v-if="pub.status_perizinan_publikasi==2">Disetujui</td>
            <td class="text-center" v-if="pub.status_perizinan_publikasi==3">Ditolak 
            <!-- Modal: Popup Edit Permintaan Protokoler -->
                <div class="modal fade bd-example-modal-lg" id="popup-perizinan-publikasi" tabindex="-1" role="dialog" aria-labelledby="popup-protokoler" aria-hidden="true">
                    <div class="modal-dialog modal-lg" role="document">
                        <div class="modal-content">
                        <form>
                            
                <div class="border-form">      
                    <div class="form-row">        
                        <div class="col-12 col-md-6 px-4 py-2">
                            <label for="inputPublikasiLuarRuangan">Publikasi Luar Ruangan</label>
                            <span v-for="publikasi in publikasi_luar_ruangan" v-bind:key="publikasi.id">
                                <input id="input_publikasi" v-model="jenis_publikasi" type="checkbox" :value="publikasi"> <span class="checkbox-label">{{publikasi.deskripsi_publikasi}}</span><br>
                            </span>
                        </div>
                        <div class="col-12 col-md-6  px-4 py-2">
                            <label for="inputPublikasi">Publikasi</label>
                            <hr noshade >
                            <span v-for="publikasi in publikasi" v-bind:key="publikasi.id">
                                <input id="input_publikasi" v-model="jenis_publikasi" type="checkbox" :value="publikasi"> <span class="checkbox-label">{{publikasi.deskripsi_publikasi}}</span><br>
                            </span>
                        </div>                    
                    </div>            
                    <div class="form-row">
                        <div class="col-12 col-md-6  px-4 py-2">
                            <label for="inputKeterangan">Keterangan <span class="text-keterangan">(Harap isi jenis dan lokasi publikasi disini, jika memilih "Lainnya")</span></label>
                            <textarea id="input_keterangan" type="text" v-model="keterangan" class="form-control" placeholder="e.g. Baliho di Depan Gedung x ukuran (axb)"></textarea>
                        </div>   
                        <div class="col-12 col-md-6  px-4 py-2"> 
                            <label for="inputMateriKegiatan">Materi Kegiatan / Press Release:<span class="text-keterangan">  (Dapat diunggah dalam format zip)</span> </label>
                            <input id= "file_materi" type="file" ref="fileMateri" @change="onFileMateriChange" class="form-control-file">
                            <p v-if="this.file_materi_kegiatan !=null" class="text-right note-field" @Click="deleteFileMateri()">Hapus File</p>
                            <label for="inputFlyerPengumuman">Flyer Pengumuman / Poster Kegiatan:<span class="text-keterangan">  (jika ada)</span></label>
                            <input id= "file_flyer" type="file" ref="fileFlyer" @change="onFileFlyerChange" class="form-control-file">
                            <p v-if="this.file_flyer_pengumuman !=null" class="text-right note-field" @Click="deleteFileFlyer()">Hapus File</p>
                        </div>                                     
                    </div>
                    <div class="form-row">
                        <div class="col-12 col-md-6  px-4 py-2">
                            <label for="inputTanggalMulai">Tanggal Mulai<span class="text-danger">*</span></label>
                            <input id="input_tanggal_mulai" v-model="tanggal_mulai_publikasi" type="date" class="form-control" >                   
                        </div>
                        <div class="col-12 col-md-6  px-4 py-2 ">
                            <label for="inputTanggalAkhir">Tanggal Akhir<span class="text-danger">*</span></label>
                            <input id="input_tanggal_akhir" v-model="tanggal_akhir_publikasi" type="date" class="form-control" >
                        </div>                        
                    </div>
                </div>                       
                        </form>
                        <div class="modal-footer">
                                <div class="text-center">
                                    <button class="btn btn-outline-secondary" data-dismiss="modal" style="width:80px; height:36px;">Batal</button>
                                </div>
                                <div class="text-center">
                                    <button class="btn btn-success" type="submit" style="width:80px; height:36px;" v-on:click="editPerizinanPublikasi(perizinan.perizinan_publikasi.id, perizinan.id)">Simpan</button>
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
            <template v-for="souv in list_permintaan_souvenir.length" v-bind:key="souv.id">
                <tr>
                    <td>{{list_permintaan_souvenir[souv-1].nama_penerima_souvenir}}</td>
                    <td>{{list_permintaan_souvenir[souv-1].jabatan_penerima_souvenir}}</td>
                    <td>{{list_permintaan_souvenir[souv-1].kelas_penerima_souvenir}}</td>
                    <td>{{list_permintaan_souvenir[souv-1].souvenir}}</td>
                    <td>{{list_permintaan_souvenir[souv-1].jumlah}}</td>
                    <td class="text-center" v-if="list_permintaan_souvenir[souv-1].status_permintaan_souvenir==1">Menunggu Persetujuan</td>
                    <td class="text-center" v-if="list_permintaan_souvenir[souv-1].status_permintaan_souvenir==2">Disetujui</td>
                    <td class="text-center" v-if="list_permintaan_souvenir[souv-1].status_permintaan_souvenir==3">Ditolak <button data-toggle="modal" class="btn tambah" style="padding:1px 3px;font-size:12px;"  data-target="#popup-permintaan-souvenir" @Click="openModalSouvenir(souv-1)">edit</button>
                    
                </td>       
                </tr>
            </template>
            <!-- Modal: Popup Edit Permintaan Souvenir -->
            <div v-if="indexPermintaanSouvenir!=null">
                <div class="modal fade" id="popup-permintaan-souvenir" tabindex="-1" role="dialog" aria-labelledby="popup-penolakan" aria-hidden="true" :no-enforce-focus="true">
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
                                      <input pattern="[A-Za-z]" id="input_nama_penerima" type="text" v-model="list_permintaan_souvenir[indexPermintaanSouvenir].nama_penerima_souvenir" class="form-control" placeholder="e.g. Akhmad">
                                  </div>
                                  <div class="col-12 col-md-6  px-4 py-2">
                                      <label for="inputJabatanPenerima">Jabatan Penerima:<span class="text-danger">*</span></label>
                                      <input id="input_jabatan_penerima" type="text" v-model="list_permintaan_souvenir[indexPermintaanSouvenir].jabatan_penerima_souvenir" class="form-control = $event.target.value" placeholder="e.g. Menteri" >
                                  </div>                    
                              </div>
                              <div class="col-12 col-md-6  px-4 py-2">
                                  <label for="inputKelas">Kelas:<span class="text-danger">*</span></label>
                                  <select id="input_kelas" @change="onKelasChange()"  v-model="list_permintaan_souvenir[indexPermintaanSouvenir].kelas_penerima_souvenir" class="form-control">
                                      <option disabled selected value="">Pilih...</option>
                                      <option value="1">1</option>
                                      <option value="2">2</option>
                                      <option value="3">3</option>
                                  </select> 

                              </div>
                              <div class="col-12 col-md-6  px-4 py-2">
                                  <label for="inputRegion">Region:<span class="text-danger">*</span></label>
                                  <select id="input_region" @change="onRegionChange()" v-model="list_permintaan_souvenir[indexPermintaanSouvenir].region_penerima_souvenir"  class="form-control" >
                                      <option disabled selected value="">Pilih...</option>
                                      <option value="1">Dalam Negeri</option>
                                      <option value="2">Luar Negeri</option>
                                  </select>
                              </div>                    
                            </div>
                            <div class="form-row">
                            <div class="col-12 col-md-6  px-4 py-2">
                                <label for="inputPilihanSouvenir">Pilihan Souvenir:<span class="text-danger">*</span></label>
                                <select id="input_souvenir" v-model="list_permintaan_souvenir[indexPermintaanSouvenir].souvenir" class="form-control">        
                                    <option selected disabled value="">Pilih...</option>
                                    <option v-for="pilihan_souvenir in souvenir_data_filtered" v-bind:key="pilihan_souvenir.id" :value="pilihan_souvenir.id">{{pilihan_souvenir.nama_souvenir}}</option>
                                </select>
                            </div>
                            <div class="col-12 col-md-6  px-4 py-2">
                                <label for="inputJumlah">Jumlah:<span class="text-danger">*</span></label>
                                <input id="input_jumlah" v-model="list_permintaan_souvenir[indexPermintaanSouvenir].jumlah" type="number" min="1" class="form-control" placeholder="e.g. 1">
                            </div>                    
                            </div>
                            
                              
                          </div>                       
                        </form>
                        <div class="modal-footer">
                                <div class="text-center">
                                    <button class="btn btn-outline-secondary" data-dismiss="modal" style="width:80px; height:36px;">Batal</button>
                                </div>
                                <div class="text-center">
                                    <button class="btn btn-success" type="submit" style="width:80px; height:36px;" v-on:click="editPermintaanSouvenir(list_permintaan_souvenir[indexPermintaanSouvenir].id,indexPermintaanSouvenir)">Simpan {{list_permintaan_souvenir[indexPermintaanSouvenir].id}}</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                </div>
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
                <td class="text-center" v-if="perizinan.permintaan_protokoler.status_permintaan_protokoler==3">Ditolak <a data-toggle="modal" class="btn tambah" style="padding:1px 3px;font-size:12px;" data-target="#popup-permintaan-protokoler" >edit</a></td>
                <!-- Modal: Popup Edit Permintaan Protokoler -->
                <div class="modal fade" id="popup-permintaan-protokoler" tabindex="-1" role="dialog" aria-labelledby="popup-protokoler" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered" role="document">
                        <div class="modal-content">
                        <form>
                            <div class="modal-body">
                                <label >Deskripsi Kebutuhan<span style="color:#EB5757;">*</span></label>
                                <textarea class="form-control" id="textarea-keterangan" rows="6" v-model="deskripsi_kebutuhan" placeholder="e.g. Waktu terlalu dekat"></textarea>
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
          <template v-if="perizinan.peminjaman_ruangan.length!=null">

            <template v-for="pinjam in perizinan.peminjaman_ruangan" v-bind:key="pinjam.id">
                <template v-if="pinjam.alasan_penolakan!=null" class="d-flex mb-2">
                    <div class="pt-1"> Admin Fastur </div>
                    <div class="label abu2 ml-4 pl-2 pt-1 komentar align-middle">{{pinjam.alasan_penolakan}}</div>
                </template>
            </template>
          </template>
          
            <template v-if="perizinan.permintaan_souvenir!=null">
              <template v-for="souvenir in perizinan.permintaan_souvenir" v-bind:key="souvenir.id">
                <template v-if="souvenir.alasan_penolakan!=null" class="d-flex mb-2">
                    <div class="pt-1">Admin Humas </div>
                    <div class="label abu2 pl-2 pt-1 komentar align-middle">{{souvenir.alasan_penolakan}}</div>
                </template>
              </template>
            </template>
            <template v-if="perizinan.permintaan_protokoler!=null">
                <template v-if="perizinan.permintaan_protokoler.alasan_penolakan!=null" class="d-flex mb-2">
                    <div class="pt-1">Admin Humas </div>
                    <div class="label abu2 pl-2 pt-1 komentar align-middle">{{perizinan.permintaan_protokoler.alasan_penolakan}}</div>
                </template>
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
//import IzinMahasiswaService from '../services/izinMahasiswa.service';

import moment from 'moment';
import $ from 'jquery';


export default {
    name: 'DetailPerizinan',
    data() {
        return {
            perizinan: "",
            //izin_kegiatan
            nama_kegiatan: "",
            organisasi: "",
            //detail_kegiatan:"",
            waktu_tanggal_mulai:"",
            waktu_tanggal_akhir:"",
            email_pic:"",
            nama_pic:"",
            hp_pic:"",
            npm_pic:"",
            npm_ketua_organisasi:"",
            nama_ketua_organisasi:"",
            tempat_pelaksanaan:"",
            sumber_pendanaan:"",
            file_info_kegiatan:null,

            //peminjaman_ruangan
            peminjaman_ruangan:[],
            judul_peminjaman:"",
            jumlah_peserta:"",
            waktu_mulai:"",
            waktu_akhir:"",
            catatan:"",
            ruangan:"",
            terbuka_untuk_umum:"",
            perulangan: "",
            jenjang: "",
            tanggal_mulai_peminjaman:"",
            tanggal_akhir_peminjaman:"",
            list_peminjaman_ruangan: [],
            //number_of_peminjaman:"",
            

            //permintaan_protokoler           
            permintaan_protokoler: "",
            deskripsi_kebutuhan:"",

            // perizinan publikasi
            jenis_publikasi_data: [],
            tanggal_mulai_publikasi: '',
            tanggal_akhir_publikasi: '',
            status_perizinan_publikasi: 1,
            alasan_penolakan_publikasi: '',
            keterangan: '',            
            jenis_publikasi: [],
            file_materi_kegiatan: null,
            file_flyer_pengumuman: null,

            permintaan_souvenir : "",
            souvenir_data : [],
            error_message : "",
            souvenir_data_filtered: [],
            kelas_penerima_souvenir: "",
            region_penerima_souvenir: "",
            list_ruangan: [],
            user: this.$store.state.auth.user.id_user, 
            respon_kegiatan: null,
            indexPeminjamanRuangan: null,
            list_permintaan_souvenir:[],
            indexPermintaanSouvenir: null,
        }
    },
    methods: {
            openModalSouvenir(index){
                this.indexPermintaanSouvenir = index
                $('#popup-permintaan-souvenir').modal('show')
            },
            openModal(index){ 
                this.indexPeminjamanRuangan = index
                $('#popup-peminjaman-ruangan').modal('show')
            },
             getDateDef : function (date) {
                 return moment(date, 'YYYY-MM-DDTHH:mm').format('D MMMM YYYY');
             },
             getDate : function (date) {
                 return moment(date, 'YYYY-MM-DDTHH:mm').format('HH:mm, D MMMM YYYY');
             },
             getHour : function (date) {
                 return moment(date, 'YYYY-MM-DDTHH:mm').format('HH:mm');
             },
            

             
            
            editIzinKegiatan(id, id_detail) {
              console.log("masuk edit kegiatan")
                const data_kegiatan = {
                    id: id,
                    nama_kegiatan: this.nama_kegiatan,
                    organisasi: this.organisasi,
                    user: this.user,
                    status_perizinan_kegiatan : 1,
                    detail_kegiatan: id_detail,
                };
                console.log(data_kegiatan)
                    UserService.putIzinKegiatanHeader(id,data_kegiatan).then(
                        response =>{
                            this.respon_kegiatan = response.data;
                            console.log(response.data);                   
                            },
                        error =>{
                        console.log(error.message);
                        }
                    );            
            },
            editDetailIzinKegiatan(id_detail, id_izin_kegiatan){
                console.log("masuk edit detail")
                let formDataDetail = new FormData()
                formDataDetail.append("izin_kegiatan", id_izin_kegiatan)
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
                UserService.putIzinKegiatanDetail(id_detail, formDataDetail).then(
                    response =>{
                        console.log(response.data);                                                            
                        $('#ubahModal').modal('show')
                    },
                    error =>{
                        console.log(error.message);
                        this.error_message = error.message
                        $('#notification-failed').modal('show')
                    }
                )           
            },
            editPeminjamanRuangan(id,indexPeminjamanRuangan) {
              console.log("masuk put Perminjaman Ruangan");

              const data_put = {
                  id: id,
                  judul_peminjaman: this.list_peminjaman_ruangan[indexPeminjamanRuangan].judul_peminjaman,
                  jumlah_peserta: this.list_peminjaman_ruangan[indexPeminjamanRuangan].jumlah_peserta,
                  status_peminjaman_ruangan: 1,
                  alasan_penolakan: null,
                  waktu_mulai: this.list_peminjaman_ruangan[indexPeminjamanRuangan].waktu_mulai,
                  waktu_akhir: this.list_peminjaman_ruangan[indexPeminjamanRuangan].waktu_akhir,
                  catatan: this.list_peminjaman_ruangan[indexPeminjamanRuangan].catatan,                 
                  ruangan: this.list_peminjaman_ruangan[indexPeminjamanRuangan].ruangan,
                  terbuka_untuk_umum: this.list_peminjaman_ruangan[indexPeminjamanRuangan].terbuka_untuk_umum,
                  perulangan: {
                    id: id,
                    jenjang: this.list_peminjaman_ruangan[indexPeminjamanRuangan].perulangan.jenjang,
                    tanggal_mulai: this.list_peminjaman_ruangan[indexPeminjamanRuangan].perulangan.tanggal_mulai,
                    tanggal_akhir: this.list_peminjaman_ruangan[indexPeminjamanRuangan].perulangan.tanggal_akhir
                  }

              };
              console.log(data_put);
              UserService.putPeminjamanRuangan(id, data_put).then(
                  response => {
                        console.log(response.data);
                        console.log(response.data);                                                            
                        //$('#ubahModal').modal('show')


                  },
                  error => {
                      console.log(error.message);
                       $('#notification-failed').modal('show')


                  }

              );
            },
            editPerulangan(id,indexPeminjamanRuangan) {
              console.log("masuk put Perulangan");

              const data_put = {         
                    id: id,
                    jenjang: this.list_peminjaman_ruangan[indexPeminjamanRuangan].perulangan.jenjang,
                    tanggal_mulai: this.list_peminjaman_ruangan[indexPeminjamanRuangan].perulangan.tanggal_mulai,
                    tanggal_akhir: this.list_peminjaman_ruangan[indexPeminjamanRuangan].perulangan.tanggal_akhir
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

            editPerizinanPublikasi(id, id_izin_kegiatan) {
              if(this.jenis_publikasi.length != 0){
                    let formDataPublikasi = new FormData()
                    formDataPublikasi.append("izin_kegiatan",id_izin_kegiatan)
                    formDataPublikasi.append("tanggal_mulai", this.tanggal_mulai_publikasi)
                    formDataPublikasi.append("tanggal_akhir", this.tanggal_akhir_publikasi)
                    formDataPublikasi.append("keterangan", this.keterangan)
                    let list_jenis_publikasi =[];
                    for(let i=0;i<this.jenis_publikasi.length;i++){
                        list_jenis_publikasi.push(this.jenis_publikasi[i].id)
                    }
                    console.log(list_jenis_publikasi)
                    formDataPublikasi.append("jenis_publikasi", list_jenis_publikasi)  
                    if(this.file_materi_kegiatan != null){
                        formDataPublikasi.append("file_materi_kegiatan",this.file_materi_kegiatan)
                    }
                    if(this.file_flyer_pengumuman != null){
                        formDataPublikasi.append("file_flyer_pengumuman", this.file_flyer_pengumuman)
                    }
                    for (var value of formDataPublikasi.values()) {
                    console.log(value);
                    }
                    UserService.putPerizinanPublikasi(id,formDataPublikasi).then( 
                        response => {
                            console.log(response.data);
                            $('#ubahModal').modal('show')
                        },
                        error => {
                            console.log(error.message);
                            this.error_message = error.message
                            $('#notification-failed').modal('show')
                        }                     
                    )
                }
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
        editPermintaanSouvenir(id,indexPermintaanSouvenir) {
            console.log("masuk put permintaan_souvenir");

            const data_put = {
                id: id,
                alasan_penolakan: null,
                status_permintaan_souvenir: 1,
                jumlah: this.list_permintaan_souvenir[indexPermintaanSouvenir].jumlah,
                souvenir: this.list_permintaan_souvenir[indexPermintaanSouvenir].souvenir,
                nama_penerima_souvenir:this.list_permintaan_souvenir[indexPermintaanSouvenir].nama_penerima_souvenir,
                kelas_penerima_souvenir: this.list_permintaan_souvenir[indexPermintaanSouvenir].kelas_penerima_souvenir,
                region_penerima_souvenir: this.list_permintaan_souvenir[indexPermintaanSouvenir].region_penerima_souvenir,
                jabatan_penerima_souvenir: this.list_permintaan_souvenir[indexPermintaanSouvenir].jabatan_penerima_souvenir,

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
                    $('#notification-failed').modal('show')

                    //window.location.reload();
                }

        );
        },
        ubahDone() {
            window.location.reload();
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
    computed: {
        publikasi_luar_ruangan: function(){
            return this.jenis_publikasi_data.filter(function(u){
                return u.luar_ruangan
            })
        },
        publikasi: function(){
            return this.jenis_publikasi_data.filter(function(u){
                return !u.luar_ruangan
            })
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
        UserService.getJenisPublikasi().then(
            response =>{
                this.jenis_publikasi_data = response.data;
            },
            error => {
                this.error_call_api = (error.response && error.response.data) || error.message || error.toString();
            }
        ),
        UserService.getListSouvenir().then(
            response => {
                this.souvenir_data = response.data;
                this.souvenir_data_filtered = this.souvenir_data;
                console.log(this.souvenir_data_filtered)
            },
            error => {
                this.error_call_api = (error.response && error.response.data) || error.message || error.toString();
            }
        ),
        UserService.getAllRuangan().then(
            response =>{
                this.list_ruangan = response.data
            },
            error => {
                this.error_call_api = (error.response && error.response.data) || error.message || error.toString();
            }
        )
    },
    mounted(){
        UserService.getPerizinan(this.$route.params.id).then(
            response =>{
                this.nama_kegiatan=response.data.nama_kegiatan;
                this.organisasi=response.data.organisasi;
                //detail_kegiatan:""
                this.waktu_tanggal_mulai= response.data.detail_kegiatan.waktu_tanggal_mulai;
                this.waktu_tanggal_akhir= response.data.detail_kegiatan.waktu_tanggal_akhir;
                this.email_pic= response.data.detail_kegiatan.email_pic;
                this.nama_pic= response.data.detail_kegiatan.nama_pic;
                this.hp_pic= response.data.detail_kegiatan.hp_pic;
                this.npm_pic= response.data.detail_kegiatan.npm_pic;
                this.npm_ketua_organisasi= response.data.detail_kegiatan.npm_ketua_organisasi;
                this.nama_ketua_organisasi= response.data.detail_kegiatan.nama_ketua_organisasi;
                this.tempat_pelaksanaan= response.data.detail_kegiatan.tempat_pelaksanaan;
                this.sumber_pendanaan= response.data.detail_kegiatan.sumber_pendanaan;
                //this.file_info_kegiatan= response.data.detail_kegiatan.file_info_kegiatan;

                //let r;
                this.list_peminjaman_ruangan = response.data.peminjaman_ruangan;
                this.list_permintaan_souvenir = response.data.permintaan_souvenir;
                //this.number_of_peminjaman = response.data.peminjaman_ruangan.length;
                this.deskripsi_kebutuhan = response.data.perizinan_publikasi.deskripsi_kebutuhan;
                this.tanggal_mulai_publikasi = response.data.perizinan_publikasi.tanggal_mulai;
                this.tanggal_akhir_publikasi = response.data.perizinan_publikasi.tanggal_akhir;
                this.deskripsi_kebutuhan = response.data.permintaan_protokoler.deskripsi_kebutuhan;
                              
            },
            error => {
                console.log(error.message);
            }
        );
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