<script>
export default {
  data() {
    return {
      password: "",
      email: "",
      code: "",
      id: null,
      isShowPassword: false,
      showPassword: "password",
      eyeOpen: true,
      error: "",
      eyeImg: "/src/assets/eye.svg",
      isAdmin: true,
    };
  },
  methods: {
    async getId() {
      try {
        let response = await axios.get(`/get-id`);
        this.id = response.data.res;
      } catch (err) {
        this.error = "Ошибка сервера";
      }
    },
    gotable() {
      const id = this.id;
      this.$router.push(`/Table/${id}`);
    },
  },
  mounted() {
    this.getId();
  },
};
</script>

<template>
  <div class="container">
    <h1>Кабинет</h1>
    <button class="btn-reg" type="submit" @click="gotable">
      Сменить пароль
    </button>
    <button class="btn-reg" type="submit" @click="gotable">Моя таблица</button>
    <div class="error-end-btn"></div>
  </div>
</template>

<style scoped>
form {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
.tt {
  color: white;
}
.container {
  background: #ffffff;
  padding: 20px;
  max-width: 400px;
  /* margin-left: auto;
    margin-right: auto; */
  margin-top: 100px;
  border-radius: 30px;
  -webkit-box-shadow: -1px 0px 8px 4px rgba(34, 60, 80, 0.2);
  -moz-box-shadow: -1px 0px 8px 4px rgba(34, 60, 80, 0.2);
  box-shadow: -1px 0px 8px 4px rgba(34, 60, 80, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

h1 {
  font-size: 45px;
  margin-bottom: 20px;
  user-select: none;
}

form {
  display: flex;
  flex-direction: column;
}

.form-item {
  border: 2px solid #2a2a2a;
  border-radius: 10px;
  width: 320px;
  height: 50px;
  margin-bottom: 25px;
  padding-left: 10px;
  padding-right: 10px;
  font-weight: 500;
}

.form-item:focus {
  outline: 2px solid #4200ff;
  border: none;
  transition: all 100ms;
}

.btn-reg {
  margin-top: 10px;

  width: 250px;
  height: 50px;
  border-radius: 12px;
  border: none;
  background-color: #4200ff;
  color: #fff;
  cursor: pointer;
  font-weight: 600;
  font-size: 20px;
  transition: all 0.3s;
}

.btn-reg:hover {
  background-color: #2d00aa;
  border-radius: 25px 5px;
  transition: all 0.3s;
}

.btn-reg:active {
  background-color: #240088;
  transition: all 500ms;
}

.error {
  color: #ff2600;
  height: 20px;
  user-select: none;
}

.no_have_accaunt {
  margin: 0;
  font-size: 20px;
  user-select: none;
}

div a {
  font-size: 17px;
  text-decoration: none;
  color: #4200ff;
  margin-top: 20px;
}

.nha_div {
  margin-bottom: 16px;
}

.password {
  position: relative;
}

.password-show {
  position: absolute;
  cursor: pointer;
  top: 10px;
  right: 12px;
  width: 30px;
}
</style>
