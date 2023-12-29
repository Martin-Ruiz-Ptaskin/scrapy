import DBconection as BD

# Paso 1: Obtener el webID de la tabla stockprice para el asset dado
def customNotification(asset_deseado,noti):
   
    query_paso_1 = f"SELECT webID FROM stockprice WHERE asset = '{asset_deseado}'"
    webID_result = None
    
    try:
        BD.cursor.execute(query_paso_1)
        webID_result = BD.cursor.fetchone()
    except BD.Error as err:
        print(f"Error: '{err}'")
    finally:
        if BD.connection:
            BD.connection.close()
    
    if webID_result:
        webID_obtenido = webID_result[0]
    
        # Paso 2: Buscar en la tabla usuarios si el webID está en la columna assets
        query_paso_2 = f"SELECT * FROM usuarios WHERE FIND_IN_SET('{webID_obtenido}', assets) > 0"
        usuarios_result = None
    
        try:
            BD.cursor.execute(query_paso_2)
            usuarios_result = BD.cursor.fetchall()
        except  BD.Error as err:
            print(f"Error: '{err}'")
        finally:
            if  BD.connection:
                BD.connection.close()
    
        if usuarios_result:
            print("Usuarios encontrados:")
            for row in usuarios_result:
                print(row)
        else:
            print("No se encontraron usuarios con el webID en la columna assets.")
    else:
        print(f"No se encontró webID para el asset '{asset_deseado}'.")
