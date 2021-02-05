# Exam results converter
## Cosa fa
Serve per convertire un elenco di risultati da codice persona (o matricola) e voto in un elenco di nome e voto. Ovviamente per fare l'abbinamento questi dati bisogna conoscerli a priori e vanno salvati nel database. Tutti i dati vanno in formato .csv e per crearli basta fare copia da un pdf o da una pagina web e incollare in excel o google sheet e salvare come csv.  
Alla fine dell'esecuzione ci si troverà un file chiamato output.csv con i risultati convertiti, se qualcuno non viene trovato nel database verrà lasciato il codice originario.  
Nella repo c'è anche un file `merge.py` che ho usato per completare il database ma non serve più a niente.

## Come si usa
Di base si fa:
```bash
python3 decodifica.py
```
Ho scritto `python3` perchè su mac bisogna fare cosi, sugli altri sistemi basta scrivere `python`.  
Al comando base **vanno** aggiunte delle opzioni che possono essere viste facendo:
```bash
python3 decodifica.py --help
```
ma che ora vedremo. L'ordine in cui si usano non ha importanza. Qui per semplicità userò solo la notazione con lettera singola ma dall'help si vedranno anche con la notazione estesa (non cambia niente, usa quello che ti è più comodo).  

Opzioni **obbligatorie**:
- `-cp` oppure `-matr` Servono per specificare se vuoi sostituire dei codici persona o delle matricole. Ne deve essere usato solo uno. Il file in ingresso dovrà corrispondere altrimenti ci sarà un errore.
  
Opzioni **facoltative**:
- `-f` seguito da un file, serve per specificare il file di ingresso. In caso non venga specificato il programma ne cercherà uno chiamato input.csv nella stessa cartella del file python.
- `-db` seguito da un file, serve per specificare un database. In caso non venga specificato il programma ne cercherà uno chiamato database.csv nella stessa cartella del file python.
- `-i` Serve per far convertire solo i nomi / codici persona che nel database hanno il flag "interessa" messo a 1.
  
Suggerimento: per scegliere un altro file nei casi `-f` e `-db` è comodo scrivere l'opzione, fare uno spazio e trascinare nel terminale il file desiderato.

### Esempi uso comodo
Per usare i file input.csv e database.csv nella stessa cartella del programma python e sostituire i codici persona solo delle persone che mi interessano si fa:
```bash
python3 decodifica.py -cp -i
```
Per usare un altro file di input e sostituire le matricole di tutti si fa:
```bash
python3 decodifica.py -matr -f documenti/materiedimerda/risultati_cam.csv
```
## Struttura dei dati
Questa struttura va **assolutamente** rispettata seguendo gli esempi caricati qui nella repo se non vuoi modificare il programma.  
Funziona bene con i file csv in input con separatore , e decimali . e senza virgolette "
### Database esempio
nome | cod_pers | matr | interessa
----------- | -------- | ------ | - 
Mario Rossi | 10512399 | 123456 | 1
Pippo | 10345600 | 123000 | 0

### Input codici persona esempio
Se ci sono altre colonne non importa, l'importante è che ci siano queste 2.  
Se il software con cui crei il csv non ti permette di nominare le colonne puoi aggiungere una riga all'inizio del file come quella degli esempi con un qualsiasi editor di testo. L'unica cosa a cui stare attenti è mettere tra virgolette i titoli se il software ha salvato i dati con le virgolette e senza virgolette se il software ha salvato i dati senza virgolette.
cod_pers | voto
----- | -----
10512399 | 28
10345600 | 20

### Input matricole esempio
Valgono le stesse regole della sezione precedente.
matr | voto
---- | ----
123456 | 28
123000 | 20

## Da fare
- Ricavare direttamente da un pdf la tabella in input con tabula-py