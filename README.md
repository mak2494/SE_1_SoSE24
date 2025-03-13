# UC 1.05 Laktatmessung  
## Name und Identifikationsnummer
Laktatmessung 
## Beschreibung
DiagnostikerIn misst den Laktatwert der ProbandIn jeweils zum Ende der dreiminütigen Phase am Ohrläppchen. 
## Beteiligte Akteure
DiagnostikerIn und ProbandIn
## Status
In Planung 
## Verwendete....
UC 1.01 (ProbandIn anlegen) 
UC 1.02 (Leistungstest anlegen)
## Auslöser
Phasenende, alle 3 Minuten (Testnorm)
## Vorbedingungen
Test muss gestartet sein & kein frühzeitiger Test durch ProbandIn, DiagnostikerIn oder Alarm
## Invarianten 
Aufzeichnung der bisher erhobenen Daten, bei frühzeitigem Abbruch. Bei Fehl- oder Nicht-Messung ungültiger Test, ggf. neues Testdatum vereinbaren. 
## Nachbedingung/Ergebnis 
Steigerung der Wattzahl für nächste Phase & UC 1.06 (Borgskala) 
Reset timer 
Nächste Messung vorbereiten 
## Standardablauf 
Blutprobe aus Ohrläppchen alle 3 Minuten bis Test Ende
Auswertung der Blutprobe
Eingabe der Messergebnisse 
siehe Nachbedingungen 
## Altnernative Ablaufschritte 
Bei ungültiger Blutprobe, z.B. durch Verunreinigung, Testabbruch 
Bei Verpasster Blutprobe, Testabbruch 
Bei Messgerätfehler, Testabbruch 
Bei ungewünschter Reaktion des Probanden durch Blutprobenentnahme, Testabbruch 
## Hinweise 
manuelles Laktatmessgerät ('Name Messgerät') 
Messung am Ohrläppchen 
Entsorgung der benutzen Messuntensilien nach Vorschrift 
Dokumentieren der Messergenisse in digitaler Tabelle 
## Änderungsgeschichte 
Version 1, 13.03.25, 16:30, Marie Köhl, Julia Pietschmann 
