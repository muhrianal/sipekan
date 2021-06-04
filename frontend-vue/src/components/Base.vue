<template>
<div>
   <Navbar></Navbar>
    <div class="wrapper">
        <!-- Sidebar  -->
        <nav id="sidebar" v-bind:class="{active: sidebarClosed}">
            <div class="sidebar-header">
                
                <Logout></Logout>
            </div>

            <ul class="list-unstyled components">

                <li v-if="isLoggedIn && (currentUser.role == 'MAHASISWA' || currentUser.role == 'UNIT KERJA')" v-bind:class="{active : isInHomePage}" >
                    <a class="sidebar-child" href="/pengumuman">Pengumuman</a>
                </li>
                
                <li v-if="isLoggedIn && (currentUser.role == 'MAHASISWA' || currentUser.role == 'UNIT KERJA')" v-bind:class="{active : isInHomePage}" >
                    <a class="sidebar-child" href="/perizinan">Status Perizinan</a>
                </li>

                <li v-if="isLoggedIn && currentUser.role == 'UNIT KERJA'" v-bind:class="{active : isInPeminjamanRuanganUnitKerjaPage}" >
                    <a class="sidebar-child" href="/buat-perizinan/form-ruangan/">Buat Perizinan</a>
                </li>

                <li v-if="isLoggedIn && currentUser.role == 'MAHASISWA'" v-bind:class="{active : isInPeminjamanRuanganUnitKerjaPage}" >
                    <a class="sidebar-child" href="/buat-perizinan/form-kegiatan/">Buat Perizinan</a>
                </li>


                <li v-if="isLoggedIn && (currentUser.role == 'ADMIN PKM' || currentUser.role == 'ADMIN FASTUR' || currentUser.role == 'ADMIN HUMAS')" v-bind:class="{active : isInHomePage}" >
                    <a class="sidebar-child" href="/dashboard">Dashboard</a>
                </li>

                <li v-if="isLoggedIn && currentUser.role == 'ADMIN FASTUR'" v-bind:class="{active : isInHomePage}" >
                    <a class="sidebar-child" href="/perizinan-fastur">Daftar Perizinan</a>
                </li>

                <li v-if="isLoggedIn && currentUser.role == 'ADMIN PKM'" v-bind:class="{active : isInHomePage}" >
                    <a class="sidebar-child" href="/izin-kegiatan">Daftar Perizinan</a>
                </li>
                <li v-if="isLoggedIn && currentUser.role == 'ADMIN HUMAS'" v-bind:class="{active : isInHomePage}" >
                    <a class="sidebar-child" href="/perizinan-humas">Daftar Perizinan</a>
                </li>

                <li v-if="isLoggedIn && currentUser.role == 'ADMIN HUMAS'" v-bind:class="{active : isInHomePage}" >
                    <a class="sidebar-child" href="/souvenir">Daftar Souvenir</a>
                </li>

                <li v-bind:class="{active : isInHomePage}" >
                    <a class="sidebar-child" href="/jadwal-tersedia">Jadwal Tersedia</a>
                </li>
                <li v-bind:class="{active : isInHomePage}" >
                    <a class="sidebar-child" href="/ruangan">Daftar Ruangan</a>
                </li>

                <li v-if="isLoggedIn != true" v-bind:class="{active : isInLoginPage}" >
                    <a class="sidebar-child" href="/login">Login</a>
                </li>
            </ul>
                

            <!-- <ul class="list-unstyled CTAs">
                <li>
                    <a href="https://bootstrapious.com/tutorial/files/sidebar.zip" class="download">Download source</a>
                </li>
                
            </ul> -->
        </nav>

        <!-- Page Content  -->
        <div id="content" v-bind:class="{active: sidebarClosed}">

            <i class="far fa-sign-out-alt fa-2x"   v-on:click="toggleSidebar"></i>
            
            <router-view @inLoginPage="isInLoginPageFunc" @inHomePage="isInHomePageFunc"  @inPeminjamanRuanganUnitKerjaPage="isInPeminjamanRuanganUnitKerjaPageFunc"/>
            
        </div>
    </div>
