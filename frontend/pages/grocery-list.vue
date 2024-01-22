<script setup>
  import { storeToRefs } from 'pinia';
  import { useGroceryListStore } from '../../stores/GroceryListStore';
  import { useModalStore } from '../../stores/ModalStore';
  const { prettyQuantity } = useUtils();

  const groceryListStore = useGroceryListStore();

  const {
    showModal,
    showUnitConversionModal,
    neededConversionUnits,
    showAddGroceryItemModal,
    showRecipeDetailModal,
    defaultAisle,
  } = storeToRefs(useModalStore());
  const { mealPlan, aisles, recipeIngredients, selectedRecipeIDs, getAllItemsNestedByAisle } =
    storeToRefs(groceryListStore);

  const { makeGetRequest } = useApi();

  const handleCreateGroceryList = async () => {
    const response = await makeGetRequest('/grocery-list/' + selectedRecipeIDs.value + '/');
    if (response.ok) {
      const json = await response.json();
      if (json.need_conversion) {
        showUnitConversionModal.value = true;
        neededConversionUnits.value = json.need_conversion;
      } else {
        recipeIngredients.value = json.ingredients;
        aisles.value = json.aisles;
      }
    }
  };
</script>

<template>
  <div class="grocery-list">
    <RecipeDetailModal v-if="showRecipeDetailModal"></RecipeDetailModal>
    <RecipeModal v-if="showModal"></RecipeModal>
    <AddGroceryItemModal v-if="showAddGroceryItemModal"></AddGroceryItemModal>
    <UnitConversionModal v-if="showUnitConversionModal" @conversionMade="handleCreateGroceryList"></UnitConversionModal>
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

    <div class="buttons">
      <button @click="handleCreateGroceryList">
        Create grocery list
        <SvgWand></SvgWand>
      </button>

      <button @click="groceryListStore.clearGroceryList()">
        Clear grocery list
        <SvgTrash></SvgTrash>
      </button>
    </div>

    <!-- Grocery Aisles -->
    <!-- <hr /> -->
    <div class="aisles">
      <div class="aisle" v-for="aisleItem in getAllItemsNestedByAisle" :key="aisleItem">
        <h3>{{ Object.keys(aisleItem)[0] }}</h3>
        <div v-for="item in Object.values(aisleItem)[0]" :key="item" class="ingredient">
          <span class="name">{{ item.name }}</span>
          <span>{{ prettyQuantity(item.quantity) }}</span>
          <span v-if="item.unit != 'whole'" class="unit">{{ item.unit }}</span>
          <svg-x @click="groceryListStore.removeIngredient(item)"></svg-x>
        </div>
        <button
          @click="
            showAddGroceryItemModal = true;
            defaultAisle = Object.keys(aisleItem)[0];
          "
        >
          + Add grocery item
        </button>
      </div>
    </div>
  </div>
</template>
