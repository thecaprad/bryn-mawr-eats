<script setup>
  const { makeGetRequest } = useApi();
  import { storeToRefs } from 'pinia';
  import { useModalStore } from '../../stores/ModalStore';

  const { showRecipeDetailModal, selectedRecipeId } = storeToRefs(useModalStore());
  const { prettyQuantity } = useUtils();

  // Load recipes
  const { data: recipe } = await useLazyAsyncData(
    'getRecipe',
    async () => {
      try {
        const response = await makeGetRequest('/recipes/' + selectedRecipeId.value);
        const json = await response.json();
        return json;
      } catch (e) {
        // navigateTo('/404');
      }
    },
    { initialCache: false }
  );

  const recipeData = ref({});
  // Watch for response to load.
  watch(recipe, (newRecipeData) => {
    console.log(newRecipeData);
    recipeData.value = newRecipeData;
  });
</script>

<template>
  <div class="modal-base">
    <div class="modal">
      <h2>{{ recipeData.name }}</h2>
      <div class="recipe-details">
        <div class="recipe-image">
          <img :src="recipeData.image_url" />
        </div>
        <div class="recipe-info">
          <div class="stats">
            <span><b>Prep time:</b> {{ recipeData.prep_time }} minutes</span>
            <span><b>Cook time:</b> {{ recipeData.cook_time }} minutes</span>
            <span><a :href="recipeData.source_url" target="_blank">Cooking instructions</a></span>
          </div>
          <h3>Ingredients</h3>
          <div v-for="ingredient in recipeData.recipe_ingredients" :key="ingredient" class="ingredient">
            <span class="name">{{ ingredient.grocery_item_name }}</span>
            <span>{{ prettyQuantity(ingredient.quantity) }}</span>
            <span v-if="ingredient.unit_name != 'whole'">{{ ingredient.unit_name }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
