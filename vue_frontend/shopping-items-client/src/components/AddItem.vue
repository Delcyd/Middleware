<template>
  <div>
    <h1>Add Shopping Item</h1>
    <form @submit.prevent="addItem">
      <input v-model="name" placeholder="Item Name" required />
      <input v-model.number="amount" type="number" placeholder="Amount" required />
      <button type="submit">Add</button>
    </form>
  </div>
</template>

<script>
import apiService from '@/apiService';

export default {
  data() {
    return {
      name: '',
      amount: null,
    };
  },
  methods: {
    async addItem() {
      try {
        const newItem = { name: this.name, amount: this.amount };
        await apiService.addItem(newItem);
        this.name = '';
        this.amount = null;
      } catch (error) {
        console.error('Error adding item:', error);
      }
    },
  },
};
</script>
