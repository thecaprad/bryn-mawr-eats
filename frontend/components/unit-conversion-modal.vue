<script setup>
  import { storeToRefs } from 'pinia';
  import { useModalStore } from '../../stores/ModalStore';

  const emit = defineEmits(['conversionMade']);
  const { makePostRequest } = useApi();

  const { showUnitConversionModal, neededConversionUnits, largerUnit, conversionFactor } = storeToRefs(useModalStore());
  const selectedIndex = ref(null);

  const handleSubmission = async () => {
    if (largerUnit.value && conversionFactor.value != 0 && (selectedIndex.value == 0 || selectedIndex.value == 1)) {
      const data = {
        bigger_unit: neededConversionUnits.value[selectedIndex.value],
        smaller_unit: selectedIndex.value == 0 ? neededConversionUnits.value[1] : neededConversionUnits.value[0],
        conversion_factor: 1 / conversionFactor.value,
      };
      const response = await makePostRequest('/units/', data);
      if (response.ok) {
        showUnitConversionModal.value = false;
        // Emit event to trigger recreation of grocery list after
        // conversion unit has been added.
        emit('conversionMade');
      }
    }
  };
</script>

<template>
  <div class="recipe-modal">
    <div class="modal">
      <p>Select which unit is larger</p>
      <div
        class="recipe-option"
        v-for="(unit, i) in neededConversionUnits"
        :key="unit"
        @click="
          selectedIndex = i;
          largerUnit = unit;
        "
        :class="{ active: selectedIndex == i }"
      >
        <div>{{ unit }}</div>
      </div>
      <label>How many smaller units fit into the larger one?</label>
      <input type="text" v-model="conversionFactor" />
      <button @click="handleSubmission">Submit</button>
    </div>
  </div>
</template>
