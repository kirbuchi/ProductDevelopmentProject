<template>
<div>
  <router-link class="backLink" :to="{ name: 'home' }">Go back</router-link>

  <form v-if="riskSpecification.id">
    <div v-if="error">{{ error }}</div>
    <h1>Create {{ riskSpecification.name }} instance</h1>
    <p>{{ riskSpecification.description }}</p>
    <RiskTypeField v-for="field of riskSpecification.fields"
                   v-bind:spec="field"
                   v-model="values[field.name]"
                   v-bind:key="field.id" />
    <button @click.prevent="processForm">Save</button>
</form>
</div>
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
  methods: {
    processForm() {
      // Fields may be accessed on the this.values object for sending
    },
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

<style>
.backLink {
    width: 100%;
    text-align: right;
    float: right;
}

button {
    font-size: 1em;
    border-radius: 4px;
    padding: .5em 2em;
    float: right;
    border: 2px solid rgba(60,60,60,.26);
}

</style>
