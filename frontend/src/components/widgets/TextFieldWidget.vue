<template>
<input type="text"
       :value="value"
       @input="updateValue($event.target.value)" />
</template>

<script>
export default {
  props: ['value'],
  methods: {
    updateValue(newValue) { this.$emit('input', newValue); },
  },
};
</script>

<style></style>
