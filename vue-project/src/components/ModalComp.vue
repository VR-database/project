<script>
import axios from "axios";
export default {
  props: {
    Oleg: Number,
    ShowModal: Boolean,
  },
  data() {
    return {
      dish: "",
    };
  },
  mounted() {},
  methods: {},
};
</script>

<template>
  <div class="modal-backdrop">
    <div class="window">
      <div class="close">
        <button class="btn" @click="CloseWindow">X</button>
      </div>
      <h1>Информация</h1>
      <div class="scroll">
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum libero
        neque quae culpa cupiditate laborum dolore veritatis corrupti facilis
        quisquam at harum, impedit officia, ipsa laboriosam doloribus, voluptas
        animi minima! Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        Libero illum inventore, cum sed eveniet voluptates est nam, similique
        dolore iusto error asperiores sint cumque deleniti nesciunt
        necessitatibus natus repudiandae minima? Lorem ipsum dolor sit amet
        consectetur adipisicing elit. Quas ipsam fuga qui iste quasi, tempora
        doloribus nesciunt labore deleniti possimus odit doloremque obcaecati
        voluptate sapiente. Consectetur rerum reprehenderit facilis iure? Lorem
        ipsum dolor sit amet consectetur adipisicing elit. Dolorum libero neque
        quae culpa cupiditate laborum dolore veritatis corrupti facilis quisquam
        at harum, impedit officia, ipsa laboriosam doloribus, voluptas animi
        minima! Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero
        illum inventore, cum sed eveniet voluptates est nam, similique dolore
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum libero
        neque quae culpa cupiditate laborum dolore veritatis corrupti facilis
        quisquam at harum, impedit officia, ipsa laboriosam doloribus, voluptas
        animi minima! Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        Libero illum inventore, cum sed eveniet voluptates est nam, similique
        dolore iusto error asperiores sint cumque deleniti nesciunt
        necessitatibus natus repudiandae minima? Lorem ipsum dolor sit amet
        consectetur adipisicing elit. Quas ipsam fuga qui iste quasi, tempora
        doloribus nesciunt labore deleniti pos
        


      </p>
    </div>
    </div>
  </div>
</template>

<style scoped>
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
  border: 2px solid #2a2a2a;
  width: auto;
  max-width: 800px;
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
