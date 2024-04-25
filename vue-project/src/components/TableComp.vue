<script>
import ErrorComp from "./ErrorComp.vue";
import ModalComp from "./ModalComp.vue";
import EditComp from "./EditComp.vue";
import axios from 'axios'
export default {
  data() {
    return {
      none: false,
      ShowMod: false,
      item: '',
      isAdmin: false,
      editShow: false,
      edit: null,
      items: [{
        id: '3',
        Code: '2', 
        Fio: 'Абдулбек Максим Петрович',
        Floor: 'М',
        Age: '32',
        NumberHistory: '432423',
        Date1: '20.02.23',
        Date2: '20.02.23',
        Result: '1',
        Diagnosis: 'Дебилизм, тупой, ахахахахахахахаххха, прикол',
        Date3: '20.02.23',
        NameOperation: 'ШГылрпвлрув куцкуеукц укецукеукцецу ',
        CktDisk: '',
        MrtDisk: '',
        CtkModel: '',
        MrtModel: '',
        OperationVideo: '',
        EffectOfUse1: '1',
        Notes: 'цукецукецук',
        Fgds: '',
        Fks: '',
        Ckt: '',
        Mrt: '',
        Research: '',
        Protocol: '',
        DrugVideo: '',
        GistolСonclusion: '',
      },
        {
        id: '6',
        Code: '2', 
        Fio: 'Абдулбек Максим Петрович',
        Floor: 'М',
        Age: '32',
        NumberHistory: '432423',
        Date1: '20.02.23',
        Date2: '20.02.23',
        Result: '1',
        Diagnosis: 'Дебилизм, тупой, ахахахахахахахаххха, прикол',
        Date3: '20.02.23',
        NameOperation: 'ШГылрпвлрув куцкуеукц укецукеукцецу ',
        CktDisk: '',
        MrtDisk: '',
        CtkModel: '',
        MrtModel: '',
        OperationVideo: '',
        EffectOfUse1: '1',
        Notes: 'цукецукецук',
        Fgds: '../assets/edit.png',
        Fks: '',
        Ckt: '',
        Mrt: '',
        Research: '',
        Protocol: '',
        DrugVideo: '',
        GistolСonclusion: '',
        },
        {
        id: '7',
        Code: '2', 
        Fio: 'Абдулбек Максим Петрович',
        Floor: 'М',
        Age: '32',
        NumberHistory: '432423',
        Date1: '20.02.23',
        Date2: '20.02.23',
        Result: '1',
        Diagnosis: 'Дебилизм, тупой, ахахахахахахахаххха, прикол',
        Date3: '20.02.23',
        NameOperation: 'ШГылрпвлрув куцкуеукц укецукеукцецу ',
        CktDisk: '',
        MrtDisk: '',
        CtkModel: '',
        MrtModel: '',
        OperationVideo: '',
        EffectOfUse1: '1',
        Notes: 'цукецукецук',
        Fgds: '',
        Fks: '',
        Ckt: '',
        Mrt: '',
        Research: '',
        Protocol: '',
        DrugVideo: '',
        GistolСonclusion: '',
      },
      
      

      ],
   ritems:[],
   checkedId: '',
      code: '',
      gender: '',
      death: '',
      table: null

    };
  },

  methods: {

    async Check() {
      let response = await axios.get(`/check`);
      this.isAdmin = data.isAdmin;
    },
    async Content() {
      let response = await axios.get(`/show-all`);
      // this.items = response.data.all;
      console.log(this.items, 1)
    },
    async deleteItem() {
      await axios.delete(`/delete-string`,{
        data: {
          id: this.ritems
        }
      });

    },
    Show() {
      this.none = !this.none;
      
    },
    tog(id){
  let i = this.ritems.indexOf(id);
          if (i===-1){this.ritems.push(id);}
      else { this.ritems.splice(i, 1); }
  
    },

    ShowModal(Diagnosis) {
      this.ShowMod = !this.ShowMod
      this.item = Diagnosis;
      console.log(0)
      
    },
    ShowModal(Notes) {
      this.ShowMod = !this.ShowMod
      this.item = Notes;
      
    },
    async filtre(){
      
      if (false){
        this.filters = {
          'filtr': false
        }
      }
      else {
        this.filters = {
          filtr: true,
          code: '4',
          gender: 'М',
          death: '0',
        };
      }
      let res = await axios.post('/filtre', {
          body: {
            filters: this.filters
          }
      });
      this.table = res.data.all;
      console.log(this.table)
    },
    CloseModal(Show) {
            this.ShowMod = false
        },


  },
  mounted() {this.Content()},
  components: {
    ErrorComp,
    ModalComp,
    EditComp,
  },
};
</script>

