<template>
<div id="#app">
  <div id="nav">
     <router-link to="/">Go to Home</router-link>
    <router-link to="/subjects/">Go to Subjects</router-link>
  <!-- route outlet -->
  <!-- component matched by the route will render here -->
  <router-view></router-view>
    </div>
</div>
</template>

<script>

export default {
  name: "App",
};
</script>

<style>
</style>
