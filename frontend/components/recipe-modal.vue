<script setup>
  import { storeToRefs } from 'pinia';
  import { useModalStore } from '../../stores/ModalStore';
  const { showModal } = storeToRefs(useModalStore());

  const recipes = [
    {
      name: 'Zuppa Toscana',
      image_url: 'https://www.budgetbytes.com/wp-content/uploads/2018/09/Zuppa-Toscana-V-1200.jpg',
    },
    {
      name: 'Easy Vegetable Beef Soup',
      image_url: 'https://www.budgetbytes.com/wp-content/uploads/2022/04/Vegetable-Beef-Soup-V3.jpg',
    },
    {
      name: 'Takeout',
    },
    {
      name: 'Creamy Tomato and Spinach Pasta',
      image_url: 'https://www.budgetbytes.com/wp-content/uploads/2013/07/Creamy-Tomato-Spinach-Pasta-V2-bowl.jpg',
    },
    {
      name: 'Chicken Noodle Soup',
      image_url: 'https://www.budgetbytes.com/wp-content/uploads/2017/02/Homemade-Chicken-Noodle-Soup-V3-e.jpg',
    },

    {
      name: 'Panic',
    },
    {
      name: 'Easy Sesame Chicken',
      image_url: 'https://www.budgetbytes.com/wp-content/uploads/2018/07/Easy-Sesame-Chicken-V3-1200.jpg',
    },
  ];
</script>

<template>
  <div class="recipe-modal" @click="showModal = false">
    <div class="modal">
      <div class="recipe-option" v-for="recipe in recipes" :key="recipe">
        <div>{{ recipe.name }}</div>
        <SvgPanic class="info"></SvgPanic>
      </div>
    </div>
  </div>
</template>
