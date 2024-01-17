import { defineStore } from 'pinia';

export const useGroceryListStore = defineStore('GroceryListStore', () => {
  const mealPlan = ref({
    monday: {
      recipe: {
        name: '',
        image_url: '',
        id: null,
      },
      label: 'Monday',
    },
    tuesday: {
      recipe: {
        name: '',
        image_url: '',
        id: null,
      },
      label: 'Tuesday',
    },
    wednesday: {
      recipe: {
        name: '',
        image_url: '',
        id: null,
      },
      label: 'Wednesday',
    },
    thursday: {
      recipe: {
        name: '',
        image_url: '',
        id: null,
      },
      label: 'Thursday',
    },
    friday: {
      recipe: {
        name: '',
        image_url: '',
        id: null,
      },
      label: 'Friday',
    },
    saturday: {
      recipe: {
        name: '',
        image_url: '',
        id: null,
      },
      label: 'Saturday',
    },
    sunday: {
      recipe: {
        name: '',
        image_url: '',
        id: null,
      },
      label: 'Sunday',
    },
  });

  // Persist and retrieve mealPlan
  if (localStorage.getItem('useMealPlan')) {
    mealPlan.value = JSON.parse(localStorage.getItem('useMealPlan'));
  }

  watch(
    mealPlan.value,
    (newMealPlan) => {
      localStorage.setItem('useMealPlan', JSON.stringify(newMealPlan));
    },
    { deep: true }
  );

  const aisles = ref([]);
  // Persist and retrieve aisles
  if (localStorage.getItem('useAisles')) {
    aisles.value = JSON.parse(localStorage.getItem('useAisles'));
  }

  watch(aisles, (newAisles) => {
    localStorage.setItem('useAisles', JSON.stringify(newAisles));
  });

  const recipeIngredients = ref([]);
  // Persist and retrieve recipe ingredients
  if (localStorage.getItem('useRecipeIngredients')) {
    recipeIngredients.value = JSON.parse(localStorage.getItem('useRecipeIngredients'));
  }

  watch(
    recipeIngredients,
    (newRecipeIngredients) => {
      localStorage.setItem('useRecipeIngredients', JSON.stringify(newRecipeIngredients));
    },
    { deep: true }
  );

  const getIngredientsByAisle = (aisleName) => {
    return Object.values(recipeIngredients.value).filter(
      (recipeIngredient) => recipeIngredient.grocery_aisle === aisleName
    );
  };

  const removeIngredient = (ingredient) => {
    for (let [key] of Object.entries(recipeIngredients.value)) {
      if (key == ingredient.id) {
        delete recipeIngredients.value[key];
      }
    }

    // Remove associated aisle if item was last one.
    if (getIngredientsByAisle(ingredient.grocery_aisle).length == 0) {
      let aisleIndex = aisles.value.findIndex((aisle) => aisle == ingredient.grocery_aisle);
      aisles.value.splice(aisleIndex, 1);
    }
  };

  const selectedRecipeIDs = computed(() => {
    let result = [];
    if (mealPlan.value.monday.recipe.id) {
      result.push(mealPlan.value.monday.recipe.id);
    }
    if (mealPlan.value.tuesday.recipe.id) {
      result.push(mealPlan.value.tuesday.recipe.id);
    }
    if (mealPlan.value.wednesday.recipe.id) {
      result.push(mealPlan.value.wednesday.recipe.id);
    }
    if (mealPlan.value.thursday.recipe.id) {
      result.push(mealPlan.value.thursday.recipe.id);
    }
    if (mealPlan.value.friday.recipe.id) {
      result.push(mealPlan.value.friday.recipe.id);
    }
    if (mealPlan.value.saturday.recipe.id) {
      result.push(mealPlan.value.saturday.recipe.id);
    }
    if (mealPlan.value.sunday.recipe.id) {
      result.push(mealPlan.value.sunday.recipe.id);
    }

    return result.join(',');
  });

  return {
    mealPlan,
    aisles,
    recipeIngredients,
    selectedRecipeIDs,
    removeIngredient,
  };
});
