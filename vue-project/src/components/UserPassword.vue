<script>
import axios from 'axios'
axios.defaults.baseURL = 'https://api.ar-vmgh.ru/'



export default {
    data() {
        return {
            password: '',
            isShowPassword: false,
            showPassword: 'password',
            eyeOpen: true,
            error: '',
            eyeImg: '/src/assets/eye.svg',
            Admin: false,
            form: {
                passwordOld: '',
                Newpassword1: '',
            },
            Newpassword2: '',
        }
    },
    methods: {
        check() {
            if ( this.form.passwordOld === '' || this.form.Newpassword1 === '' || this.Newpassword2 === '' ) {
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
            let response = await axios.post(`/change-pass`, {
                Login: this.form,
                Admin: this.Admin,
            }); 
            this.error = response.data.res;
            this.$router.push('/Add');
            
        },
    },
}

</script>

<template>
    <div class="container">
        <h1>Новый пароль</h1>
        <form action="#!">
           
            <div class="password">
                <input class="form-item" v-model="form.passwordOld" :type="showPassword" placeholder="Старый пароль" name="" id="">
                <img @click="toggleVisibility" class="password-show" :src="eyeImg" alt="">
            </div>
            <div class="password">
                <input class="form-item" v-model="form.Newpassword1" :type="showPassword" placeholder="Новый пароль" name="" id="">
                <img @click="toggleVisibility" class="password-show" :src="eyeImg" alt="">
            </div>
            <div class="password">
                <input class="form-item" v-model="Newpassword2" :type="showPassword" placeholder="Подтверждение нового пароля" name="" id="">
                <img @click="toggleVisibility" class="password-show" :src="eyeImg" alt="">
            </div>
        </form>
        <div class="error-end-btn">
            <p class="error">{{ error }}</p>
            <button class="btn-reg" @click="check">Войти</button>
        </div>
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
    font-size:30px;
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