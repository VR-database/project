<script>
import ErrorComp from "./ErrorComp.vue";
import ModalComp from "./ModalComp.vue";
import EditComp from "./EditComp.vue";
import axios from "axios";
axios.defaults.baseURL = "https://api.ar-vmgh.ru/";

export default {
  data() {
    return {
      none: false,
      ShowMod: false,
      item: "",
      isAdmin: false,
      editShow: false,
      edit: null,
      items: [],
      fil: {
        code: "false",
        gender: "false",
        death: "false",
      },
      ritems: [],
      checkedId: "",
      code: "",
      gender: "",
      death: "",
      table: null,
      img: false,
      video: false,
      textbool: false,
      itemPhoto: false,
      itemVideo: false,
    };
  },

  methods: {
    async Check() {
      let response = await axios.get(`/check`);
      this.isAdmin = response.data.isAdmin;
      if (true) {
        this.Content();}
      // } else if (this.isAdmin == "False") {
      //   this.$router.push("/Add");
      // } else {
      //   this.$router.push("/login");
      // }
    },
    async Content() {
      const id = this.$route.params.id;
      let response = await axios.get(`/show-by-id?id=${id}`);
      this.items = response.data.all;
      console.log(this.items, 1);
    },
    async deleteItem() {
      await axios.delete(`/delete-string`, {
        data: {
          id: this.ritems,
        },
      });
      this.Content();
    },
    Show() {
      this.none = !this.none;
    },
    tog(id) {
      let i = this.ritems.indexOf(id);
      if (i === -1) {
        this.ritems.push(id);
      } else {
        this.ritems.splice(i, 1);
      }
      console.log(this.ritems);
    },

    ShowModal1(Diagnosis) {
      this.ShowMod = !this.ShowMod;
      this.item = Diagnosis;
      console.log(0);
      this.textbool = true;
    },
     ShowModal2(OperationVideo) {
      this.ShowMod = !this.ShowMod;
      this.itm = OperationVideo.toUpperCase()
      this.item = OperationVideo;
      if(this.itm.includes(".ZIP") || 
      this.itm.includes(".RAR") ||
      this.itm.includes(".ARJ") ||
      this.itm.includes(".CAB") ||
      this.itm.includes(".TAR") ||
      this.itm.includes(".LZH") 
    ) {
      this.isVideo = false
      this.isFile = true
      return;
    }
      if (
        this.item.includes(".jpg") ||
        this.item.includes(".png") ||
        this.item.includes(".jpeg")
      ) {
        this.textbool = false;
        this.itemPhoto = true;
        this.itemVideo = false;
      } else if (this.item.includes(".mkv") || this.item.includes(".mp4")) {
        this.textbool = false;
        this.itemPhoto = false;
        this.itemVideo = true;
      }
    },
    ShowModal3(Notes) {
      this.ShowMod = !this.ShowMod;
      this.item = Notes;
      this.textbool = true;
    },
    ShowModal4(DrugVideo) {
      this.ShowMod = !this.ShowMod;
      this.itm = DrugVideo.toUpperCase()
      this.item = DrugVideo;
      if(this.itm.includes(".ZIP") || 
      this.itm.includes(".RAR") ||
      this.itm.includes(".ARJ") ||
      this.itm.includes(".CAB") ||
      this.itm.includes(".TAR") ||
      this.itm.includes(".LZH") 
    ) {
      this.isVideo = false
      this.isFile = true
      return;
    }
      if (
        this.item.includes(".jpg") ||
        this.item.includes(".png") ||
        this.item.includes(".jpeg")
      ) {
        this.textbool = false;
        this.itemPhoto = true;
        this.itemVideo = false;
      } else if (this.item.includes(".mkv") || this.item.includes(".mp4")) {
        this.textbool = false;
        this.itemPhoto = false;
        this.itemVideo = true;
      }
    },
    ShowModal5(CktDisk) {
      this.ShowMod = !this.ShowMod;
      this.item = CktDisk;
      if (
        this.item.includes(".jpg") ||
        this.item.includes(".png") ||
        this.item.includes(".jpeg")
      ) {
        this.textbool = false;
        this.itemPhoto = true;
        this.itemVideo = false;
      } else if (this.item.includes(".mkv") || this.item.includes(".mp4")) {
        this.textbool = false;
        this.itemPhoto = false;
        this.itemVideo = true;
      }
    },
    ShowModal6(MrtDisk) {
      this.ShowMod = !this.ShowMod;
      this.item = MrtDisk;
      if (
        this.item.includes(".jpg") ||
        this.item.includes(".png") ||
        this.item.includes(".jpeg")
      ) {
        this.textbool = false;
        this.itemPhoto = true;
        this.itemVideo = false;
      } else if (this.item.includes(".mkv") || this.item.includes(".mp4")) {
        this.textbool = false;
        this.itemPhoto = false;
        this.itemVideo = true;
      }
    },
    ShowModal7(NameOperation) {
      this.ShowMod = !this.ShowMod;
      this.Item = NameOperation;
      this.textbool = true;
    },
    CloseModal(Show) {
      this.ShowMod = false;
    },
  },
  mounted() {
    this.Check();
  },
  components: {
    ErrorComp,
    ModalComp,
    EditComp,
  },
};
</script>

