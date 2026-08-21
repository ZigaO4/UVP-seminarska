import csv
import copy
from cilji import *
from match_id import match_ids
from ekstrakcija import match_stats



def objective_stats(name):
    """Vrne slovar s statistiko vseh ciljev vseh iger"""
    data = copy.deepcopy(template)
    metric_list = ["choice", "drafted", "appeared", "completed", "lost"]

    for match_id in match_ids(name):
        match_data = match_stats(name, match_id)
        for item in match_data:
            for metric in metric_list:
                data[item][metric] += match_data[item][metric]
    return data



def create_csv(name):
    """Ustvari csv s podatki vseh iger"""
    data = objective_stats(name)
    with open(f"{name}.csv", "w", newline="", encoding="UTF-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "choice", "drafted", "appeared", "completed", "lost"])
        i = 0
        for goal in data:
            stats = data[goal]
            writer.writerow([i, goal, stats["choice"], stats["drafted"], stats["appeared"], stats["completed"], stats["lost"]])
            i += 1