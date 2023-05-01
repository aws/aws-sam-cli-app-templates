<template>
  <div>    
    <form @submit.prevent="createItem">
      <div>
        <label for="itemId">Item ID</label>
        <input type="text" id="itemId" v-model="formData.itemId" />
      </div>
      
      <button @click="getItemsById">Get Item</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'GetItemById',  
  data() {
    return {
      formData: {
        itemId: '',
      },      
      errorMsg: '',
    }
  },
  methods: {
    getItemsById() {
      axios
        .get(process.env.VUE_APP_API_ENDPOINT + this.formData.itemId)
        .then((response) => {
          console.log(response)
          this.posts = response.data
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