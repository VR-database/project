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
        Date3: '',
        NameOperation: '',




        CktDisk: '',
        MrtDisk: '',
        CtkModel: '',
        MrtModel: '',
        OperationVideo: '',
        EffectOfUse1: '',
        Notes: '',
        
        

        Fgds: '',
        Fks: '',
        Ckt: '',
        Mrt: '',
        
        
        Research: '',



        Protocol: '',
        DrugVideo: '',
        GistolСonclusion: '',
      },
      
      
      file: '',
      status: '',
      id: '',


    }
  },
  methods: {
    routGet(){
       this.id = this.$route.query.id 
    },
    check() {
      if (this.form.Code == '' || this.form.Fio == '' || this.form.Floor == '' || this.form.Age == '' ||
        this.form.NumberHistory == '' || this.form.Date1 == '' || this.form.Date2 == '' && this.form.Result == '' ||
        this.form.Diagnosis == '' ||
        this.form.Date3 == '' || this.form.NameOperation == '' || 
        this.form.Notes == '') {
        this.status = 'Заполните все поля!'

      } else {
        this.status = 'Данные занесены в таблицу.'
        this.postData()
      }
    },
    async postData() {
        let response = await axios.put(`/update-string`, {
          form: this.form
        })
    },
    async getData() {
      let response = await axios.get(`/show-one`, {
        params: {
            id: this.id
          }
        }) 
    },

    convertFileFGDS(event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = () => {
        this.Fgds = reader.result;
        console.log(this.Fgds);

      };

      reader.readAsDataURL(file);
    },
    convertFileFKS(event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = () => {
        this.Fks = reader.result;
        console.log(this.Fks);

      };
      reader.readAsDataURL(file);
    },
    convertFileMRT(event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = () => {
        this.Mrt = reader.result;
        console.log(this.Mrt);

      };
      reader.readAsDataURL(file);
    },
    convertFileCKT(event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = () => {
        this.Ckt = reader.result;
        console.log(reader.result);

      };
      reader.readAsDataURL(file);
    },
    convertFileProtocol(event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = () => {
        this.Protocol = reader.result;
        console.log(reader.result);

      };
      reader.readAsDataURL(file);
    },

    convertFileDrugVideo(event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = () => {
        this.DrugVideo = reader.result;
        console.log(reader.result);

      };
      reader.readAsDataURL(file);
    },
    convertFileGistolСonclusion(event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = () => {
        this.GistolСonclusion = reader.result;
        console.log(reader.result);

      };
      reader.readAsDataURL(file);
    },
    convertFileResearch(event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = () => {
        this.Research = reader.result;
        console.log(reader.result);

      };
      reader.readAsDataURL(file);
    },
    convertFileCktDisk(event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = () => {
        this.CktDisk = reader.result;
        console.log(reader.result);

      };
      reader.readAsDataURL(file);
    },
    convertFileMrtDisk(event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = () => {
        this.MrtDisk = reader.result;
        console.log(reader.result);

      };
      reader.readAsDataURL(file);
    },
    convertFileCtkModel(event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = () => {
        this.CtkModel = reader.result;
        console.log(reader.result);

      };
      reader.readAsDataURL(file);
    },
    convertFileMrtModel(event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = () => {
        this.MrtModel = reader.result;
        console.log(reader.result);

      };
      reader.readAsDataURL(file);
    },
    convertFileOperationVideo(event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = () => {
        this.OperationVideo = reader.result;
        console.log(reader.result);

      };
      reader.readAsDataURL(file);
    },
    convertFileEffectOfUse1(event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = () => {
        this.EffectOfUse1 = reader.result;
        console.log(reader.result);

      };
      reader.readAsDataURL(file);
    },

  },
  mounted() {
    this.postData( )
  },
  props: {
    edit: Object,
  }
 
} 

</script>

<template>
  <div class="big-container d-flex">
    <div class="input-group">
      <h1 class="head" @click="routGet">Внести изменения</h1>
      <div class=""><button class="btn-back"><a href="/Table"><img src="../assets/back.png" alt=""></a></button></div>
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
  <input type="file" class="form-control"  placeholder="ФГДС"  @change="convertFileFGDS">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">ФКС</label>
  <input type="file" class="form-control"  placeholder="ФКС" @change="convertFileFKS">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Протокол СКТ</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Протокол" @change="convertFileCKT">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Протокол МРТ</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Протокол" @change="convertFileMRT">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Прочие исследования</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Исследования" @change="convertFileResearch">
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
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Протокол" @change="convertFileProtocol">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Фото (видео) препарата</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Фото, видео" @change="convertFileDrugVideo">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Гистологическое заключение</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Заключение" @change="convertFileGistolСonclusion">
    </div>

    <h4 class="mt-5 mb-3">Ссылки </h4>
    <div class="mb-3 mt-4">
  <label for="exampleFormControlInput1" class="form-label">Диск СКТ</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка" @change="convertFileCktDisk">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Диск МРТ</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка"  @change="convertFileMrtDisk">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Построенная модель СТК</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка"  @change="convertFileCtkModel">
    </div>

    <div class="mb-3">
  <label for="eleFormControlInput1" class="form-label">Построенная модель МРТ</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка" @change="convertFileMrtModel">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Видео(фото) операции с ДР</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка"  @change="convertFileOperationVideo">
    </div>

    <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Эффект предоперационного применения ДР(0/1)</label>
  <input type="file" class="form-control" id="exampleFormControlInput1" placeholder="Ссылка"  @change="convertFileEffectOfUse1">
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
.btn-back{
background: none;
border: none;
}
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