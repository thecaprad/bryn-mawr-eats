<script setup>
  import { storeToRefs } from 'pinia'
  import { useModalStore } from '../../stores/ModalStore'
  const { showModal } = storeToRefs(useModalStore())
</script>

<template>
  <div>
    <RecipeModal v-if="showModal"></RecipeModal>
    <h1>This Week</h1>
    <RecipeWeek></RecipeWeek>
  </div>
</template>

<style scoped>
  h1 {
    text-align: center;
  }
</style>
