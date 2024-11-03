<script>
import axios from "axios";
axios.defaults.baseURL = "https://api.ar-vmgh.ru/";

// иди нах с точками и запятимыи так это не импорт

export default {
  data() {
    return {
      form: {
        Code: "",
        Fio: "",
        Floor: "",
        Age: "",
        NumberHistory: "",
        Date1: "",
        Date2: "",
        Result: "",
        Diagnosis: "",
        Date3: "",
        NameOperation: "",

        CktDisk: "", //
        MrtDisk: "", //
        CktModel: "", //
        MrtModel: "", //
        OperationVideo: "", //
        EffectOfUse1: "",
        Notes: "",

        Fgds: "", //
        Fks: "", //
        Ckt: "", //
        Mrt: "", //

        Research: "", //

        Protocol: "", //
        DrugVideo: "", //
        GistolConclusion: "", //
        xyi: {
          xyi1: "",
          xyi2: "",
          xyi3: "",
          xyi4: "",
          xyi5: "",
          xyi6: "",
          xyi7: "",
          xyi8: "",
          xyi9: "",
          xyi10: "",
          xyi11: "",
          xyi12: "",
          xyi13: "",
          xyi14: "",
          xyi14: "",
          xyi15: "",
        },
      },

      file: "",
      status: "",

      // isLoading: false,
      // uploadProgress: 0,

      convertFileFGDStext: "Файл незагружен.",
      convertFileFKStext: "Файл незагружен.",
      convertFileCKTtext: "Файл незагружен.",
      convertFileFKStext: "Файл незагружен.",
      convertFileFGDStext: "Файл незагружен.",
      convertFileCKTtext: "Файл незагружен.",
      convertFileMRTtext: "Файл незагружен.",
      convertOtherstext: "Файл незагружен.",
      convertProtokolOperationtext: "Файл незагружен.",
      convertPhotoVudeotext: "Файл незагружен.",
      convertGostoltext: "Файл незагружен.",
      convertDiskCKTtext: "Файл незагружен.",
      convertDiskMRTtext:"Файл незагружен.",
      convertModelCKTtext:"Файл незагружен.",
      convertModelMRTtext: "Файл незагружен.",
      convertOperationVideotext: "Файл незагружен.",
      convertPhotoVideotext: "Файл незагружен.",

      classFileFGDStext: "notdownload",
      classFileFKStext: "notdownload",
      classFileCKTtext: "notdownload",
      classFileFKS: "notdownload",
      classFileFGDS: "notdownload",
      classFileCKT: "notdownload",
      classFileMRT: "notdownload",
      classOthers: "notdownload",
      classProtokolOperation: "notdownload",
      classPhotoVudeo: "notdownload",
      classGostol: "notdownload",
      classDiskCKT: "notdownload",
      classDiskMRT: "notdownload",
      classModelCKT: "notdownload",
      classModelMRT: "notdownload",
      classOperationVideo: "notdownload",
      classPhotoVideo: "notdownload",
      
      isUploading: true,
      percentCompleted: 0,
      isLoading: false,

    };
  },
  methods: {
    async Check() {
      let response = await axios.get(`/check`);
      this.isAdmin = response.data.isAdmin;
      if (this.isAdmin == "True") {
        this.getData();
        this.routGet();
      } else if (this.isAdmin == "False") {
        this.getData();
        this.routGet();
      } else {
        this.$router.push("/login");
      }
    },
    check() {
      if (false) {
        this.status = "Заполните все поля!";
      } else {
        this.postInfo();
        console.log(this.form);
      }
    },
    async postInfo() {

  this.isLoading = true;
  this.isUploading = true;


    try {
      await axios.post(
        "/new-string",
        {
          chunk: chunk,
          index: i,
          totalChunks: totalChunks
        },
        {
          onUploadProgress: (progressEvent) => {
            const percentCompleted = Math.round(
              (progressEvent.loaded * 100) / progressEvent.total
            );
            this.percentCompleted = percentCompleted;
          }
        }
      );
    } catch (error) {
      console.error("Ошибка при отправке данных:", error);
      this.isUploading = false;
      // Добавьте обработку ошибки
      return;
    }


  this.isUploading = false;
  this.isLoading = false;
  this.status = "Данные занесены в таблицу.";
  this.$router.push('/Table');
},
    async postData() {
      let response = await axios.post(`/new-string`, {
        form: this.form,
      });
      this.$router.push('/Table');
    },
    convertFileCktDisk(event) {
      if (this.form.Fgds == 0 || true) {
      this.convertDiskCKTtext = "Файл загружается...";
      this.classDiskCKT ="load";
        
      const file = event.target.files[0];
      const filename = event.target.files[0].name;
      this.form.xyi.xyi1 = filename;

      const reader = new FileReader();

      reader.onload = () => {
        this.form.CktDisk = reader.result;
        ;

        this.convertDiskCKTtext = "Файл загружен";
        this.classDiskCKT = "download";
      };

      reader.readAsDataURL(file);
      }
    },
    convertFileMrtDisk(event) {
      if (true) {
        this.convertDiskMRTtext = "Файл загружается...";
        this.classDiskMRT = "load";

        const file = event.target.files[0];
        const reader = new FileReader();
        const filename = event.target.files[0].name;
        this.form.xyi.xyi2 = filename;
        
        reader.onload = () => {
          this.form.MrtDisk = reader.result;
          console.log(this.form.MrtDisk);
          
          this.convertDiskMRTtext = "Файл загружен";
          this.classDiskMRT = "download";
        };
        reader.readAsDataURL(file);
      }

    },
    convertFileCktModel(event) {
      if (this.form.CktModel == 0 || true) {
      this.convertModelCKTtext = "Файл загружается...";
      this.classModelCKT = "load";

      const file = event.target.files[0];
      const reader = new FileReader();
      const filename = event.target.files[0].name;
      this.form.xyi.xyi3 = filename;

      reader.onload = () => {
        this.form.CktModel = reader.result;
        console.log(this.form.CktModel);
      
        this.convertModelCKTtext = "Файл загружен";
        this.classModelCKT = "download";
      };
      reader.readAsDataURL(file);
      }
    },
    convertFileMrtModel(event) {
      if (this.form.MrtModel == 0 || true) {
      this.convertModelMRTtext = "Файл загружается...";
      this.classModelMRT = "load";

      const file = event.target.files[0];
      const reader = new FileReader();
      const filename = event.target.files[0].name;
      this.form.xyi.xyi4 = filename;

      reader.onload = () => {
        this.form.MrtModel = reader.result;
        console.log(reader.result);

        this.convertModelMRTtext = "Файл загружен";
        this.classModelMRT = "download";
      };
      reader.readAsDataURL(file);
      }
    },
    convertFileOperationVideo(event) {
      if (this.form.OperationVideo == 0 || true) {
      this.convertOperationVideotext = "Файл загружается...";
      this.classOperationVideo = "load";

      const file = event.target.files[0];
      const reader = new FileReader();
      const filename = event.target.files[0].name;
      this.form.xyi.xyi5 = filename;

      reader.onload = () => {
        this.form.OperationVideo = reader.result;
        console.log(reader.result);

        this.convertOperationVideotext = "Файл загружен";
        this.classOperationVideo = "download";
      };
      reader.readAsDataURL(file);
      }
    },

    convertFileEffectOfUse1(event) {
      if (this.form.EffectOfUse1 == 0 || true) {
      const file = event.target.files[0];
      const reader = new FileReader();
      const filename = event.target.files[0].name;
      this.form.xyi.xyi6 = filename;

      reader.onload = () => {
        this.form.EffectOfUse1 = reader.result;
        console.log(reader.result);
      };
      reader.readAsDataURL(file);
      }
    },
    convertFileGistolConclusion(event) {
      if (this.form.GistolConclusion == 0 || true) {
      this.convertGostoltext = "Файл загружается..."
      this.classGostol = "load"

      const file = event.target.files[0];
      const reader = new FileReader();
      const filename = event.target.files[0].name;
      this.form.xyi.xyi15 = filename;

      reader.onload = () => {
        this.form.GistolConclusion = reader.result;
        console.log(reader.result);

        this.convertGostoltext = "Файл загружен"
        this.classGostol = "download"
      };
      reader.readAsDataURL(file);
      }
    },
    convertFileFGDS(event) {
      if (this.form.Fgds == 0 || true) {
        this.convertFileFGDStext = "Файл загружается...";
        this.classFileFGDS = "load";

        const file = event.target.files[0];
        const reader = new FileReader();
        const filename = file.name;
        this.form.xyi.xyi8 = filename;

        reader.onload = () => {
          this.form.Fgds = reader.result;
          console.log(reader.result);

          // Обновляем текст и класс после завершения загрузки файла
          this.convertFileFGDStext = "Файл загружен.";
          this.classFileFGDS = "download";
        };

        reader.readAsDataURL(file);
        }
    },
    convertFileFKS(event) {
      if (this.form.Fks == 0 || true) {
        this.convertFileFKStext = "Файл загружается...";
        this.classFileFKS = "load";

        const file = event.target.files[0];
        const reader = new FileReader();
        const filename = event.target.files[0].name;
        this.form.xyi.xyi9 = filename;

        reader.onload = () => {
          this.form.Fks = reader.result;
          console.log(reader.result);

          this.convertFileFKStext = "Файл загружен.";
          this.classFileFKS = "download";
        };
        reader.readAsDataURL(file);
        }
    },
    convertFileCKT(event) {
      if (this.form.Ckt == 0 || true) {
        this.convertFileCKTtext = "Файл загружается...";
        this.classFileCKT = "load";

        const file = event.target.files[0];
        const reader = new FileReader();
        const filename = event.target.files[0].name;
        this.form.xyi.xyi10 = filename;
        console.log(this.form.xyi.xyi10);

        reader.onload = () => {
          this.form.Ckt = reader.result;
          console.log(reader.result);

          this.convertFileCKTtext = "Файл загружен.";
          this.classFileCKT = "download";
        };
        reader.readAsDataURL(file);
        }
    },
  convertFileMRT(event) {
    if (this.form.Mrt == 0 || true) {
    this.convertFileMRTtext = "Файл загружается...";
    this.classFileMRT = "load";

    const file = event.target.files[0];
    const reader = new FileReader();
    const filename = event.target.files[0].name;
    this.form.xyi.xyi11 = filename;

    reader.onload = () => {
      this.form.Mrt = reader.result;
      console.log(reader.result);

      this.convertFileMRTtext = "Файл загружен";
      this.classFileMRT = "download";
    };
    reader.readAsDataURL(file);
    }
  },
  convertFileProtocol(event) {
    if (this.form.Protocol == 0 || true) {
    this.convertProtokolOperationtext = "Файл загружается...";
    this.classProtokolOperation = "load";

    const file = event.target.files[0];
    const reader = new FileReader();
    const filename = event.target.files[0].name;
    this.form.xyi.xyi13 = filename;

    reader.onload = () => {
      this.form.Protocol = reader.result;
      console.log(reader.result);

      this.convertProtokolOperationtext = "Файл загружен";
      this.classProtokolOperation = "download";
    };
    reader.readAsDataURL(file);
    }
  },
  convertFileDrugVideo(event) {
    if (this.form.DrugVideo == 0 || true) {
      this.convertPhotoVideotext= "Файл заугружается"
      this.classPhotoVideo = "load"

      const file = event.target.files[0];
      const reader = new FileReader();
      const filename = event.target.files[0].name;
      this.form.xyi.xyi14 = filename;

      reader.onload = () => {
        this.form.DrugVideo = reader.result;
        console.log(reader.result);

        this.convertPhotoVideotext = "Файл заугружен"
        this.classPhotoVideo = "download"
      };
      reader.readAsDataURL(file);
    }
  },
  convertFileResearch(event) {
    if (this.form.Research == 0 || true) {
    this.convertOtherstext = "Файл загружается..."
    this.classOthers = "load";

    const file = event.target.files[0];
    const reader = new FileReader();
    const filename = event.target.files[0].name;
    this.form.xyi.xyi14 = filename;

    reader.onload = () => {
      this.form.Research = reader.result;
      console.log(reader.result);

      this.convertOtherstext = "Файл Загружен"
      this.classOthers = "download";
    };
    reader.readAsDataURL(file);
    }
  },
},
  // ниже заготовки под лоудер

  // simulateUpload(file) {
  //     this.isLoading = true;
  //     this.uploadProgress = 0;

  //     const updateProgress = () => {
  //       if (this.uploadProgress < 100) {
  //         this.uploadProgress += 10; // Увеличиваем прогресс на 10% каждую итерацию
  //         setTimeout(updateProgress, 200); // Обновляем каждые 200 мс
  //       } else {
  //         this.isLoading = false;
  //         console.log('Файл успешно загружен:', file.name);
  //       }
  //     };

  //   updateProgress();
  //   console.log(this.isLoading)
  //   },
  mounted() {
    this.Check();
  },
};
</script>

