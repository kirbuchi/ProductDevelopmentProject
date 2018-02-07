<template>
  <div id="app">
    <RiskTypeForm/>
  </div>
</template>

<script>
import RiskTypeForm from '@/components/RiskTypeForm';

export default {
  name: 'App',
  components: {
    RiskTypeForm,
  },
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
