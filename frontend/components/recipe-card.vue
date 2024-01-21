<script setup>
  import { storeToRefs } from 'pinia';
  import { useModalStore } from '../../stores/ModalStore';
  import { useGroceryListStore } from '../../stores/GroceryListStore';

  const groceryListStore = useGroceryListStore();

  const { showModal, selectedDay, showRecipeDetailModal, selectedRecipeId } = storeToRefs(useModalStore());

  const props = defineProps(['day', 'recipe']);
  const { day, recipe } = toRefs(props);

  const handleSelect = (recipe, day) => {
    showModal.value = !showModal.value;
    selectedDay.value = day;
  };

  const handleRecipeSwapOrDelete = (recipe, day) => {
    // clear existing recipe
    if (recipe.name) {
      groceryListStore.clearMealByDayName(day);
    } else {
      handleSelect(recipe, day);
    }
  };
</script>

<template>
  <div class="recipe-card">
    <div v-if="recipe.name == 'Takeout'" class="takeout">
      <SvgTakeout></SvgTakeout>
    </div>
    <div v-else-if="recipe.name == 'Panic'" class="panic">
      <SvgPanic></SvgPanic>
    </div>
    <div v-else-if="!recipe.name" class="panic" @click="handleSelect(recipe, day)">
      <SvgUtensils></SvgUtensils>
    </div>
    <img
      :src="recipe.image_url"
      @click="
        showRecipeDetailModal = true;
        selectedRecipeId = recipe.id;
      "
      v-else
    />
    <div class="recipe-info">
      <div>
        <div class="name-and-icon">
          <!-- Name -->
          <h2 v-if="recipe.name">{{ recipe.name }}</h2>
          <h2 v-else>Select recipe</h2>
          <!-- Icon -->
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" @click="handleRecipeSwapOrDelete(recipe, day)">
            <path
              v-if="recipe.name"
              d="M342.6 150.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192 210.7 86.6 105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L146.7 256 41.4 361.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L192 301.3 297.4 406.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L237.3 256 342.6 150.6z"
            />
            <path
              v-else
              d="M112 48H16v96h96V48zm80 16H160v64h32H480h32V64H480 192zm0 160H160v64h32H480h32V224H480 192zm0 160H160v64h32H480h32V384H480 192zM16 208v96h96V208H16zm96 160H16v96h96V368z"
            />
          </svg>
        </div>
        <h3>{{ day }}</h3>
      </div>
    </div>
  </div>
</template>
