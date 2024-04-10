<script>
import Axios from 'axios'; 
axios.defaults.baseURL = 'http://127.0.0.1:5000';
// иди нах с точками и запятимыи так это не импорт

export default {



  data() {
return {
      id: '', 
      form:{
        
           },
      
  
      status: '',


    }
  },
  methods: {
  

    async renderData() {
          let responce = await axios.post(`/update-string`, {
            id: this.id
          });Уверен?
          this.form = responce.data;
    },

    // вы со своей красотой кода заебали

  },
  mounted() {
    this.renderData();
    setInterval( () => { this.renderData(); }, 1000);
  }
} 

</script>

<template>
    <div class="big-container d-flex">
        <div class="input-group">
    <h1 class="head">Добавить в таблицу</h1>
    <form>
    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Код диагноза</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="1/2/3/4/5/6/7/8/9" v-model="Code">
  <p></p>
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">ФИО</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="ФИО" v-model="Fio">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Пол</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="М/Ж" v-model="Floor">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Возраст</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Возраст" v-model="Age">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Номер истории болезни</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Номер истории болезни" v-model="NumberHistory">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Дата госпитализации</label>
  <input type="date" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com" v-model="Date1">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Дата выписки (смерти)</label>
  <input type="date" class="form-control" id="exampleFormControlInput1" placeholder="Дата выписки (смерти)" v-model="Date2">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Исход (1 - выписан / 0 - умер)</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Исход" v-model="Result">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Диагноз окончательный</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Диагноз" v-model="Diagnosis">
    </div>

        <div class="mb-3">
  <label for="formFile" class="form-label">.docx/.doc</label>
  <input class="form-control form-control" id="formFileSm" type="file">
        </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">ФГДС</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="ФГДС" v-model="Fgds">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">ФКС</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="ФКС" v-model="Fks">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Протокол СКТ</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Протокол" v-model="Ckt">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Протокол МРТ</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Протокол" v-model="Mrt">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Прочие исследования</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Исследования" v-model="Research">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Дата операции</label>
  <input type="date" class="form-control" id="exampleFormControlInput1" placeholder="Дата операции" v-model="Date3">
    </div>


    <div class="mb-3">
  <label for="formFile" class="form-label">Файлы docx/doc</label>
  <input class="form-control form-control" id="formFileSm" type="file">
        </div>


    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Название операции</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Название" v-model="NameOperation">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Протокол операции</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Протокол" v-model= "Protocol">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Фото (видео) препарата</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Фото, видео" v-model="DrugVideo">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Гистологическое заключение</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Заключение" v-model="GistolСonclusion">
    </div>

    <h4 class="mt-5 mb-3">Ссылки</h4>
    <div class="mb-3 mt-4">
  <label for="exampleFormControlInput1" class="form-label">Диск СКТ</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка" v-model="CktDisk">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Диск МРТ</label>
  <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка" v-model="MrtDisk">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Построенная модель СТК</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка" v-model="CtkModel">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Построенная модель МРТ</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка" v-model="MrtModel">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Видео(фото) операции с ДР</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка" v-model="OperationVideo">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Эффект предоперационного применения ДР(0/1)</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка" v-model="EffectOfUse">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlTextarea1" class="form-label">Примечания.</label>
  <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" v-model="Notes"></textarea>
    </div>
</form>
   <p class="p">{{ status }}</p> 
</div>

</div>
<div class="btn">
<button class="btn-reg" @click="check">Добавить</button>
</div>
</template>

<style scoped>
.p{
  color: red;
}
.big-container{
    display: flex;
    margin-left: 40;
    margin-right: auto;
    margin-top: 20px;
    justify-content: center;
}
.container{
    background-color: black;
    width: 1000px;
    height: 700px;
    
}
.head{
    font-size: 50px;
    
}
.input-group{
    flex-direction: column;
    width: 900px;
    display: flex;
    gap: 20px;
    margin-top: 33px;
}
label{
    font-size: 18px;
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
    margin-left: 100px;
    justify-content: center;
    
}
.btn{
    display: block;
    margin-right: auto;
    margin-left: auto;
}
.btn-reg:hover {
    background-color: #2d00aa;
    border-radius: 25px 5px;
}

.btn-reg:active {
    background-color: #240088;
    transition: all 500ms;
}
</style>