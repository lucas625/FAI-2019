const express = require('express');//importanto o express

const app = express();//cria seu app

app.get('/', function(req, res, next){
    return res.status(200).send('Hello!');
});

app.listen(3000, () => {
    console.log('servidor inicializado na porta 3000.');
});//inicia a aplicação