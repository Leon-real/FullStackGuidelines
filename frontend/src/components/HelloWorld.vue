<template>
    <div class="hello">
      <h1>{{ msg }}</h1>
    </div>
  </template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      // Message to display
      msg: 'Hello'
    }
  }
}
</script>

  <style scoped>
  h1 {
    font-weight: bold;
  }
  </style>
