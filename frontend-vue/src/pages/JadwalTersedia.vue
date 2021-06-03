<template>
    <div class="root-class">
        <div class="header">
            <h3 class="header-page">My Calendar</h3>
            <hr class="line-header">
        </div>
        
        <div class="formulir">
            <form>
                <div class="form-row">
                    <div class="col-12 col-md-6">
                        <label for="exampleFormControlSelect1">Ruangan*:</label>
                        <select class="form-control" id="exampleFormControlSelect1" v-model="ruang" @change="cari(ruang)" >
                            <option v-for="ruang in ruangan" v-bind:key="ruang.id" :value="ruang.id">{{ruang.nama}}</option>
                        </select>

                    </div>
                   
                    <div class="col-12 col-md-6">
                        <label for="exampleFormControlSelect1">Periode:</label>
                        <select class="form-control" id="exampleFormControlSelect1" v-model="displayPeriodUom">
                            <option value="week">Mingguan</option>
                            <option value="month">Bulanan</option>
                            <option value="year">Tahunan</option>
                        </select>
                    </div>

                    
                </div>
                <br>
                <br>
                <div class="container-fluid" id="app">
                    <calendar-view
                        :show-date="showDate"
                        :events="events"
                        :items="items"
                        :enable-date-selection="true"
                        :selection-start="selectionStart"
                        :selection-end="selectionEnd"
                        :displayWeekNumbers="false"
                        :display-period-uom="displayPeriodUom"
                        :itemTop="themeOptions.top"
                        :itemContentHeight="themeOptions.height"
                        :itemBorderHeight="themeOptions.border"
                        :class="`theme-` + theme"
                        :currentPeriodLabel="themeOptions.currentPeriodLabel"
                        :period-changed-callback="periodChanged"
                        @date-selection-start="setSelection"
                        @date-selection="setSelection"
                        @date-selection-finish="finishSelection"
                        @click-date= "onClickDate"
                        @click-item="onClickItem"
                        class="holiday-us-traditional holiday-us-official"
                    >
                        <template #header="{ headerProps }">
                            <calendar-view-header
                                :header-props="headerProps"
                                @input="setShowDate" />
                        </template>
                        
                    </calendar-view>
                </div>
            </form>
        </div>

    </div>
    
</template>

<script>
import { CalendarView, CalendarViewHeader } from "vue-simple-calendar";
import "vue-simple-calendar/dist/style.css";
import moment from "moment";

import UserService from "../services/user.service";
import IzinMahasiswaService from '../services/izinMahasiswa.service';

