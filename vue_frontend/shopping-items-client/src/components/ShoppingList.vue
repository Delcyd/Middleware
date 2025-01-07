<template>
  <div>
    <h1>Shopping List</h1>
    <ul>
      <li v-for="item in items" :key="item.name">
        {{ item.name }} - {{ item.amount }}
        <button @click="deleteItem(item.name)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script>
import apiService from '@/apiService';

export default {
  data() {
    return {
      items: [],
    };
  },
  created() {
    this.fetchItems();
  },
  methods: {
    async fetchItems() {
      try {
        const response = await apiService.getAllItems();
        this.items = response.data;
      } catch (error) {
        console.error('Error fetching items:', error);
      }
    },
    async deleteItem(name) {
      try {
        await apiService.deleteItem(name);
        this.fetchItems();
      } catch (error) {
        console.error('Error deleting item:', error);
      }
    },
  },
};
</script>
