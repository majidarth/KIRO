# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 15:27:56 2021

@author: thoma
"""

import lecture
fichier_en = "KIRO-medium.json"
fichier_sol = "solution_medium.json"
instance_en = lecture.lire_instances(fichier_en)
instance_sol = lecture.lire_instances(fichier_sol)

def score(instance_en, instance_sol):
    building = instance_en["parameters"]["buildingCosts"]
    production = instance_en["parameters"]["productionCosts"]
    routing = instance_en["parameters"]["routingCosts"]
    capacity = instance_en["parameters"]["capacityCost"]
    capacities = instance_en["parameters"]["capacities"]
    if False:
        print(building)
        print(production)
        print(routing)
        print(capacity)
        print(capacities)
    building_cost = 0
    production_cost = 0
    routing_cost = 0
    capacity_cost = 0
    for key, val in instance_en["clients"].items():
        continue
    for key, val in instance_sol["distributionCenters"].items():
        continue
    

score(instance_en, instance_sol)