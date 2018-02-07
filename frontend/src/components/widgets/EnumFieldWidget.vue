<template>
  <v-select :options="options.choices"
            :value="value"
            @input="updateValue" />
</template>

<script>
import vSelect from 'vue-select';

export default {
  components: { vSelect },
  props: ['value', 'options'],
  methods: {
    updateValue(newValue) { this.$emit('input', newValue); },
  },
};
</script>

<style>
</style>
