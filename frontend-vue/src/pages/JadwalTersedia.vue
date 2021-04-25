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
                        <select class="form-control" id="exampleFormControlSelect1" v-model="ruangan" @click="listAll">
                            <option selected disabled value="">Pilih...</option>
                            <template v-for="i in ruangan">
                                <option v-bind:key="i">{{i.nama}}</option>
                            </template>
                        </select>
                        <p class="note-ruangan note-form text-right">Lihat daftar ruangan disini</p>

                    </div>
                </div>
                <br>
                <br>
                <!-- <div id="app">
                    <calendar-view
                        :show-date="showDate"
                        class="theme-default holiday-us-traditional holiday-us-official">
                        <template #header="{ headerProps }">
                            <calendar-view-header
                                :header-props="headerProps"
                                @input="setShowDate" />
                        </template>
                    </calendar-view>
                </div> -->
                <div id="app">
                    <calendar-view
                        :show-date="showDate"
                        :events="events"
                        :items="items"
                        :enable-date-selection="true"
                        :selection-start="selectionStart"
                        :selection-end="selectionEnd"
                        :displayWeekNumbers="false"
                        :itemTop="themeOptions.top"
                        :itemContentHeight="themeOptions.height"
                        :itemBorderHeight="themeOptions.border"
                        :class="`theme-` + theme"
                        :currentPeriodLabel="themeOptions.currentPeriodLabel"
                        @date-selection-start="setSelection"
                        @date-selection="setSelection"
                        @date-selection-finish="finishSelection"
                        @click-date= "onClickDate"
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
// 	// The next two lines are optional themes

import UserService from "../services/user.service";

export default {
		name: 'JadwalTersedia',
		data: function() {
		// 	return { showDate: new Date(), ruangan: '' }
        // },
        return { showDate: new Date(),
            ruangan: [],
			selectionStart: null,
			selectionEnd: null,
			theme: "gcal",
			items: Array(25)
				.fill()
				.map((_, i) => this.getRandomEvent(i)),
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
		setShowDate(d) {
			this.showDate = d
		},
		setSelection(dateRange) {
			this.selectionEnd = dateRange[1]
			this.selectionStart = dateRange[0]
		},
		finishSelection(dateRange) {
			this.setSelection(dateRange)
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
        onClickDate(...params){
            console.log(params);
        },
        listAll(){
            UserService.getAllRuanganKalender().then (
                response => {
                    this.ruangan = response.data;
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