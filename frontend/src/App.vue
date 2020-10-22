<template>
  <div id="app">
    <b>Напишите метод суммирующий два числа a и b:</b>
    <Training />
  </div>
</template>

<script>
import Training from './components/Training'

export default {
  name: 'app',
  components: {
    Training
  }
}

console.log('hello')
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  color: #2c3e50;
  margin-top: 60px;
  padding-left: 50px;
  padding-right: 50px;
}
</style>
