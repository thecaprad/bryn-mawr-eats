<script setup>
  const { makeGetRequest } = useApi();
  import { storeToRefs } from 'pinia';
  import { useModalStore } from '../../stores/ModalStore';
  const { showUnitConversionModal, neededConversionUnits, largerUnit, conversionFactor } = storeToRefs(useModalStore());
  const selectedIndex = ref(null);
  // // Load recipes
  // const { data: recipes } = await useLazyAsyncData(
  //   'getRecipes',
  //   async () => {
  //     try {
  //       const response = await makeGetRequest('/recipes');
  //       const json = await response.json();
  //       return json;
  //     } catch (e) {
  //       // navigateTo('/404');
  //     }
  //   },
  //   { initialCache: false }
  // );

  // Watch for response to load.
  // watch(recipes, (newRecipes) => {
  //   recipeList.value.push(...newRecipes);
  // });
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
      <input type="text" />
      <button>Submit</button>
    </div>
  </div>
</template>
