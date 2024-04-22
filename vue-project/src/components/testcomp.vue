<template>
    <input type="file" @change="convertFile">
    {{ b64 }}
  </template>
  
  <script>
export default {
    data() {
        return {
            b64: '',
        }
    },
    methods: {
      convertFile(event) {
        const file = event.target.files[0];
        const reader = new FileReader();
  
        reader.onload = () => {
            this.b64 = reader.result;
            console.log(reader.result);
          // Выполните что-нибудь с закодированной строкой Base64
        };
  
            reader.readAsDataURL(file);
        
      }
    }
  };
  </script>