<template>
<form v-if="riskSpecification.id">
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

const mockData = {
  id: 1,
  name: 'risk0',
  description: 'Nullam libero mauris, consequat quis, varius et, dictum id, arcu. Nullam libero mauris, consequat quis, varius et, dictum id, arcu. Nullam libero mauris, consequat quis, varius et, dictum id, arcu. Nullam libero mauris, consequat quis, varius et, dictum id, arcu. Nullam libero mauris, consequat quis, varius et, dictum id, arcu.',
  fields: [{
    description: 'Description for field 74779c08ce5145c89d9139db5a3df26f',
    id: 1,
    name: 'Field 74779c08ce5145c89d9139db5a3df26f',
    options: {},
    type: 'text',
  }, {
    description: 'Description for field ec27ede5bfb746c78e95564cf626f744',
    id: 2,
    name: 'Field ec27ede5bfb746c78e95564cf626f744',
    options: {},
    type: 'number',
  }, {
    description: 'Another field',
    id: 3,
    name: 'A date field',
    options: {},
    type: 'date',
  }, {
    description: 'An enum field',
    id: 4,
    name: 'Enum Field',
    options: {
      choices: ['First option', 'Second Option', 'Third Option'],
    },
    type: 'enum',
  }],
};

const loadRiskTypeSpecification = () => (
  new Promise((resolve) => {
    setTimeout(() => { resolve(mockData); }, 3000);
  })
);

export default {
  data() {
    return {
      riskSpecification: {},
      values: {},
    };
  },
  created() {
    loadRiskTypeSpecification()
      .then((data) => {
        this.riskSpecification = data;
      });
  },
  components: {
    RiskTypeField,
  },
};

</script>

<style>
</style>
