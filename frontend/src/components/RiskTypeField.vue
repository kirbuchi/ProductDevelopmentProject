<template>
  <div class="riskField">
    <label :for="fieldId">{{ spec.name }}:</label>
    <component :id="fieldId"
               :is="typeToComponent(spec.type)"
               :options="spec.options"
               @input="updateValue"
               v-model="value" />
    <small>{{ spec.description }}</small>
  </div>
</template>

<script>
import {
  TextFieldWidget,
  NumberFieldWidget,
  DateFieldWidget,
  EnumFieldWidget,
} from '@/components/widgets';

export default {
  props: ['value', 'spec'],
  methods: {
    typeToComponent(type) {
      const mapping = {
        text: TextFieldWidget,
        number: NumberFieldWidget,
        date: DateFieldWidget,
        enum: EnumFieldWidget,
      };
      return mapping[type];
    },
    updateValue(newValue) { this.$emit('input', newValue); },
  },
  data() {
    return { fieldValue: null };
  },
  computed: {
    fieldId() { return `field_${this.spec.id}`; },
  },
  components: {
    TextFieldWidget,
    NumberFieldWidget,
    DateFieldWidget,
    EnumFieldWidget,
  },
};
</script>

<style>
.riskField {
    padding: 15px 0;
}

.riskField input {
    width: 100%;
    height: 2.5em;
    border-radius: 5px;
}

.riskField label {
    display: block;
    font-weight: bold;
    text-decoration: underline;
    margin-bottom: 1em;
}

.riskField small {
    display: inline-block;
    width: 100%;
    margin-top: .5em;
}
</style>
