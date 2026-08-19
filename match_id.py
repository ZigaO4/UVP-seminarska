import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
depth = 5

def profile(name):
    """Shrani HTML profila uporabnika"""
    url = f"https://draftoutmc.com/leaderboard/{name}?metric=elo&filter=competitive"
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)   
    driver.get(url)
    time.sleep(2)


    for _ in range (0, depth):
        scroll = driver.find_element(By.XPATH, "(//div[@data-scroll-key])[last()]")
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        time.sleep(1)

    profile_content = driver.page_source
    driver.quit()
    with open(f"{name}.html", "w", encoding='UTF-8') as f:
        f.write(profile_content)
        
    return None


def match_ids(name):
    profile(name)
    time.sleep(2)
    with open(f"{name}.html", "r", encoding='UTF-8') as f:
        html_profile = f.read()

    ids = re.findall(r'data-scroll-key="(\d+)"', html_profile)
    print(str(len(ids)) + " matches")
    return ids







