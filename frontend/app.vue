<script setup>
  import { storeToRefs } from 'pinia';
  import { useModalStore } from '/stores/ModalStore';
  const { showModal, showAddGroceryItemModal, showUnitConversionModal, showRecipeDetailModal, selectedRecipeId } =
    storeToRefs(useModalStore());

  // Close modals globally on ESC keydown.
  onMounted(() => {
    const body = document.querySelector('body');
    body.addEventListener('keydown', (e) => {
      if (e.key == 'Escape') {
        showModal.value = false;
        showAddGroceryItemModal.value = false;
        showUnitConversionModal.value = false;
        showRecipeDetailModal.value = false;
        selectedRecipeId.value = null;
      }
    });
  });
</script>

<template>
  <div>
    <Header></Header>
    <NuxtPage class="slot-container"></NuxtPage>
  </div>
</template>
