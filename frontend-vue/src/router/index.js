import {createRouter, createWebHistory} from 'vue-router';

import Login from '../pages/Login.vue';
import Home from '../pages/Home.vue'; 
import Profile from '../pages/Profile.vue';
import IzinKegiatan from '../pages/IzinKegiatan.vue';
import IzinKegiatanVerifikasi from '../pages/IzinKegiatanVerifikasi.vue';
 


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
    path: "/izin-kegiatan",
    name: "Izin Kegiatan",
    component: IzinKegiatan
  },
  {
    path: "/izin-kegiatan/:id",
    name: "IzinKegiatanVerifikasi",
    component: IzinKegiatanVerifikasi
  },
  // {
  //   path: "/izin-kegiatan/update/:id",
  //   name: "Verifikasi Izin Kegiatan",
  //   component: IzinKegiatanVerifikasi
  // },
];


const router = createRouter({
  history: createWebHistory(),
  routes
  
});


router.beforeEach((to, from, next) =>{
  const publicPages = [
    '/login',
    '/',
    '/izin-kegiatan',
    '/izin-kegiatan/:id',
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