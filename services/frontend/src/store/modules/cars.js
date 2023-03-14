import axios from 'axios';

const state = {
  cars: null,
  car: null
};

const getters = {
  stateCars: state => state.cars,
  stateCar: state => state.car,
};

const actions = {
  async getCars({commit}) {
    let {data} = await axios.get('cars');
    commit('setCars', data);
  },
  async filterCars({commit}) {
    let filterCarsPayload = {
      "page": 1,
      "limit": 200,
      "price": 0,
      "year": 0,
      "mileage": 0,
      "gearbox": 0,
      "engine_size": 0,
      "colour": 0,
      "fuel_type": 0,
      "body_type": 0,
      "doors": 0,
      "seats": 0,
      "make": "string",
      "model": "string"
    }
    let {data} = await axios.post('all', filterCarsPayload);
    commit('setCars', data.content);
  },
  async viewCar({commit}, id) {
    let {data} = await axios.get(`car/${id}`);
    commit('setCar', data);
  }
};

const mutations = {
  setCars(state, cars) {
    state.cars = cars;
  },
  setCar(state, car) {
    state.car = car;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
