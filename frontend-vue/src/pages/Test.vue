<template>
    <div>
        Test
    </div>
</template>


<script>
import UserService from '../services/user.service';


export default {
    name: 'Test',
    data(){
        return {
            photos : '',
            error_call_api: '',

        }
    },
    created() {
        UserService.getPhotos().then(
            response => {
                this.photos = response.data;

            },
            error => {
                this.error_call_api = (error.response && error.response.data) || error.message || error.toString();
            }
        );
    },
    mounted(){
        console.log(this.photos);
    }
}
</script>