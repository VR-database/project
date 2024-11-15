<script>
//   "/update-string"
// let response = await axios.get(`/show-one?id=${this.id}`, {
//    routGet(){
// this.id = this.$route.query.id
// console.log(this.id)
//},
import axios from "axios";
axios.defaults.baseURL = "https://api.ar-vmgh.ru/";

// иди нах с точками и запятимыи так это не импорт

export default {
  data() {
    return {
      formdata: new FormData(),
      form: {
        // текстовые input

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
        EffectOfUse1: "",
        Notes: "",

        // файловые input

        CktDisk: "",
        MrtDisk: "",
        CktModel: "", //
        MrtModel: "", //
        OperationVideo: "", //
        Fgds: "", //
        Fks: "", //
        Ckt: "", //
        Mrt: "", //
        Research: "", //
        Protocol: "", //
        DrugVideo: "", //
        GistolConclusion: "", //
      },

      file: "",
      status: "",

      // isLoading: false,
      // uploadProgress: 0,
      isUploading: true,
      percentCompleted: 0,
      isLoading: false,

      load: {
        Fgds: {
          status: "Файл незагружен.",
          class: "notdownloadFgds",
          classRedownload: "redownloadFgds",
          classDownload: "downloadFgds",
          classNotdownload: "notdownloadFgds",
          p: "Файл незагружен.",
          pp: "Файл загружен",
          Fgds: "Fgds",
          isLoaded: false,
        },
        Fks: {
          status: "Файл незагружен.",
          class: "notdownloadFks",
          classRedownload: "redownloadFks",
          classDownload: "downloadFks",
          classNotdownload: "notdownloadFks",
          Fks: "Fks",
          p: "Файл незагружен.",
          pp: "Файл загружен",
          isLoaded: false,
        },
        Ckt: {
          status: "Файл незагружен.",
          class: "notdownloadCkt",
          classRedownload: "redownloadCkt",
          classDownload: "downloadCkt",
          classNotdownload: "notdownloadCkt",
          Ckt: "Ckt",
          p: "Файл незагружен.",
          pp: "Файл загружен",

          isLoaded: false,
        },
        Mrt: {
          status: "Файл незагружен.",
          class: "notdownloadMrt",
          classRedownload: "redownloadMrt",
          classDownload: "downloadMrt",
          classNotdownload: "notdownloadMrt",
          Mrt: "Mrt",
          p: "Файл незагружен.",
          pp: "Файл загружен",

          isLoaded: false,
        },
        Research: {
          status: "Файл незагружен.",
          class: "notdownloadResearch",
          classRedownload: "redownloadResearch",
          classDownload: "downloadResearch",
          classNotdownload: "notdownloadResearch",
          Research: "Research",
          p: "Файл незагружен.",
          pp: "Файл загружен",

          isLoaded: false,
        },
        Protocol: {
          status: "Файл незагружен.",
          class: "notdownloadProtocol",
          classRedownload: "redownloadProtocol",
          classDownload: "downloadProtocol",
          classNotdownload: "notdownloadProtocol",
          p: "Файл незагружен.",
          pp: "Файл загружен",

          Protocol: "Protocol",
          isLoaded: false,
        },
        DrugVideo: {
          status: "Файл незагружен.",
          class: "notdownloadDrugVideo",
          classRedownload: "redownloadDrugVideo",
          classDownload: "downloadDrugVideo",
          classNotdownload: "notdownloadDrugVideo",
          DrugVideo: "DrugVideo",
          isLoaded: false,
          pp: "Файл загружен",

          p: "Файл незагружен.",
        },
        GistolConclusion: {
          status: "Файл незагружен.",
          class: "notdownloadGistolConclusion",
          classRedownload: "redownloadGistolConclusion",
          classDownload: "downloadGistolConclusion",
          classNotdownload: "notdownloadGistolConclusion",
          GistolConclusion: "GistolConclusion",
          isLoaded: false,
          pp: "Файл загружен",

          p: "Файл незагружен.",
        },
        CktDisk: {
          status: "Файл незагружен.",
          class: "notdownloadCktDisk",
          classRedownload: "redownloadCktDisk",
          classDownload: "downloadCktDisk",
          classNotdownload: "notdownloadCktDisk",
          CktDisk: "CktDisk",
          p: "Файл незагружен.",
          isLoaded: false,
          pp: "Файл загружен",

        },
        MrtDisk: {
          status: "Файл незагружен.",
          class: "notdownloadMrtDisk",
          classRedownload: "redownloadMrtDisk",
          classDownload: "downloadMrtDisk",
          classNotdownload: "notdownloadMrtDisk",
          MrtDisk: "MrtDisk",
          p: "Файл незагружен.",
          pp: "Файл загружен",

          isLoaded: false,
        },
        CktModel: {
          status: "Файл незагружен.",
          class: "notdownloadCktModel",
          classRedownload: "redownloadCktModel",
          classDownload: "downloadCktModel",
          classNotdownload: "notdownloadCktModel",
          CktModel: "CktModel",
          p: "Файл незагружен.",
          pp: "Файл загружен",

          isLoaded: false,
        },
        MrtModel: {
          status: "Файл незагружен.",
          class: "notdownloadMrtModel",
          classRedownload: "redownloadMrtModel",
          classDownload: "downloadMrtModel",
          classNotdownload: "notdownloadMrtModel",
          p: "Файл незагружен.",
          MrtModel: "MrtModel",
          pp: "Файл загружен",

          isLoaded: false,
        },
        OperationVideo: {
          status: "Файл незагружен.",
          class: "notdownloadOperationVideo",
          classRedownload: "redownloadOperationVideo",
          classDownload: "downloadOperationVideo",
          classNotdownload: "notdownloadOperationVideo",
          p: "Файл незагружен.",
          OperationVideo: "OperationVideo",
          isLoaded: false,
          pp: "Файл загружен",

        },

        // Fgds: "Fgds",
        // Fks: "Fks",
        // Ckt: "Ckt",
        // Mrt: "Mrt",
        // Research: "Research",
        // Protocol: "Protocol",
        // DrugVideo: "DrugVideo",
        // GistolConclusion: "GistolConclusion",
        // CktDisk: "CktDisk",
        // MrtDisk: "MrtDisk",
        // CktModel: "CktModel",
        // MrtModel: "MrtModel",
        // OperationVideo: "OperationVideo",
      },
    };
  },
  methods: {
    async Check() {
      let response = await axios.get(`/check`);
      this.isAdmin = response.data.isAdmin;
      if (this.isAdmin == "True") {
        this.getInfo();
        this.routGet();
      } else if (this.isAdmin == "False") {
        this.getInfo();
        this.routGet();
      } else {
        this.$router.push("/login");
      }
    },
    routGet() {
      this.id = this.$route.query.id;
      console.log(this.id);
    },
    check() {
      if (false) {
        this.status = "Заполните все поля!";
      } else {
        this.putInfo();
        console.log(this.form);
      }
    },
    async putInfo() {
      this.isLoading = true;
      this.isUploading = true;

      try {
        await axios.put("/update-string/text", {
          form: this.form,
          id: this.id,
        });
      } catch (error) {
        this.status = "Ошибка отправки.";
        this.isLoading = false;
      }

      try {
        await axios.put("/update-string/file ", this.formdata, {
          headers: {
            "Content-Type": "enctype=multipart/form-data",
          },
          onUploadProgress: (progressEvent) => {
            const percentCompleted = Math.round(
              (progressEvent.loaded * 100) / progressEvent.total
            );
            this.percentCompleted = percentCompleted;
          },
        });
      } catch (error) {
        console.error("Ошибка при отправке данных:", error);
        this.isUploading = false;
        this.isLoading = false;
        this.status = "Ошибка отправки.";
        return;
      }

      this.isUploading = false;
      this.isLoading = false;
      this.status = "Данные занесены в таблицу.";
      this.$router.push("/Table");
    },
    async getInfo() {
      let response = await axios.get(`/show-one?id=${this.id}`);
      this.form = response.data.all[0];
    },
    async convertFile(event, name) {
      console.log(this.load);
      if (event && name) {
        this.load[name].class = this.load[name].classRedownload;
        this.load[name].p = "Файл загружается...";
        const file = event.target.files[0];
        // this.form.avatar = file;
        this.formdata.append(name, file);
        const reader = new FileReader();
        reader.onload = (e) => {
          if (reader.result) {
            this.load[name].class = this.load[name].classDownload;
            this.load[name].p = "Файл загружен.";
          }
        };
        reader.readAsDataURL(file);
      }
    },
  },
  mounted() {
    this.id = this.$route.query.id;
    this.Check();
    
  },
};
</script>

