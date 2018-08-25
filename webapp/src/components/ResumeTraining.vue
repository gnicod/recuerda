<template>
  <div>
    <h3>
      Resume soon
    </h3>
    <p>nb wrong: {{wrong.length}}</p>
    <p>nb right: {{right.length}}</p>
  </div>
</template>

<script>
  export default {
    props: {
      right: Array,
      wrong: Array,
    },
    name: 'ResumeTraining',
  };
</script>

<style scoped>

</style>
