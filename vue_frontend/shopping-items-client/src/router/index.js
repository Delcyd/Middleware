import Vue from 'vue';
import Router from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import AddItemView from '@/views/AddItemView.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    { path: '/', name: 'Home', component: HomeView },
    { path: '/add', name: 'AddItem', component: AddItemView },
  ],
});


