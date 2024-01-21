<script setup>
  const { makeGetRequest } = useApi();
  import { storeToRefs } from 'pinia';
  import { useModalStore } from '../../stores/ModalStore';
  import { useGroceryListStore } from '../../stores/GroceryListStore';
  const { showModal, selectedDay } = storeToRefs(useModalStore());
  const { mealPlan } = storeToRefs(useGroceryListStore());

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

  const makeSelection = (recipe) => {
    if (selectedDay.value == 'Monday') {
      mealPlan.value.monday.recipe.name = recipe.name;
      mealPlan.value.monday.recipe.image_url = recipe.image_url;
      mealPlan.value.monday.recipe.id = recipe.id;
    }
    if (selectedDay.value == 'Tuesday') {
      mealPlan.value.tuesday.recipe.name = recipe.name;
      mealPlan.value.tuesday.recipe.image_url = recipe.image_url;
      mealPlan.value.tuesday.recipe.id = recipe.id;
    }
    if (selectedDay.value == 'Wednesday') {
      mealPlan.value.wednesday.recipe.name = recipe.name;
      mealPlan.value.wednesday.recipe.image_url = recipe.image_url;
      mealPlan.value.wednesday.recipe.id = recipe.id;
    }
    if (selectedDay.value == 'Thursday') {
      mealPlan.value.thursday.recipe.name = recipe.name;
      mealPlan.value.thursday.recipe.image_url = recipe.image_url;
      mealPlan.value.thursday.recipe.id = recipe.id;
    }
    if (selectedDay.value == 'Friday') {
      mealPlan.value.friday.recipe.name = recipe.name;
      mealPlan.value.friday.recipe.image_url = recipe.image_url;
      mealPlan.value.friday.recipe.id = recipe.id;
    }
    if (selectedDay.value == 'Saturday') {
      mealPlan.value.saturday.recipe.name = recipe.name;
      mealPlan.value.saturday.recipe.image_url = recipe.image_url;
      mealPlan.value.saturday.recipe.id = recipe.id;
    }
    if (selectedDay.value == 'Sunday') {
      mealPlan.value.sunday.recipe.name = recipe.name;
      mealPlan.value.sunday.recipe.image_url = recipe.image_url;
      mealPlan.value.sunday.recipe.id = recipe.id;
    }
  };
</script>

<template>
  <div class="modal-base" @click="showModal = false">
    <div class="modal">
      <h2>Select recipe</h2>
      <div class="modal-option recipe-option" v-for="recipe in recipeList" :key="recipe" @click="makeSelection(recipe)">
        <div>{{ recipe.name }}</div>
        <SvgPanic v-if="recipe.name == 'Panic'"></SvgPanic>
        <SvgTakeout v-else-if="recipe.name == 'Takeout'"></SvgTakeout>
        <img v-else :src="recipe.image_url" />
      </div>
    </div>
  </div>
</template>
