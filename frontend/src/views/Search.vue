<template>
    <div>
        <div class="logo-container">
            <img height="100" src="/static/img/logo.png" class="logo">
        </div>
        <div class="search">
            <input class="shadow-input" v-model="search" v-on:keyup.enter="run" autofocus/>
            <button class="search-button shadow-button" v-on:click="run">Search</button>
        </div>

        <div class="center-text">
            <span class="fa-stack fa-4x icon-circle">
                <i class="fa fa-circle fa-stack-2x icon-background"></i>
                <i class="fa fa-search fa-stack-1x icon-color"></i>
                
            </span>

            <span class="fa-stack fa-4x icon-circle">
            <i class="fa fa-circle fa-stack-2x icon-background"></i>
            <i class="fa fa-terminal fa-stack-1x icon-color"></i>
            </span>

            <span class="fa-stack fa-4x icon-circle">
            <i class="fa fa-circle fa-stack-2x icon-background"></i>
            <i class="fa fa-code fa-stack-1x icon-color"></i>
            </span>
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
