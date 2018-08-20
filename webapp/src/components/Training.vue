<template>
  <v-container grid-list-xl text-xs-center>
    <v-progress-linear v-model="progress"></v-progress-linear>
    <v-layout row  align-center justify-space-around  wrap>
      <v-flex xs12 md3 class="mb-3">
        <v-card dark color="primary" v-bind:class="{'pa-5' : $vuetify.breakpoint.smAndUp}">
          <v-card-text>xs10 offset-xs1</v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row  align-center justify-space-around  wrap>
      <v-flex xs12 md3>
        <v-card hover v-bind:class="{'pa-5' : $vuetify.breakpoint.smAndUp}">
          <v-card-text>xs10 offset-xs1</v-card-text>
        </v-card>
      </v-flex>
      <v-flex  xs12 md3>
        <v-card hover v-bind:class="{'pa-5' : $vuetify.breakpoint.smAndUp}">
          <v-card-text>xs10 offset-xs1</v-card-text>
        </v-card>
      </v-flex>
      <v-flex  xs12 md3>
        <v-card hover v-bind:class="{'pa-5' : $vuetify.breakpoint.smAndUp}">
          <v-card-text>xs10 offset-xs1</v-card-text>
        </v-card>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
  export default {
    name: 'Training',
    data() {
      return {
        progress: 25,
      };
    },
  };
</script>

<style scoped>

</style>
