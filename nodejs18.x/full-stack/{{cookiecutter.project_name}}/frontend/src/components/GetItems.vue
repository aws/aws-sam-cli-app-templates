<template>
  <div>
    <button @click="getItems">Get User</button>
    <div v-for="user in users" :key="user.id">      
      <h4>{{ user.id }} || {{ user.name }}</h4>            
    </div>
    <h3 class="error" v-if="errorMsg">{{ errorMsg }}</h3>
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