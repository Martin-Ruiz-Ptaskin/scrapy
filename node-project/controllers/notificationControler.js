const { text } = require("express");
const NotificacionesService = require("../service/notificacionesService.js");
const mysql = require('mysql2');
const TelegramBot = require('node-telegram-bot-api');

// replace the value below with the Telegram token you receive from @BotFather
const token = '6374242902:AAGIWd6vkwID8LOmTEy5Y9Q6cDzOjIuBRUo';
const bot = new TelegramBot(token, { polling: true });

// MySQL Connection Pool
const pool = mysql.createPool({
  connectionLimit: 10, // Puedes ajustar este límite según tus necesidades
  host: "50.87.144.185",
  user: "datodtal_scrapy",
  password: "%V]B]Rvvl}uo",
  database: "datodtal_scrapy"
});

// Matches "/echo [whatever]"
bot.onText(/\/echo (.+)/, (msg, match) => {
  const chatId = msg.chat.id;
  const resp = match[1]; // the captured "whatever"
  bot.sendMessage(chatId, resp);
});

bot.on('message', (msg) => {
  const chatId = msg.chat.id;
  console.log(msg.text);

  const url = "https://econoba.martinruizptaskin.com.ar?key=" + chatId;
  const textoAenviar = "Configura los activos sobre los que recibirás notificaciones " + url;

  switch (msg.text) {
    case "/activos":
      bot.sendMessage(chatId, textoAenviar);
      break;
    default:
      bot.sendMessage(chatId, "Envía /activos para comenzar a editar tus notificaciones");
  }
});

async function sendNotificaciones(req, res) {
  return new Promise((resolve, reject) => {
    const query =      
    'SELECT *FROM notificaciones WHERE id = (SELECT id FROM notificaciones WHERE usado = 0 AND Importancia = (SELECT MAX(Importancia) FROM notificaciones WHERE usado = 0 LIMIT 1)LIMIT 1) LIMIT 1;';
 ;    
    // Usar la función pool.query en lugar de connection.query
    pool.query(query, (err, results) => {
      if (err) {
        console.error('Error fetching data: ', err);
        reject(err);
        return;
      }
      if (results.length === 0) resolve("nada que mostrar");
      else {
        const notificaciones = results;
        const notidata = JSON.parse(notificaciones[0].data);
        const test = NotificacionesService.formatMessage(notidata, notificaciones[0].activo, notificaciones[0].tipoNotificacion, notificaciones[0]);
        updateNotificaciones(notificaciones[0].id);
        bot.sendMessage(-1001757976417, test);
        resolve(notidata);
      }
    });
  });
}

// Otras funciones (alive, customNotification, updateNotificaciones) siguen siendo las mismas.
// ... (código anterior)

function alive() {
  // Usar la función pool.query en lugar de connection.query


  bot.sendMessage(1914457326, "sigue vivo");
}

function customNotification(body, res) {
  return new Promise((resolve, reject) => {
    const query = `SELECT * FROM notificaciones WHERE activo = '${body.info}' LIMIT 1;`;
    let msj = "";

    // Usar la función pool.query en lugar de connection.query
    pool.query(query, (err, results) => {
      if (err) {
        console.error('Error fetching data: ', err);
        reject(err);
        return;
      }

      if (results.length === 0) {
        // Hacer algo si no hay resultados
      } else {
        const notificaciones = results;
        const notidata = JSON.parse(notificaciones[0].data);
        msj = NotificacionesService.formatMessage(notidata, notificaciones[0].activo, notificaciones[0].tipoNotificacion, notificaciones[0]);

        body.users.forEach(user => {
          try {
            bot.sendMessage(user, msj);
          } catch (error) {
            console.log("Error sending message", error);
          }
        });

        resolve(notidata);
      }
    });
  });
}

function updateNotificaciones(id) {
  const updateData = {
    usado: 1,
  };

  const query = 'UPDATE notificaciones SET ? WHERE id = ?';

  // Usar la función pool.query en lugar de connection.query
  pool.query(query, [updateData, id], (err, results) => {
    if (err) {
      console.error('Error updating data: ', err);
      return;
    }
    //console.log('Data updated successfully:', results);
  });
}

// ... (código posterior)

// Cerrar el pool de conexiones cuando la aplicación se apague
process.on('SIGINT', () => {
  pool.end();
  console.log('Connection pool closed.');
  process.exit();
});

process.on('exit', () => {
  pool.end();
  console.log('Connection pool closed.');
});

// Escuchar eventos no manejados
process.on('unhandledRejection', (reason, p) => {
  console.error('Unhandled Rejection at:', p, 'reason:', reason);
  // Aquí puedes manejar el error de manera adecuada si es necesario
});

  // FIN UPDATE  NOTIFICACIONES
  module.exports = {
    sendNotificaciones,updateNotificaciones,alive,customNotification
   
  };