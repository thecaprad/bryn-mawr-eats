import { defineStore } from 'pinia';
// import { useLocalStorage } from '@vueuse/core'

export const useModalStore = defineStore('ModalStore', () => {
  const showModal = ref(false);
  const showUnitConversionModal = ref(false);
  const showAddGroceryItemModal = ref(false);
  const showRecipeDetailModal = ref(false);
  const selectedRecipeId = ref(null);
  const neededConversionUnits = ref([]);
  const largerUnit = ref('');
  const conversionFactor = ref(0);
  const selectedDay = ref('');
  const defaultAisle = ref('');

  watch(showModal, (newValue) => {
    if (newValue) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'auto';
    }
  });

  watch(showAddGroceryItemModal, (newValue) => {
    if (newValue) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'auto';
    }
  });

  watch(showUnitConversionModal, (newValue) => {
    if (newValue) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'auto';
    }
  });

  watch(showRecipeDetailModal, (newValue) => {
    if (newValue) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'auto';
    }
  });

  return {
    showModal,
    showUnitConversionModal,
    showAddGroceryItemModal,
    showRecipeDetailModal,
    selectedRecipeId,
    neededConversionUnits,
    largerUnit,
    conversionFactor,
    selectedDay,
    defaultAisle,
  };
});
