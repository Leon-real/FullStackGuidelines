<template>
  <div id="app">
    <!-- Navigation component -->
    <nav>
      <router-link to="/">Home</router-link>
    </nav>
    <!-- Router view component -->
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
