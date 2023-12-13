<?php
// Permitir todas las solicitudes de origen (CORS)
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: Content-Type");

include 'dbConector.php';
$key = $_GET['key'];

// Inicializar un array para almacenar los resultados
$response = array("statusCode" => 200, "mensaje" => array());

// Realizar la consulta para obtener los activos del usuario
$query = "SELECT assets FROM usuarios WHERE name = '$key'";
$result = $conn->query($query);

if ($result->num_rows > 0) {
    // Existen resultados, agregarlos al array de respuesta
    while ($row = $result->fetch_assoc()) {
        // Convertir la cadena de activos en un array
        $activos = explode(",", $row['assets']);
        $response["mensaje"] = $activos;
    }
} else {
    // No hay resultados para el key proporcionado
    $response["statusCode"] = 0;
    $response["mensaje"][] = "No se encontraron activos para el usuario con key = $key";
}

// Cerrar la conexión
$conn->close();

// Devolver el resultado como JSON
echo json_encode($response);
?>
