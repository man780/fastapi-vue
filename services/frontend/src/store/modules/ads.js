import axios from 'axios';

const state = {
  ads: null,
  ad: null
};

const getters = {
  stateAds: state => state.ads,
  stateAd: state => state.ad,
};

const actions = {
  async createAd({dispatch}, ad) {
    await axios.post('ads', ad);
    await dispatch('getAds');
  },
  async getAds({commit}) {
    let {data} = await axios.get('ads');
    commit('setAds', data);
  },
  async viewAd({commit}, id) {
    let {data} = await axios.get(`ad/${id}`);
    commit('setAd', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateAd({}, ad) {
    await axios.patch(`ad/${ad.id}`, ad.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteAd({}, id) {
    await axios.delete(`ad/${id}`);
  }
};

const mutations = {
  setAds(state, ads){
    state.ads = ads;
  },
  setAd(state, ad){
    state.ad = ad;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
