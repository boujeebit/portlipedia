<template>
  <div>
      <div class="results-search">
        <div class="search">
          <input v-model="$route.params.query" v-on:keyup.enter="run" autofocus/>
          <!-- <button class="search-button" v-on:click="run">Search</button> -->
        </div>
      </div>
    results -- {{this.$route.params.query}}



    <br>
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
      output: ""
    }
  },
  beforeMount (){
    let self = this;
    api(`query { search(search:"${this.$route.params.query}") { name port protocol description } }`).then(data => {
      console.log(data.search)
      self.output = data.search;
    })
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
