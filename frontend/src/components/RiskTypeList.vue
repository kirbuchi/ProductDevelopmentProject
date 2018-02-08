<docs>
## Utility component to help navigation of different risk types.
## Using real links just for demo purposes.
</docs>

<template>
<div>
  <h1>Risk Types</h1>
  <ul>
    <li v-for="riskType of riskTypes"
        :key="riskType.id">
      <a :href="riskType.id">{{ riskType.name }}</a>
    </li>
  </ul>
</div>
</template>

<script>
import { loadRiskTypeSpecificationList } from '@/services';

export default {
  data() { return { riskTypes: [] }; },
  created() {
    loadRiskTypeSpecificationList()
      .then((data) => { this.riskTypes = data; });
  },
};
</script>
