import {createRouter, createWebHistory} from 'vue-router';

import Login from '../pages/Login.vue';
import Home from '../pages/Home.vue'; 
import Profile from '../pages/Profile.vue';
import Ruangan from '../pages/Ruangan';
import AddRuangan from '../pages/AddRuangan';
import DetailRuangan from '../pages/DetailRuangan';
import UbahRuangan from '../pages/UbahRuangan';




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
    path: "/ruangan/ubah",
    name: "UbahRuangan",
    component: UbahRuangan
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
    '/ruangan/5',
    '/ruangan/ubah',
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