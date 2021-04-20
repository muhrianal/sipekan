<template>
    <div>
        Dashboard
    </div>
</template>

<script>
export default {
    mounted(){
        this.$emit('inDashboardPage', true);
    }

}
</script>
