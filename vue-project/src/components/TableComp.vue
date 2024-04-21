<script>
import ErrorComp from "./ErrorComp.vue";
import ModalComp from "./ModalComp.vue";
export default {
  data() {
    return {
      none: false,
      ShowMod: false,
      item: '',
      users: [
         {diagnosis: 'Плохой человек', urr: 'lflflf' },
         {diagnosis: 'Плохой человек' },
         {diagnosis: 'Плохой человек' },
         {diagnosis: 'Плохой человек' },
         {diagnosis: 'Плохой человек' },
         {diagnosis: 'Плохой человек' },

      ]

    };
  },

  methods: {
    Show() {
      this.none = !this.none;
      
    },
    ShowModal(diagnosis) {
      this.ShowMod = !this.ShowMod
      this.item = diagnosis;
      
    },
    ShowModal(urr) {
      this.ShowMod = !this.ShowMod
      this.item = urr;
      
    }


  },
  mounted() {},
  components: {
    ErrorComp,
    ModalComp,
  },
};
</script>

<template>
  <error-comp v-if="false" />
  <div class="container" v-if="true">
    <h1 class="head">DataBase</h1>
    <div class="buttons mb-5">
      <a class="button1" href="/Add"
        ><img src="../assets/image.png" alt=""
      /></a>
      <a class="button1" @click="Show"
        ><img src="../assets/delete.png" alt=""
      /></a>
      <a href="#1" class="button1"><img src="../assets/up.png" alt="" /></a>
    </div>
  </div>

  <div class="Container Flipped" v-if="true">
    <div class="Content">
      <table>
        <thead>
          <tr>
            <th v-if="none">
              <button class="none-btn">
                <img src="../assets/delete.png" alt="" class="none-img" />
              </button>
            </th>
            <th id="1">ПП</th>
            <th>Код диагноза</th>
            <th>ФИО</th>
            <th>Пол</th>
            <th>Возраст</th>
            <th>№ истории болезни</th>
            <th>Дата госпитализации</th>
            <th>Дата выписки (смерти)</th>
            <th>Исход (1 - выписан / 0 - умер)</th>
            <th>Диагноз окончательный</th>
            <th>.docx/.doc</th>
            <th>ФГДС</th>
            <th>ФКС</th>
            <th>Протокол СКТ</th>
            <th>Протокол МРТ</th>
            <th>Прочие исследования</th>
            <th>Дата операции</th>
            <th>Файлы docx/doc</th>
            <th>Название операции</th>
            <th>Протокол операции</th>
            <th>Фото (видео) препарата</th>
            <th>Гистологическое заключение</th>
            <th>Диск СКТ</th>
            <th>Диск МРТ</th>
            <th>Построенная модель СТК</th>
            <th>Построенная модель МРТ</th>
            <th>Видео(фото) операции с ДР</th>
            <th>Эффект предоперационного применения ДР(0/1)</th>
            <th>Видео(фото) операции с ДР</th>
            <th>Примечания</th>
          </tr>
        </thead>
        <tbody>
            <tr v-for="user in users">
            <td v-if="none"><input type="checkbox" /></td> 
            <td><a><div class="div">1</div></a></td>
            <td>3234</td>
            <td>Абдулбек Максим Петрович</td>
            <td>М</td>
            <td>30</td>
            <td>6537457</td>
            <td>06.04.24</td>
            <td>-</td>
            <td>1</td>
            <td @click="ShowModal(user.diagnosis)"><img src="../assets/share.png" class="share" :alt="user.diagnosis"></td>
            <td><a href=""><img src="../assets/folder.png" alt="" class="folder" /></a></td>
            <td><a href=""><img src="../assets/folder.png" alt="" class="folder" /></a></td>
            
            <td><a href=""><img src="../assets/folder.png" alt="" class="folder"/></a></td>
            <td><a href=""><img src="../assets/folder.png" alt="" class="folder"/></a></td>
            <td><a href=""><img src="../assets/folder.png" alt="" class="folder"/></a></td>
            <td><a href=""><img src="../assets/folder.png" alt="" class="folder"/></a></td>
            <td>07.04.24</td>
            <td>27539</td>
            <td><img src="../assets/share.png" class="share"></td>
            <td><a href=""><img src="../assets/folder.png" alt="" class="folder"/></a></td>
            <td><a href=""><img src="../assets/folder.png" alt="" class="folder"/></a></td>
            <td><a href=""><img src="../assets/folder.png" alt="" class="folder"/></a></td>
            <td><a href=""><img src="../assets/folder.png" alt="" class="folder"/></a></td>
            <td><a href=""><img src="../assets/folder.png" alt="" class="folder"/></a></td>
            <td><a href=""><img src="../assets/folder.png" alt="" class="folder"/></a></td>
            <td><a href=""><img src="../assets/folder.png" alt="" class="folder"/></a></td>
            <td><a href=""><img src="../assets/folder.png" alt="" class="folder"/></a></td>
            <td><a href=""><img src="../assets/folder.png" alt="" class="folder"/></a></td>
            <td><a href=""><img src="../assets/folder.png" alt="" class="folder"/></a></td>
            <td @click="ShowModal(user.urr)"><img src="../assets/share.png" class="share" :alt="user.urr"></td>
            </tr>

            

        </tbody>
      </table>
    </div>
  </div>
  <modal-comp v-if="ShowMod" :item="item" />
</template>
<style scoped>
.div{
width: 100%;
height: 100%;
}

table tbody tr:hover{
  background-color: rgba(128, 128, 128, 0.396);
}
table thead {
  background: #f2f2f2;
  position: sticky;
  top: 0;
  z-index: 1000;
  margin-top: 0px;
  border: 0.5px solid #fe00bf;
}
table th {
  border: 1px solid #fe00bf;
  padding: 15px 15px;
  text-align: center;
  max-width: 600px; /* Максимальная ширина ячейки */
  overflow: hidden;
  text-overflow: ellipsis;
}
.share{
  width: 30px;
  height: 30px;
  cursor:pointer;
}
/* стили скрола */

.Container {
  overflow-y: scroll;
  height: 500px;
  margin-right: 35px;
  margin-left: 30px;
  margin-bottom: 0px;
}

.Container table {
  display: inline-block;
  vertical-align: top;
  max-width: 100%;
  white-space: nowrap;
  table-layout: fixed;
  margin-right: 10px;
  margin-left: 10px;
  position: relative;
}
.folder {
  width: 30px;
  height: 30px;
}

.head {
  font-size: 60px;
  margin-top: 30px;
}
.buttons {
  margin-top: 30px;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.button1 img {
  width: 50px;
  height: 47px;
  cursor: pointer;
}
.button2 {
  background-color: red;
  width: 200px;
  height: 39px;
  color: white;
  border-radius: 10px;
  font-size: 20px;
  font-weight: 550;
  text-align: center;
  cursor: pointer;
}

.button1 img:hover {
  width: 55px;
  height: 50px;
  transition: all 0.4s;
}

table td {
  border: 1px solid #fe00bf;
  padding: 15px 15px;
  text-align: center;
  max-width: 600px; /* Максимальная ширина ячейки */
  overflow: hidden;
  text-overflow: ellipsis;
}

.none-btn {
  border: none;
  background: none;
}
.none-img {
  width: 20px;
  height: 20px;
  cursor: pointer;
}
</style>
