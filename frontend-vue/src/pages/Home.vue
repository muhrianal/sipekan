<template>
    <div>
        Home
    </div>
    <button-batal><p>Kontol</p></button-batal>
    
</template>

<script>
// import ButtonBatal from '../components/button/ButtonBatal';
import ButtonBatal from '../components/button/ButtonBatal.vue';

export default{
    components: { ButtonBatal },
    mounted(){
        this.$emit('inHomePage', true);
    },

}
</script>
