<script setup>
  import { storeToRefs } from 'pinia';
  import { useGroceryListStore } from '../../stores/GroceryListStore';
  import { useModalStore } from '../../stores/ModalStore';

  const { showModal } = storeToRefs(useModalStore());
  const { mealPlan } = storeToRefs(useGroceryListStore());

  const { makeGetRequest } = useApi();

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
  <div class="grocery-list">
    <RecipeModal v-if="showModal"></RecipeModal>
    <h1>Grocery List</h1>
    <div class="recipe-week">
      <Recipe-Card :day="mealPlan.monday.label" :recipe="mealPlan.monday.recipe"></Recipe-Card>
      <Recipe-Card :day="mealPlan.tuesday.label" :recipe="mealPlan.tuesday.recipe"></Recipe-Card>
      <Recipe-Card :day="mealPlan.wednesday.label" :recipe="mealPlan.wednesday.recipe"></Recipe-Card>
      <Recipe-Card :day="mealPlan.thursday.label" :recipe="mealPlan.thursday.recipe"></Recipe-Card>
      <Recipe-Card :day="mealPlan.friday.label" :recipe="mealPlan.friday.recipe"></Recipe-Card>
      <Recipe-Card :day="mealPlan.saturday.label" :recipe="mealPlan.saturday.recipe"></Recipe-Card>
      <Recipe-Card :day="mealPlan.sunday.label" :recipe="mealPlan.sunday.recipe"></Recipe-Card>
    </div>
  </div>
</template>
