<template>
  <div>
      <div class="flexContainer flexColumn fullHeight whiteBackground">
          <nav class="flexContainer">
              <ul class="nav flexItem flexStart">
                  <img height="25" src="/static/img/logo.png" class="logo" @click="$router.push({name: 'Search'});">
              </ul>
              <ul class="nav flexContainer flexEnd">
                  <li><a href="#"><i class="fa fa-book fa-lg" aria-hidden="true"></i></a></li>
                  <li><a href="#"><i class="fa fa-github fa-lg" aria-hidden="true"></i></a></li>
                  <li><a href="#"><i class="fa fa-twitter fa-lg" aria-hidden="true"></i></a></li>
              </ul>
          </nav>
          <div class="flexContainer flexItem">
              <main class="flexItem whiteBackground main">
                <router-view></router-view>
              </main>
          </div>
          <footer class="flexContainer flexCenter grayText height50">&copy; 0xCODEs</footer>
      </div>
  </div>
</template>

<script>

export default {
  name: 'default',
  data () {
    return {
    }
  }
}
</script>

<style>

</style>
