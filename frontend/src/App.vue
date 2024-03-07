<template>
    <h1 class="text-blue-500">Hello, Tailwind CSS!</h1>
  <div id="app" class="min-h-screen bg-gray-100">
    <header class="bg-blue-500 text-white p-4 ">
      <h1>Welcome to the Interview Simulator</h1>
    </header>
    <main class="p-4">
      <HomePage />
    </main>
  </div>
</template>

<script>
import HomePage from './components/HomePage.vue'

export default {
  components: {
    HomePage
  },
}
</script>