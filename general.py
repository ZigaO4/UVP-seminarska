import copy
import csv
from misc import *
from match_id import *
from analysis import *





def objective_stats(name):
    """Vrne slovar s statistiko vseh objectivov vseh iger"""
    data = copy.deepcopy(template)


    for match_id in match_ids(name):
        match_data = match_stats(name, match_id)
        for item in match_data:
            data[item]["choice"]+=match_data[item]["choice"]
            data[item]["drafted"]+=match_data[item]["drafted"]
            data[item]["appeared"]+=match_data[item]["appeared"]
            data[item]["completed"]+=match_data[item]["completed"]
            data[item]["lost"]+=match_data[item]["lost"]
    return data


def create_csv(name):
    """ustvari csv s podatki vseh iger"""
    data = objective_stats(name)
    with open(f"{name}.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "choice", "drafted", "appeared", "completed", "lost"])
        i=0
        for goal in data:
            writer.writerow([i, goal, data[goal]["choice"], data[goal]["drafted"], data[goal]["appeared"], data[goal]["completed"], data[goal]["lost"]])
            i+=1
    return None
 
print(create_csv("Feinberg"))