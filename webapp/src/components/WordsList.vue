<template>
  <v-flex md7 sm12>
    <v-layout row>
      <div class="mr-4">
        <v-switch
          label="Show back"
          v-model="showBack"
        ></v-switch>
      </div>
      <div class="mr-4">
        <v-switch
          label="Show tags"
          v-model="showTags"
        ></v-switch>
      </div>
    </v-layout>
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
    <v-card v-for="it in words" style="width: 100%" class="mb-2">
      <v-card-title primary-title @click="openDialogUpdate(it)">
        <div style="width: 100%">
          <h3><i :class="`${it.lang} flag mr-2`"></i>{{it.front}} <v-progress-circular style="right: 0;float: right" class="" :value="80"></v-progress-circular></h3>
          <div v-if="showBack">{{it.back}}</div>
          <div v-if="showTags">
            <v-chip v-for="tag in it.tags" color="primary" small text-color="white">{{tag}}</v-chip>
          </div>
        </div>
      </v-card-title>
    </v-card>
    <v-dialog
      v-model="dialogUpdate"
      transition="dialog-bottom-transition">
      <v-card>
        <v-card-title>
          <span class="headline">Modify</span>
        </v-card-title>
        <v-card-text>
          <form-add-word :word.sync="selected"/>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-flex>
</template>

<script>
  import { getMemo, getTags, me } from '../api/recuerda';
  import FormAddWord from './FormAddWord';

  export default {
    name: 'WordsList',
    components: { FormAddWord },
    data() {
      return {
        words: [],
        showBack: false,
        showTags: false,
        dialogUpdate: false,
        tags: [],
        items: [],
        selected: {},
      };
    },
    methods: {
      openDialogUpdate(item) {
        console.log('shoul open');
        this.selected = item;
        this.dialogUpdate = true;
      },
    },
    mounted() {
      getMemo()
        .then((res) => {
          this.words = res.data.memos;
        });
      getTags()
        .then((res) => {
          this.items = res.data.tags;
        });
      me();
    },
  };
</script>

<style scoped>
  .flag {
    display: inline-block;
    width: 30px;
    height: 20px;
  }
</style>
