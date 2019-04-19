<template>
  <div>
    results -- {{this.$route.params.query}}
    {{output}}
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
    this.$route.params.query ? console.log("true") : this.$router.push({name: "Search"});

    let self = this;
    api(`query { search(search:"${this.$route.params.query}") { name port protocol description } }`).then(data => {
      console.log(data.search)
      self.output = data.search;
    })
  }
}
</script>

<style>
</style>
