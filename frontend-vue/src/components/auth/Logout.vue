<template>
    <div class="card card-custom-root mb-3 rounded">
        <div class="card-body card-custom">
            <p id="masuk-sebagai">MASUK SEBAGAI:</p>
            <p id="nama-user">Akhmad Diponegoro</p>
            <p id="role-user">Admin PKM</p>
            <button type="button" class="btn btn-danger" id="button-logout">Logout</button>
        </div>
    </div>  
</template>


<script>
export default {
    name:'Logout'
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

