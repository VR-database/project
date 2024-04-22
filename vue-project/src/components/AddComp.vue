<script>
import axios from 'axios'; 
axios.defaults.baseURL = 'http://127.0.0.1:5000';
// иди нах с точками и запятимыи так это не импорт

export default {



  data() {
    return{
      form:{
        Code: '', 
        Fio: '',
        Floor: '',
        Age: '',
        NumberHistory: '',
        Date1: '',
        Date2: '',
        Result: '',
        Diagnosis: '',
        Fgds: '',
        Fks: '',
        Ckt: '',
        Mrt: '',
        Research: '',
        Date3: '',
        NameOperation: '',
        Protocol: '',
        DrugVideo: '',
        GistolСonclusion: '',
        CktDisk: '',
        MrtDisk: '',
        CtkModel: '',
        MrtModel: '',
        OperationVideo: '',
        EffectOfUse: '',
        Notes: ''
      },
      
  
      status: '',


    }
  },
  methods: {
    check() {
      if (this.form.Code.length == 0 && this.form.Fio.length == 0 && this.form.Floor.length == 0 && this.form.Age.length == 0 &&
        this.form.NumberHistory.length == 0 && this.form.Date1.length == 0 && this.form.Date2.length == 0 && this.form.Result.length == 0 &&
        this.form.Diagnosis.length == 0 && this.form.Fgds.length == 0 && this.form.Fks.length == 0 && this.form.Ckt.length == 0 &&
        this.form.Mrt.length == 0 && this.form.Research.length == 0 &&

        this.form.Date3.length == 0 && this.form.NameOperation.length == 0 && this.form.Protocol.length == 0 && this.form.DrugVideo.length == 0 &&
        this.form.GistolСonclusion.length == 0 && this.form.CktDisk.length == 0 && this.form.MrtDisk.length == 0 &&

        this.form.CtkModel.length == 0 && this.form.MrtModel.length == 0 && this.form.OperationVideo.length == 0 && this.form.EffectOfUse.length == 0 &&
        this.form.Notes.length == 0) {
        return false

      } else {
        return true
      }
    },
    async postData() {
      if (check()) {
        let response = await axios.post(`/new-string`, {
          form: this.form
        })
        this.status = 'Данные занесены в таблицу.'
      } else {
        this.status = 'Заполните все поля.'
      }

    },
    

  

  },
 
} 

</script>

<template>
    <div class="big-container d-flex">
        <div class="input-group">
    <h1 class="head">Добавить в таблицу</h1>
    <form>
    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Код диагноза</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="1/2/3/4/5/6/7/8/9" v-model="form.Code">
  <p></p>
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">ФИО</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="ФИО" v-model="form.Fio">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Пол</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="М/Ж" v-model="form.Floor">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Возраст</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Возраст" v-model="form.Age">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Номер истории болезни</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Номер истории болезни" v-model="form.NumberHistory">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Дата госпитализации</label>
  <input type="date" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com" v-model="form.Date1">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Дата выписки (смерти)</label>
  <input type="date" class="form-control" id="exampleFormControlInput1" placeholder="Дата выписки (смерти)" v-model="form.Date2">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Исход (1 - выписан / 0 - умер)</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Исход" v-model="form.Result">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Диагноз окончательный</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Диагноз" v-model="form.Diagnosis">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">ФГДС</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="ФГДС" >
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">ФКС</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="ФКС" >
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Протокол СКТ</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Протокол">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Протокол МРТ</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Протокол">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Прочие исследования</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Исследования">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Дата операции</label>
  <input type="date" class="form-control" id="exampleFormControlInput1" placeholder="Дата операции" v-model="form.Date3">
    </div>



    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Название операции</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Название" v-model="form.NameOperation">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Протокол операции</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Протокол" >
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Фото (видео) препарата</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Фото, видео" >
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Гистологическое заключение</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Заключение">
    </div>

    <h4 class="mt-5 mb-3">Ссылки 
      (с протоколом http/https)
    </h4>
    <div class="mb-3 mt-4">
  <label for="exampleFormControlInput1" class="form-label">Диск СКТ</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка" v-model="form.CktDisk">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Диск МРТ</label>
  <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка" v-model="form.MrtDisk">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Построенная модель СТК</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка" v-model="form.CtkModel">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Построенная модель МРТ</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка" v-model="form.MrtModel">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Видео(фото) операции с ДР</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка" v-model="form.OperationVideo">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Эффект предоперационного применения ДР(0/1)</label>
  <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка" v-model="form.EffectOfUse">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlTextarea1" class="form-label">Примечания.</label>
  <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" v-model="form.Notes"></textarea>
    </div>
</form>
   <p class="p">{{ status }}</p> 
</div>

</div>
<div class="btn">
<button class="btn-reg btn" @click="check">Добавить</button>
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