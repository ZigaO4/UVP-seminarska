import re
import copy
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from cilji import remove_quot, template, objectives



def match_stats(name, match_id):
    """Vrne slovar statistike od specifične igre"""
    url = f"https://draftoutmc.com/leaderboard/{name}/{match_id}?metric=elo&filter=competitive"
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(1)
    
    #Shranjevanje HTML od Igre
    content = driver.page_source
    with open(f"{name}-{match_id}.html", "w", encoding='UTF-8') as f:
        f.write(content)
    remove_quot(f"{name}-{match_id}.html")

    #Selenium klikne na gumb
    draft_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Draft')]")
    draft_button.click()
    time.sleep(1)

    #Shranjevanje HTML od Drafta
    content = driver.page_source
    driver.quit()
    with open(f"{name}-{match_id}-draft.html", "w", encoding='UTF-8') as f:
        f.write(content)
    remove_quot(f"{name}-{match_id}-draft.html")
    
    

    data = copy.deepcopy(template)

    #Ekstrakcija podatkov iz igre
    with open(f"{name}-{match_id}.html", "r", encoding='UTF-8') as file:
        html_profile = file.read()
        completed_objectives = re.findall(fr'title="([^"]+) - {name}', html_profile)

        #Če je igralec zmagal cilj
        for item in completed_objectives:
            if item in objectives:
                data[item]["completed"] += 1

        #Če je igralec izgubil cilj
        lost_objectives = re.findall(fr'title="([^"]+) - (?!{name})', html_profile)
        for item in objectives:
            if item in lost_objectives:
               data[item]["lost"] += 1

    #Ekstrakcija podatkov iz drafta
    with open(f"{name}-{match_id}-draft.html", "r", encoding='UTF-8') as file:
        html_profile = file.read()

        #Če se je cilj pojavil v igri
        appeared_objectives = re.findall(fr'role="gridcell" title="([^"]+)', html_profile)
        for item in appeared_objectives:
            if item in objectives:
                data[item]["appeared"] += 1


        #Če se je cilj pojavil v draftu
        appeared_draft = re.findall(rf'100">{name}<span.*?picks:.*?text-neutral-\d*"[^>]*>([^<]*)<.*?text-neutral-\d*"[^>]*>([^<]*)<', html_profile)
        for match in appeared_draft:
            choice_insert_goals(match[0], data)
            choice_insert_goals(match[1], data)


        #Če je igralec izbral cilj
        drafted = re.findall(rf'(100">{name}<span class="ml-1.*?picks.*?break-words hyphens-auto text-neutral-100">(.+?)<\/span>)', html_profile)
    
        for match in drafted:
            if "Not completed" not in match[0] and "reroll" not in match[0]:
                objective=match[1].replace('"', '')
                if objective in objectives:
                    data[objective]["drafted"]+=1



    return data




def choice_insert_goals(goal, data):
    """Počisti objective ter ga shrani v choice"""
    goal=goal.replace('"', '')
    if goal in objectives:
        data[goal]["choice"]+=1
    else:
        print(goal + " does not exist")