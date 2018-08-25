<template>
  <div>
    <v-layout row align-center justify-space-around wrap>
      <v-flex xs12 md3 class="mb-3">
        <v-card dark color="primary" v-bind:class="{'pa-5' : $vuetify.breakpoint.smAndUp}">
          <v-card-text>{{question.front}}</v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row align-center justify-space-around wrap>
      <v-flex xs12 md3>
        <v-card hover v-bind:class="{'pa-5' : $vuetify.breakpoint.smAndUp}">
          <v-card-text @click="checkAnswer(0)">{{answers[0].back}}</v-card-text>
        </v-card>
      </v-flex>
      <v-flex xs12 md3>
        <v-card hover v-bind:class="{'pa-5' : $vuetify.breakpoint.smAndUp}">
          <v-card-text @click="checkAnswer(1)">{{answers[1].back}}</v-card-text>
        </v-card>
      </v-flex>
      <v-flex xs12 md3>
        <v-card hover v-bind:class="{'pa-5' : $vuetify.breakpoint.smAndUp}">
          <v-card-text @click="checkAnswer(2)">{{answers[2].back}}</v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
  export default {
    name: 'Training',
    props: {
      question: Object,
      answers: Array,
      onRight: Function,
      onWrong: Function,
    },
    data() {
      return {
      };
    },
    methods: {
      checkAnswer(i) {
        if (this.answers[i].front === this.question.front) {
          window.setTimeout(this.onRight, 500);
        } else {
          window.setTimeout(this.onWrong, 500);
        }
      },
    },
  };
</script>

<style scoped>

</style>
