<template>
    <div>
        Home
    </div>
    
</template>

<script>

export default {
    mounted(){
        this.$emit('inHomePage', true);
    }

}
</script>
