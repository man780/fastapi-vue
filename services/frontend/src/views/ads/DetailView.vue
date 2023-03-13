<template>
  <div v-if="ad">
    <p><strong>Title:</strong> {{ ad.title }}</p>
    <p><strong>Content:</strong> {{ ad.content }}</p>
    <p><strong>Author:</strong> {{ ad.author.username }}</p>

    <div v-if="user.id === ad.author.id">
      <p><router-link :to="{name: 'EditAd', params:{id: ad.id}}" class="btn btn-primary">Edit</router-link></p>
      <p><button @click="removeAd()" class="btn btn-secondary">Delete</button></p>
    </div>
  </div>
</template>


<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'Ad',
  props: ['id'],
  async created() {
    try {
      await this.viewAd(this.id);
    } catch (error) {
      console.error(error);
      this.$router.push('/ads');
    }
  },
  computed: {
    ...mapGetters({ ad: 'stateAd', user: 'stateUser'}),
  },
  methods: {
    ...mapActions(['viewAd', 'deleteAd']),
    async removeAd() {
      try {
        await this.deleteAd(this.id);
        this.$router.push('/ads');
      } catch (error) {
        console.error(error);
      }
    }
  },
});
</script>
