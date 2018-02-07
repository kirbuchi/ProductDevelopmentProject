<template>
<form action="">
  <div>{{ name }}</div>
  <div>{{ description }}</div>
  <RiskTypeField
    v-for="field of fields"
    v-bind="field"
    v-bind:key="field.id" />
</form>
</template>

<script>
import RiskTypeField from '@/components/RiskTypeField';

const mockData = {
  id: 1,
  name: 'risk0',
  description: 'risk0 description',
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
  }],
};

export default {
  data() {
    return mockData;
  },
  components: {
    RiskTypeField,
  },
};

</script>

<style>
</style>
