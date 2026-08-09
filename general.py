import copy
from misc import *
from match_id import *
from analysis import *





def objective_stats(name):
    """Vrne slovar s statistiko vseh objectivov vseh iger"""
    data = copy.deepcopy(template)


    #for match_id in match_ids(name):
    for i in range (0,2):
        match_id = match_ids(name)[i]
        match_data = match_stats(name, match_id)
        for item in match_data:
            data[item]["choice"]+=match_data[item]["choice"]
            data[item]["drafted"]+=match_data[item]["drafted"]
            data[item]["appeared"]+=match_data[item]["appeared"]
            data[item]["completed"]+=match_data[item]["completed"]
            data[item]["lost"]+=match_data[item]["lost"]
    return data["Kill Bogged"]


print(objective_stats("Feinberg"))