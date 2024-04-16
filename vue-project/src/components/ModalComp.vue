<script>
import axios from 'axios';
axios.defaults.baseURL = 'http://localhost:3005';
export default {
    props: {
        Oleg: Number,
        ShowModal: Boolean,
    },
    data() {
        return {
            dish: '',
        }
    },
    mounted() {
        this.loadMorePreparation(),
        this.addCooking()
    },
    methods: {
        CloseWindow() {
            this.$emit('CloseWindow', this.ShowModal)
           
        },
        async loadMorePreparation() {
            let response = await axios.get(`/dish?id=${this.Oleg}`);
            this.dish = response.data;
        },
        async addCooking() {
            let responce = await axios.post(`/cooking/cook`, {
                id: this.Oleg,
            });
            
        }
    },
}
</script>

<template>
    <div class="modal-backdrop">
    <div class="window">
        <div class="close">
            <button class="btn" @click="CloseWindow">X</button>
        </div>
        <h1>Рецепт {{dish.title}}</h1>
        <p>{{ dish.preparation }}</p>
       

        <button class="btn btn-primary" @click="addCooking">Отправить на приготовление</button>

    </div>
</div>

</template>

<style scoped>
.window{
    padding: 30px;
}

.window h1{
    margin-top: 70px;
}

.window {
    background-color: #ffffff;
    border: 2px solid #2a2a2a;
    width: 500px;
    height: 500px;
    border-radius: 30px;
    
    display: flex;
    flex-direction: column;
    
    align-items: center;
    gap: 50px;

    position: relative;

    font-family: "Rubik", sans-serif;
    user-select: none;
}

.btn {
    width: 170px;
    height: 50px;
    border-radius: 12px;
    border: none;
    color: #fff;
    cursor: pointer;
    font-weight: 600;
    font-size: 16px;

    transition: all 100ms;
}


.buttons {
    display: flex;
    gap: 20px;
}

.close {
    width: 50px;
    height: 50px;
    background-color: #2a2a2a;
    position: absolute;
    top: 0;
    right: 0;
    border-radius: 0px 16px 0px 16px;

    display: flex;
    justify-content: center;
    align-items: center;

    transition: all 100ms;
}

.close:hover {
    background-color: #1a1a1a;
    border-radius: 0px 16px 0px 25px;
}

.close:active {
    background-color: #111111;
}

.btn-close {
    width: 50px;
    height: 50px;
    border-radius: 16px;
    background: none;
    border: none;
    color: #fff;
    font-size: 22px;
    font-weight: 500;

    cursor: pointer;
}
.modal-backdrop 
    {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

</style>