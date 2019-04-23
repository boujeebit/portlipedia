<template>
<div>

    <div class="flexContainer flexColumn fullHeight whiteBackground">
        <nav class="flexContainer">
            <ul class="nav flexItem flexStart">
                <img height="25" src="/static/img/logo.png" class="logo" @click="$router.push({name: 'Search'});">
            </ul>
            <ul class="nav flexContainer flexEnd grayText">
                <li><a href="#"><i class="fa fa-book fa-lg" aria-hidden="true"></i></a></li>
                <li><a href="#"><i class="fa fa-github fa-lg" aria-hidden="true"></i></a></li>
                <li><a href="#"><i class="fa fa-twitter fa-lg" aria-hidden="true"></i></a></li>
            </ul>
        </nav>
        <div class="flexContainer flexItem">
            <main class="flexItem whiteBackground main">



        <div class="logo-container">
          <img height="100" src="/static/img/logo.png" class="logo">
        </div>
        <div class="search">
          <input v-model="search" v-on:keyup.enter="run" autofocus/>
          <button class="search-button" v-on:click="run">Search</button>
        </div>

        <div class="center-text">
            <!-- <h3 >Ways to interact</h3> -->
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

            </main>
        </div>
        <footer class="flexContainer flexCenter grayText height50">&copy; 0xCODEs</footer>
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


h2 {
    text-align: center;
}
.container {
    width: 60%;
    margin: 50px auto;
    background: white;
    border-radius: 8px;
    padding: 50px 25px;
    border: 1px solid gray;
    box-shadow: 7px 7px 7px #777777;
}


/* *********************************
 *    Generic FlexBox Styling      *
 **********************************/
.flexContainer {
    display: flex;
}
.flexItem {
    flex: 1;
    align-items: center;
}
.flexStart {
    justify-content: flex-start;
}
.flexCenter {
    justify-content: center;
}
.flexEnd {
    justify-content: flex-end;
}
.flexWrap {
    flex-wrap: wrap;
}
.itemCenter {
    align-items: center;
}
.flexColumn {
    flex-direction: column;
}
.flexSpaceBetween {
    justify-content: space-between;
}
.flexSpaceAround {
    justify-content: space-around;
}

/* *********************************
 *    Shared Styling               *
 **********************************/
.fullHeight {
    height: 100vh;
}
.grayText {
    color: #6d6d6d;
}
.whiteBackground {
    background: white;
}
.whiteText {
    color: white;
}
.height50 {
    height: 50px;
    line-height: 50px;
}
.marginTop {
    margin-top: 50px;
}
.marginBottom {
    margin-bottom: 25px;
}

/* *********************************
 *    Navigation                   *
 **********************************/
.nav {
    list-style: none;
}
.nav a {
    text-decoration: none;
    display: block;
    padding: 0 1em;
    color: #6d6d6d;
}

.nav > img {
  -webkit-filter: grayscale(100%); /* Safari 6.0 - 9.0 */
  filter: grayscale(100%);
}
/* *********************************
 *    Responsive Website           *
 **********************************/
.main{
    order: 2;
    padding: 20px;
}

.center-text {
    text-align: center;
}

.icon-background {
    /* color: #0277be; */
    color: #f2f2f2;
}
.icon-color {
    color: #00579b;
}

.icon-circle {
    margin: 20px 15px 0 15px;
}



input {
  height: 50px;
  width: 50px;
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
