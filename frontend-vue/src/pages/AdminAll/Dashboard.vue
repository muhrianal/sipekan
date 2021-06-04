<template>
  <div>
    <div class="row">
      <div class="col-12">
        <div class="card mb-2 p-4" style="">
          <div class="row">
            <div class="col-8">
              <h3>Kegiatan Terverifikasi</h3>
            </div>
            <div class="col-4">
              <select class="form-control" v-model="choices">
                <option disabled value="-1">Pilih status</option>
                <option value="1">Menunggu Persetujuan</option>
                <option selected value="2">Disetujui</option>
                <option value="3">Ditolak</option>
              </select>
            </div>
          </div>
          <div v-if="choices == 3">
            <BarChart
              v-if="bulan1.length > 0"
              :chart-data="bulan1"
              :info="'Ditolak'"
            />
          </div>
          <div v-if="choices == 1">
            <BarChart
              v-if="bulan2.length > 0"
              :chart-data="bulan2"
              :info="'Menunggu Persetujuan'"
            />
          </div>
          <div v-if="choices == 2">
            <BarChart
              v-if="bulan.length > 0"
              :chart-data="bulan"
              :info="'Disetujui'"
            />
          </div>
        </div>
        <div class="card mb-2 p-4" style="height: 50 !important">
          <div class="row">
            <div class="col-8">
              <h3>Ruangan Populer</h3>
            </div>
            <div class="col-4">
              <select class="form-control" v-model="choicess" @change="filterPerizinan">
                <option disabled value="-1">Pilih periode</option>
                <option value="1">Hari ini</option>
                <option value="2">7 Hari Terakhir</option>
                <option value="3">30 Hari Terakhir</option>
                <option value="-4">Semua</option>
              </select>
            </div>
          </div>
          <div v-if="choicess == -4">
          <CasesLine
            v-if="total.length > 0"
            :label="ruangans_unique"
            :chart-data="total"
          ></CasesLine>
          <h5 v-else-if="total.length == 0" class="text-center"> <br>Data belum tersedia. <br></h5>
          </div>
          
          <div v-if="choicess == 1">
          <CasesLine
            v-if="harian1_total.length > 0"
            :label="harian1_unique"
            :chart-data="harian1_total"
          ></CasesLine>
          <h5 v-else-if="harian1_total.length == 0" class="text-center"> <br>Data belum tersedia. <br></h5>
          </div>
          <div v-if="choicess == 2">
          <CasesLine
            v-if="harian7_total.length > 0"
            :label="harian7_unique"
            :chart-data="harian7_total"
          ></CasesLine>
          </div>
          <h5 v-else-if="harian7_total.length == 0" class="text-center"> <br>Data belum tersedia. <br></h5>
          <div v-if="choicess == 3">
          <CasesLine
            v-if="harian30_total.length > 0"
            :label="harian30_unique"
            :chart-data="harian30_total"
          ></CasesLine>
          <h5 v-else-if="harian30_total.length == 0" class="text-center"> <br>Data belum tersedia. <br></h5>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6">
        <div class="card" style="height: 13.3rem">
          <div class="card-body">
            <h5
              class="card-title d-flex justify-content-center"
              style="font-weight: 700 !important"
            >
              Sedang Diverifikasi
            </h5>
            <table class="table table-bordered">
              <thead>
                <tr>
                  <th
                    class="text-center"
                    style="font-weight: 700 !important; width: 33.33%"
                    scope="col"
                  >
                    Admin PKM
                  </th>
                  <th
                    class="text-center"
                    style="font-weight: 700 !important; width: 33.33%"
                    scope="col"
                  >
                    Admin Fastur
                  </th>
                  <th
                    class="text-center"
                    style="font-weight: 700 !important; width: 33.33%"
                    scope="col"
                  >
                    Admin Humas
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td
                    class="text-center"
                    style="font-weight: 700 !important; font-size: 30px"
                    scope="col"
                  >
                    {{ listWaitingPKM.length }}
                  </td>
                  <td
                    class="text-center"
                    style="font-weight: 600 !important; font-size: 30px"
                    scope="col"
                  >
                    {{ listWaitingFastur.length }}
                  </td>
                  <td
                    class="text-center"
                    style="font-weight: 700 !important; font-size: 30px"
                    scope="col"
                  >
                    {{ listAllHumas }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <h5
              class="card-title d-flex justify-content-center"
              style="font-weight: 700 !important"
            >
              Ruangan
            </h5>
            <table class="table table-bordered">
              <thead>
                <tr>
                  <th
                    class="text-center"
                    style="font-weight: 700 !important; width: 50%"
                    scope="col"
                  >
                    Aktif
                  </th>
                  <th
                    class="text-center"
                    style="font-weight: 700 !important; width: 50%"
                    scope="col"
                  >
                    Tidak Aktif
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td
                    class="text-center"
                    style="font-weight: 700 !important; font-size: 30px"
                    scope="col"
                  >
                    {{ listRuanganAktif.length }}
                  </td>
                  <td
                    class="text-center"
                    style="font-weight: 600 !important; font-size: 30px"
                    scope="col"
                  >
                    {{ listRuanganNonAktif.length }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <div class="col-md-2">
        <div class="card" style="height: 13.3rem">
          <div class="card-body">
            <h5
              class="card-title d-flex justify-content-center"
              style="font-weight: 700 !important"
            >
              Souvenir
            </h5>
            <br />
            <p class="text-center" :style="[jumlah_souvenir > jumlah_souvenir_min ? {'color': '#6FCF97'} : {'color': '#F2994A'}]">
              <span style="font-weight: 700 !important; font-size: 40px"
                >{{ jumlah_souvenir}}</span
              >
              buah
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios';
import BarChart from "../../components/BarChart";
import CasesLine from "../../components/CasesLine";
import UserService from "../../services/user.service";
// import PlanetChart from "../../components/PlanetChart.vue";
// import ChartDoughnut from '../../components/ChartDoughnut';
import moment from "moment";

export default {
  name: "Dashboard",
  components: {
    // PlanetChart,
    CasesLine,
    BarChart,
  },
  methods: {
    getDatas: function (a) {
      var array_elements = a;
      var result = [];

      array_elements.sort();

      var current = null;
      var cnt = 0;
      for (var i = 0; i < array_elements.length; i++) {
        if (array_elements[i] != current) {
          if (cnt > 0) {
            result.push({ label: current, total: cnt });
          }
          current = array_elements[i];
          cnt = 1;
        } else {
          cnt++;
        }
      }
      if (cnt > 0) {
        result.push({ label: current, total: cnt });
      }
      return result;
    },
  },
  data() {
    return {
      souvenir: [],
      jumlah_souvenir: 0,
      jumlah_souvenir_min: 0,
      listAllRuangan: [],
      listRuanganAktif: [],
      listRuanganNonAktif: [],
      listAllFastur: [],
      listAllHumas: [],
      listWaitingPKM: [],
      listWaitingFastur: [],
      listWaitingHumas: [],
      disetujuiAll: [],
      disetujuiEdit: [],
      disetujuiFinal: [],
      ditolakAll: [],
      ditolakEdit: [],
      ditolakFinal: [],
      menungguAll: [],
      menungguEdit: [],
      menungguFinal: [],
      bulan: [],
      bulan1: [],
      bulan2: [],
      harian1: [],
      harian1_unique: [],
      harian1_total: [],
      harian1_count: [],
      harian7: [],
      harian7_total: [],
      harian7_unique: [],
      harian7_count: [],
      harian30: [],
      harian30_total: [],
      harian30_unique: [],
      harian30_count: [],
      perizinan: [],
      ruangans: [],
      ruangans_unique: [],
      ruangans_filtered: [],
      //   ruangans_unique: [],
      count: [],
      total: [],
      choices: 2,
      choicess: -4,

      //   total: [],
    };
  },

  created() {
    UserService.getChartDisetujui().then(
      (response) => {
        this.disetujuiAll = response.data;
        this.disetujuiAll.forEach((a) => {
          const today = new Date();
          if (a.detail_kegiatan != null) {
            const date = moment(
              a.detail_kegiatan.waktu_tanggal_mulai,
              "YYYY-MM-DDTHH:mm"
            ).format("MM");
            const year = moment(
              a.detail_kegiatan.waktu_tanggal_mulai,
              "YYYY-MM-DDTHH:mm"
            ).format("YYYY");
            if (year == today.getFullYear()) {
              this.disetujuiEdit.push(date);
            }
          }
        });
        this.disetujuiFinal = this.getDatas(this.disetujuiEdit);
        let bln = new Array(12);
        let jml = new Array(12);
        bln.fill(0);
        jml.fill(0);
        this.disetujuiFinal.forEach((e) => {
          var mm = parseInt(e.label);
          jml[mm - 1] = e.total;
        });
        this.bulan = jml;
        // console.log(this.bulan);
        // console.log(this.disetujuiEdit);
        // console.log(this.disetujuiFinal);
      },
      (error) => {
        this.error_message =
          (error.response && error.response.data) ||
          error.message ||
          error.toString();
      }
    );
    UserService.getChartDitolak().then(
      (response) => {
        this.ditolakAll = response.data;
        this.ditolakAll.forEach((a) => {
          const today = new Date();
          if (a.detail_kegiatan != null) {
            const date = moment(
              a.detail_kegiatan.waktu_tanggal_mulai,
              "YYYY-MM-DDTHH:mm"
            ).format("MM");
            const year = moment(
              a.detail_kegiatan.waktu_tanggal_mulai,
              "YYYY-MM-DDTHH:mm"
            ).format("YYYY");
            if (year == today.getFullYear()) {
              this.ditolakEdit.push(date);
            }
          }
        });
        this.ditolakFinal = this.getDatas(this.ditolakEdit);
        let bln = new Array(12);
        let jml = new Array(12);
        bln.fill(0);
        jml.fill(0);
        this.ditolakFinal.forEach((e) => {
          var mm = parseInt(e.label);
          jml[mm - 1] = e.total;
        });
        this.bulan1 = jml;
        // console.log(this.bulan1);
        // console.log(this.ditolakEdit);
        // console.log(this.ditolakFinal);
      },
      (error) => {
        this.error_message =
          (error.response && error.response.data) ||
          error.message ||
          error.toString();
      }
    );
    UserService.getChartMenunggu().then(
      (response) => {
        this.menungguAll = response.data;
        this.menungguAll.forEach((a) => {
          const today = new Date();
          if (a.detail_kegiatan != null) {
            const date = moment(
              a.detail_kegiatan.waktu_tanggal_mulai,
              "YYYY-MM-DDTHH:mm"
            ).format("MM");
            const year = moment(
              a.detail_kegiatan.waktu_tanggal_mulai,
              "YYYY-MM-DDTHH:mm"
            ).format("YYYY");
            if (year == today.getFullYear()) {
              this.menungguEdit.push(date);
            }
          }
        });
        this.menungguFinal = this.getDatas(this.menungguEdit);
        let bln = new Array(12);
        let jml = new Array(12);
        bln.fill(0);
        jml.fill(0);
        this.menungguFinal.forEach((e) => {
          var mm = parseInt(e.label);
          jml[mm - 1] = e.total;
        });
        this.bulan2 = jml;
        // console.log(this.bulan2);
        // console.log(this.menungguEdit);
        // console.log(this.menungguFinal);
      },
      (error) => {
        this.error_message =
          (error.response && error.response.data) ||
          error.message ||
          error.toString();
      }
    );
    UserService.getRuanganDetailed().then(
      (response) => {
        this.perizinan = response.data;
        this.perizinan.forEach((d) => {
          d.peminjaman_ruangan.forEach((p) => {
            this.ruangans.push(p.ruangan.nama);
          });
        });
        this.count = this.getDatas(this.ruangans);
        this.count.forEach((h) => {
          if (this.count.length < 4) {
            this.ruangans_unique.push(h.label);
            this.total.push(h.total);
          }
        });
        // console.log(this.ruangans_unique);
        // console.log(this.total);
        // console.log(this.count);
      },
      
      (error) => {
        this.error_message =
          (error.response && error.response.data) ||
          error.message ||
          error.toString();
      }
    );
    UserService.getRuanganDetailed().then(
      (response) => {
        this.perizinan = response.data;
        this.perizinan.forEach((d) => {
          d.peminjaman_ruangan.forEach((p) => {
            const today = new Date();
            const date = moment(p.waktu_mulai, "YYYY-MM-DDTHH:mm").format("DD");
            const month = moment(p.waktu_mulai, "YYYY-MM-DDTHH:mm").format("MM");
            const year = moment(p.waktu_mulai, "YYYY-MM-DDTHH:mm").format("YYYY");
            if (
              today.getFullYear() == year &&
              today.getMonth() + 1 == month &&
              today.getDate() == date
            ) {
              this.harian1.push(p.ruangan.nama);
            }
          });
        });
        if (this.harian1.length > 0){
        this.harian1_count = this.getDatas(this.harian1);
        this.harian1_count.forEach((h) => {
          if (this.count.length < 4) {
            this.harian1_unique.push(h.label);
            this.harian1_total.push(h.total);
          }
        })}
      },
      (error) => {
        this.error_message =
          (error.response && error.response.data) ||
          error.message ||
          error.toString();
      }
    );
      UserService.getRuanganDetailed().then(
      (response) => {
        this.perizinan = response.data;
        this.perizinan.forEach((d) => {
          d.peminjaman_ruangan.forEach((p) => {
            const dateTo = moment(p.waktu_mulai, "YYYY-MM-DDTHH:mm").format(
            "YYYY-MM-DD"
              );
            const dateFrom7 = moment().subtract(7, "d").format("YYYY-MM-DD");
            if (
              dateTo > dateFrom7
            ) {
              this.harian7.push(p.ruangan.nama);
            }
          });
        });
        if (this.harian7.length > 0){
        this.harian7_count = this.getDatas(this.harian7);
        this.harian7_count.forEach((h) => {
          if (this.count.length < 4) {
            this.harian7_unique.push(h.label);
            this.harian7_total.push(h.total);
          }
        })}
      },
      (error) => {
        this.error_message =
          (error.response && error.response.data) ||
          error.message ||
          error.toString();
      }
    );
      UserService.getRuanganDetailed().then(
      (response) => {
        this.perizinan = response.data;
        this.perizinan.forEach((d) => {
          d.peminjaman_ruangan.forEach((p) => {
            const dateTo = moment(p.waktu_mulai, "YYYY-MM-DDTHH:mm").format(
            "YYYY-MM-DD"
              );
            const dateFrom30 = moment().subtract(30, "d").format("YYYY-MM-DD");
            if (
              dateTo > dateFrom30
            ) {
              this.harian30.push(p.ruangan.nama);
            }
          });
        });
        if (this.harian30.length > 0){
        this.harian30_count = this.getDatas(this.harian30);
        this.harian30_count.forEach((h) => {
          if (this.count.length < 4) {
            this.harian30_unique.push(h.label);
            this.harian30_total.push(h.total);
          }
        })}
      },
      (error) => {
        this.error_message =
          (error.response && error.response.data) ||
          error.message ||
          error.toString();
      }
    );
    // console.log(this.ruangans);
    UserService.getWaitingPKM().then(
      (response) => {
        this.listWaitingPKM = response.data;
        // console.log(this.listWaitingPKM)
      },
      (error) => {
        this.error_message =
          (error.response && error.response.data) ||
          error.message ||
          error.toString();
      }
    );
    UserService.getListPerizinanFastur().then(
      (response) => {
        this.listAllFastur = response.data;
        this.listAllFastur.forEach((d) => {
          if (d.peminjaman_ruangan.length != 0) {
            d.peminjaman_ruangan.forEach((e) => {
              if (e.status_peminjaman_ruangan == 1) {
                this.listWaitingFastur.push(e);
              }
            });
          }
        });
        // console.log(this.listAllFastur)
        // console.log(this.listWaitingFastur)
      },
      (error) => {
        this.error_message =
          (error.response && error.response.data) ||
          error.message ||
          error.toString();
      }
    );
    UserService.getWaitingHumas().then(
      (response) => {
        this.listAllHumas = response.data.length;
        // console.log(this.listAllHumas);
      },
      (error) => {
        this.error_message =
          (error.response && error.response.data) ||
          error.message ||
          error.toString();
      }
    );

    UserService.getAllRuangan().then(
      (response) => {
        this.listAllRuangan = response.data;
        this.listAllRuangan.forEach((ruangan) => {
          if (ruangan.status == 1) {
            this.listRuanganAktif.push(ruangan);
          } else {
            this.listRuanganNonAktif.push(ruangan);
          }
        });
        // console.log(this.listRuanganAktif);
        // console.log(this.listRuanganNonAktif);
      },
      (error) => {
        this.error_message =
          (error.response && error.response.data) ||
          error.message ||
          error.toString();
      }
    );
    UserService.getStokSouvenir().then(
      (response) => {
      this.souvenir = response.data;
      this.souvenir.forEach((s) => {
        this.jumlah_souvenir += s.stok
        this.jumlah_souvenir_min += s.stok_minimum
      })
      // console.log(this.jumlah_souvenir)
      // console.log(this.jumlah_souvenir_min)
      },
      (error) => {
        this.error_message =
          (error.response && error.response.data) ||
          error.message ||
          error.toString();
      }

    )
  },
};
</script>

<style>
</style>