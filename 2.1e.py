#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:05:33 2020

@author: Egidio
"""

import json

# Legge la lista dei log in formato json e la memorizza 
# in una struttura dati python
fin = open('/Users/Egidio/Desktop/input_data.json')
text = fin.read()
data = json.loads(text)

# Inizializza i dizionari e le variabili utilizzate
tabella = {}
tabella_eventi = {}
tabella_date = {}
num_utente = 1
num_evento = 1
num_data = 1
cont = 1
num_acc = 1
num_acc_evento = 1

# Estrae le informazioni relative ai log. Crea tre tabelle riferite al numero
# di utenti, il numero di eventi ed alla distribuzione temporale dei log.
# Conta quante volte compare quell'informazione
for log in data:    
    for info in log:
        if info[1] not in tabella: 
            tabella[info[1]] = num_utente 
            cont += 1
        elif info[1] in tabella:
            tabella[info[1]] += 1 
        if info[5] not in tabella_eventi:
            tabella_eventi[info[5]] = num_evento
        elif info[5] in tabella_eventi:
            tabella_eventi[info[5]] += 1   
        if info[0][0:8] not in tabella_date:
            tabella_date[info[0][0:8]] = num_data
        elif info[0][0:8] in tabella_date:
            tabella_date[info[0][0:8]] += 1
            

# Stampa il numero totale di utenti
print("Il numero totale degli utenti è:", cont)
print(" ") 

# Stampa il numero totale di log
num_log = len(log)
print("Il numero totale dei log è:", num_log)
print(" ")

# Stampa il numero medio intero di log per utente
media_log = int(num_log/cont)
print("Il numero numero medio di log per utente circa è:", media_log)
print(" ")

# Stampa l'identificatore unico che ha fatto più log
for id_unico in tabella:
    if tabella[id_unico] > num_acc:
        utente = id_unico
        num_acc = tabella[id_unico]
print("L'identificatore unico che ha fatto più accessi è:", utente)   
print("e il suo numero di accessi è pari a:", num_acc)   
print(" ")

# Stampa l'evento eseguito più spesso
for evento in tabella_eventi:
    if tabella_eventi[evento] > num_acc_evento:
        evento_frequente = evento
        num_acc_evento = tabella_eventi[evento]
print("L'evento eseguito più spesso è:", evento_frequente)
print("ed il numero delle volte che è stato eseguito è pari a:", num_acc_evento)
print(" ")

# Stampa la distribuzione temporale dei log. Viene associata alla data il 
# numero di log effettuati nel formato: 'gg/mm/aa': numero di log
print("La distribuzione temporale dei log è:", tabella_date)

# Salva su file il report relativo alle informazioni sui log richieste
report = ["Il numero totale degli utenti e' " + str(cont),
          "Il numero totale dei log e' " + str(num_log),
          "Il numero numero medio di log per utente circa e' " + str(media_log),
          "L'identificatore unico che ha fatto piu' accessi e' il " + utente + " ed il numero delle volte che e' stato eseguito e' pari a " + str(num_acc),            
          "L'evento eseguito piu' spesso e' '" + evento_frequente + "' ed il numero delle volte che e' stato eseguito e' pari a " + str(num_acc_evento),
          "La distribuzione temporale dei log e'" + str(tabella_date)]

with open("report.json", "w") as outfile:
    json.dump(report, outfile, indent=1)
    
fin.close()
outfile.close()


        
