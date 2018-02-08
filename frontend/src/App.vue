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
    margin-top: 60px;
    margin-left: 30%;
    margin-right: 30%;
}
</style>
