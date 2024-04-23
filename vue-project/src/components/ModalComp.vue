<script>
import axios from "axios";
export default {
  props: {
    
    ShowMod: Boolean,
    item: String
  },
  data() {
    return {
      dish: "",
    };
  },
  mounted() {
    this.editInformation()
  },
  methods: {
    async editInformation() {
      
    },
    CloseModal() {
            this.$emit('CloseModal', this.ShowMod)
        }
  },

};
</script>

<template>
  <div class="modal-backdrop">
    <div class="window">
      <div class="close">
        <button class="btn" @click="CloseModal">X</button>
      </div>
      <h1>Информация <img src="../assets/edit.png" alt="" class="edit" @click="editInformation"></h1>
      <div class="scroll">
      <p>
        {{ item }}
      </p>
    </div>
    </div>
  </div>
</template>

<style scoped>
.edit{
  background: none;
  width: 30px;
  height: 30px;
  margin-left: 10px;
  cursor: pointer;
}
.scroll{
    overflow-x: scroll;
    height: 350px;
    padding: 20px;
}
.window {
  padding: 30px;
  z-index: 1000;
}

.window h1 {
  margin-top: 5px;
}

.window {
  background-color: #ffffff;
  border: 3px solid #2a2a2a;
  width: auto;
  max-width: 800px;
  min-width: 400px;
  height: auto;
  border-radius: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 50px;
  position: absolute;
  font-family: "Rubik", sans-serif;
  user-select: none;
  z-index: 3;
  margin-left: 10px;
  margin-right: 15px;
}

.buttons {
  display: flex;
  gap: 20px;
}

.close {
  width: 45px;
  height: 45px;
  background-color: #2a2a2a;
  position: absolute;
  top: 0px;
  right: 0px;
  border-radius: 0px 16px 0px 16px;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  border: none;
  border: 3px solid black;
}

.close:hover {
 
  border-radius: 0px 16px 0px 25px;
}



.btn {
  width: 45px;
  height: 45px;
  border-radius: 16px;
  background: none;
  border: none;
  color: #fff;
  font-size: 22px;
  font-weight: 500;
  cursor: pointer;
}
.modal-backdrop {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}
@media (max-width: 900px) {
    .window{
        margin-top: 50px;
    }
}
</style>
