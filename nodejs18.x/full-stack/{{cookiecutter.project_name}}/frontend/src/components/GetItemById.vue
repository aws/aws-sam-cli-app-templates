<template>
  <div>    
    <form @submit.prevent="createItem">
      <div>
        <label for="userId">Item ID</label>
        <input type="text" id="userId" v-model="formData.userId" />
      </div>      
      <button @click="getItemsById">Get Item</button>
    </form>
  </div>
  <h3 v-if="user">{{ user.userId }} . {{ user.userName }}</h3>      
  <h3 v-if="errorMsg">{{ errorMsg }}</h3>
    
</template>

<script>
import axios from 'axios'

export default {
  name: 'GetItemById',  
  data() {
    return {
      user: '',
      formData: {
        userId: '',
      },      
      errorMsg: '',
    }
  },
  methods: {
    getItemsById() {
      axios
        .get(process.env.VUE_APP_API_ENDPOINT + this.formData.userId)
        .then((response) => {
          console.log(response)
          this.user = response.data
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