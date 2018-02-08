<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import routes from '@/routes';
import VueRouter from 'vue-router';

const router = new VueRouter({ routes });

export default {
  router,
  name: 'App',
};
</script>

<style>
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    width: 650px;
    margin:60px auto;
}

@media (max-width: 700px) {
    #app {
        width: 100%
    }
}
</style>
