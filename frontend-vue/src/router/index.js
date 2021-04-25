import {createRouter, createWebHistory} from 'vue-router';

import Login from '../pages/Login.vue';
// import Home from '../pages/Home.vue'; 
import Profile from '../pages/Profile.vue';
import PeminjamanRuanganUnitKerja from '../pages/UnitKerja/PeminjamanRuanganUnitKerja';
import Test from '../pages/Test.vue';
import JadwalTersedia from '../pages/JadwalTersedia.vue';
// import Home from '../pages/Home.vue'; 
// import Profile from '../pages/Profile.vue';


const routes = [
  {
    path: "/",
    name: "Home",
    component: Test

  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile
  },
  {
    path: "/buat-perizinan/form-ruangan/",
    name: "Form Peminjaman Ruangan Unit Kerja",
    component: PeminjamanRuanganUnitKerja,
  },
  {
    path: "/jadwal-tersedia/",
    name: "Jadwal Tersedia",
    component: JadwalTersedia,
  }

];


const router = createRouter({
  history: createWebHistory(),
  routes
  
});


router.beforeEach((to, from, next) =>{
  const publicPages = [
    '/login',
    '/',
    '/buat-perizinan/form-ruangan/',
    '/jadwal-tersedia',

  ];

  const authRequired = !publicPages.includes(to.path);
  const isLoggedIn = localStorage.getItem('user');

  if (authRequired && !isLoggedIn){
    next('/login');
  } else {
    next();
  }
});

export default router;