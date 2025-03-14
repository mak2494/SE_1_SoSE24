from datetime import date

def experiments(first_experiment_id:int=1): #sicherstellen id beginnt bei 1
    try: 
        first_experiment_id = int(first_experiment_id)
        if first_experiment_id < 1: #sicherstellen dass ID größer gleich 1 ist
            raise ValueError("Error: Id muss größer oder gleich 1 sein.")
    except (ValueError, TypeError):#Fehlhafte eingabe absichern 
        print("Error: Id muss ganze Zahl sein")
        return [] #bei Fehler leere Liste zurückgeben 
       

    experiments = [] #leere Liste für alle Experimente erstellen
    today:str = date.today().strftime("%Y-%m-%d") #heutiges Datum definieren 
    
    for i in range(10): #Dictionary für jedes individuelles Experiment erstellen, 10 Experimente
        experiment = {
            "Id_Nummer": first_experiment_id + i, 
            "Versuchsleiter": "Marie Köhl",
            "Erstellungsdatum": today
        }
        experiments.append(experiment) #liste mit 10 erstellten Dictionaries füllen 
    return experiments

experiments_list = experiments(1)  
for experiment in experiments_list[:5]:  # Die ersten 5 Einträge ausgeben
    print(experiment)

even_ids:int=0  
for experiment in experiments_list:
    if experiment["Id_Nummer"] % 2 == 0:  # gerade ID?
        even_ids += 1  

print("Anzahl Experimente mit gerader Id:", even_ids)

