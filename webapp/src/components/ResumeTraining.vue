<template>
  <div>
    <hr class="mt-3 mb-3"/>

    <p class="text-xs-left" v-for="it in wrong"><b>{{it.front}}</b>: {{it.back}}</p>
  </div>
</template>

<script>
  import { postTraining } from '../api/recuerda';

  export default {
    props: {
      right: Array,
      wrong: Array,
    },
    mounted() {
      const payload = {};
      this.right.forEach((x) => {
        payload[x.front] = true;
      });
      this.wrong.forEach((x) => {
        payload[x.front] = false;
      });
      postTraining(payload).then((res) => {
        console.log(res);
      });
    },
    name: 'ResumeTraining',
  };
</script>

<style scoped>

</style>
