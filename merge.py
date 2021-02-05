import csv
import string

data_file = open('dati.csv')
data = csv.DictReader(data_file)

newdata_file = open('nuovi_dati.csv')
newdata = csv.DictReader(newdata_file, delimiter=',')

output_file = open('output.csv', 'w')
output = csv.writer(output_file)

for esistente in data:
    curr_cod_pers = esistente['cod_pers']
    #2 righe successive servono per riparte ogni volta dall'inizio skippando l'header
    newdata_file.seek(0)
    next(newdata, None)
    trovato = False
    for nuovo in newdata:
        if curr_cod_pers == nuovo["cod_pers"]:
            print("trovato"+str(curr_cod_pers))
            output.writerow([esistente["nome"],esistente["cod_pers"],nuovo["matr"], esistente["interessa"]])
            trovato = True
    if trovato == False:
        output.writerow([esistente["nome"],esistente["cod_pers"],esistente["matr"], esistente["interessa"]])
