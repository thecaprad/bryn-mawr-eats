import { defineStore } from 'pinia';
// import { useLocalStorage } from '@vueuse/core'

export const useModalStore = defineStore('ModalStore', () => {
  const showModal = ref(false);
  const selectedDay = ref('');

  return {
    showModal,
    selectedDay,
  };
});
