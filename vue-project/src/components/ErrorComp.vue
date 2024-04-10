<script>
    
</script>

<template>
    <div class="background">
        <h1>404</h1>
        <a href="#/Main"><button>На главную</button></a>
    </div>
</template>

<style scoped>
.background {
    width: 100%;
    height: 100vh;
     
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    gap: 30px;

    user-select: none;
}

h1 {
    font-size: 150px;
    font-weight: 500;
    color: #161616;
}

button {
    width: 190px;
    height: 50px;
    border-radius: 12px;
    border: none;
    background-color: #4200FF;
    color: #fff;
    cursor: pointer;

    font-weight: 600;
    font-size: 20px;

    transition: all 100ms;
}

button:hover {
    background-color: #2d00aa;
    border-radius: 25px 5px;
}

button:active {
    background-color: #240088;
}
</style>