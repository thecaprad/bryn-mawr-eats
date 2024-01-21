<script setup>
  import { storeToRefs } from 'pinia';
  import { useModalStore } from '../../stores/ModalStore';
  const { showModal, showRecipeDetailModal } = storeToRefs(useModalStore());
</script>

<template>
  <div>
    <RecipeDetailModal v-if="showRecipeDetailModal"></RecipeDetailModal>
    <RecipeModal v-if="showModal"></RecipeModal>
    <h1>This Week</h1>
    <RecipeWeek></RecipeWeek>
  </div>
</template>
