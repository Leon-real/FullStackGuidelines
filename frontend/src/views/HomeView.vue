<template>
  <div class="home">
    <!-- Hello component -->
    <HelloWorld />
  </div>
</template>

<script>
// Import HelloWorld component
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>
