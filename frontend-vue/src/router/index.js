import {createRouter, createWebHistory} from 'vue-router';

import Login from '../pages/Login.vue';
import PeminjamanRuanganUnitKerja from '../pages/UnitKerja/PeminjamanRuanganUnitKerja';
import Profile from '../pages/Profile.vue';
import IzinKegiatan from '../pages/IzinKegiatan.vue';
import IzinKegiatanVerifikasi from '../pages/IzinKegiatanVerifikasi.vue';
import Ruangan from '../pages/AdminFastur/Ruangan';
import AddRuangan from '../pages/AdminFastur/AddRuangan';
import DetailRuangan from '../pages/AdminFastur/DetailRuangan';
import UbahRuangan from '../pages/AdminFastur/UbahRuangan';
import StatusPerizinan from '../pages/StatusPerizinan';
import DetailPerizinan from '../pages/DetailPerizinan';
import UbahPeminjamanRuangan from '../pages/UbahPeminjamanRuangan';
import JadwalTersedia from '../pages/JadwalTersedia.vue';
import DaftarPerizinanRuangan from '../pages/AdminFastur/DaftarPerizinanRuangan';
import DetailPerizinanRuangan from '../pages/AdminFastur/DetailPerizinanRuangan'
import PerizinanKegiatanMahasiswa from '../pages/Mahasiswa/PerizinanKegiatanMahasiswa.vue';
import PermohonanHumas from '../pages/Mahasiswa/PermohonanHumas.vue';
import PeminjamanRuanganMahasiswa from '../pages/Mahasiswa/PeminjamanRuanganMahasiswa.vue';
import Dashboard from '../pages/AdminAll/Dashboard.vue';

import Souvenir from '../pages/AdminHumas/Souvenir';
import AddSouvenir from '../pages/AdminHumas/AddSouvenir';
import UbahSouvenir from '../pages/AdminHumas/UbahSouvenir';
import UbahPermintaanProtokoler from '../pages/Mahasiswa/UbahPermintaanProtokoler';
import DaftarPerizinanHumas from '../pages/AdminHumas/DaftarPerizinanHumas';
import DetailPerizinanHumas from '../pages/AdminHumas/DetailPerizinanHumas';
import DetailKegiatan from '../pages/Mahasiswa/DetailKegiatan';

import BuatPengumuman from '../pages/AdminAll/BuatPengumuman.vue';
import EditPengumuman from '../pages/AdminAll/EditPengumuman.vue';
import Pengumuman from '../pages/Mahasiswa/Pengumuman.vue';

const routes = [
  {
    path: "/pengumuman/create",
    name: "BuatPengumuman",
    component: BuatPengumuman,
  },
  {
    path: "/pengumuman/edit/:id",
    name: "EditPengumuman",
    component: EditPengumuman,
  },
  {
    path: "/perizinan-fastur/:id",
    name: "DetailPerizinanRuangan",
    component: DetailPerizinanRuangan,
  },
  {
    path:"/perizinan-fastur",
    name:"DaftarPerizinanRuangan",
    component: DaftarPerizinanRuangan,
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
    path: "/jadwal-tersedia/",
    name: "Jadwal Tersedia",
    component: JadwalTersedia,
  },
  {
    path: "/buat-perizinan/form-ruangan-mahasiswa/",
    name: "Form Peminjaman Ruangan Mahasiswa",
    component: PeminjamanRuanganMahasiswa,
    props: true
  },
  {

    path: "/dashboard/",
    name: "Dashboard",
    component: Dashboard,
  },
  {  
    path: "/souvenir",
    name: "Souvenir",
    component: Souvenir
  },
  {
    path: "/souvenir/add",
    name: "AddSouvenir",
    component: AddSouvenir
  },
  {
    path: "/souvenir/ubah/:id",
    name: "UbahSouvenir",
    component: UbahSouvenir
  },
  {
    path: "/perizinan/:id/permintaan-protokoler/ubah/:id2",
    name: "UbahPermintaanProtokoler",
    component: UbahPermintaanProtokoler,
  },
  {
    path: "/perizinan-humas/:id",
    name: "DetailPerizinanHumas",
    component: DetailPerizinanHumas,
  },
  {
    path:"/perizinan-humas",
    name:"DaftarPerizinanHumas",
    component: DaftarPerizinanHumas,
  },
  {
    path:"/detail-kegiatan/:id",
    name:"DetailKegiatan",
    component: DetailKegiatan,
   },
  {
    path: "/pengumuman",
    name: "Pengumuman",
    component: Pengumuman,
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
    '/izin-kegiatan',
    '/izin-kegiatan/:id',
    '/ruangan',
    '/ruangan/add',
    '/perizinan',
    '/buat-perizinan',
    '/buat-perizinan/form-ruangan/',
    '/jadwal-tersedia',
    "/perizinan-fastur",
    "/dashboard",

    '/souvenir',
    '/souvenir/add',
    '/perizinan-humas',
    '/pengumuman',
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