<template>
    <div id="app">

<table class="table">
  <thead>
  <tr>
  <th>Id</th>
  <th>User Id</th>
  <th>Title</th>
  <th>Description</th>
  <th>Status</th>
  <th>Created At</th>
  <th>Updated At</th>
  <th>Due</th>
  </tr>
  </thead>
  <tbody>
  <tr v-for="task in tasks" :key="task.id">
    <td>{{task.id}}</td>
    <td>{{task.user_id}}</td>
    <td>{{task.title}}</td>
    <td>{{task.description}}</td>
    <td>{{task.status}}</td>
    <td>{{task.createdat}}</td>
    <td>{{task.updatedat}}</td>
    <td>{{task.duedate}}</td>
  </tr>
  </tbody>
</table>


    </div>

</template>

<script>


export default {
  name: 'App',
  data(){
    return{
        tasks: []
    }
  },
  async created(){
    var response = await fetch('http://0.0.0.0:8000/api/v1/tasks');
     this.tasks = await response.json();
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
