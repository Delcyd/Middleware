import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'PUT_YOUR_SERVER_IN_HERE/api', // Replace with your server URL
  headers: {
    'Content-Type': 'application/json',
  },
});

export default {
  getAllItems() {
    return apiClient.get('/shoppingItems');
  },
  getItemByName(name) {
    return apiClient.get(`/shoppingItems/${name}`);
  },
  addItem(item) {
    return apiClient.post('/shoppingItems', item);
  },
  updateItem(name, item) {
    return apiClient.put(`/shoppingItems/${name}`, item);
  },
  deleteItem(name) {
    return apiClient.delete(`/shoppingItems/${name}`);
  },
};
