import {createRouter, createWebHistory} from 'vue-router';

import Login from '../pages/Login.vue';
import Home from '../pages/Home.vue'; 
import Profile from '../pages/Profile.vue';
import PerizinanKegiatanMahasiswa from '../pages/Mahasiswa/PerizinanKegiatanMahasiswa.vue';
import PermohonanHumas from '../pages/Mahasiswa/PermohonanHumas.vue';


const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
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
    '/buat-perizinan'
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