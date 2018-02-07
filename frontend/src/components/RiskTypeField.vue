<template>
<dl>
  <dt>ID</dt>
  <dd>{{ id }}</dd>
  <dt>Name</dt>
  <dd>{{ name }}</dd>
  <dt>Description</dt>
  <dd>{{ description }}</dd>
  <dt>Type</dt>
  <dd>{{ type }}</dd>
  <component v-bind:is="typeToComponent(type)">
  </component>
</dl>
</template>

<script>
import { TextInputWidget, NumberInputWidget } from '@/components/widgets';

export default {
  props: ['id', 'name', 'description', 'type', 'options'],
  methods: {
    typeToComponent(type) {
      const mapping = {
        text: TextInputWidget,
        number: NumberInputWidget,
      };
      return mapping[type];
    },
  },
  components: {
    TextInputWidget,
    NumberInputWidget,
  },
};
</script>

<style>
dl {
    border: 1px solid black;
    padding: 15px;
}
</style>
