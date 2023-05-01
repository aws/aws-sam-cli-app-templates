<template>
  <div>
    <form @submit.prevent="createItem">
      <div>
        <label for="userId">Post User ID</label>
        <input type="text" id="userId" v-model="formData.userId" />
      </div>
      <div>
        <label for="title">Post Title</label>
        <input type="text" id="title" v-model="formData.title" />
      </div>
      <div>
        <label for="body">Post Body</label>
        <input type="text" id="body" v-model="formData.body" />
      </div>
      <button>Create Item</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CreateItem',
  data() {
    return {
      formData: {
        userId: '',
        title: '',
        body: '',
      },
    }
  },
  methods: {
    createItem() {
      axios
        .post(process.env.VUE_APP_API_ENDPOINT, this.formData)
        .then((response) => {
          console.log(response)
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
}
</script>

<style scoped>
</style>