import re
from selenium import webdriver
import time




def createObjectivesHTML():
    """Shrani HTML File spletne strani z objectivi"""
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    url = f"https://draftoutmc.com/wiki"
    driver.get(url)
    time.sleep(3)
    objectives_content = driver.page_source
    driver.quit()
    with open(f"objectives.html", "w", encoding='UTF-8') as f:
        f.write(objectives_content)
    
    remove_quot(f"objectives.html")
    return None

#createObjectivesHTML()


#Ustvari seznam objectivov iz HTML kode
objectives = []
with open(f"objectives.html", "r", encoding='UTF-8') as file:
    html_objectives = file.read()
objectives = re.findall(r'title="([^"]+)"', html_objectives)


def remove_quot(file):
    """Iz HTML datoteke počisti &quot;"""
    with open(f"{file}", "r", encoding="UTF-8") as f:
        html_code = f.read()
    new_html = html_code.replace("&quot;", "")

    with open(f"{file}", "w", encoding="UTF-8") as f:
        f.write(new_html)
    return None

#Predloga za obliko shranjevanja podatkov
entry= {
        "choice": 0,
        "drafted": 0,

        "appeared": 0,
        "completed": 0,
        "lost": 0,
    }
template = {}
for i in range (0, len(objectives)):
    template[objectives[i]]=entry.copy()
