const express= require("express") //importo Express
const app = express() // Creo una instancia
const miFunciones = require("./controllers/notificationControler.js");



app.listen(3000)//uso el puerto 3000



app.get('/', function (req, res,bot) { // creo el servicio y mapeo la peticion /
    console.log("llega")
 miFunciones.sendNotificaciones(req,res).then((result) => {
  console.log(result)
  res.write(JSON.stringify( result))
  res.end()})
.catch((error) => {
  res.write('Error:');
  res.end()
});
 
})
