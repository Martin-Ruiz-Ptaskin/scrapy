const mysql = require('mysql2');

const pool = mysql.createPool({
    connectionLimit: 10, // Puedes ajustar este límite según tus necesidades
    host: "50.87.144.185",
    user: "datodtal_scrapy",
    password: "%V]B]Rvvl}uo",
    database: "datodtal_scrapy"
  });
  module.exports={
    pool
    };