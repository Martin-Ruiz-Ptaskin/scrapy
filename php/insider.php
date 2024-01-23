<?php
include 'dbConector.php';

// Obtener el cuerpo de la solicitud POST
$json_data = file_get_contents("php://input");

// Decodificar los datos JSON
$data = json_decode($json_data);

// Verificar si la decodificación fue exitosa
if ($data === null) {
    // Error en la decodificación JSON
    $response = array('error' => 'Error decoding JSON data');
    echo json_encode($response);
} else {
    // Acceder a los valores individuales
    $date = $data->date;
    $code = $data->code;
    $company = $data->company;
    $tradetype = $data->tradetype;
    $title = $data->title;
    $QTY = $data->QTY;
    $own = $data->own;
    $value = $data->value;
    $insider = $data->insider;
 
    // Verificar la conexión
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Escapar los datos para evitar inyección SQL
    $title = mysqli_real_escape_string($conn, $title);
    $insider = mysqli_real_escape_string($conn, $insider);

    // Construir la consulta SQL
    $query = "INSERT INTO `insider` 
              ( `clave`, `name`, `company`, `amount`, `trade`, `date`, `cantidad`, `own`,`position`) 
              VALUES ('$company', '$insider', '$code', '$value', '$tradetype', '$date', '$QTY', '$own', '$title')";
    
    // Ejecutar la consulta
    if ($conn->query($query) === TRUE) {
        $response = array('success' => 'Data inserted successfully');
        echo json_encode($response);
    } else {
        $response = array('error' => 'Error executing SQL query: ' . $conn->error);
        echo json_encode($response);
    }

    // Cerrar la conexión a la base de datos
    $conn->close();
}
?>
