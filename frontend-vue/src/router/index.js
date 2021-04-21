import {createRouter, createWebHistory} from 'vue-router';

import Login from '../pages/Login.vue';
import Home from '../pages/Home.vue'; 
import Profile from '../pages/Profile.vue';
import Ruangan from '../pages/Ruangan';
 


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