const DBconecion = require("../service/conection.js");

let users=[]
async function getUSer(req, res) {
    return new Promise((resolve, reject) => {
      const query =      
      'SELECT name FROM usuarios ';
   ;    
      // Usar la función pool.query en lugar de connection.query
      DBconecion.pool.query(query, (err, results) => {
        if (err) {
          console.error('Error fetching data: ', err);
          reject(err);
          return;
        }
        if (results.length === 0) resolve("nada que mostrar");
        else {
          const resultados = results;
          console.log(resultados)
          resultados.forEach(objeto => {
            users.push(objeto.name);
          });
          
        }
      });
    });
  }


  function AddUser(id) {
    if( users.includes(id.toString() )){
        console.log("ya existe en bd")
        return
    }
    else{

    }
    const updateData = {
        name: id, // Asumo que id contiene el valor que deseas insertar en la columna "name"
    };
    
    const query = 'INSERT INTO usuarios (name) VALUES (?)'; // Corregí la sintaxis SQL
    
    // Utiliza la función pool.query en lugar de connection.query
    DBconecion.pool.query(query, [updateData.name], (err, results) => {
        if (err) {
            console.error('Error inserting data: ', err);
            return;
        }
        console.log('Data inserted successfully:', results);
        users.push(id.toString())
    });
  }
  module.exports={
    getUSer,AddUser
    };