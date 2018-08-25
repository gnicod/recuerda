import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home';
import TrainingWrapper from '@/components/TrainingWrapper';
import Callback from '@/components/Callback';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/training',
      name: 'TrainingWrapper',
      component: TrainingWrapper,
    },
    {
      path: '/training/:num',
      name: 'TrainingWrapper',
      component: TrainingWrapper,
    },
    {
      path: '/callback',
      name: 'Callback',
      component: Callback,
    },
  ],
});
