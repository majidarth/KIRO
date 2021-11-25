import lecture

fichier = "KIRO-small.json"
fichier_sol = "solution_small.json"
instances = lecture.lire_instances(fichier)

def solution_triviale(instances):
    solution = dict.fromkeys(["productionCenters","distributionCenters","clients"])
    solution["productionCenters"] = [{"id": 1, "automation": 0}]
    solution["distributionCenters"] = []
    clients = []
    for i in range(1,len(instances["clients"])+1):
        clients.append({"id": i, "parent": 1})
    solution["clients"] = clients
    return solution

lecture.ecrire_instances(solution_triviale(instances), fichier_sol)