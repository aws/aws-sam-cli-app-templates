<template>
  <div>
    <form @submit.prevent="createItem">
      <div>
        <label for="userId">User ID </label>
        <input type="text" id="userId" v-model="formData.id" />
      </div>
      <div>
        <label for="userName">User Name</label>
        <input type="text" id="userName" v-model="formData.name" />
      </div>      
      <div>
        <button>Create User</button>
      </div>
    </form>
    <h3 v-if="response"> User created</h3>
    <h3 class="error" v-if="errorMsg">{{ errorMsg }}</h3>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CreateItem',
  data() {
    return {
      formData: {
        id: '',
        name: '',
      },
      errorMsg: '',
      response: '',
    }
  },
  methods: {
    createItem() {
      axios
        .post(process.env.VUE_APP_API_ENDPOINT, this.formData)
        .then((response) => {
          console.log(response)
          this.response = response
        })
        .catch((error) => {
          console.log(error)
          this.errorMsg = 'Error posting data'
        })
    },
  },
}
</script>

<style scoped>

</style>