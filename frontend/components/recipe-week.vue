<script setup>
  import { storeToRefs } from 'pinia';
  import { useGroceryListStore } from '../../stores/GroceryListStore';
  const { mealPlan } = storeToRefs(useGroceryListStore());
</script>

<template>
  <div class="recipe-week">
    <Recipe-Card :day="mealPlan.monday.label" :recipe="mealPlan.monday.recipe"></Recipe-Card>
    <Recipe-Card :day="mealPlan.tuesday.label" :recipe="mealPlan.tuesday.recipe"></Recipe-Card>
    <Recipe-Card :day="mealPlan.wednesday.label" :recipe="mealPlan.wednesday.recipe"></Recipe-Card>
    <Recipe-Card :day="mealPlan.thursday.label" :recipe="mealPlan.thursday.recipe"></Recipe-Card>
    <Recipe-Card :day="mealPlan.friday.label" :recipe="mealPlan.friday.recipe"></Recipe-Card>
    <Recipe-Card :day="mealPlan.saturday.label" :recipe="mealPlan.saturday.recipe"></Recipe-Card>
    <Recipe-Card :day="mealPlan.sunday.label" :recipe="mealPlan.sunday.recipe"></Recipe-Card>
  </div>
</template>
