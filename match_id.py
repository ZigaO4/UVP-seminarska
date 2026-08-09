import re
from selenium import webdriver
import time



def profile(name):
    """Shrani HTML profila uporabnika"""
    url = f"https://draftoutmc.com/leaderboard/{name}?metric=elo&filter=competitive"
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)   
    driver.get(url)
    time.sleep(2)
    profile_content = driver.page_source
    with open(f"{name}.html", "w", encoding='UTF-8') as f:
        f.write(profile_content)
        driver.quit()
    return None


def match_ids(name):
    profile(name)
    time.sleep(2)
    with open(f"{name}.html", "r", encoding='UTF-8') as f:
        html_profile = f.read()
    return re.findall(r'data-scroll-key="(\d+)"', html_profile)