</div>
</template>
<script>
import Navbar from './Navbar'
import Logout from './auth/Logout'
export default {
    name: 'Base',
    components:{
        Navbar,
        Logout
    },
    data(){
        return {
            sidebarClosed : false,
            isInHomePage : false,
            isInLoginPage : false,
            isInPeminjamanRuanganUnitKerjaPage : false,
        }
    },
    computed: {
        isLoggedIn() {
            return this.$store.state.auth.status.loggedIn;
        },
        currentUser() {
            return this.$store.state.auth.user;
        }
    },
    methods:{
        toggleSidebar: function(){
            this.sidebarClosed = !this.sidebarClosed;
            console.log(this.$router.currentRoute._value.href)
        },
        // getting a var from child to get to know that it is the active one
        isInLoginPageFunc(value){
            this.isInLoginPage = value;
        },
        isInHomePageFunc(value){
            this.isInHomePage = value;
        },
        isInPeminjamanRuanganUnitKerjaPageFunc(value){
            this.isInPeminjamanRuanganUnitKerjaPage = value;
        }
    },
}
</script>



<style>
/*
    DEMO STYLE
*/

@import "https://fonts.googleapis.com/css2?family=Mulish:wght@200&display=swap";
body {
    font-family: 'Times', sans-serif;
    background: #fafafa;
}
p {
    font-family: 'Poppins', sans-serif;
    font-size: 1.1em;
    font-weight: 300;
    line-height: 1.7em;
    color: #999;
}
a,
a:hover,
a:focus {
    color: inherit;
    text-decoration: none;
    transition: all 0.3s;
}
.navbar {
    padding: 15px 10px;
    background: #fff;
    border: none;
    border-radius: 0;
    margin-bottom: 40px;
    box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
}
.navbar-btn {
    box-shadow: none;
    outline: none !important;
    border: none;
}
.line {
    width: 100%;
    height: 1px;
    border-bottom: 1px dashed #ddd;
    margin: 40px 0;
}
/* ---------------------------------------------------
    SIDEBAR STYLE
----------------------------------------------------- */
.wrapper {
    display: flex;
    width: 100%;
}
#sidebar {
    width: 250px;
    position: fixed;
    top: 62px;
    left: 0;
    height: 100vh;
    z-index: 999;
    background: #FFFFFF;
    color:green;
    transition: all 0.3s;
}
#sidebar.active {
    margin-left: -250px;
}
#sidebar .sidebar-header {
    padding: 20px;
    background: #FFFFFF;
}
#sidebar ul.components {
    padding: 20px 0;
    border-bottom: 1px solid blanchedalmond;
}
#sidebar ul p {
    color: #fff;
    padding: 10px;
}
#sidebar ul li a {
    padding: 10px;
    font-size: 1.1em;
    display: block;
}
#sidebar ul li a:hover {
    color: black;
    background: #FFD505;
}
#sidebar ul li.active>a,
a[aria-expanded="true"] {
    color: black;
    background: #FFD505;
}
.sidebar-child {
    color: #828282;
}
a[data-toggle="collapse"] {
    position: relative;
}
.dropdown-toggle::after {
    display: block;
    position: absolute;
    top: 50%;
    right: 20px;
    transform: translateY(-50%);
}
ul ul a {
    font-size: 0.9em !important;
    padding-left: 30px !important;
    background: #6d7fcc;
}
ul.CTAs {
    padding: 20px;
}
ul.CTAs a {
    text-align: center;
    font-size: 0.9em !important;
    display: block;
    border-radius: 5px;
    margin-bottom: 5px;
}
/* a.download {
    background: #fff;
    color: #7386D5;
} */
a.article,
a.article:hover {
    background: #FFD505 !important;

    color: #fff !important;
}
/* ---------------------------------------------------
    CONTENT STYLE
----------------------------------------------------- */
#content {
    width: calc(100% - 250px);
    padding: 45px;
    min-height: 100vh;
    transition: all 0.3s;
    position: absolute;
    top: 30px;
    right: 0;
    background: #F2F2F2;
}
#content.active {
    width: 100%;
}
/* ---------------------------------------------------
    MEDIAQUERIES
----------------------------------------------------- */
@media (max-width: 768px) {
    #sidebar {
        margin-left: -250px;
    }
    #sidebar.active {
        margin-left: 0;
    }
    #content {
        width: 100%;
    }
    #content.active {
        width: calc(100% - 250px);
    }
    #sidebarCollapse span {
        display: none;
    }
}
</style>