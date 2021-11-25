import json

def lire_instances(instances):
    with open(instances) as file:
        instances_enonce = json.load(file)
    return instances_enonce
    