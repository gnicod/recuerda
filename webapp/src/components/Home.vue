<template>
  <v-container fluid>
    <v-slide-y-transition mode="out-in">
      <v-layout row wrap>
        <v-flex  sm12 md5 pr-3 mb-5 class="hidden-xs-only">
          <form-add-word v-if="authenticated"/>
        </v-flex>

        <words-list v-if="authenticated"/>
      </v-layout>
    </v-slide-y-transition>
    <v-btn fab right dark fixed bottom color="primary" @click="dialogAdd = true">
      <v-icon dark>add</v-icon>
    </v-btn>

    <v-dialog
      v-model="dialogAdd"
      transition="dialog-bottom-transition">
      <v-card>
        <v-card-title>
          <span class="headline">Add</span>
        </v-card-title>
        <v-card-text>
          <form-add-word/>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
<script>
  import WordsList from './WordsList';
  import FormAddWord from './FormAddWord';

  export default {
    data() {
      return {
        dialogAdd: false,
      };
    },
    props: ['authenticated'],
    components: { FormAddWord, WordsList },
  };
</script>
