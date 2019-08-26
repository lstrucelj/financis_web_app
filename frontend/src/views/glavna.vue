<template>
    <div>
        <dodavanje-troska>
        </dodavanje-troska>
        <router-link to="statistika">
            <b-img v-bind="props" :src="statBtn" alt="stat"></b-img>
        </router-link>
        <d3-pie :data="data" :options="options" :margin="margin" width="100%" height="400px"> </d3-pie>
    </div>
</template>

<script>
    import dodavanjeTroska from "../components/dodavanjeTroska";
    export default {
        name: "glavna",
        data(){
            return{
                props:{
                    height: 85, width: 85
                },
                data:[{
                    key:'50', value:'50'
                },{
                    key:'20', value:'20'
                }],
                options:"",
                margin:""
            }
        },
        components: {
            dodavanjeTroska
        },
        computed:{
            statBtn(){
                return require('../assets/stat.png');
            },
        }
    }
</script>

<style scoped>

</style>