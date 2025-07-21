from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random

# s = Service(r"chromedriver.exe")
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:5001")
# driver = webdriver.Chrome(service=s, options=options)
driver = webdriver.Chrome(options=options)

all_web = ['ffgaminggearguide.online','ffbrowgameparadise.online','ffgameespstraininmy.online','ffgamesolerssance.online','ffpcgaminginsider.online','ffindiegamefestival.online','ffwomeningame.online','huarcinggame.online','huextremgame.online','humobilemgame.online','huesportingsgame.online','hustratinegygame.online','hucasualingame.online','hupuzzledgame.online','huadventturegame.online','husimulationsgame.online','huraacinggame.online','huacstiongame.online','huroleplayeinggame.online','hubrainegame.online','hufunniinggame.online','hucasuallgame.online','humultiiutpgame.online','huonlineegame.online','huarcadecclasicgame.online','huinddiegame.online','huretroogame.online','husocialkgame.online','huworddgame.online','hucardboogame.online','hucasualarcegame.online','humueronlinegame.online','hucasualpulegame.online','hufasttacedgame.online','hucasualturegame.online','hutriviggagame.online','husportppsgame.online','hufamiflygame.online','hucasualracvinggame.online','huskivllgame.online','hucasualadctiongame.online','hucasualrolefcinggame.online','hucasualstdafegygame.online','hucasualsilationgame.online','hucasualsportsgame.online','hucasualmokbilegame.online','hucasuaneclassicgame.online','huhdefhnndhgame.online']
for i in all_web:
    driver.find_element(By.XPATH, '//a[@data-testid="link-homepage"]').click()
    time.sleep(6)
    driver.find_element(By.XPATH, '//span[text()="网站"]').click()
    time.sleep(6)
    try:
        driver.find_element(By.XPATH, '//*[@data-testid="account-zone-selector-search"]').send_keys(i)
        time.sleep(3)
    except:
        pass
    driver.find_element(By.XPATH, '//span[contains(text(),"搜索")]').click()
    time.sleep(random.randint(5, 8))


    try:
        driver.find_element(By.XPATH, '//*[text()="' + i + '"]').click()
        time.sleep(random.randint(5, 8))
        # driver.find_element(By.XPATH, '//*[@data-testid="zone-cards"]/a').click()
        # time.sleep(random.randint(5, 8))
        driver.find_element(By.XPATH, '//span[text()="DNS 记录"]').click()
        time.sleep(random.randint(5, 8))
        try:
            try:
                driver.find_element(By.XPATH, '//*[contains(@title,"image")]/../..//*[text()="编辑"]').click()
            except:
                driver.find_element(By.XPATH, '//*[contains(@title,"img")]/../..//*[text()="编辑"]').click()
            time.sleep(random.randint(3, 5))
            driver.find_element(By.XPATH, '//input[@name="ipv4_address"]').clear()
            driver.find_element(By.XPATH, '//input[@name="ipv4_address"]').send_keys('69.197.186.10')
            time.sleep(random.randint(3, 5))
            driver.find_element(By.XPATH, '//button[contains(text(),"保存")]').click()
            time.sleep(random.randint(8, 10))
        except:
            pass
        root_xtpah = '//*[@title="'+i+'"]/../..//*[text()="编辑"]'

        driver.find_element(By.XPATH, root_xtpah).click()
        time.sleep(random.randint(3, 4))
        driver.find_element(By.XPATH, '//input[@name="ipv4_address"]').clear()
        driver.find_element(By.XPATH, '//input[@name="ipv4_address"]').send_keys('107.150.60.90')
        time.sleep(random.randint(3, 5))
        driver.find_element(By.XPATH, '//button[contains(text(),"保存")]').click()
        time.sleep(random.randint(8, 10))
    except:
        print(i, "未找到")
        pass
    # driver.find_element(By.XPATH, '//*[@data-testid="link-homepage"]').click()
    time.sleep(random.randint(5, 8))
