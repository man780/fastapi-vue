import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue';
import AboutView from '@/views/AboutView.vue';
import RegisterView from '@/views/RegisterView.vue';
import LoginView from '@/views/LoginView.vue';
import DashboardView from '@/views/DashboardView.vue';
import ProfileView from '@/views/ProfileView.vue';
import NoteView from '@/views/NoteView.vue';
import EditNoteView from '@/views/EditNoteView.vue';
import AdsView from '@/views/ads/ListView.vue';
import DetailAdView from '@/views/ads/DetailView.vue';
import EditAdView from '@/views/ads/EditView.vue';

import CarsView from '@/views/cars/ListView.vue';
import DetailCarView from '@/views/cars/DetailView.vue';
import BookCarView from '@/views/cars/BookView.vue';

import store from '@/store'; // NEW


const routes = [
  {
    path: '/',
    name: "Home",
    component: HomeView,
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterView,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardView,
    meta: { requiresAuth: true },
  },
  {
    path: '/cars',
    name: 'Cars',
    component: CarsView,
    meta: { requiresAuth: true },
  },
  {
    path: '/car/:id',
    name: 'Car',
    component: DetailCarView,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/car/:id',
    name: 'BookCar',
    component: BookCarView,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/ads',
    name: 'Ads',
    component: AdsView,
    meta: { requiresAuth: true },
  },
  {
    path: '/ad/:id',
    name: 'Ad',
    component: DetailAdView,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/editad/:id',
    name: 'EditAd',
    component: EditAdView,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView,
    meta: { requiresAuth: true },
  },
  {
    path: '/about',
    name: 'About',
    component: AboutView,
  },
  {
    path: '/note/:id',
    name: 'Note',
    component: NoteView,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/editnote/:id',
    name: 'EditNote',
    component: EditNoteView,
    meta: { requiresAuth: true },
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, _, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next('/login');
  } else {
    next();
  }
});

export default router;
