<script>

</script>
<template>
<nav class="navbar ">
  <div class="container-fluid">
    <a class="navbar-brand" href="/">
      <img src="../assets/database.png" alt="" width="30" height="24" class="d-inline-block align-text-top">
      <span class="title">VR Database</span>
    </a>
   <a href="/Table"><img src="../assets/stats.png" alt="" class="table"></a>
    <a href="/login" class="link">Войти</a>
  </div>
</nav>


</template>

<style scoped>
.navbar{
  background-color: blue;
  margin: 2px;
  border-radius: 10px;
  
}

.container-fluid{
  z-index: 2000;
}
.title{
  font-weight: 700;
  color: white;
}
.navbar-brand{
  margin-left: 10px;
}
.link{
  text-decoration: none;
  color: white;
  font-weight: 700;
  font-size: 22px;
  margin-right: 5px;
}
.table{
  width: 40px;
  height: 40px;
  margin-top: 0;
  margin-bottom: 0;
  position: absolute;
  right: 100px;
  cursor: pointer;
  top: 9px;
}
@media (max-width: 1000px){
  .table{
  width: 30px;
  height: 30px;
  right: 90px;
  top: 11px;
}
}
</style>
