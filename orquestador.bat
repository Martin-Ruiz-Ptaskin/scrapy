@echo off
cd C:\Users\Usuario\scrapy\

echo Ejecutando superinvetors.py
C:\Users\Usuario\AppData\Local\Programs\Python\Python310\python.exe superinvetors.py

echo Ejecutando insiderstrack.py
C:\Users\Usuario\AppData\Local\Programs\Python\Python310\python.exe insiderstrack.py

echo Ejecutando GeneradorNotificaciones.py
C:\Users\Usuario\AppData\Local\Programs\Python\Python310\python.exe GeneradorNotificaciones.py

echo Ejecutando envioDeNotificaciones.py
C:\Users\Usuario\AppData\Local\Programs\Python\Python310\python.exe requestByBatch.py

echo Todos los archivos han sido ejecutados.


exit