<template>
  <div>    
    <form @submit.prevent="GetItemById">
      <div>
        <label for="userId">User ID</label>
        <input type="text" id="userId" v-model="formData.userId" />
      </div>
      <div>
        <button @click="getItemsById">Get User</button>
      </div>
    </form>
    <h3 v-if="user.id">{{ user.id }} . {{ user.name }}</h3>      
    <h3 class="error" v-if="errorMsg">{{ errorMsg }}</h3>
  </div>
    
</template>

<script>
import axios from 'axios'

export default {
  name: 'GetItemById',  
  data() {
    return {
      user: {
        id: '',
        name: ''
      },
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