<template>
<date-picker lang="en"
             :value="value"
             @input="updateValue" />
</template>

<script>
import DatePicker from 'vue2-datepicker';

export default {
  components: { DatePicker },
  props: ['value'],
  methods: {
    updateValue(newValue) { this.$emit('input', newValue); },
  },
};
</script>

<style>
</style>
