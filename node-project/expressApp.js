const express= require("express") //importo Express
const app = express() // Creo una instancia
const miFunciones = require("./controllers/notificationControler.js");
//const stockFunciones=require("./controllers/Stocks.js")



app.listen(3000)//uso el puerto 3000
app.use(express.json());



app.get('/', function (req, res,bot) { // creo el servicio y mapeo la peticion /
    console.log("llega")
 miFunciones.sendNotificaciones(req,res).then((result) => {
  res.write(JSON.stringify( result))
  res.end()})
.catch((error) => {
  res.write('Error:');
  res.end()
});
 
})
app.get('/alive', function (req, res,bot) { // creo el servicio y mapeo la peticion /
miFunciones.alive()
  res.write("Bien")
  res.end()


})
app.post('/customNotification', function (req, res,bot) { // creo el servicio y mapeo la peticion /
  let body=(req.body)
  miFunciones.customNotification(body
    , res)
    res.write("Bien")
    res.end()
  
  
  })
