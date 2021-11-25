# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 15:27:56 2021

@author: thoma
"""

import numpy as np
import lecture
fichier_en = "KIRO-tiny.json"
fichier_sol = "solution_tiny.json"
instance = lecture.lire_instances(fichier_en)
solution = lecture.lire_instances(fichier_sol)

def score(instance, solution):
    nb_S = len(instance["sites"])
    P = np.array([center["id"] for center in solution["productionCenters"]])
    D = np.array([center["id"] for center in solution["distributionCenters"]])
    a = (-1)*np.ones(nb_S)
    for prod_center in P :
        a[prod_center] = prod_center["automation"]
    p = np.zeros(nb_S)
    for distr_center in D:
        p[distr_center] = distr_center["parent"]
    s = solution["clients"]

    parameters = instance["parameters"]

    # bulding cost
    buildingCosts = parameters["buildingCosts"]
    building_cost = 0


    capacity_cost = 0
    production_cost = 0
    routing_cost = 0


    

score(instance_en, instance_sol)