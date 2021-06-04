<template>
    <div v-if="isLoggedIn" class="card card-custom-root mb-3 rounded">
        <div class="card-body card-custom">
            <p style="font-weight: 500 !important; " id="masuk-sebagai">MASUK SEBAGAI:</p>
            <p style="font-weight: 500 !important; text-transform:" id="nama-user">{{getName}}</p>
            <p style="font-weight: 500 !important;" id="role-user">{{currentUser.role}}</p>
            
            <button type="submit" @click="logOut" class="btn btn-danger" id="button-logout">Logout</button>
        </div>
    </div>  
</template>


<script>
export default {
    name:'Logout',
    methods: {
        logOut() {
            this.$store.dispatch('auth/logout');
            this.$router.push('/login');
        }
    },
    computed: {
        isLoggedIn() {
            return this.$store.state.auth.status.loggedIn;
        },
        currentUser() {
            return this.$store.state.auth.user;
        },
        getName(){
            var name = this.$store.state.auth.user.name;
            if (name.length > 15){
                name = name.substring(0, 15) + '..';
            }
            return name;
        }
  },
}
</script>

<style>
.card-custom{
    margin-left: -5px;
    margin-top: -5px;
}

.card-custom-root {
    width: 216px;
    height: 125px;
    border-color: #BDBDBD;
}

#masuk-sebagai{
    color: #BDBDBD;
    font-weight:500;
    font-size: 10px;
    height: 0px;

}

#nama-user{
    color: black;
    height: 5px;
    font-weight:400;
    font-size: 16px;


}

#role-user{
    color: #828282;
    height: 8px;
    font-size: 13px;
}
#button-logout{
    width: 182px;
    height: 32px;
    font-size: 13px;
}

</style>

