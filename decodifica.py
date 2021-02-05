import argparse
import csv

#Setto gli argomenti di input accettati
parser = argparse.ArgumentParser(description="Converte una colonna di un file csv sostituendo i nomi veri ai codici persona o matricola. USA I FILE DI INPUT COME QUELLI DI ESEMPIO")
parser.add_argument("-f", "--file", default="input.csv", help="Seleziona file csv di input, se non lo specifichi userà un file chiamato input.csv nella stessa cartella dello script")
parser.add_argument("-db", "--database", default="database.csv", help="Seleziona un csv di dati, di default ne usa uno chiamato database.csv nella cartella dello script")
parser.add_argument("-i", "--interessanti", action="store_true", help="Converti solo persone interessanti")

modalita = parser.add_mutually_exclusive_group(required=True)
modalita.add_argument("-cp", "--cod_pers", action="store_true", help="Converti usando i codici persona")
modalita.add_argument("-matr", "--matricola", action="store_true", help="Converti usando le matricole")

#Leggo gli input
args = parser.parse_args()
#print(args)

#Apro tutti i file necessari
data_file = open(args.database, 'r')
data = csv.DictReader(data_file)
ingresso = csv.DictReader(open(args.file, 'r'))
output = csv.writer(open('output.csv', 'w'))

#Preparazione alla conversione
if args.cod_pers == True:
    campo = "cod_pers"
elif args.matricola == True:
    campo = "matr"

contatore = 0
#Inizio conversione
for risultato in ingresso:
    data_file.seek(0)
    #next(data, None)
    trovato = False
    for persona in data:
        if risultato[campo] == persona[campo]:
            #Schifo per sistemare il formato della colonna interessa (se nel database il flag è "1" lo vede come una stringa, se è 1 è un int)
            if isinstance(persona["interessa"], str):
                interessa = int(persona["interessa"])
            else:
                interessa = persona["interessa"]
            
            #Verifica se vuoi solo quelli interessanti o tutti
            if (args.interessanti == True and interessa==1) or args.interessanti == False:
                contatore = contatore + 1
                trovato = True
                output.writerow([persona["nome"], risultato["voto"]]) #Salvi sostituendo al codice il nome
    
    if trovato == False:
        output.writerow([risultato[campo], risultato["voto"]]) #Salvo uguale al risultato in ingresso

print("Ho convertito: " + str(contatore) + " " + campo)