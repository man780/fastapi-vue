<template>
  <div>
    <section>
      <h1>Add new ad</h1>
      <hr/><br/>

      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="title" class="form-label">Title:</label>
          <input type="text" name="title" v-model="form.title" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="content" class="form-label">Content:</label>
          <textarea name="content" v-model="form.content" class="form-control"></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>

    <br/><br/>

    <section>
      <h1>Ads</h1>
      <hr/><br/>

      <div v-if="ads.length">
        <div v-for="ad in ads" :key="ad.id" class="ads">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
              <ul>
                <li><strong>Ad Title:</strong> {{ ad.title }}</li>
                <li><strong>Author:</strong> {{ ad.author.username }}</li>
                <li><router-link :to="{name: 'Ad', params:{id: ad.id}}">View</router-link></li>
              </ul>
            </div>
          </div>
          <br/>
        </div>
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
      ads: [],
      form: {
        title: '',
        content: '',
      },
    };
  },
  created: function() {
    return this.$store.dispatch('getAds');
  },
  computed: {
    ...mapGetters({ ads: 'stateAds'}),
  },
  methods: {
    ...mapActions(['createAd']),
    async submit() {
      await this.createAd(this.form);
    },
  },
});
</script>
