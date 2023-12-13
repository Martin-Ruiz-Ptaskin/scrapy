const express= require("express") //importo Express
const app = express() // Creo una instancia
const miFunciones = require("./controllers/stocksControler.js");
const cors = require('cors');

//const stockFunciones=require("./controllers/Stocks.js")


const corsOptions = {
  origin: 'http://localhost:4200',
  optionsSuccessStatus: 200, // Algunos navegadores (por ejemplo, Firefox) pueden requerir esto
};

// Habilitar CORS solo para las solicitudes desde http://localhost:4200
app.use(cors(corsOptions));
  
const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});//uso el puerto 3000


app.get('/', function (req, res,bot) { // creo el servicio y mapeo la peticion /
    console.log("llega")
  res.write("llega")
  res.end()})

 

app.get('/alive', function (req, res,bot) { // creo el servicio y mapeo la peticion /
miFunciones.alive()
  res.write("Bien")
  res.end()


})
app.get('/Stocks', function (req, res,bot) { // creo el servicio y mapeo la peticion /
  let response=miFunciones.Getstock().then(resultadoConsulta => {
    //console.log(resultadoConsulta);

    //JSON.stringify(resultadoConsulta, null, 2); // El tercer parámetro (2) es para indentación
    res.write(resultadoConsulta)
    res.end()
    // Ahora puedes trabajar con los datos resueltos
  }).catch(error => {
    console.error('Error:', error);
  });
    
  
  
  })