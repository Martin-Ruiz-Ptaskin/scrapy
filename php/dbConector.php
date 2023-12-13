<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: Content-Type");
/*
$servername = "localhost";
$username = "root";
$password = "";
$database = "scrapy";
*/
$servername = "localhost";
$username = "datodtal_scrapy";
$password = "%V]B]Rvvl}uo";
$database = "datodtal_scrapy";
// Crear una conexión
$conn = new mysqli($servername, $username, $password, $database);

// Verificar la conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
} 

// Realizar consultas, operaciones en la base de datos, etc.

// Cerrar la conexión al finalizar
?>
