<script setup>
  import { storeToRefs } from 'pinia';
  import { useModalStore } from '../../stores/ModalStore';
  const { showModal } = storeToRefs(useModalStore());

  const props = defineProps(['day', 'recipe']);
  const { day, recipe } = toRefs(props);
</script>

<template>
  <div class="recipe-card">
    <div v-if="recipe.name == 'Takeout'" class="takeout">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512">
        <path
          d="M64 32L97.4 221.4 117.7 272H128V90.7L112 0 64 32zM18.7 192H59.7L41.8 90.5 0 80 18.7 192zM384 80L342.7 90.3 325.8 192h7.3c10.4-6.1 22-11.7 35-16.5L384 80zM256 512V304H96L64 224H0L64 512H256zm0-240h4c2.2-5.2 4.7-10.3 7.6-15.3c3.1-5.3 7-11.3 11.9-17.7l10.2-25.5L320 32 256 48V272zm-96 0h64V240 32L160 0V272zm480 15.8s-32-96-176-96s-176 96-176 96v32H640v-32zm-256-48a16 16 0 1 1 0 32 16 16 0 1 1 0-32zm64 0a16 16 0 1 1 32 0 16 16 0 1 1 -32 0zm96 0a16 16 0 1 1 0 32 16 16 0 1 1 0-32zm-256 112v64H640v-64H288zm0 96v64H640v-64H288z"
        />
      </svg>
    </div>
    <div v-else-if="recipe.name == 'Panic'" class="panic">
      <SvgPanic></SvgPanic>
    </div>
    <img :src="recipe.image_url" v-else-if="recipe" />
    <div class="recipe-info">
      <div>
        <h2 v-if="recipe">{{ recipe.name }}</h2>
        <h2 v-else>Select recipe</h2>
        <h3>{{ day }}</h3>
      </div>
      <!-- Remove recipe 'X' -->
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" @click="showModal = !showModal">
        <path
          d="M342.6 150.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192 210.7 86.6 105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L146.7 256 41.4 361.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L192 301.3 297.4 406.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L237.3 256 342.6 150.6z"
        />
      </svg>
    </div>
  </div>
</template>
