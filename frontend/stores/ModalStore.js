import { defineStore } from 'pinia';
// import { useLocalStorage } from '@vueuse/core'

export const useModalStore = defineStore('ModalStore', () => {
  const showModal = ref(false);
  const showUnitConversionModal = ref(false);
  const neededConversionUnits = ref([]);
  const largerUnit = ref('');
  const conversionFactor = ref(0);
  const selectedDay = ref('');
  const showAddGroceryItemModal = ref(false);
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

  return {
    showModal,
    showUnitConversionModal,
    neededConversionUnits,
    largerUnit,
    conversionFactor,
    selectedDay,
    showAddGroceryItemModal,
    defaultAisle,
  };
});
