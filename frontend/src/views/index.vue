<template>
  <div class="flex-container">
      <div class="row"> 
        <div class="logo-container">
          <img height="100" src="/static/img/logo.png" class="logo">
        </div>
        <div class="search">
          <input v-model="search" v-on:keyup.enter="run" autofocus/>
          <button class="search-button" v-on:click="run">Search</button>
        </div>
        <div class="code-block" v-if="output">
          <pre id="json">{{output}}</pre>
        </div>
        <div class="clear">
          <button v-on:click="clear" v-if="output">CLEAR</button>
        </div>
      </div>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      search: "",
      output: ""
    }
  },
  methods: {
    run() {
      console.log(this.search)
      this.$router.push({ name: 'Results', params: { query: this.search } })
    },
    clear(){
      this.search = "";
      this.output = "";
    }
  }
}
</script>

<style>

</style>
