import {createRouter, createWebHistory} from 'vue-router';

import Login from '../pages/Login.vue';
import Home from '../pages/Home.vue'; 
import Profile from '../pages/Profile.vue';
import Ruangan from '../pages/AdminFastur/Ruangan';
import AddRuangan from '../pages/AdminFastur/AddRuangan';
import DetailRuangan from '../pages/AdminFastur/DetailRuangan';
import UbahRuangan from '../pages/AdminFastur/UbahRuangan';
import StatusPerizinan from '../pages/StatusPerizinan';
import DetailPerizinan from '../pages/DetailPerizinan';
import UbahPeminjamanRuangan from '../pages/UbahPeminjamanRuangan';




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
    path: "/ruangan",
    name: "Ruangan",
    component: Ruangan
  },
  {
    path: "/ruangan/add",
    name: "AddRuangan",
    component: AddRuangan
  },
  {
    path: "/ruangan/:id",
    name: "DetailRuangan",
    component: DetailRuangan
  },
  {
    path: "/ruangan/ubah/:id",
    name: "UbahRuangan",
    component: UbahRuangan
  },
  {
    path: "/perizinan",
    name: "StatusPerizinan",
    component: StatusPerizinan
  },
  {
    path: "/perizinan/:id",
    name: "DetailPerizinan",
    component: DetailPerizinan
  },
  {
    path: "/peminjaman-ruangan/ubah/:id",
    name: "UbahPeminjamanRuangan",
    component: UbahPeminjamanRuangan
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
    '/ruangan',
    '/ruangan/add',
    '/perizinan',
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