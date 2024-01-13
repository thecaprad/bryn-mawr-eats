import { defineStore } from 'pinia';
import { useLocalStorage } from '@vueuse/core';

export const useGroceryListStore = defineStore(
  'GroceryListStore',
  () => {
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

    return {
      mealPlan,
    };
  },
  { persist: true }
);
