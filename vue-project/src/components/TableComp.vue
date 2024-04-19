<script>
import ErrorComp from "./ErrorComp.vue";

export default {
  data() {
    return {
      none: false,
    };
  },

  methods: {
    Show() {
      this.none = !this.none;
      console.log(0);
    },
  },
  mounted() {},
  components: {
    ErrorComp,
  },
};
</script>

<template>
  <error-comp v-if="false" />
  <div class="container" v-if="true">
    <h1 class="head">DataBase</h1>
    <div class="buttons mb-5">
      <a class="button1" href="#/Add"
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
            <th>234123</th>
            <th>П3413ол</th>
            <th>14</th>
            <th>13424123</th>
            <th>14234</th>
            <th>142423</th>
            <th>14312412</th>
            <th>341</th>
            <th>.43324/.134124</th>
            <th>1234123</th>
            <th>134</th>
            <th>41313Т</th>
            <th>1234124</th>
            <th>124124123</th>
            <th>1234124</th>
            <th>14124124</th>
            <th>143124123</th>
            <th>1242412341</th>
            <th>Г124</th>
            <th>Д42124123</th>
            <th>Д42124123</th>
            <th>Пqertregtwegte</th>
            <th>Пqertregtwegte</th>
            <th>Виqqertregtwegte</th>
            <th>twret wteert нцн45г3</th>
            <th>wter.</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td v-if="none"><input type="checkbox" /></td>
            <td>1</td>
            <td>wertertwert</td>
            <td>ertwerМ</td>
            <td>rtwer</td>
            <td>327rtwertw983</td>
            <td>wtrwetwe</td>
            <td>-</td>
            <td>1</td>
            <td>-</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>17.01.24</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>Ппшпащащгпашгвашгвашшгвагшваппв</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>-</td>
          </tr>
          <tr>
            <td v-if="none"><input type="checkbox" /></td>
            <td>2</td>
            <td>terwertwe</td>
            <td>Мwtre</td>
            <td>3erwter0</td>
            <td>32twertwert7983</td>
            <td>1wertwert.01.24</td>
            <td>-</td>
            <td>1</td>
            <td>-</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>17.01.24</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>Ппшпащащгпашгвашгвашшгвагшваппв</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>-</td>
          </tr>
          <tr>
            <td v-if="none"><input type="checkbox" /></td>
            <td>3</td>
            <td>ere</td>
            <td>erewМ</td>
            <td>3retwret0</td>
            <td>327rtewter983</td>
            <td>17.wertwertwer.24</td>
            <td>-</td>
            <td>1</td>
            <td>-</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>17.01.24</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>Ппшпащащгпашгвашгвашшгвагшваппв</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>-</td>
          </tr>
          <tr>
            <td v-if="none"><input type="checkbox" /></td>
            <td>3</td>
            <td>ere</td>
            <td>erewМ</td>
            <td>3retwret0</td>
            <td>327rtewter983</td>
            <td>17.wertwertwer.24</td>
            <td>-</td>
            <td>1</td>
            <td>-</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>17.01.24</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>Ппшпащащгпашгвашгвашшгвагшваппв</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>-</td>
          </tr>
          <tr>
            <td v-if="none"><input type="checkbox" /></td>
            <td>3</td>
            <td>ere</td>
            <td>erewМ</td>
            <td>3retwret0</td>
            <td>327rtewter983</td>
            <td>17.wertwertwer.24</td>
            <td>-</td>
            <td>1</td>
            <td>-</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>17.01.24</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>Ппшпащащгпашгвашгвашшгвагшваппв</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>-</td>
          </tr>
          <tr>
            <td v-if="none"><input type="checkbox" /></td>
            <td>3</td>
            <td>ere</td>
            <td>erewМ</td>
            <td>3retwret0</td>
            <td>327rtewter983</td>
            <td>17.wertwertwer.24</td>
            <td>-</td>
            <td>1</td>
            <td>-</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>17.01.24</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>Ппшпащащгпашгвашгвашшгвагшваппв</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>-</td>
          </tr>
          <tr>
            <td v-if="none"><input type="checkbox" /></td>
            <td>3</td>
            <td>ere</td>
            <td>erewМ</td>
            <td>3retwret0</td>
            <td>327rtewter983</td>
            <td>17.wertwertwer.24</td>
            <td>-</td>
            <td>1</td>
            <td>-</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>17.01.24</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>Ппшпащащгпашгвашгвашшгвагшваппв</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>-</td>
          </tr>
          <tr>
            <td v-if="none"><input type="checkbox" /></td>
            <td>3</td>
            <td>ere</td>
            <td>erewМ</td>
            <td>3retwret0</td>
            <td>327rtewter983</td>
            <td>17.wertwertwer.24</td>
            <td>-</td>
            <td>1</td>
            <td>-</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>17.01.24</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>Ппшпащащгпашгвашгвашшгвагшваппв</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>-</td>
          </tr>
          <tr>
            <td v-if="none"><input type="checkbox" /></td>
            <td>3</td>
            <td>ere</td>
            <td>erewМ</td>
            <td>3retwret0</td>
            <td>327rtewter983</td>
            <td>17.wertwertwer.24</td>
            <td>-</td>
            <td>1</td>
            <td>-</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>17.01.24</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>Ппшпащащгпашгвашгвашшгвагшваппв</td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>
              <a href=""
                ><img src="../assets/folder.png" alt="" class="folder"
              /></a>
            </td>
            <td>-</td>
          </tr>
          
        </tbody>
      </table>
    </div>
  </div>
</template>
<style scoped>
table thead {
  position: sticky;
  top: 100;
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
table thead {

    background: #f2f2f2;
    position: sticky;
    top: 0;
    z-index: 1000;
    /* Add some space between the header and the main content */
    margin-top: 0px;
  
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
