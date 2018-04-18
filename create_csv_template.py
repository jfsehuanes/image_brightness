import csv

with open('brillo_percibido.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Dia de Muestreo', 'Fase Lunar', 'Fecha', 'Hora', 'Brillo Percibido', 'Nombre del Archivo'])

