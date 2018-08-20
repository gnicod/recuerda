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
      <v-combobox
        v-model="lang"
        :items="langItems"
        label="Lang"
        chips
        clearable
        solo
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
      <v-btn v-if="!word" depressed large block v-on:click="addWord">Add</v-btn>
      <div v-if="word" >
        <v-btn color="info" depressed large block v-on:click="addWord">Update</v-btn>
        <v-btn color="error" depressed large block v-on:click="addWord">Delete</v-btn>
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
        lang: '',
        tags: [],
        items: [],
        langItems: ['es', 'cat'],
      };
    },
    watch: {
      word(newVal) {
        this.notes = newVal.notes;
        this.front = newVal.front;
        this.back = newVal.back;
        this.tags = newVal.tags;
        this.lang = newVal.lang;
      },
    },
    mounted() {
      getTags()
        .then((res) => {
          this.items = res.data.tags;
        });
    },
    methods: {
      addWord() {
        addMemo(this.front, this.back, this.lang, this.tags)
          .then(() => {
            this.snackbar = true;
            this.front = '';
            this.lang = '';
            this.back = '';
            this.tags = [];
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
