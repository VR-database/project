<script>
import ErrorComp from './ErrorComp.vue';

export default {
    data() {
        return {
            none: false,
        }
    },

    methods: {
        Show() {
            this.none = !this.none;
        }
    },
    components:{
            ErrorComp
                }
}
</script>

<template>

    <error-comp v-if="false" />
    <div class="container" v-if="true">
    <h1 class="head">DataBase</h1>
    <div class="buttons mb-5">
        <a class="button1" href="#/Add"><img src="../assets/image.png" alt=""></a>
        <a class="button1" @click="Show"><img src="../assets/delete.png" alt=""></a>
    </div>
    </div>
    <div class="Container Flipped" v-if="true">
     <div class="Content ">   
        <table>
		<thead>
			<tr>
                <th v-if="none"><button class="none-btn"><img src="../assets/delete.png" alt="" class="none-img"></button></th>
				<th>ПП</th>
				<th>ФИО</th>
				<th>Пол</th>
				<th>Возраст</th>
				<th>№ истории болезни</th>
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
                <th>Фото (видео) препарата</th>
                <th>Гистологическое заключение</th>
                <th>Диск СКТ</th>
                <th>Диск МРТ</th>
                <th>Построенная модель СТК</th>
                <th>Построенная модель МРТ</th>
                <th>Видео(фото) операции с ДР</th>
                <th>Эффект предоперационного применения ДР(0/1)</th>
                <th>Примечания.</th>
			</tr>
		</thead>
		<tbody>
			<tr>
                <td v-if="none"><input type="checkbox"></td>
				<td>1</td>
				<td>Сергей Константинович Пончикewrwerwerwerwerwerw</td>
				<td>М</td>
				<td>30</td>
				<td>327983</td>
				<td>17.01.24</td>
				<td>-</td>
				<td>1</td>
				<td>-</td>
				<td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
				<td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
				<td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td>17.01.24</td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td>Ппшпащащгпашгвашгвашшгвагшваппв</td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td>-</td>

			</tr>
			<tr>
                <td v-if="none"><input type="checkbox"></td>
				<td>2</td>
				<td>Сергей Константинович Пончик</td>
				<td>М</td>
				<td>30</td>
				<td>327983</td>
				<td>17.01.24</td>
				<td>-</td>
				<td>1</td>
				<td>-</td>
				<td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
				<td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
				<td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td>17.01.24</td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td>Ппшпащащгпашгвашгвашшгвагшваппв</td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td>-</td>

			</tr>
			<tr>
                <td v-if="none"><input type="checkbox"></td>
				<td>3</td>
				<td>Сергей Константинович Пончик</td>
				<td>М</td>
				<td>30</td>
				<td>327983</td>
				<td>17.01.24</td>
				<td>-</td>
				<td>1</td>
				<td>-</td>
				<td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
				<td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
				<td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td>17.01.24</td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td>Ппшпащащгпашгвашгвашшгвагшваппв</td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td><a href=""><img src="../assets/folder.png" alt="" class="folder"></a></td>
                <td>-</td>

			</tr>
			
		</tbody>
	</table>
</div>
</div>
</template>

<style scoped>
.folder{
    width: 30px;
    height: 30px;
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

.button1 img:hover{
    width: 55px;
    height: 50px;
    transition: all 0.4s;
}
table th {
	border: 1px solid #ff0090;
	padding: 15px 20px;
	text-align: center;
    
}
table td {
	border: 1px solid #fe00bf;
	padding: 15px 15px;
	text-align: center;
    max-width: 600px;  /* Максимальная ширина ячейки */
    overflow: hidden;
    text-overflow: ellipsis;
}

.Container {
    overflow-y: auto;
}
.Content
{
    width: auto;
}
.Flipped, .Flipped .Content{
    
    transform:rotateX(360deg);
    -ms-transform:rotateX(360deg);
    -webkit-transform:rotateX(180deg); /* Safari and Chrome */

}
.Container table {
	display: inline-block;
	vertical-align: top;
	max-width: 100%;
	overflow-x: auto;
	white-space: nowrap;
	-webkit-overflow-scrolling: touch;
    table-layout: fixed;
}
.none-btn{
    border: none;
    background: none;
}
.none-img{
    width: 20px;
    height: 20px;
    cursor: pointer;
}
</style>