<template>
  <div class="big-container d-flex">
    <div class="input-group">
      <h1 class="head">Добавить в таблицу</h1>
      <form>
        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Код диагноза</label
          >
          <input
            type="text"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="1/2/3/4/5/6/7/8/9"
            v-model="form.Code"
          />
          <p></p>
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label">ФИО</label>
          <input
            type="text"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="ФИО"
            v-model="form.Fio"
          />
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label">Пол</label>
          <input
            type="text"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="М/Ж"
            v-model="form.Floor"
          />
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Возраст</label
          >
          <input
            type="text"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Возраст"
            v-model="form.Age"
          />
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Номер истории болезни</label
          >
          <input
            type="text"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Номер истории болезни"
            v-model="form.NumberHistory"
          />
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Дата госпитализации</label
          >
          <input
            type="date"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="name@example.com"
            v-model="form.Date1"
          />
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Дата выписки (смерти)</label
          >
          <input
            type="date"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Дата выписки (смерти)"
            v-model="form.Date2"
          />
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Исход (1 - выписан / 0 - умер)</label
          >
          <input
            type="text"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Исход"
            v-model="form.Result"
          />
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Диагноз окончательный</label
          >
          <input
            type="text"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Диагноз"
            v-model="form.Diagnosis"
          />
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label">ФГДС</label>
          <input
            type="file"
            class="form-control"
            placeholder="ФГДС"
            @change="convertFileFGDS"
          />
          <div>
            <p :class="this.classFileFGDS">{{ this.convertFileFGDStext }}</p>
          </div>
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label">ФКС</label>
          <input
            type="file"
            class="form-control"
            placeholder="ФКС"
            @change="convertFileFKS"
          />
          <div>
            <p :class="this.classFileFKS">{{ this.convertFileFKStext }}</p>
          </div>
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Протокол СКТ</label
          >
          <input
            type="file"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Протокол"
            @change="convertFileCKT"
          />
          <div>
            <p :class="this.classFileCKT">{{ this.convertFileCKTtext }}</p>
          </div>
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Протокол МРТ</label
          >
          <input
            type="file"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Протокол"
            @change="convertFileMRT"
          />
          <div>
            <p :class="this.classFileMRT">{{ this.convertFileMRTtext }}</p>
          </div>
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Прочие исследования</label
          >
          <input
            type="file"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Исследования"
            @change="convertFileResearch"
          />
          <div>
            <p :class="this.classOthers">{{ this.convertOtherstext }}</p>
          </div>
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Дата операции</label
          >
          <input
            type="date"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Дата операции"
            v-model="form.Date3"
          />
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Название операции</label
          >
          <input
            type="text"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Название"
            v-model="form.NameOperation"
          />
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Протокол операции</label
          >
          <input
            type="file"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Протокол"
            @change="convertFileProtocol"
          />
          <div>
            <p :class="this.classProtokolOperation">{{ this.convertProtokolOperationtext }}</p>
          </div>
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Фото (видео) препарата</label
          >
          <input
            type="file"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Фото, видео"
            @change="convertFileDrugVideo"
          />
          <div>
            <p :class="this.classPhotoVideo">{{ this.convertPhotoVideotext }}</p>
          </div>
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Гистологическое заключение</label
          >
          <input
            type="file"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Заключение"
            @change="convertFileGistolConclusion"
          />
          <div>
            <p :class="this.classGostol">{{ this.convertGostoltext }}</p>
          </div>
        </div>

        <h4 class="mt-5 mb-3">Ссылки</h4>
        <div class="mb-3 mt-4">
          <label for="exampleFormControlInput1" class="form-label"
            >Диск СКТ</label
          > 
          <input
            type="file"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Ссылка"
            @change="convertFileCktDisk"
          />
          <div>
            <p :class="this.classDiskCKT">{{ this.convertDiskCKTtext }}</p>
          </div>
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Диск МРТ</label
          >
          <input
            type="file"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Ссылка"
            @change="convertFileMrtDisk"
          />
          <div>
            <p :class="this.classDiskMRT">{{ this.convertDiskMRTtext }}</p>
          </div>
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Построенная модель СТК</label
          >
          <input
            type="file"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Ссылка"
            @change="convertFileCktModel"
          />
          <div>
            <p :class="this.classModelCKT">{{ this.convertModelCKTtext }}</p>
          </div>
        </div>

        <div class="mb-3">
          <label for="eleFormControlInput1" class="form-label"
            >Построенная модель МРТ</label
          >
          <input
            type="file"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Ссылка"
            @change="convertFileMrtModel"
          />
          <div>
            <p :class="this.classModelMRT">{{ this.convertModelMRTtext }}</p>
          </div>
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Видео(фото) операции с ДР</label
          >
          <input
            type="file"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="Ссылка"
            @change="convertFileOperationVideo"
          />
          <div>
            <p :class="this.classOperationVideo">{{ this.convertOperationVideotext }}</p>
          </div>
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label"
            >Эффект предоперационного применения ДР(0/1)</label
          >
          <input
            type="text"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder="0/1"
            v-model="form.EffectOfUse1"
          />
        </div>

        <div class="mb-3">
          <label for="exampleFormControlTextarea1" class="form-label"
            >Примечания.</label
          >
          <textarea
            class="form-control"
            id="exampleFormControlTextarea1"
            rows="3"
            v-model="form.Notes"
          ></textarea>
        </div>
      </form>
      <p class="p">{{ status }}</p>
    </div>
  </div>
  <div class="btn">
    <!-- <a href="/Table"> -->
      <div class="mb-3" v-if="isLoading">
              <label for="exampleFormControlInput1" class="form-label mt-3"
                ><h5>Загрузка данных на сервер...</h5></label
              >
              <br>
              <progress
                max="100"
                :value="this.percentCompleted"
                v-if="this.isUploading"
              ></progress>
              <p>{{ this.percentCompleted }} %</p>
      </div>
      <button class="btn-reg btn" @click="check">Добавить</button>
    <!-- </a> -->
  </div>
</template>

<style scoped>
.load {
  color: orange;
  margin-top: 10px;
}
.notdownload {
  color: red;
  margin-top: 10px;
}
.download {
  color: green;
  margin-top: 10px;
}
.p {
  color: red;
}
.big-container {
  display: flex;
  margin-left: 40;
  margin-right: auto;
  margin-top: 20px;
  justify-content: center;
}
.container {
  background-color: black;
  width: 1000px;
  height: 700px;
}
.head {
  font-size: 50px;
}
.input-group {
  flex-direction: column;
  width: 900px;
  display: flex;
  gap: 20px;
  margin-top: 33px;
}
label {
  font-size: 18px;
}
.btn-reg {
  margin-top: 10px;
  width: 250px;
  height: 50px;
  border-radius: 12px;
  border: none;
  background-color: #4200ff;
  color: #fff;
  cursor: pointer;
  font-weight: 600;
  font-size: 20px;
  margin-left: 100px;
  justify-content: center;
}
.btn {
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
