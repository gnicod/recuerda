<template>
  <v-flex>
    <v-form>
      <v-text-field
        v-model="front"
        label="Front"
        required
      ></v-text-field>
      <v-text-field
        v-model="back"
        label="Back"
        required
        block
      ></v-text-field>
      <v-combobox
        v-model="tags"
        :items="items"
        label="Tags"
        chips
        clearable
        prepend-icon="filter_list"
        solo
        multiple
      >
        <template slot="selection" slot-scope="data">
          <v-chip
            :selected="data.selected"
            close
            @input="remove(data.item)"
          >
            <strong>{{ data.item }}</strong>&nbsp;
          </v-chip>
        </template>
      </v-combobox>
      <div>
        <v-btn depressed large block v-on:click="addWord">Add</v-btn>
      </div>
    </v-form>
    <v-snackbar
      v-model="snackbar"
      :bottom="true"
      :timeout="6000"
    >
      Saved
      <v-btn
        color="pink"
        flat
        @click="snackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>
  </v-flex>
</template>

<script>
  import { addMemo, getTags } from '../api/recuerda';

  export default {
    name: 'FormAddWord',
    props: {
      word: Object,
    },
    data() {
      return {
        snackbar: false,
        front: '',
        back: '',
        tags: [],
        items: [],
      };
    },
    watch: {
      word(newVal, oldVal) { // watch it
        console.log('Prop changed: ', newVal, ' | was: ', oldVal);
        this.front = newVal.front;
        this.back = newVal.back;
        this.tags = newVal.tags;
      },
    },
    mounted() {
      getTags()
        .then((res) => {
          console.log(res);
          this.items = res.data.tags;
        });
    },
    methods: {
      addWord() {
        addMemo(this.front, this.back, this.tags)
          .then(() => {
            this.snackbar = true;
            this.front = '';
            this.back = '';
          });
      },
      remove(item) {
        this.tags.splice(this.tags.indexOf(item), 1);
        this.tags = [...this.tags];
      },
    },
  };
</script>

<style scoped>

</style>
