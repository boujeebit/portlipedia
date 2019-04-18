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
        <router-link tag="button" class="btn btn-secondary btn-sm" style="float: right" :to="{ name: 'Results', params: { query: 'vue' } }">Edit</router-link>
      </div>
  </div>
</template>

<script>
import { api } from '@/api'

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
      let self = this;
      api(`query { search(search:"${this.search}") { name port protocol description } }`).then(data => {
        console.log(data.search)
        self.output = data.search;
      }) 
    },
    clear(){
      this.search = "";
      this.output = "";
    }
  }
}
</script>

<style>
html, body {
    height: 100%;
    background-color: #fafbfc;
}
body {
    margin: 0;
}
.header {
  width: 100%;
  text-align: center;
}
.logo-container {
  width: 100%;
  text-align: center;
  margin-bottom: 15px;
}
.submit {
  background-color: #aaa;
}
.clear {
  text-align: center;
}
.clear > button {
  margin: 10px;
  height: 30px;
  width: 80px;
  border-radius: 10px;
  font-size: 14px;
}
.flex-container {
    height: 100%;
    padding: 0;
    margin: 0;
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;
    /* flex-wrap: nowrap; */
    align-items: center;
    justify-content: center;
}
.row {
    width: 40%;
}
.flex-item {
    background-color: tomato;
    padding: 5px;
    width: 500px;
    height: 20px;
    margin: 10px;
    line-height: 20px;
    color: white;
    font-weight: bold;
    font-size: 2em;
    text-align: center;
}

.code-block{
  margin-top: 15px; 
  background-color: #ddd;
  border: 1px solid #00579b;
  border-radius: 10px; 
  overflow-x: hidden;
}

.search {
  display:flex;
  flex-direction:row;

  padding:2px;
}
input {
  height: 50px;
  width: 100%;
  border: none;
  border-radius: 10px 0 0 10px;
  border: 1px solid #00579b;
  text-align: center; 
  font-size: 20px;
  flex-grow:2;
}
input:focus{
  outline: none;
}

.search-button {
  border:1px solid #00579b;
  background: #0277be;
  color:white;
  border-radius: 0 10px 10px 0;
  font-size: 14px;
}

button:focus {
  outline: none;
}
</style>