export default {
		name: 'JadwalTersedia',
        
		data: function() {
		
        return { showDate: this.thisMonth(1),
            status: "aktif",
            ruangan: [],
			selectionStart: null,
			selectionEnd: null,
            displayPeriodUom: "month",
			theme: "gcal",
            items: [],
            }
        },

		components: {
			CalendarView,
			CalendarViewHeader,
        },
        
        computed: {
		themeOptions() {
			return this.theme == "gcal"
				? {
						top: "2.6em",
						height: "2.1em",
						border: "0px",
						previousYearLabel: "\uE5CB\uE5CB",
						previousPeriodLabel: "\uE5CB",
						nextPeriodLabel: "\uE5CC",
						nextYearLabel: "\uE5CC\uE5CC",
						currentPeriodLabel: "Today",
				}
				: {
						top: "1.4em",
						height: "1.4em",
						border: "2px",
						previousYearLabel: "<<",
						previousPeriodLabel: "<",
						nextPeriodLabel: ">",
						nextYearLabel: ">>",
						currentPeriodLabel: "",
				}
		},
	},
    created(){
            IzinMahasiswaService.getRuangan().then(
            response =>{
                this.ruangan = response.data               
            },
            error => {
                this.error_call_api = (error.response && error.response.data) || error.message || error.toString();
            }
        )
        },
	methods: {
        periodChanged() {},
            thisMonth(d, h, m) {
            const t = new Date();
            return new Date(t.getFullYear(), t.getMonth(), d, h || 0, m || 0);
        },

        setShowDate(d) {
            this.message = `Changing calendar view to ${d.toLocaleDateString()}`;
            this.showDate = d;
        },

        convert(str) {
            var mnths = {Jan: "01", Feb: "02", Mar: "03", Apr: "04", May: "05", Jun: "06", Jul: "07", Aug: "08",
                Sep: "09", Oct: "10", Nov: "11", Dec: "12"},
            date = str.split(" ");

            return [date[3], mnths[date[1]], date[2]].join("-");
        },

       
        cari(ruang){
            UserService.getJadwalPeminjamanRuangan().then (
                response => {
                    this.items =[];
                    var loncatan = 0;
                    var periodePerulangan = "";
                    var tmp = response.data;
                    var id = "";
                    var startDate = "";
                    var endDate = "";
                    var title = "";
                    var agenda = "";
                    
                    for (let i = 0; i < tmp.length; i++){
                        if (ruang == tmp[i].ruangan.id){
                            if(tmp[i].perulangan.jenjang == 1){
                                id = tmp[i].ruangan.id;
                                startDate= tmp[i].perulangan.tanggal_mulai;
                                endDate= tmp[i].perulangan.tanggal_akhir;
                                title= tmp[i].judul_peminjaman + "\n" + "(" + tmp[i].waktu_mulai.slice(11,16) + " - " + tmp[i].waktu_akhir.slice(11,16) + ")";
                                agenda = {"id":id, "startDate":startDate, "endDate":endDate, "title":title};
                                this.items.push(agenda);
                            } else{
                                // awal peminjaman ruangan
                                id = tmp[i].ruangan.id;
                                startDate= tmp[i].perulangan.tanggal_mulai;
                                endDate= tmp[i].perulangan.tanggal_mulai;
                                title= tmp[i].judul_peminjaman + "\n" + "(" + tmp[i].waktu_mulai.slice(11,16) + " - " + tmp[i].waktu_akhir.slice(11,16) + ")";
                                agenda = {"id":id, "startDate":startDate, "endDate":endDate, "title":title};
                                this.items.push(agenda);
                                // masuk mekanisme perulangan
                                var tanggalanAwal = Date.parse(tmp[i].perulangan.tanggal_mulai);
                                var tanggalanAkhir = Date.parse(tmp[i].perulangan.tanggal_akhir);
                                while(tanggalanAwal < moment(tanggalanAkhir).add(1,"d")){
                                    id = tmp[i].ruangan.id;
                                    startDate= this.convert(tanggalanAwal.toString());
                                    endDate= this.convert(tanggalanAwal.toString());
                                    title= tmp[i].judul_peminjaman + "\n" + "(" + tmp[i].waktu_mulai.slice(11,16) + " - " + tmp[i].waktu_akhir.slice(11,16) + ")";
                                    agenda = {"id":id, "startDate":startDate, "endDate":endDate, "title":title};
                                    this.items.push(agenda);
                                    if(tmp[i].perulangan.jenjang == 2){
                                        loncatan = 1;
                                        periodePerulangan = "days";
                                    } else if(tmp[i].perulangan.jenjang == 3){
                                        loncatan = 7;
                                        periodePerulangan = "days";
                                    } else{
                                        loncatan = 1;
                                        periodePerulangan = "months";
                                    }
                                    tanggalanAwal = moment(tanggalanAwal).add(loncatan, periodePerulangan);
                                }   
                                    
                            }         
                        } 
                    }

                },
                error => {
                    this.error_message = (error.response && error.response.data) || error.message || error.toString();
                }
            )
        },
    },
	}
</script>

<style>
#app {
		font-family: 'Avenir', Helvetica, Arial, sans-serif;
		color: #2c3e50;
		height: 90vh;
		width: 70vw;
		margin-left: auto;
		margin-right: auto;
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
    font-size: 23px;
    color: #FFD505;
    font-weight: 550;
}

.line-header {
    background-color: #BDBDBD ;
}

</style>