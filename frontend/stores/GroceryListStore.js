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

  const recipeIngredients = ref({});
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

  const groceryItems = ref({});
  // Persist and retrieve grocery items.
  if (localStorage.getItem('useGroceryItems')) {
    groceryItems.value = JSON.parse(localStorage.getItem('useGroceryItems'));
  }

  watch(
    groceryItems,
    (newGroceryItems) => {
      localStorage.setItem('useGroceryItems', JSON.stringify(newGroceryItems));
    },
    { deep: true }
  );

  // Aggregate recipeIngredients and groceryItems
  const allItems = computed(() => {
    return { ...recipeIngredients.value, ...groceryItems.value };
  });

  const getAllItemsNestedByAisle = computed(() => {
    let result = [];
    for (let [key, value] of Object.entries(allItems.value)) {
      let aisleExists = false;
      let existingIndex = null;
      result.forEach((aisleItemObj, i) => {
        if (Object.keys(aisleItemObj)[0] == value.grocery_aisle) {
          aisleExists = true;
          existingIndex = i;
        }
      });

      let obj = {
        id: value.id,
        grocery_aisle: value.grocery_aisle,
        name: value.name,
        quantity: value.quantity,
        unit: value.unit,
      };

      if (!aisleExists) {
        let item = {};
        item[value.grocery_aisle] = [obj];
        result.push(item);
      } else {
        result[existingIndex][value.grocery_aisle].push(obj);
      }
    }
    return result;
  });

  const removeIngredient = (ingredient) => {
    // Try to delete from recipeIngredients
    for (let [key] of Object.entries(recipeIngredients.value)) {
      if (key == ingredient.id) {
        delete recipeIngredients.value[key];
      }
    }
    // Try to delete from groceryItems
    for (let [key] of Object.entries(groceryItems.value)) {
      if (key == ingredient.id) {
        delete groceryItems.value[key];
      }
    }
  };

  const clearGroceryList = () => {
    recipeIngredients.value = {};
    groceryItems.value = {};
  };

  const clearMealByDayName = (name) => {
    for (let [key, value] of Object.entries(mealPlan.value)) {
      if (value.label == name) {
        mealPlan.value[key].recipe.name = '';
        mealPlan.value[key].recipe.image_url = '';
        mealPlan.value[key].recipe.id = null;
      }
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
    groceryItems,
    allItems,
    selectedRecipeIDs,
    removeIngredient,
    clearGroceryList,
    clearMealByDayName,
    getAllItemsNestedByAisle,
  };
});
