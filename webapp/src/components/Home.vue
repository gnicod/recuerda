<script>
</script>

<template>
  <div>
    <h4 v-if="authenticated">
        You are logged in!
    </h4>
    <listlinguee v-if="authenticated" />
    <h4 v-if="!authenticated">
      You are not logged in! Please <a @click="auth.login()">Log In</a> to continue.
    </h4>
  </div>
</template>

<script>
  export default {
    name: 'home',
    props: ['auth', 'authenticated']
  }
</script>

<style>
  a {
    cursor: pointer;
  }
</style>

