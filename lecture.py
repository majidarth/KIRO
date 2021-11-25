import json

def lire_instances(instances):
    with open(instances) as file:
        instances_enonce = json.load(file)
    return instances_enonce
    
def ecrire_instances(solution,fichier):
    with open(fichier, "w") as file:
        json.dump(solution,file, indent=4)