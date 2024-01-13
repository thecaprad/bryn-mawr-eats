<script setup>
  const { makeGetRequest } = useApi();
  import { storeToRefs } from 'pinia';
  import { useModalStore } from '../../stores/ModalStore';
  const { showModal } = storeToRefs(useModalStore());

  const recipeList = ref([]);

  // Load recipes
  const { data: recipes } = await useLazyAsyncData(
    'getRecipes',
    async () => {
      try {
        const response = await makeGetRequest('/recipes');
        const json = await response.json();
        return json;
      } catch (e) {
        // navigateTo('/404');
      }
    },
    { initialCache: false }
  );

  // Watch for response to load.
  watch(recipes, (newRecipes) => {
    recipeList.value.push(...newRecipes);
  });
</script>

<template>
  <h1>Grocery List</h1>
</template>
