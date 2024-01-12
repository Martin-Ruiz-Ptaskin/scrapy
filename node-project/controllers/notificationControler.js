const { text } = require("express");
const NotificacionesService= require("../service/notificacionesService.js")
//INICIO SQL
const mysql = require('mysql2');
let msjColector=[]
let notificaciones

//Telegram Bot
const TelegramBot = require('node-telegram-bot-api');


// replace the value below with the Telegram token you receive from @BotFather
const token = '6374242902:AAGIWd6vkwID8LOmTEy5Y9Q6cDzOjIuBRUo';

// Create a bot that uses 'polling' to fetch new updates
const bot = new TelegramBot(token, {polling: true});

//  FIN TELEGRAM BOT

//FIN  SQL

// Matches "/echo [whatever]"
bot.onText(/\/echo (.+)/, (msg, match) => {
  
  const chatId = msg.chat.id;

  const resp = match[1]; // the captured "whatever"

  bot.sendMessage(chatId, resp);
});

// Listen for any kind of message. There are different kinds of
// messages.
bot.on('message', (msg) => {
  const chatId = msg.chat.id;
  //console.log(msg)

  console.log(msg.text)
  url="https://econoba.martinruizptaskin.com.ar?key="+chatId
  textoAenviar="Configura los activos sobre los que recibiras notificaciones " +url
  console.log(chatId)
  //msjColector.push( {id:chatId, texto:msg.text})
  //console.log(msjColector.filter(msj=> msj.id ==chatId ))
  switch(msg.text){
    case "/activos":
      bot.sendMessage(chatId, textoAenviar);
      break
    default:
      bot.sendMessage(chatId, "envia /activos para comenzar a editar tus notificaciones");


  }
  

  // send a message to the chat acknowledging receipt of their message
  
});
/*const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'scrapy'
});
*/
const connection = mysql.createConnection({
  host:"50.87.144.185",
  user:"datodtal_scrapy",
  password:"%V]B]Rvvl}uo",
  database:"datodtal_scrapy"
});

connection.connect((err) => {
    if (err) {
      console.error('Error connecting to the database: ', err);
      return;
    }
    console.log('Connected to the MySQL server.');
  });

  async function sendNotificaciones(req, res) {
    return new Promise((resolve, reject) => {
      const query =
        'SELECT *FROM notificaciones WHERE id = (SELECT id FROM notificaciones WHERE usado = 0 AND Importancia = (SELECT MAX(Importancia) FROM notificaciones WHERE usado = 0 LIMIT 1)LIMIT 1) LIMIT 1;';
      
      connection.query(query, (err, results) => {
        if (err) {
          console.error('Error fetching data: ', err);
          reject(err); // Rechazamos la promesa en caso de error
          return;
        }
        if(results.length==0) resolve("nada que mostrar");
        else{
          const notificaciones = results;
          const notidata = JSON.parse(notificaciones[0].data);

          const test = NotificacionesService.formatMessage(notidata, notificaciones[0].activo,notificaciones[0].tipoNotificacion,notificaciones[0]);
          updateNotificaciones(notificaciones[0].id);
          
          bot.sendMessage(-1001757976417, test);
          resolve(notidata);
        }
       
      });
    });
  }
  function alive(){
    bot.sendMessage(1914457326, "sigue vivo");

  }
  function customNotification(body, res) {
    return new Promise((resolve, reject) => {
      console.log("entra")
      const query = `SELECT * FROM notificaciones WHERE activo = '${body.info}' LIMIT 1;`;
      let msj = "";
  
      connection.query(query, (err, results) => {
        if (err) {
          console.error('Error fetching data: ', err);
          reject(err); // Rechazamos la promesa en caso de error
          return;
        }
  
        if (results.length === 0) {
          // Hacer algo si no hay resultados
        } else {
          const notificaciones = results;
          const notidata = JSON.parse(notificaciones[0].data);
  
          msj = NotificacionesService.formatMessage(notidata, notificaciones[0].activo, notificaciones[0].tipoNotificacion, notificaciones[0]);
  
          // Enviamos la notificación después de obtener la respuesta de la base de datos
          console.log(msj)
          body.users.forEach(user => {
            console.log(user)
            try {
              bot.sendMessage(user, msj);
            } catch (error) {
              console.log("Error sending message", error);
            }
          });
  
          // Resolvemos la promesa con los datos necesarios
          resolve(notidata);
        }
      });
    });
  }
  
  // Uso de la función
  
  // UPDATE NOTIFICACIONES
  function updateNotificaciones(id){ 
    const updateData = {
        usado: 1,
      };
    
const query = 'UPDATE notificaciones SET ? WHERE id = ?';

connection.query(query, [updateData, id], (err, results) => {
        if (err) {
          console.error('Error fetching data: ', err);
          return;
        }
        //console.log('Data retrieved successfully:', results);
      });
}

  // FIN UPDATE  NOTIFICACIONES
  module.exports = {
    sendNotificaciones,updateNotificaciones,alive,customNotification
   
  };