import lecture

fichier = "KIRO-small.json"
fichier_sol = "solution_small.json"
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
    
    demande = [0 for i in range(len(instances["sites"]))]
    for j in instances["clients"]:
        site = 1
        while(demande[site-1] + j["demand"] > instances["parameters"]["capacities"]["productionCenter"] + instances["parameters"]["capacities"]["automationBonus"]):
            site += 1
        if(demande[site-1] == 0):
            solution["productionCenters"].append({"id": site, "automation": 1})
        demande[site-1] += j["demand"]
        solution["clients"].append({"id": j["id"], "parent": site})
    
    return solution

lecture.ecrire_instances(solution_sans_saturation(instances), fichier_sol)