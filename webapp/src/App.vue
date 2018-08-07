<template>
  <v-app>
    <v-toolbar
      app
      :clipped-left="clipped"
    >
      <v-btn icon @click.stop="fixed = !fixed">
        <v-icon>remove</v-icon>
      </v-btn>
      <v-toolbar-title v-text="title"></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon @click.stop="rightDrawer = !rightDrawer">
        <v-icon>menu</v-icon>
      </v-btn>
    </v-toolbar>
    <v-content>
      <router-view
        :auth="auth"
        :authenticated="authenticated">
      </router-view>

      <v-btn color="info"
             id="qsLoginBtn"
             class="btn btn-primary btn-margin"
             v-if="!authenticated"
             @click="login()">
        Log in
      </v-btn>

      <v-btn
        color="warning"
        id="qsLogoutBtn"
        class="btn btn-primary btn-margin"
        v-if="authenticated"
        @click="logout()">
        Log Out
      </v-btn>
    </v-content>
    <v-navigation-drawer
      temporary
      :right="right"
      v-model="rightDrawer"
      fixed
      app
    >
      <v-list>
        <v-list-tile @click="right = !right">
          <v-list-tile-action>
            <v-icon>compare_arrows</v-icon>
          </v-list-tile-action>
          <v-list-tile-title>Switch drawer (click me)</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-footer :fixed="fixed" app>
      <span>&copy; 2017</span>
    </v-footer>
  </v-app>
</template>

<script>
  import AuthService from './auth/AuthService';

  const auth = new AuthService();

  const { login, logout, authenticated, authNotifier } = auth;

  export default {
    data() {
      authNotifier.on('authChange', (authState) => {
        console.log('looooo');
        this.authenticated = authState.authenticated;
      });
      return {
        clipped: false,
        drawer: true,
        fixed: false,
        items: [{
          icon: 'bubble_chart',
          title: 'Inspire',
        }],
        miniVariant: false,
        right: true,
        rightDrawer: false,
        title: 'Vuetify.js',
        auth,
        authenticated,
      };
    },
    methods: {
      login,
      logout,
    },
    name: 'App',
  };
</script>
