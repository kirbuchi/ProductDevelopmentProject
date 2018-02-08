<template>
  <div id="app">
    <RiskTypeForm v-if="riskTypeId" :riskTypeId="riskTypeId" />
    <RiskTypeList v-else />
  </div>
</template>

<script>
import RiskTypeForm from '@/components/RiskTypeForm';
import RiskTypeList from '@/components/RiskTypeList';

export default {
  name: 'App',
  data() {
    return { riskTypeId: window.location.pathname.match('[0-9]+') };
  },
  components: {
    RiskTypeForm,
    RiskTypeList,
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
