<script>
import axios from "axios";

export default {
  data() {
    return {
      code: "",
      isShowPassword: false,
      showPassword: "password",
      eyeOpen: true,
      error: "",
      eyeImg: "/src/assets/eye.svg",
      isAdmin: true,
    };
  },
  methods: {
    toggleVisibility() {
      this.isShowPassword = !this.isShowPassword;
      this.eyeOpen = !this.eyeOpen;

      if (this.isShowPassword) {
        this.showPassword = "text";
        this.eyeImg = "/src/assets/svg-editor-image2.svg";
      } else {
        this.showPassword = "password";
        this.eyeImg = "/src/assets/eye.svg";
      }
    },
    async login() {
      try {
        let response = await axios.post(`/check-pass-email`, {
          code: this.code,
        });
        const answer = response.data;
        if (answer == "True") {
          this.$router.push("/NewPass");
        } else if (answer == "False") {
          this.error = "Неверный код";
        }
      } catch (err) {
        this.error = "Ошибка сервера";
      }
    },
  },
};
</script>

<template>
  <div class="container">
    <h1>Код подтверждения</h1>
    <form @submit.prevent="login" >
      <div class="username">
        <input
          class="form-item"
          v-model="username"
          type="text"
          placeholder="Код"
          required
        />
        <p class="error" v-if="error">{{ error }}</p>

      </div>
      <button class="btn-reg" type="submit">Подтвердить</button>
    </form>
     
  </div>
</template>
<style scoped>
form{
    display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
.p {
  color: rgb(39, 18, 18);
}
.container {
  background: #ffffff;
  padding: 20px;
  max-width: 400px;
  /* margin-left: auto;
    margin-right: auto; */
  margin-top: 100px;
  border-radius: 30px;
  /* border: solid 3px #2a2a2a; */
  -webkit-box-shadow: -1px 0px 8px 4px rgba(34, 60, 80, 0.2);
  -moz-box-shadow: -1px 0px 8px 4px rgba(34, 60, 80, 0.2);
  box-shadow: -1px 0px 8px 4px rgba(34, 60, 80, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

h1 {
  font-size: 35px;
  margin-bottom: 50px;
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
  margin-bottom: 15px;
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
  transition: all .3s;
}

.btn-reg:hover {
  background-color: #2d00aa;
  border-radius: 25px 5px;
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
