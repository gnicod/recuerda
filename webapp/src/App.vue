<template>
  <v-app>
    <v-toolbar
      color="white"
      app
      :clipped-left="clipped"
    >
      <v-btn icon @click.stop="rightDrawer = !rightDrawer">
        <v-icon>menu</v-icon>
      </v-btn>
      <router-link to="/">
        <v-toolbar-title v-text="title" ></v-toolbar-title>
      </router-link>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down-nope">
        <v-btn flat to="/training">Training</v-btn>
      </v-toolbar-items>
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
    </v-toolbar>
    <v-content>
      <router-view
        :auth="auth"
        :authenticated="authenticated">
      </router-view>
      <v-navigation-drawer
        temporary
        v-model="rightDrawer"
        app
      >
        <v-list>
          <v-list-tile>
            <v-list-tile-title>Recuerda</v-list-tile-title>
          </v-list-tile>
        </v-list>
        <v-divider></v-divider>

        <v-list class="pt-2">
          <v-list-tile >
            <v-list-tile-content>
              <v-list-tile-title>Logout</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-navigation-drawer>

    </v-content>
  </v-app>
</template>

<script>
  import AuthService from './auth/AuthService';

  const auth = new AuthService();

  const { login, logout, authenticated, authNotifier } = auth;

  export default {
    data() {
      authNotifier.on('authChange', (authState) => {
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
        title: 'Recuerda',
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
