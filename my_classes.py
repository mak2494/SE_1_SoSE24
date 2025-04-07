from datetime import datetime

class Subject():
    def __init__(self, first_name, last_name, sex,age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age 
        pass

    def estimate_max_hr(self):
        """A function that estimates the maximum heart rate of a subject"""
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 *  self.age
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)
        pass

class Supervisor():
    def __init__(self, name, role):
        self.name = name
        self.role = role
        pass

class Experiment:
    def __init__(self, experiment_id, supervisor, creation_date):
        self.experiment_id = experiment_id  # Experiment ID
        self.supervisor = supervisor  # Supervisor
        if creation_date is None:
            self.creation_date = datetime.today().strftime('%Y-%m-%d')  # Datum im Format YYYY-MM-DD
        else:
            self.creation_date = creation_date
        self.subject = None  # Zu Beginn gibt es noch kein Subjekt

    def add_subject(self, subject):
        """Füge ein Subjekt zum Experiment hinzu"""
        self.subject = subject

    def add_supervisor(self, supervisor):
        """Füge einen Supervisor zum Experiment hinzu"""
        self.supervisor = supervisor

    def __str__(self):
        subject_info = f"{self.subject.first_name} {self.subject.last_name}" if self.subject else "No subject added"
        return f"Experiment ID: {self.experiment_id}, Supervisor: {self.supervisor}, Subject: {subject_info}, Date: {self.creation_date}"