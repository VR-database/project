<script>
import axios from 'axios'
axios.defaults.baseURL = 'https://api.ar-vmgh.ru/'
export default {
  data() {
    return {
      id: null,
      isShowPassword: false,
      showPassword: "password",
      eyeOpen: true,
      error: "",
      eyeImg: "/src/assets/eye.svg",
      isAdmin: true,
      isUser: null,

      isSession: null,
    };
  },
  methods: {
    async getId() {
      try {
        let response = await axios.get(`/get-id`);
        this.id = response.data.res;
        if (this.id === null) {
          this.isSession = false;
        } else {
          this.isSession = true;
        };
      } catch (err) {
        console.error(err);
        this.error = "Ошибка сервера";
        this.isSession = false;

      }
    },
    async Check() {
      let response = await axios.get(`/check`);
      this.isAdmin = response.data.isAdmin;
      if (this.isAdmin == "True") {
        this.isAdmin = true;
      } else if (this.isAdmin == "False") {
        this.isUser = true;
      } else {
        this.isUser = true;
      }
    },
  },
  mounted() {
    this.getId();
  },
};
</script>
<template>
  <nav class="navbar">
    <div class="container-fluid">
      <a class="navbar-brand" href="/">
        <img
          src="../assets/database.png"
          alt=""
          width="30"
          height="24"
          class="d-inline-block align-text-top"
        />
        <span class="title">VR Database</span>
      </a>
      <div>
      <a href="/Table" v-if="isAdmin"
        ><img src="../assets/stats.png" alt="" class="table"
      /></a>
      <a :href="`/Table/` + this.id" v-if="isUser"
        ><img src="../assets/stats.png" alt="" class="table"
      /></a>
    </div>
      <a href="/Profile" class="link" v-if="isSession">Кабинет</a>
      <a href="/Enter" class="link" v-else>Войти</a>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  background-color: blue;
  margin: 2px;
  border-radius: 10px;
}

.container-fluid {
  z-index: 2000;
}
.title {
  font-weight: 700;
  color: white;
}
.navbar-brand {
  margin-left: 10px;
}
.link {
  text-decoration: none;
  color: white;
  font-weight: 700;
  font-size: 22px;
  margin-right: 5px;
}
.table {
  width: 40px;
  height: 40px;
  margin-top: 0;
  margin-bottom: 0;
  position: absolute;
  right: 120px;
  cursor: pointer;
  top: 9px;
}
@media (max-width: 1000px) {
  .table {
    width: 30px;
    height: 30px;
    right: 90px;
    top: 11px;
  }
}
</style>