<template>
  <div class="big-container d-flex">
    <div class="input-group">
      <h1 class="head">Внести изменения.</h1>
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
            @change="convertFile($event, 'Fgds')"
          />
          <div>
            <p :class="this.load[`Fgds`].classDownload" v-if="this.form.Fgds">{{ this.load["Fgds"].pp }}</p>
            <p :class="this.load[`Fgds`].class" v-else>{{ this.load["Fgds"].p }}</p>
            <a
              :href="this.form.Fgds"
              class="download-link"
              v-if="this.form.Fgds"
              >Скачать</a
            >
          </div>
        </div>

        <div class="mb-3">
          <label for="exampleFormControlInput1" class="form-label">ФКС</label>
          <input
            type="file"
            class="form-control"
            placeholder="ФКС"
            @change="convertFile($event, 'Fks')"
          />
          <div>
            <p :class="this.load[`Fks`].classDownload" v-if="this.form.Fks">{{ this.load["Fks"].pp }}</p>
            <p :class="this.load[`Fks`].class" v-else>{{ this.load["Fks"].p }}</p>
            <a :href="this.form.Fks" class="download-link" v-if="this.form.Fks"
              >Скачать</a
            >
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
            @change="convertFile($event, 'Ckt')"
          />
          <div>
            <p :class="this.load[`Ckt`].classDownload" v-if="this.form.Ckt">{{ this.load["Ckt"].pp }}</p>
            <p :class="this.load[`Ckt`].class" v-else>{{ this.load["Ckt"].p }}</p>
            <a :href="this.form.Ckt" class="download-link" v-if="this.form.Ckt"
              >Скачать</a
            >
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
            @change="convertFile($event, 'Mrt')"
          />
          <div>
            <p :class="this.load[`Mrt`].classDownload" v-if="this.form.Mrt">{{ this.load["Mrt"].pp }}</p>
            <p :class="this.load[`Mrt`].class" v-else>{{ this.load["Mrt"].p }}</p>
            <a :href="this.form.Mrt" class="download-link" v-if="this.form.Mrt"
              >Скачать</a
            >
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
            @change="convertFile($event, 'Research')"
          />
          <div>
            <p :class="this.load[`Research`].classDownload" v-if="this.form.Research">
              {{ this.load["Research"].pp }}
            </p>
            <p :class="this.load[`Research`].class" v-else>
              {{ this.load["Research"].p }}
            </p>
            <a
              :href="this.form.Research"
              class="download-link"
              v-if="this.form.Research"
              >Скачать</a
            >
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
            @change="convertFile($event, 'Protocol')"
          />
          <div>
            <p :class="this.load[`Protocol`].classDownload" v-if="this.form.Protocol">
              {{ this.load["Protocol"].pp }}
            </p>
            <p :class="this.load[`Protocol`].class">
              {{ this.load["Protocol"].p }}
            </p>
            <a
                :href="this.form.Protocol"
                class="download-link"
                v-if="this.form.Protocol"
                >Скачать</a
              >
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
            @change="convertFile($event, 'DrugVideo')"
          />
          <div>
            <p :class="this.load[`DrugVideo`].classDownload" v-if="this.form.DrugVideo">
              {{ this.load["DrugVideo"].pp }}
            </p>
            <p :class="this.load[`DrugVideo`].class" v-else>
              {{ this.load["DrugVideo"].p }}
            </p>
            <a
              :href="this.form.DrugVideo"
              class="download-link"
              v-if="this.form.DrugVideo"
              >Скачать</a
            >
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
            @change="convertFile($event, 'GistolConclusion')"
          />
          <div>
            <p :class="this.load[`GistolConclusion`].classDownload" v-if="this.form.GistolConclusion">
              {{ this.load["GistolConclusion"].pp }}
            </p>
            <p :class="this.load[`GistolConclusion`].class" v-else>
              {{ this.load["GistolConclusion"].p }}
            </p>
            <a
              :href="this.form.GistolConclusion"
              class="download-link"
              v-if="this.form.GistolConclusion"
              >Скачать</a
            >
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
            @change="convertFile($event, 'CktDisk')"
          />
          <div>
            <p :class="this.load[`CktDisk`].classDownload" v-if="this.form.CktDisk">
              {{ this.load["CktDisk"].pp }}
            </p>
            <p :class="this.load[`CktDisk`].class" v-else>
              {{ this.load["CktDisk"].p }}
            </p>
          </div>
          <a
              :href="this.form.CktDisk"
              class="download-link"
              v-if="this.form.CktDisk"
              >Скачать</a
            >
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
            @change="convertFile($event, 'MrtDisk')"
          />
          <div>
            <p :class="this.load[`MrtDisk`].classDownload" v-if="this.form.MrtDisk">
              {{ this.load["MrtDisk"].pp }}
            </p>
            <p :class="this.load[`MrtDisk`].class" v-else>
              {{ this.load["MrtDisk"].p }}
            </p>
            <a
              :href="this.form.MrtDisk"
              class="download-link"
              v-if="this.form.MrtDisk"
              >Скачать</a
            >
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
            @change="convertFile($event, 'CktModel')"
          />
          <div>
            <p :class="this.load[`CktModel`].classDownload" v-if="this.form.CktModel">
              {{ this.load["CktModel"].pp }}
            </p>
            <p :class="this.load[`CktModel`].class" v-else>
              {{ this.load["CktModel"].p }}
            </p>
            <a
              :href="this.form.CktModel"
              class="download-link"
              v-if="this.form.CktModel"
              >Скачать</a
            >
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
            @change="convertFile($event, 'MrtModel')"
          />
          <div>
            <p :class="this.load[`MrtModel`].classDownload" v-if="this.form.MrtModel">
              {{ this.load["MrtModel"].pp }}
            </p>
            <p :class="this.load[`MrtModel`].class" v-else>
              {{ this.load["MrtModel"].p }}
            </p>
            <a
              :href="this.form.MrtModel"
              class="download-link"
              v-if="this.form.MrtModel"
              >Скачать</a
            >
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
            @change="convertFile($event, 'OperationVideo')"
          />
          <div>
            <p :class="this.load[`OperationVideo`].classDownload" v-if="this.form.OperationVideo">
              {{ this.load["OperationVideo"].pp }}
            </p>
            <p :class="this.load[`OperationVideo`].class" v-else>
              {{ this.load["OperationVideo"].p }}
            </p>
            <a
              :href="this.form.OperationVideo"
              class="download-link"
              v-if="this.form.OperationVideo"
              >Скачать</a
            >
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
      <br />
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
.redownload {
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

.notdownloadFgds {
  color: red;
  margin-top: 10px;
}
.notdownloadFks {
  color: red;
  margin-top: 10px;
}
.notdownloadCkt {
  color: red;
  margin-top: 10px;
}
.notdownloadMrt {
  color: red;
  margin-top: 10px;
}
.notdownloadResearch {
  color: red;
  margin-top: 10px;
}
.notdownloadProtocol {
  color: red;
  margin-top: 10px;
}
.notdownloadDrugVideo {
  color: red;
  margin-top: 10px;
}
.notdownloadGistolConclusion {
  color: red;
  margin-top: 10px;
}
.notdownloadCktDisk {
  color: red;
  margin-top: 10px;
}
.notdownloadMrtDisk {
  color: red;
  margin-top: 10px;
}
.notdownloadCktModel {
  color: red;
  margin-top: 10px;
}
.notdownloadMrtModel {
  color: red;
  margin-top: 10px;
}
.notdownloadOperationVideo {
  color: red;
  margin-top: 10px;
}

.downloadFgds {
  color: green;
  margin-top: 10px;
}
.downloadFks {
  color: green;
  margin-top: 10px;
}
.downloadCkt {
  color: green;
  margin-top: 10px;
}
.downloadMrt {
  color: green;
  margin-top: 10px;
}
.downloadResearch {
  color: green;
  margin-top: 10px;
}
.downloadProtocol {
  color: green;
  margin-top: 10px;
}
.downloadDrugVideo {
  color: green;
  margin-top: 10px;
}
.downloadGistolConclusion {
  color: green;
  margin-top: 10px;
}
.downloadCktDisk {
  color: green;
  margin-top: 10px;
}
.downloadMrtDisk {
  color: green;
  margin-top: 10px;
}
.downloadCktModel {
  color: green;
  margin-top: 10px;
}
.downloadMrtModel {
  color: green;
  margin-top: 10px;
}
.downloadOperationVideo {
  color: green;
  margin-top: 10px;
}

.redownloadFgds {
  color: orange;
  margin-top: 10px;
}
.redownloadFks {
  color: orange;
  margin-top: 10px;
}
.redownloadCkt {
  color: orange;
  margin-top: 10px;
}
.redownloadMrt {
  color: orange;
  margin-top: 10px;
}
.redownloadResearch {
  color: orange;
  margin-top: 10px;
}
.redownloadProtoorange {
  color: orange;
  margin-top: 10px;
}
.redownloadDrugVideo {
  color: orange;
  margin-top: 10px;
}
.redownloadGistolConclusion {
  color: orange;
  margin-top: 10px;
}
.redownloadCktDisk {
  color: orange;
  margin-top: 10px;
}
.renotdownloadMrtDisk {
  color: orange;
  margin-top: 10px;
}
.redownloadCktModel {
  color: orange;
  margin-top: 10px;
}
.redownloadMrtModel {
  color: orange;
  margin-top: 10px;
}
.redownloadOperationVideo {
  color: orange;
  margin-top: 10px;
}
</style>
