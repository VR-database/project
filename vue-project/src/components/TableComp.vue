<script>
export default {
    data() {
        return {
            Dnone: true,
        }
    },
    methods: {
        Show() {
            this.Dnone = !this.Dnone
        }
    }
}
</script>

<template>
    <div class="container">
    <h1 class="head">DataBase</h1>
    <div class="buttons mb-5">
        <a class="button1" href="#/Add"><img src="../assets/image.png" alt=""></a>
        <a class="button1" @click="Show"><img src="../assets/delete.png" alt=""></a>
    </div>
    </div>
    <div class="big-table">
    <table>
        <tbody>
            <thead>
                <th v-if="Dnone">/</th>
                <th>ПП</th>
                <th>Код диагноза</th>
                <th>ФИО</th>
                <th>Пол</th>
                <th>Возраст</th>
                <th>Номер истории болезни</th>
                <th>Дата госпитализации</th>
                <th>Дата выписки (смерти)</th>
                <th>Исход</th>
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
                <th>Фото\видео препарата</th>
                <th>Гистологическое заключение</th>
                <th>Диск СКТ</th>
                <th>Диск МРТ</th>
                <th>Построенная модель СТК</th>
                <th>Построенная модель МРТ</th>
                <th>Фото\видео операции с ДР</th>
                <th>Эффект предоперационного применения ДР(0/1)</th>
                <th>Примечания.</th>


            </thead>
            <!-- ппц полный -->
            <tr>
                <td v-if="Dnone"></td>
                <td>1</td>
                <td>1</td>
                <td>Семен Олегович Дегенерат</td>
                <td>freferf</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1ккеewffewfrewreferfwerfwersifwiurwepi77766777776urypoiytporyporetpowiytpoeportywepitwepriterwtwef</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>1</td>
            </tr>
        </tbody>
    </table>
</div>
</template>

<style scoped>


table {
    border-collapse: collapse;
    border: 1px solid grey;
    border-radius: 5px;
    
}
th {
    border: 1px solid grey;
    padding: 10px;
    width: 30px;
    width: 50px;
}

td {
    border: 1px solid grey;
    padding: 10px;
    overflow: hidden;
    text-overflow: ellipsis;
}
.head{
    font-size: 60px;
    margin-top: 30px;
    
}
.buttons{
    margin-top: 30px;
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.button1 img{
    width: 50px;
    height: 47px;
    cursor: pointer;
}
.button2{
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
.big-table {
	overflow: auto;
	position: relative;
}
.big-table table {
	display: inline-block;
	vertical-align: top;
	max-width: 100%;
	overflow-x: auto;
	white-space: nowrap;
	-webkit-overflow-scrolling: touch;
}
.button1 img:hover{
    width: 55px;
    height: 50px;
    transition: all 0.4s;
}
</style>
