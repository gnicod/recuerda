<template>
  <v-container grid-list-xl text-xs-center>
    <v-progress-linear v-model="progress"></v-progress-linear>
    <h3 v-if="i>0">Score: {{Math.round((this.nbRight/this.i)*100)}}%</h3>
    <h3 v-else>Score: </h3>
    <training
      v-if="i<training.length && training.length > 0"
      :question="training[i].question"
      :answers="training[i].answers"
      :onRight="onRight"
      :onWrong="onWrong"/>
    <resume-training
      v-if="i===training.length && training.length>0"
      :wrong="wrong"
      :right="right"
    />
  </v-container>
</template>

<script>
  import Training from './Training';
  import ResumeTraining from './ResumeTraining';
  import { getMemo } from '../api/recuerda';
  import { shuffle } from '../utils';

  export default {
    name: 'TrainingWrapper',
    computed: {
      progress() {
        return (this.i / this.training.length) * 100;
      },
    },
    data() {
      return {
        i: 0,
        nbRight: 0,
        training: [],
        wrong: [],
        right: [],
      };
    },
    methods: {
      onRight(question) {
        this.nbRight = this.nbRight + 1;
        this.i = this.i + 1;
        this.right.push(question);
      },
      onWrong(question) {
        this.i = this.i + 1;
        this.wrong.push(question);
      },
    },
    mounted() {
      getMemo()
        .then((res) => {
          const rndIndexes = [];
          const memos = res.data.memos;
          const randomIntFromInterval = (min, max, notIn = null) => {
            let rnd = Math.floor(Math.random() * (max - min + 1) + min);
            if (notIn === null) {
              return rnd;
            }
            while (notIn.includes(rnd)) {
              rnd = Math.floor(Math.random() * (max - min + 1) + min);
            }
            rndIndexes.push(rnd);
            return rnd;
          };
          const pickQuestion = (words, uniq = false) => {
            let rnd = 0;
            if (uniq) {
              rnd = randomIntFromInterval(0, words.length - 1, rndIndexes);
            } else {
              rnd = randomIntFromInterval(0, words.length - 1);
            }

            return words[rnd];
          };
          const nbQuestions = memos.length >= 10 ? 10 : memos.length;
          for (let i = 1; i <= nbQuestions; i++) {
            const el = pickQuestion(memos, true);
            const training = {
              question: el,
              answers: [
                el,
                pickQuestion(memos),
                pickQuestion(memos),
              ],
            };
            this.training.answers = shuffle(training.answers);
            this.training.push(training);
          }
        });
    },
    components: { ResumeTraining, Training },
  };
</script>

<style scoped>

</style>
