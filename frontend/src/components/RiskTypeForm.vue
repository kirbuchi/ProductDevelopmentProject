<template>
<form v-if="riskSpecification.id">
  <div v-if="error">{{ error }}</div>
  <h1>Create {{ riskSpecification.name }}</h1>
  <p>{{ riskSpecification.description }}</p>
  <RiskTypeField v-for="field of riskSpecification.fields"
                 v-bind:spec="field"
                 v-model="values[field.name]"
                 v-bind:key="field.id" />
</form>
</template>

<script>
import RiskTypeField from '@/components/RiskTypeField';
import { loadRiskTypeSpecification } from '@/services';

export default {
  data() {
    return {
      riskSpecification: {},
      values: {},
      error: null,
    };
  },
  created() {
    loadRiskTypeSpecification(this.$route.params.id)
      .then((data) => {
        this.riskSpecification = data;
      }).catch((error) => {
        this.error = error;
      });
  },
  components: {
    RiskTypeField,
  },
};
</script>
