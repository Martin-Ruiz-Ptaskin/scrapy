const NotificacionesService= require("../service/notificacionesService.js")
//INICIO SQL
const mysql = require('mysql2');
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'scrapy'
});
async function Getstock() {
  return new Promise((resolve, reject) => {
    const query =
      'SELECT *FROM stockprice ;';
    
    connection.query(query, (err, results) => {
      if (err) {
        console.error('Error fetching data: ', err);
        reject(err); // Rechazamos la promesa en caso de error
        return;
      }
      if(results.length==0) resolve("nada que mostrar");
      else{
        const stocks = results;

        resolve(JSON.stringify(results));

        //resolve(JSON.stringify(results, null, 2));
      }
     
    });
  });
}

  // FIN UPDATE  NOTIFICACIONES
  module.exports = {
    Getstock
   
  };