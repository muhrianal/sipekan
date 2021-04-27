import {createRouter, createWebHistory} from 'vue-router';

import Login from '../pages/Login.vue';
import PeminjamanRuanganUnitKerja from '../pages/UnitKerja/PeminjamanRuanganUnitKerja';
import Test from '../pages/Test.vue';
// import Home from '../pages/Home.vue'; 
import Profile from '../pages/Profile.vue';
import PerizinanKegiatanMahasiswa from '../pages/Mahasiswa/PerizinanKegiatanMahasiswa.vue';
import PermohonanHumas from '../pages/Mahasiswa/PermohonanHumas.vue';
import PeminjamanRuanganMahasiswa from '../pages/Mahasiswa/PeminjamanRuanganMahasiswa.vue';



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

    path: "/buat-perizinan/form-kegiatan",
    name: "Form Izin Kegiatan Mahasiswa",
    component: PerizinanKegiatanMahasiswa,
  },
  {
    path: "/buat-perizinan/form-humas",
    name: "Form Permohonan Humas Mahasiswa",
    component: PermohonanHumas,
    props: true
  },
  {
    path: "/buat-perizinan/form-ruangan/",
    name: "Form Peminjaman Ruangan Unit Kerja",
    component: PeminjamanRuanganUnitKerja,
  },
  {
    path: "/buat-perizinan/form-ruangan-mahasiswa/",
    name: "Form Peminjaman Ruangan Mahasiswa",
    component: PeminjamanRuanganMahasiswa,
    props: true
  },
];


const router = createRouter({
  history: createWebHistory(),
  routes
  
});


router.beforeEach((to, from, next) =>{
  const publicPages = [
    '/login',
    '/',
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