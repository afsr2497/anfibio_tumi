import requests
import time



indicador = 1
start_time = time.time()
counter = 0
while indicador:
    resp = requests.get(url='http://192.168.137.30:8666/infoRobot')
    print(resp.json())
    counter = counter + 1
    end_time = time.time()
    if (end_time - start_time) > 1.00:
        indicador = 0

print('El tiempo de respuesta es:')
print(round(end_time-start_time,2))
print('Se han hecho x requests : ')
print(counter)