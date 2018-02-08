<template>
<div class="riskField">
  <label :for="fieldId">{{ spec.name }}:</label>
  <component :id="fieldId"
              :is="typeToComponent(spec.type)"
              :options="spec.options"
              :value="value"
              @input="updateValue" />
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

const fieldTypeToComponentMapping = {
  text: TextFieldWidget,
  number: NumberFieldWidget,
  date: DateFieldWidget,
  enum: EnumFieldWidget,
};

export default {
  props: ['value', 'spec'],
  methods: {
    typeToComponent(type) {
      return fieldTypeToComponentMapping[type];
    },
    updateValue(newValue) { this.$emit('input', newValue); },
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
    box-sizing: border-box;
    width: 100%;
    height: 2.5em;
    border-radius: 4px;
    font-size: medium;
    border: 1px solid rgba(60,60,60,.26);
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
