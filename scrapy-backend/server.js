const port="3000";// puerto
const hostname="localhost"//nombre
const http =require('http')//modulo requerido
const moment=require('moment')


const server =http.createServer((req,res) =>{ //inicio el servidor
console.log("a request is made")


//el parámetro req representa una peticion http con info
switch(res.url){
    case "/saludame":
        res.write("hola")
    res.end()
    break
    case "/despedirme":
        res.write("chau")
        res.end()
        break
    default:
    res.write("que hacelga")
    res.end()
}





})
//para escuchar lo que le llega al server debo usar
   server.listen(port,hostname,()=>{ //escucho las peticiones al server
        console.log('listening on port  ${port}')
    })
