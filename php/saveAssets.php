<?php
include 'dbConector.php';

$jsonData = file_get_contents("php://input");
$data = json_decode($jsonData, true);





// Datos del objeto JSON
$key = $data['key'];
$dataArray = $data['data'];

// Verificar si el key ya existe en la tabla usuario
$checkUserQuery = "SELECT id FROM usuarios WHERE name = '$key'";
$checkUserResult = $conn->query($checkUserQuery);

if ($checkUserResult->num_rows > 0) {
    // El key ya existe, realizar una actualización
    $newAssets = implode(",", array_column($dataArray, 'webID'));

    // Actualizar la columna assets en la tabla usuario
    $updateUserQuery = "UPDATE usuarios SET assets = '$newAssets' WHERE name = '$key'";
    if ($conn->query($updateUserQuery) === TRUE) {
        echo json_encode(array("statusCode" => 200, "mensaje" => "Usuario actualizado correctamente."));
    } else {
        echo json_encode(array("statusCode" => 0, "mensaje" => "Error al actualizar usuario."));
    }
} else {
    // El key no existe, realizar una inserción
    $insertUserQuery = "INSERT INTO usuarios (name, assets) VALUES ('$key', '" . implode(",", array_column($dataArray, 'webID')) . "')";
    if ($conn->query($insertUserQuery) === TRUE) {
        echo json_encode(array("statusCode" => 200, "mensaje" => "Usuario insertado correctamente."));
    } else {
        echo json_encode(array("statusCode" => 0, "mensaje" => "Error al insertar usuario."));
    }
}

// Cerrar la conexión
$conn->close();
?>