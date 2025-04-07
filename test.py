from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":

    # Erstellen eines Leistungstests
    supervisor = Supervisor("Carol", 'Supervisor')
    subject = Subject("Tina", "Twitch", "female", 30)
    max_hr = subject.estimate_max_hr()
    print(max_hr)

    experiment = Experiment(experiment_id=1, supervisor=Supervisor, creation_date='1.1.2021')
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)

    print(experiment)
