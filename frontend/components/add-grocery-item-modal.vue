<script setup>
  import { storeToRefs } from 'pinia';
  import { useModalStore } from '../../stores/ModalStore';
  import { useGroceryListStore } from '../../stores/GroceryListStore';

  const { makeGetRequest, makePostRequest } = useApi();

  const { showAddGroceryItemModal, defaultAisle } = storeToRefs(useModalStore());
  const { groceryItems } = storeToRefs(useGroceryListStore());

  const groceryItemsList = ref([{ name: 'New grocery item', id: 0 }]);
  const unitsList = ref([{ name: 'New unit', id: 0 }]);

  const selectedGroceryItem = ref({});
  const selectedUnit = ref({});
  const quantity = ref(0);

  // Load ingredients
  const { data: groceryItemsResponse } = await useLazyAsyncData(
    'getGroceryItems',
    async () => {
      try {
        const response = await makeGetRequest('/grocery-items');
        const json = await response.json();
        return json;
      } catch (e) {
        // navigateTo('/404');
      }
    },
    { initialCache: false }
  );

  // Watch for response to load.
  watch(groceryItemsResponse, (newGroceryItems) => {
    groceryItemsList.value.push(...newGroceryItems);
  });

  // Load units
  const { data: units } = await useLazyAsyncData(
    'getUnits',
    async () => {
      try {
        const response = await makeGetRequest('/ingredient-units');
        const json = await response.json();
        return json;
      } catch (e) {
        // navigateTo('/404');
      }
    },
    { initialCache: false }
  );

  // Watch for response to load.
  watch(units, (newUnits) => {
    unitsList.value.push(...newUnits);
  });

  const handleSelect = (groceryOrUnitStr, selection) => {
    if (groceryOrUnitStr == 'grocery') {
      if (selection.id != 0) {
        selectedGroceryItem.value = selection;
      }
    }

    if (groceryOrUnitStr == 'unit') {
      if (selection.id != 0) {
        selectedUnit.value = selection;
      }
    }
  };

  const handleSubmission = async () => {
    if (selectedGroceryItem.value && selectedUnit.value && quantity.value != 0) {
      let item = {
        id: selectedGroceryItem.value.id,
        grocery_aisle: selectedGroceryItem.value.grocery_aisle_name,
        name: selectedGroceryItem.value.name,
        quantity: quantity.value,
        unit: selectedUnit.value.name,
      };

      let result = {};
      result[selectedGroceryItem.value.id.toString()] = item;

      groceryItems.value.push(result);
      showAddGroceryItemModal.value = false;
      defaultAisle.value = '';
    }
  };
</script>

<template>
  <div class="grocery-modal">
    <div class="modal">
      <p>Add grocery item</p>

      <!-- Select or submit ingredient -->
      <div class="grocery-option">
        <select>
          <option v-for="item in groceryItemsList" :key="item" @click="handleSelect('grocery', item)">
            {{ item.name }}
          </option>
        </select>
      </div>

      <!-- Quantity -->
      <div class="grocery-option">
        <label for="quantity">Quantity</label>
        <input id="quantity" type="number" v-model="quantity" />
      </div>

      <!-- Select or submit unit -->
      <div class="grocery-option">
        <select>
          <option v-for="unit in unitsList" :key="unit" @click="handleSelect('unit', unit)">{{ unit.name }}</option>
        </select>
      </div>

      <button @click="handleSubmission()">Submit</button>
    </div>
  </div>
</template>
