import { createStore } from "vuex";

import notes from './modules/notes';
import users from './modules/users';
import ads from './modules/ads';
import cars from './modules/cars';

export default createStore({
  modules: {
    notes,
    users,
    ads,
    cars,
  }
});
