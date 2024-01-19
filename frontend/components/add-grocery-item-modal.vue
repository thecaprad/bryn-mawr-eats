<script setup>
  import { storeToRefs } from 'pinia';
  import { useModalStore } from '../../stores/ModalStore';
  import { useGroceryListStore } from '../../stores/GroceryListStore';

  const { makeGetRequest, makePostRequest } = useApi();

  const { showAddGroceryItemModal, defaultAisle } = storeToRefs(useModalStore());
  const { groceryItems } = storeToRefs(useGroceryListStore());

  const groceryItemsList = ref([{ name: 'New grocery item', id: 0 }]);
  const unitsList = ref([{ name: 'New unit', id: 0 }]);
  const aislesList = ref([{ name: 'New aisle', id: 0 }]);

  const selectedGroceryItem = ref({});
  const selectedUnit = ref({});
  const selectedAisle = ref({});
  const quantity = ref(0);
  const newItemName = ref('');
  const newAisleName = ref('');
  const newUnitName = ref('');

  const groceryItemSelected = computed(() => {
    return Object.keys(selectedGroceryItem.value).length == 0 ? false : true;
  });

  const aisleSelected = computed(() => {
    return Object.keys(selectedAisle.value).length == 0 ? false : true;
  });

  const unitSelected = computed(() => {
    return Object.keys(selectedUnit.value).length == 0 ? false : true;
  });

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

  // Load aisles
  const { data: aisles } = await useLazyAsyncData(
    'getAisles',
    async () => {
      try {
        const response = await makeGetRequest('/aisles');
        const json = await response.json();
        return json;
      } catch (e) {
        // navigateTo('/404');
      }
    },
    { initialCache: false }
  );

  // Watch for response to load.
  watch(aisles, (newAisles) => {
    aislesList.value.push(...newAisles);
  });

  const handleSelect = (groceryOrUnitStr, selection) => {
    if (groceryOrUnitStr == 'grocery') {
      if (selection.id != 0) {
        selectedGroceryItem.value = selection;
      } else {
        selectedGroceryItem.value = {};
      }
    }

    if (groceryOrUnitStr == 'aisle') {
      if (selection.id != 0) {
        selectedAisle.value = selection;
      } else {
        selectedAisle.value = {};
      }
    }

    if (groceryOrUnitStr == 'unit') {
      if (selection.id != 0) {
        selectedUnit.value = selection;
      } else {
        selectedUnit.value = {};
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
      <!-- Select existing grocery item -->
      <div class="grocery-option">
        <select>
          <option v-for="item in groceryItemsList" :key="item" @click="handleSelect('grocery', item)">
            {{ item.name }}
          </option>
        </select>
      </div>

      <!-- Add new grocery item -->
      <div class="grocery-option" v-if="!groceryItemSelected">
        <label for="new-ingredient">New ingredient</label>
        <input id="new-ingredient" type="text" v-model="newItemName" />
      </div>

      <!-- Existing aisle for new grocery item -->
      <div class="grocery-option" v-if="!groceryItemSelected">
        <label>Grocery aisle</label>
        <select id="aisles">
          <option v-for="aisle in aislesList" :key="aisle" @click="handleSelect('aisle', aisle)">
            {{ aisle.name }}
          </option>
        </select>
      </div>

      <!-- Add new aisle -->
      <div class="grocery-option" v-if="!groceryItemSelected && !aisleSelected">
        <label for="new-aisle">New aisle</label>
        <input id="new-aisle" type="text" v-model="newAisleName" />
      </div>

      <!-- Quantity -->
      <div class="grocery-option">
        <label for="quantity">Quantity</label>
        <input id="quantity" type="number" v-model="quantity" />
      </div>

      <!-- Select existing unit -->
      <div class="grocery-option">
        <label for="unit">Unit</label>
        <select id="unit">
          <option v-for="unit in unitsList" :key="unit" @click="handleSelect('unit', unit)">{{ unit.name }}</option>
        </select>
      </div>

      <!-- Add new unit -->
      <div class="grocery-option" v-if="!unitSelected">
        <label for="new-unit">New unit</label>
        <input id="new-unit" type="text" v-model="newUnitName" />
      </div>

      <button @click="handleSubmission()">Submit</button>
    </div>
  </div>
</template>
