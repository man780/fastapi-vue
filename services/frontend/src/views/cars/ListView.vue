<template>
  <div>
    
    <section>
      <h1>Cars</h1>
      <hr/><br/>

      <div v-if="cars">
        <table class="table">
          <thead>
            <tr>
              <th>Image</th>
              <th>Data</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="car in cars" :key="car.id">
              <td>
                <img :src="car.hero_image" class="img-thumbnail" style="height:100px;">
              </td>
              <td>
                <ul>
                  <li><strong>Car Title:</strong> {{ car.title }}</li>
                  <li><strong>Price:</strong> {{ car.price }}</li>
                  <li><strong>Make:</strong> {{ car.make }}</li>
                  <li><strong>Model:</strong> {{ car.model }}</li>
                </ul>
              </td>
              <td>
                <router-link :to="{name: 'Car', params:{id: car.id}}" class="btn btn-primary">Detail view</router-link>
                <router-link :to="{name: 'BookCar', params:{id: car.id}}" class="btn btn-success">Book</router-link>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div v-else>
        <p>Nothing to see. Check back later.</p>
      </div>
    </section>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'List',
  data() {
    return {
    };
  },
  computed: {
    ...mapGetters({ cars: 'stateCars'}),
  },
  methods: {
  },
  created: function() {
    return this.$store.dispatch('filterCars');
  },
});
</script>
