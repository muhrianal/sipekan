import {createApp} from 'vue';
import App from './App.vue';
// import { router } from './router';
// import store from './store';
import 'bootstrap';
import 'chart.js';
import 'vue-chartjs';
import 'bootstrap/dist/css/bootstrap.min.css';
// import VeeValidate from 'vee-validate';
// import { library } from '@fortawesome/fontawesome-svg-core';
// import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
// import Login from './pages/Login.vue'
// import { BNavbar } from 'bootstrap-vue'

// import SuksesMembuatPeminjamanRuangan from './components/modal/SuksesMembuatPeminjamanRuangan.vue';

import router from "./router";
import store from "./store";

// import {
    // faChevronCircleLeft,
    // faUser,
    // faUserPlus,
    // faSignInAlt,
    // faSignOutAlt
// } from '@fortawesome/free-solid-svg-icons';

// library.add(faChevronCircleLeft, faUser);


// app.use(VeeValidate);
// app.component('font-awesome-icon', FontAwesomeIcon);

// app.use(store);

const app = createApp(App)

// app.component('modal-sukses-ruangan', SuksesMembuatPeminjamanRuangan)



app.use(router).use(store).mount('#app')