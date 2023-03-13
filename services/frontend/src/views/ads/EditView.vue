<template>
  <section>
    <h1>Edit ad</h1>
    <hr/><br/>

    <form @submit.prevent="submit">
      <div class="mb-3">
        <label for="title" class="form-label">Title:</label>
        <input type="text" name="title" v-model="form.title" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="content" class="form-label">Content:</label>
        <textarea
          name="content"
          v-model="form.content"
          class="form-control"
        ></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'EditAd',
  props: ['id'],
  data() {
    return {
      form: {
        title: '',
        content: '',
      },
    };
  },
  created: function() {
    this.GetAd();
  },
  computed: {
    ...mapGetters({ ad: 'stateAd' }),
  },
  methods: {
    ...mapActions(['updateAd', 'viewAd']),
    async submit() {
    try {
      let ad = {
        id: this.id,
        form: this.form,
      };
      await this.updateAd(ad);
      this.$router.push({name: 'Ad', params:{id: this.ad.id}});
    } catch (error) {
      console.log(error);
    }
    },
    async GetAd() {
      try {
        await this.viewAd(this.id);
        this.form.title = this.ad.title;
        this.form.content = this.ad.content;
      } catch (error) {
        console.error(error);
        this.$router.push('/ads');
      }
    }
  },
});
</script>