<template>
  <error-comp v-if="false"/>
  <div class="container" v-if="true">
    <h1 class="head">DataBase</h1>
    <button @click='filtre'></button>
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
            <th>Построенная модель СТК</th>
            <th>Построенная модель МРТ</th>
            <th>Видео(фото) операции с ДР</th>
            <th>Эффект предоперационного применения ДР(0/1)</th>
            <th>Видео(фото) операции с ДР</th>
            <th>Примечания</th>
          </tr>
        </thead>
        <tbody>
            <tr v-for="(item, index) in items">
            <td v-if="none"><input type="checkbox" :value="item.id" @change="tog(item.id)" /></td> 
            <td><a :href="'/edit?id=' + item.id"><img src="../assets/edit.png" :alt="item" class="edit"></a></td>
            <td><a><div class="div">{{index + 1}}</div></a></td>
            <td>{{ item.Code }}</td>
            <td>{{item.Fio}}</td>
            <td>{{item.Floor}}</td>
            <td>{{item.Age}}</td>
            <td>{{ item.NumberHistory }}</td>
            <td>{{item.Date1}}</td>
            <td>{{item.Date2}}</td>
            <td>{{ item.Result }}</td>
            <td @click="ShowModal(item.Diagnosis)"><img src="../assets/share.png" class="share" :alt="item.Diagnosis"></td>
            <td><a :href="item.Fgds" download="fgds"><img src="../assets/folder.png" :alt="item.Fgds" class="folder" /></a></td>
            <td><a :href="item.Fks"><img src="../assets/folder.png" :alt="item.Fks" class="folder" /></a></td>
            <td><a :href="item.Ckt"><img src="../assets/folder.png" :alt="item.Ckt" class="folder"/></a></td>
            <td><a :href="item.Mrt"><img src="../assets/folder.png" :alt="item.Mrt" class="folder"/></a></td>
            <td><a :href="item.Research"><img src="../assets/folder.png" :alt="item.Research" class="folder"/></a></td>
            <td>{{ item.Date3 }}</td>
           <td @click="ShowModal(item.NameOperation)"><img src="../assets/share.png" class="share" :alt="item.NameOperation"></td>
            <td><a :href="item.Protocol"><img src="../assets/folder.png" :alt="item.Protocol" class="folder"/></a></td>
            <td><a :href="item.DrugVideo"><img src="../assets/folder.png" :alt="item.DrugVideo"  class="folder"/></a></td>
            <td><a :href="item.GistolСonclusion"><img src="../assets/folder.png" :alt="item.GistolСonclusion" class="folder"/></a></td>
            <td><a :href="item.CktDisk"><img src="../assets/Link.png" :alt="item.CktDisk" class="folder"/></a></td>
            <td><a :href="item.MrtDisk"><img src="../assets/Link.png" :alt="item.MrtDisk" class="folder"/></a></td>
            <td><a :href="item.CtkModel"><img src="../assets/Link.png" :alt="item.CtkModel" class="folder"/></a></td>
            <td><a :href="item.MrtModel"><img src="../assets/Link.png" :alt="item.MrtModel" class="folder"/></a></td>
            <td><a :href="item.OperationVideo"><img src="../assets/Link.png" :alt="item.OperationVideo" class="folder"/></a></td>
            <td>{{ item.EffectOfUse1 }}</td>
            <td><a :href="item.OperationVideo"><img src="../assets/folder.png" :alt="item.OperationVideo" class="folder"/></a></td>
            <td @click="ShowModal(item.Notes)"><img src="../assets/share.png" class="share" :alt="items.Notes"></td>
            </tr>

            
            
          </tbody>
        </table>
      </div>
    </div>
    <modal-comp v-if="ShowMod" :item="item" @CloseModal="CloseModal" />
</template>
<style scoped>

.edit{
  background: none;
  width: 30px;
  height: 30px;
  margin-left: 10px;
  cursor: pointer;
}
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
  max-width: 500px; /* Максимальная ширина ячейки */
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
@media (max-width: 900px) {
  .button1 img{
    width: 40px;
    height: 37px;
  }
  .buttons {
  margin-top: 20px;
  gap: 10px;
}
}
</style>
