<template>
  <CreateItem />
  <hr />  
  <GetItemById />
  <hr />
  <GetItems />
</template>

<script>
import CreateItem from './components/CreateItem'
import GetItems from './components/GetItems'
import GetItemById from './components/GetItemById'
export default {
  name: 'App',
  components: {
    GetItems,
    CreateItem,
    GetItemById,
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
