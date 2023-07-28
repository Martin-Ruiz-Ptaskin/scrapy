const express= require("express") //importo Express
const app = express() // Creo una instancia
app.listen(3000)//uso el puerto 3000

let msjColector=[]
let notificaciones
//Telegram Bot
const TelegramBot = require('node-telegram-bot-api');


// replace the value below with the Telegram token you receive from @BotFather
const token = '6374242902:AAGIWd6vkwID8LOmTEy5Y9Q6cDzOjIuBRUo';

// Create a bot that uses 'polling' to fetch new updates
const bot = new TelegramBot(token, {polling: true});

//  FIN TELEGRAM BOT
//INICIO SQL
const mysql = require('mysql2');

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'scrapy'
});
connection.connect((err) => {
    if (err) {
      console.error('Error connecting to the database: ', err);
      return;
    }
    console.log('Connected to the MySQL server.');
  });
  // SELECIONO NOTIFICACIONES


  // FIN NOTIFICACIONES

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
  console.log(chatId)
  msjColector.push( {id:chatId, texto:msg.text})
  console.log(msjColector.filter(msj=> msj.id ==chatId ))

  // send a message to the chat acknowledging receipt of their message
  if(chatId!=1914457326){
    bot.sendMessage(chatId, 'Perdon no hablo con trolas');

  }
  else{
    bot.sendMessage(chatId, 'Hola Persona integra');

  }
});

app.get('/', function (req, res) { // creo el servicio y mapeo la peticion /
    const query = 'SELECT * FROM notificaciones where usado != 1 limit 1';
    connection.query(query, (err, results) => {
      if (err) {
        console.error('Error fetching data: ', err);
        return;
      }
      notificaciones=results
      res.send(notificaciones)
    console.log(notificaciones)
    test=" INSIDER ACTIVITY                                                -----------------------                                     Empresa()                                                    ------                                                         Nombre                                                   Compra                                                 Cantidad acciones"
    updateNotificaciones(notificaciones[0].id)
    bot.sendMessage(1914457326, test);

    });
    

})