<template>
  <error-comp v-if="false" />
  <div class="container" v-if="true">
    <h1 class="head">Моя таблица</h1>

    <div class="buttons mb-5">
      <a class="button1" href="/Add"
        ><img src="../assets/image.png" alt=""
      /></a>
      <a class="button1" @click="Show"
        ><img src="../assets/delete.png" alt=""
      /></a>
    </div>
  </div>

  <div class="Container Flipped" v-if="true">
    <div class="Content">
      <table>
        <thead>
          <tr>
            <th v-if="none">
              <button class="none-btn" @click="deleteItem">
                <img src="../assets/delete.png" alt="" class="none-img" />
              </button>
            </th>
            <th id="1"></th>
            <th>ПП</th>
            <th>Код диагноза</th>
            <th>ФИО</th>
            <th>Пол</th>
            <th>Возраст</th>
            <th>№ истории болезни</th>
            <th>Дата госпитализации</th>
            <th>Дата выписки (смерти)</th>
            <th>Исход (1 - выписан / 0 - умер)</th>
            <th>Диагноз окончательный</th>
            <th>ФГДС</th>
            <th>ФКС</th>
            <th>Протокол СКТ</th>
            <th>Протокол МРТ</th>
            <th>Прочие исследования</th>
            <th>Дата операции</th>
            <th>Название операции</th>
            <th>Протокол операции</th>
            <th>Фото (видео) препарата</th>
            <th>Гистологическое заключение</th>
            <th>Диск СКТ</th>
            <th>Диск МРТ</th>
            <th>Построенная модель СКТ</th>
            <th>Построенная модель МРТ</th>
            <th>Эффект предоперационного применения ДР(0/1)</th>
            <th>Видео(фото) операции с ДР</th>
            <th>Примечания</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in items">
            <td v-if="none">
              <input type="checkbox" :value="item.id" @change="tog(item.id)" />
            </td>
            <td>
              <a :href="'/Edit?id=' + item.id"
                ><img src="../assets/edit.png" :alt="item" class="edit"
              /></a>
            </td>
            <td>
              <a
                ><div class="div">{{ index + 1 }}</div></a
              >
            </td>
            <td>{{ item.Code }}</td>
            <td>{{ item.Fio }}</td>
            <td>{{ item.Floor }}</td>
            <td>{{ item.Age }}</td>
            <td>{{ item.NumberHistory }}</td>
            <td>{{ item.Date1 }}</td>
            <td>{{ item.Date2 }}</td>
            <td>{{ item.Result }}</td>
            <td @click="ShowModal1(item.Diagnosis)">
              <img
                src="../assets/share.png"
                class="share"
                :alt="item.Diagnosis"
              />
            </td>
            <td>
              <a :href="item.Fgds" download="fgds" target="_blank"
                ><img
                  src="../assets/folder.png"
                  :alt="item.Fgds"
                  class="folder"
              /></a>
            </td>
            <td>
              <a :href="item.Fks" target="_blank"
                ><img src="../assets/folder.png" :alt="item.Fks" class="folder"
              /></a>
            </td>
            <td>
              <a :href="item.Ckt" target="_blank"
                ><img src="../assets/folder.png" :alt="item.Ckt" class="folder"
              /></a>
            </td>
            <td>
              <a :href="item.Mrt" target="_blank"
                ><img src="../assets/folder.png" :alt="item.Mrt" class="folder"
              /></a>
            </td>
            <td>
              <a :href="item.Research" target="_blank"
                ><img
                  src="../assets/folder.png"
                  :alt="item.Research"
                  class="folder"
              /></a>
            </td>
            <td>{{ item.Date3 }}</td>
            <td @click="ShowModal1(item.NameOperation)">
              <img
                src="../assets/share.png"
                class="share"
                :alt="item.NameOperation"
              />
            </td>
            <td>
              <a :href="item.Protocol" target="_blank"
                ><img
                  src="../assets/folder.png"
                  :alt="item.Protocol"
                  class="folder"
              /></a>
            </td>
            <td >
              <a :href="item.DrugVideo" target="_blank" v-if="this.isFile"
                ><img
                  src="../assets/folder.png"
                  :alt="item.DrugVideo"
                  class="folder"
              /></a>
            </td>
            <td>
              <a :href="item.GistolСonclusion" target="_blank"
                ><img
                  src="../assets/folder.png"
                  :alt="item.GistolСonclusion"
                  class="folder"
              /></a>
            </td>
            <td>
              <a :href="item.CktDisk" target="_blank"
                ><img
                  src="../assets/Link.png"
                  :alt="item.CktDisk"
                  class="folder"
              /></a>
            </td>
            <td>
              <a :href="item.MrtDisk" target="_blank"
                ><img
                  src="../assets/Link.png"
                  :alt="item.MrtDisk"
                  class="folder"
              /></a>
            </td>
            <td>
              <a :href="item.CktModel" target="_blank"
                ><img
                  src="../assets/Link.png"
                  :alt="item.CktModel"
                  class="folder"
              /></a>
            </td>
            <td>
              <a :href="item.MrtModel" target="_blank"
                ><img
                  src="../assets/Link.png"
                  :alt="item.MrtModel"
                  class="folder"
              /></a>
            </td>
            <td>{{ item.EffectOfUse1 }}</td>
            <td>
            
              <a :href="item.OperationVideo" target="_blank" v-if="this.isFile"
                ><img
                  src="../assets/folder.png"
                  :alt="item.OperationVideo"
                  class="folder"
              /></a>
            
            </td>
            <td @click="ShowModal3(item.Notes)">
              <img src="../assets/share.png" class="share" :alt="item.Notes" />
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <modal-comp
    v-if="ShowMod"
    :item="item"
    :textbool="textbool"
    :itemPhoto="itemPhoto"
    :itemVideo="itemVideo"
    @CloseModal="CloseModal"
  />
</template>
<style scoped>
.form-select {
  width: 200px;
}
.edit {
  background: none;
  width: 30px;
  height: 30px;
  margin-left: 10px;
  cursor: pointer;
}
.div {
  width: 100%;
  height: 100%;
}

table tbody tr:hover {
  background-color: rgba(128, 128, 128, 0.396);
}
table thead {
  background: #f2f2f2;
  position: sticky;
  top: 0;
  z-index: 1000;
  margin-top: 0px;
  border: 0.5px solid #000000;
}
table th {
  border: 1px solid #000;
  padding: 15px 15px;
  text-align: center;
  max-width: 500px; /* Максимальная ширина ячейки */
  overflow: hidden;
  text-overflow: ellipsis;
}
.share {
  width: 30px;
  height: 30px;
  cursor: pointer;
}
/* стили скрола */

.Container {
  overflow-y: scroll;
  height: 450px;
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
table td {
  border: 1px solid #000000;
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
@media (max-width: 900px) {
  .button1 img {
    width: 40px;
    height: 37px;
  }
  .buttons {
    margin-top: 20px;
    gap: 10px;
  }
}
</style>
