import re
import time
from selenium import webdriver


def create_objectives_html():
    """Shrani HTML File spletne strani z objectivi"""
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    url = "https://draftoutmc.com/wiki"
    driver.get(url)
    time.sleep(4)
    objectives_content = driver.page_source
    driver.quit()
    with open("objectives.html", "w", encoding='UTF-8') as f:
        objectives_content = objectives_content.replace("&quot;", "")
        f.write(objectives_content)
    

create_objectives_html()



#Ustvari seznam objectivov iz HTML kode
objectives = []
with open("objectives.html", "r", encoding='UTF-8') as file:
    html_objectives = file.read()
objectives = re.findall(r'title="([^"]+)"', html_objectives)



#Predloga za obliko shranjevanja podatkov
entry = {
        "choice": 0,
        "drafted": 0,
        "appeared": 0,
        "completed": 0,
        "lost": 0,
    }
template = {}
for i in range(0, len(objectives)):
    template[objectives[i]] = entry.copy()
