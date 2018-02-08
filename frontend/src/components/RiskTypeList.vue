<docs>
## Utility component to help navigation of different risk types.
</docs>

<template>
<div>
  <h1>Risk Types</h1>
  <ul>
    <li v-for="riskType of riskTypes"
        :key="riskType.id">
      <router-link :to="{ name: 'form', params: { id: riskType.id }}">
        {{ riskType.name }}
      </router-link>
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
