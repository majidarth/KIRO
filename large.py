import lecture
import numpy as np

fichier = "KIRO-large.json"
fichier_sol = "solution_large.json"
instances = lecture.lire_instances(fichier)

def solution_triviale(instances):
    solution = dict.fromkeys(["productionCenters","distributionCenters","clients"])
    solution["productionCenters"] = [{"id": 1, "automation": 1}]
    solution["distributionCenters"] = []
    clients = []
    for i in range(1,len(instances["clients"])+1):
        clients.append({"id": i, "parent": 1})
    solution["clients"] = clients
    return solution

def solution_sans_saturation(instances):
    solution = dict.fromkeys(["productionCenters","distributionCenters","clients"])
    solution["productionCenters"] = []
    solution["distributionCenters"] = []
    solution["clients"] = []
    
    production = [0 for i in range(len(instances["sites"]))]
    for j in instances["clients"]:
        site = 1
        while(production[site-1] + j["demand"] > instances["parameters"]["capacities"]["productionCenter"] + instances["parameters"]["capacities"]["automationBonus"]):
            site += 1
        if(production[site-1] == 0):
            solution["productionCenters"].append({"id": site, "automation": 1})
        production[site-1] += j["demand"]
        solution["clients"].append({"id": j["id"], "parent": site})
    
    return solution

def solution_heuristique_1(instances):
    solution = dict.fromkeys(["productionCenters","distributionCenters","clients"])
    solution["productionCenters"] = []
    solution["distributionCenters"] = []
    solution["clients"] = []
    
    demande_totale = 0
    for j in instances["clients"]:
        demande_totale += j["demand"]
    nb_usines_total = int(demande_totale//(instances["parameters"]["capacities"]["productionCenter"] + instances["parameters"]["capacities"]["automationBonus"]) + 1)

    usines = instances["sites"]
    clients_deja_visites = []
    
    for i in range(nb_usines_total):
        usine = np.random.choice(usines)
        solution["productionCenters"].append({"id" : usine["id"], "automation" : 1})
        usines.remove(usine)
        distances = instances["siteClientDistances"][usine["id"]-1]
        
        for client in clients_deja_visites :
            distances[client["id"]-1] = 5000000000
            
        production = 0
        capacity  = instances["parameters"]["capacities"]["productionCenter"] + instances["parameters"]["capacities"]["automationBonus"]
        while(production < capacity):
            client_plus_proche = np.argmin(distances)
            distances[client_plus_proche] = 5000000000
            cl = instances["clients"][client_plus_proche]
            clients_deja_visites.append(cl)
            production += instances["clients"][client_plus_proche]["demand"]
            solution["clients"].append({"id" : cl["id"], "parent": usine["id"]})
        
    return solution
            
        
    
print(solution_heuristique_1(instances))   

lecture.ecrire_instances(solution_heuristique_1(instances), fichier_sol)


def solution_heuristique_main_1(instances):
    solution = dict.fromkeys(["productionCenters", "distributionCenters", "clients"])
    solution["productionCenters"] = []
    solution["distributionCenters"] = []
    solution["clients"] = []

    centres_prod_ids = [4, 7, 2, 30, 19, 39, 33, 12, 38,59, 36, 18, 25, 56, 44, 16, 37]
    clients_satisfaits = []
    for id in centres_prod_ids:
        solution["productionCenters"].append({"id": id, "automation":1})
        site = instances["sites"][id]
        nouveaux_clients_satisfaits = []
        clients_satisfaits.append(nouveaux_clients_satisfaits)


    for centre in centres_prod:


        for client in nouveaux_clients_satisfaits:
            id = client["id"]
            solution["clients"].append({"id":id, "parent":centre})







    return solution