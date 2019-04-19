<template>
  <div>
      <div class="results-search">
        <div class="top-margin-10">
          <div class="logo-container">
            <img height="40" src="/static/img/logo.png" class="logo">
          </div>
        </div>
        <div class="search">
          <input v-model="search" v-on:keyup.enter="run" autofocus/>
          <button class="search-button" v-on:click="run">Search</button>
        </div>
      </div>



    <br>
    Loading: {{loading}} -- {{search}}


    <div class="code-block" v-if="output">
          <pre id="json">{{output}}</pre>
        </div>
  </div>
</template>

<script>
import { api } from '@/api'

export default {
  name: 'results',
  props: ['query'],
  data () {
    return {
      search: "",
      output: "",
      loading: false
    }
  },
  beforeMount (){
    this.search = this.$route.params.query;
    let self = this;
    api(`query { search(search:"${this.search}", skip:0, first:10) { name port protocol description } }`).then(data => {
      console.log(data.search)
      self.output = data.search;
    })
  },
  methods: {
    run() {
      this.output = "";
      let self = this;
      this.loading = true;
      api(`query { search(search:"${this.search}", skip:0, first:10) { name port protocol description } }`).then(data => {
        console.log(data.search)
        self.output = data.search;
        self.loading = false;
      })
    }
  }
}
</script>

<style>
.results-search {
  height: 100px;
  background-color: #fff;
  border-bottom: 1px solid #ebebeb;
}
</style>
