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

  const selectedGroceryItem = ref({ name: 'New grocery item', id: 0 });
  const selectedUnit = ref({ name: 'New unit', id: 0 });
  const selectedAisle = ref({ name: 'New aisle', id: 0 });
  const quantity = ref(0);
  const newItemName = ref('');
  const newAisleName = ref('');
  const newUnitName = ref('');

  const groceryItemSelected = computed(() => {
    return selectedGroceryItem.value.id != 0 ? true : false;
  });

  const aisleSelected = computed(() => {
    return selectedAisle.value.id != 0 ? true : false;
  });

  const unitSelected = computed(() => {
    return selectedUnit.value.id != 0 ? true : false;
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
      }
    }

    if (groceryOrUnitStr == 'aisle') {
      if (selection.id != 0) {
        selectedAisle.value = selection;
      }
    }

    if (groceryOrUnitStr == 'unit') {
      if (selection.id != 0) {
        selectedUnit.value = selection;
      }
    }
  };

  const handleSubmission = async () => {
    if (quantity.value) {
      // Add new unit.
      if (!unitSelected.value && newUnitName.value) {
        let data = { new_unit_name: newUnitName.value };
        let response = await makePostRequest('/ingredient-units/', data);
        if (response.ok) {
          let json = await response.json();
          let newUnit = { name: json.name, id: json.id };
          unitsList.value.push(newUnit);
          handleSelect('unit', newUnit);
        }
      }

      // Add new aisle.
      if (!aisleSelected.value && newAisleName.value) {
        let data = { new_aisle_name: newAisleName.value };
        let response = await makePostRequest('/aisles/', data);
        if (response.ok) {
          let json = await response.json();
          let newAisle = { name: json.name, id: json.id };
          aislesList.value.push(newAisle);
          handleSelect('aisle', newAisle);
        }
      }

      // Add new item.
      if (!groceryItemSelected.value && newItemName.value && aisleSelected.value) {
        let data = { new_item_name: newItemName.value, grocery_aisle_id: selectedAisle.value.id };
        let response = await makePostRequest('/grocery-items/', data);
        if (response.ok) {
          let json = await response.json();
          let newItem = {
            name: json.name,
            id: json.id,
            grocery_aisle_name: json.grocery_aisle_name,
            quantity: quantity.value,
            unit: selectedUnit.value.name,
          };
          groceryItemsList.value.push(newItem);
          handleSelect('grocery', newItem);
        }
      }

      let item = {
        id: selectedGroceryItem.value.id,
        grocery_aisle: selectedGroceryItem.value.grocery_aisle_name,
        name: selectedGroceryItem.value.name,
        quantity: quantity.value,
        unit: selectedUnit.value.name,
      };

      groceryItems.value[selectedGroceryItem.value.id.toString()] = item;
      showAddGroceryItemModal.value = false;
      defaultAisle.value = '';
    }
  };
</script>

<template>
  <div class="modal-base">
    <div class="modal">
      <h2>Add grocery item</h2>
      <!-- Select existing grocery item -->
      <label>Grocery item</label>
      <div class="modal-option">
        <select v-model="selectedGroceryItem">
          <option
            v-for="item in groceryItemsList"
            :key="item"
            :selected="item.name == selectedGroceryItem.name ? true : false"
            :value="item"
          >
            {{ item.name }}
          </option>
        </select>
      </div>

      <!-- Add new grocery item -->
      <label for="new-ingredient" class="modal-label" v-if="!groceryItemSelected">New ingredient</label>
      <div class="modal-option" v-if="!groceryItemSelected">
        <input id="new-ingredient" type="text" v-model="newItemName" />
      </div>

      <!-- Existing aisle for new grocery item -->
      <label class="modal-label" v-if="!groceryItemSelected">Grocery aisle</label>
      <div class="modal-option" v-if="!groceryItemSelected">
        <select id="aisles" v-model="selectedAisle">
          <option
            v-for="aisle in aislesList"
            :key="aisle"
            :selected="aisle.name == selectedAisle.name ? true : false"
            :value="aisle"
          >
            {{ aisle.name }}
          </option>
        </select>
      </div>

      <!-- Add new aisle -->
      <label for="new-aisle" class="modal-label" v-if="!groceryItemSelected && !aisleSelected">New aisle</label>
      <div class="modal-option" v-if="!groceryItemSelected && !aisleSelected">
        <input id="new-aisle" type="text" v-model="newAisleName" />
      </div>

      <!-- Quantity -->
      <label for="quantity" class="modal-label">Quantity</label>
      <div class="modal-option">
        <input id="quantity" type="number" v-model="quantity" />
      </div>

      <!-- Select existing unit -->
      <label for="unit" class="modal-label">Unit</label>
      <div class="modal-option">
        <select id="unit" v-model="selectedUnit">
          <option
            v-for="unit in unitsList"
            :key="unit"
            :selected="unit.name == selectedUnit.name ? true : false"
            :value="unit"
          >
            {{ unit.name }}
          </option>
        </select>
      </div>

      <!-- Add new unit -->
      <label for="new-unit" class="modal-label" v-if="!unitSelected">New unit</label>
      <div class="modal-option" v-if="!unitSelected">
        <input id="new-unit" type="text" v-model="newUnitName" />
      </div>

      <button @click="handleSubmission()" class="submit">Submit</button>
    </div>
  </div>
</template>
