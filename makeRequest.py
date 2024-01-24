import requests



url2 = "http://localhost/generarActivo.php"
datas = {
    "date": "2024-01-24 07:00:31",
    "code": "CMP",
    "company": "Compass Minerals International Inc",
    "tradetype": "P - Purchase",
    "title": "Dir",
    "QTY": "43,496",
    "own": "+13%",
    "value": "+$106,200",
    "insider": "Reece Joseph E"
}


def makeRequest(url,data):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'User-Agent': 'XY'
    }
    print(data)
    response = requests.post(url2, headers=headers, json=data)
    
    # Verificar el código de estado
    if response.status_code == 200:
        # Verificar si la respuesta no está vacía antes de intentar analizarla como JSON
        if response.text:
            try:
                # Intentar analizar la respuesta JSON
                result = response
                print(result.text)
            except requests.exceptions.JSONDecodeError as e:
                print(f"Error al decodificar la respuesta JSON: {e}")
        else:
            print("La respuesta está vacía.")
    else:
        print(f"Error en la solicitud. Código de estado: {response.status_code}")
