<script>
import axios from 'axios'
axios.defaults.baseURL = 'http://127.0.0.1:5000/'
export default {
    data() {
        return {
            password: '',
            isShowPassword: false,
            showPassword: 'password',
            eyeOpen: true,
            error: '',
            eyeImg: '/src/assets/eye.svg',
            isAdmin: true,
        }
    },
    methods: {
        check() {
            if ( this.password === '') {
                this.error = '*Заполните поле ввода*'
            } else { 
                this.error = ''
                this.login()
            } 
        },
        toggleVisibility() {
            this.isShowPassword = !this.isShowPassword
            this.eyeOpen = !this.eyeOpen

            if (this.isShowPassword) {
                this.showPassword = 'text'
                this.eyeImg = '/src/assets/svg-editor-image2.svg'
            } else {
                this.showPassword = 'password'
                this.eyeImg = '/src/assets/eye.svg'
            } 

        },
        async login() {
            let response = await axios.post(`/login`, {
                Login: this.password
            }); 
            this.isAdmin = response.data.isAdmin;
            if (this.isAdmin == 'Неверный пароль!') {
                this.error = this.isAdmin;
            } else if (this.isAdmin == false) {
                this.$router.push('/Add');
            } else if (this.isAdmin == true) {
                this.$router.push('/Table');
            }
            
        },
    },
}

</script>

<template>
    <div class="container">
        <h1>Вход</h1>
        <form action="#!">
           
            <div class="password">
                <input class="form-item" v-model="password" :type="showPassword" placeholder="Введите ключ доступа" name="" id="">
                <img @click="toggleVisibility" class="password-show" :src="eyeImg" alt="">
            </div>
        </form>
        <div class="error-end-btn">
            <p class="error">{{ error }}</p>
            <button class="btn-reg" @click="check">Войти</button>
        </div>
        <a href="/AcceptPassword">Сменить пароль</a>
    </div>
</template>

<style scoped>
.tt{
    color: white
}
.container {
    background: #ffffff;
    width: 400px;
    height: 500px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 100px;
    border-radius: 30px;
    border: solid 3px #2a2a2a;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}

h1 {
    font-size: 45px;
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
    margin-bottom: 25px;
    padding-left: 10px;
    padding-right: 10px;
}

.form-item:focus {
    outline: 2px solid #4200FF;
    border: none;
    transition: all 100ms;
}

.btn-reg {
    margin-top: 10px;

    width: 250px;
    height: 50px;
    border-radius: 12px;
    border: none;
    background-color: #4200FF;
    color: #fff;
    cursor: pointer;
    font-weight: 600;
    font-size: 20px;

   
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
    color: #4200FF;
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