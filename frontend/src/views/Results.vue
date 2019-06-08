<template>
  <div>
    <div class="results-search">
      <div class="top-margin-10">
        <div class="logo-container">
          <img
            height="40"
            src="/static/img/logo.png"
            class="logo"
            @click="$router.push({name: 'Search'});"
          >
        </div>
      </div>
      <div class="search">
        <input v-model="search" v-on:keyup.enter="run" autofocus>
        <button class="search-button" v-on:click="run">Search</button>
      </div>
    </div>

    <br>
    <div v-for="entry in output" :key="entry.id">
      <h3>Port: {{entry.port}} ({{entry.name}})</h3>
      <span>protocol: {{entry.protocol}}</span>
      <p>{{entry.description}}</p>

      <hr>
    </div>

    <div class="code-block" v-if="output">
      <pre id="json">{{output}}</pre>
    </div>
  </div>
</template>

<script>
import { api } from "@/api";

export default {
  name: "results",
  props: ["query"],
  data() {
    return {
      search: "",
      output: "",
      loading: false
    };
  },
  beforeMount() {
    if (this.$route.params.query) {
      this.search = this.$route.params.query;
      let self = this;
      api(
        `query { search(search:"${
          this.search
        }", skip:0, first:10) { name port protocol description } }`
      ).then(data => {
        console.log(data.search);
        self.output = data.search;
      });
    } else {
      this.$router.push({ name: "Search" });
    }
  },
  methods: {
    run() {
      this.output = "";
      let self = this;
      this.loading = true;
      api(
        `query { search(search:"${
          this.search
        }", skip:0, first:10) { name port protocol description } }`
      ).then(data => {
        console.log(data.search);
        self.output = data.search;
        self.loading = false;
      });
    }
  }
};
</script>

<style>
.results-search {
  height: 100px;
  background-color: #fff;
  border-bottom: 1px solid #ebebeb;
}
</style>
