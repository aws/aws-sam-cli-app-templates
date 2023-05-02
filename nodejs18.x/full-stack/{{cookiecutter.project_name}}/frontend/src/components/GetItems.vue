<template>
  <div>
    <button @click="getItems">Get Items</button>
    <div v-for="user in users" :key="user.id">
      <h3>{{ user.id }}. {{ user.name }}</h3>      
      <hr />
    </div>
    <h3 v-if="errorMsg">{{ errorMsg }}</h3>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'GetItems',
  
  data() {
    return {
      users: [],
      errorMsg: '',
    }
  },
  methods: {
    getItems() {
      axios
        .get(process.env.VUE_APP_API_ENDPOINT)
        .then((response) => {
          console.log(response)
          this.users = response.data
        })
        .catch((error) => {
          console.log(error)
          this.errorMsg = 'Error retrieving data'
        })
    },
  },
}
</script>

<style scoped>
</style>