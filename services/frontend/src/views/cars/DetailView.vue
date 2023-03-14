<template>
  <div v-if="car">
    <h1>{{ car.title }}</h1>
    <div class="row">
      <div class="col">
        <img :src="car.hero_image" alt="">
      </div>
      <div class="col">
        <p><strong>Content:</strong> {{ car.content }}</p>
        <p><strong>Price:</strong> {{ car.price }}</p>
        <router-link class="btn btn-danger" to="/cars">Back to list</router-link>
      </div>
    </div>
    
    
  </div>
</template>


<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'Car',
  props: ['id'],
  async created() {
    try {
      await this.viewCar(this.id);
    } catch (error) {
      console.error(error);
      this.$router.push('/cars');
    }
  },
  computed: {
    ...mapGetters({ car: 'stateCar'}),
  },
  methods: {
    ...mapActions(['viewCar']),
    
  },
});
</script>
