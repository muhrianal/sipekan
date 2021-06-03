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
                        <select class="form-control" id="exampleFormControlSelect1" v-model="ruangan" @click="daftar()" @change="cari(ruangan)">
                            <option selected disabled value="">Pilih...</option>
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
                <div id="app">
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

import UserService from "../services/user.service";
import IzinMahasiswaService from '../services/izinMahasiswa.service';

export default {
		name: 'JadwalTersedia',
        
		data: function() {
		
        return { showDate: this.thisMonth(1),
            ruangan: [],
			selectionStart: null,
			selectionEnd: null,
            displayPeriodUom: "month",
			theme: "gcal",
            items: [
        {
          id: "e0",
          startDate: "2021-05-25",
        },
        {
          id: "e1",
          startDate: new Date(),
          title: "Memancing",
          
        },
        {
          id: "e2",
          startDate: new Date(2021, 5, 1),
          endDate: new Date(2021, 5, 10),
          title: "Multi-day item with a long title and times",
        },
      ],
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
	methods: {
        periodChanged() {},
            thisMonth(d, h, m) {
            const t = new Date();
            return new Date(t.getFullYear(), t.getMonth(), d, h || 0, m || 0);
        },
        onClickDay(d) {
            this.selectionStart = null;
            this.selectionEnd = null;
            this.message = `You clicked: ${d.toLocaleDateString()}`;
        },
        onClickItem(e) {
            this.message = `You clicked: ${e.title}`;
        },
        setShowDate(d) {
            this.message = `Changing calendar view to ${d.toLocaleDateString()}`;
            this.showDate = d;
        },
        setSelection(dateRange) {
            this.selectionEnd = dateRange[1];
            this.selectionStart = dateRange[0];
        },
        finishSelection(dateRange) {
            this.setSelection(dateRange);
            this.message = `You selected: ${this.selectionStart.toLocaleDateString()} -${this.selectionEnd.toLocaleDateString()}`;
        },
		getRandomEvent(index) {
			const startDay = Math.floor(Math.random() * 28 + 1)
			const endDay = Math.floor(Math.random() * 4 + 1) + startDay
			var d = new Date()
			return {
				id: index,
				title: "Event " + (index + 1),
				startDate: Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), startDay),
				endDate: Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), endDay),
            }
        },
        daftar(){
            IzinMahasiswaService.getRuangan().then(
            response =>{
                // console.log(response.data);
                this.ruangan = response.data               
            },
            error => {
                this.error_call_api = (error.response && error.response.data) || error.message || error.toString();
            }
        )
        },

        cari(ruang){
            console.log('tes');
            console.log(ruang);
            UserService.getJadwalPeminjamanRuangan().then (
                response => {
                    this.items =[];
                    var tmp = response.data;
                    for (let i = 0; i < tmp.length; i++){
                        if (ruang == tmp[i].ruangan.id){
                            var id = tmp[i].ruangan.id;
                            var startDate= tmp[i].waktu_mulai;
                            var endDate= tmp[i].waktu_akhir;
                            var title= tmp[i].judul_peminjaman;
                            this.items.push(new Array(id, startDate, endDate, title));
                            console.log(tmp[i]);                        
                        }
                    }
                    console.log(this.items);

                },
                error => {
                    this.error_message = (error.response && error.response.data) || error.message || error.toString();
                }
            )
        },

        daftar_kegiatan(data){
            console.log(data);
        }
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
    /* padding: 15px 0px 3px 15px; */
    font-size: 23px;
    color: #FFD505;
    font-weight: 550;
}

.line-header {
    background-color: #BDBDBD ;
}

.note-form{
    font-size: 12px;
}

.note-ruangan{
    margin-bottom: -16px;
}
</style>