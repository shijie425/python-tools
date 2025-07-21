from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random

s = Service(r"chromedriver.exe")
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:5001")
driver = webdriver.Chrome(service=s, options=options)

all_web = ['best-games.top','h5gogo.top','h5-online.top','justh5.top','gamegood.top','game-start.top']
for i in all_web:
    driver.find_element(By.XPATH,'//span[contains(text(),"添加站点")]').click()
    time.sleep(random.randint(5, 8))
    driver.find_element(By.XPATH,'//*[@name="zoneName"]').send_keys(i)
    time.sleep(random.randint(2, 3))
    driver.find_element(By.XPATH,'//*[@data-testid="control-button"]/span').click()
    time.sleep(random.randint(8, 12))
    driver.find_element(By.XPATH,'//*[@data-testid="plan-card-free"]').click()
    time.sleep(random.randint(3, 5))
    driver.find_element(By.XPATH,'//*[@data-testid="control-button"]').click()
    time.sleep(random.randint(10, 15))
    while True:
        try:
            driver.find_element(By.XPATH,'//span[contains(text(),"添加记录")]').click()
            break
        except:
            time.sleep(5)
    time.sleep(random.randint(3, 5))
    driver.find_element(By.XPATH,'//*[@name="name"]').send_keys('@')
    time.sleep(random.randint(3, 5))
    driver.find_element(By.XPATH,'//*[@name="ipv4_address"]').send_keys('45.79.75.83')
    time.sleep(random.randint(3, 5))
    driver.find_element(By.XPATH,'//*[@data-testid="dns-record-form-save-button"]').click()
    time.sleep(random.randint(5, 8))
    driver.find_element(By.XPATH, '//span[contains(text(),"添加记录")]').click()
    time.sleep(random.randint(3, 4))
    driver.find_element(By.XPATH, '//*[@name="name"]').send_keys('images')
    time.sleep(random.randint(3, 4))
    driver.find_element(By.XPATH, '//*[@name="ipv4_address"]').send_keys('45.79.75.83')
    time.sleep(random.randint(3, 4))
    driver.find_element(By.XPATH, '//*[@data-testid="dns-record-form-save-button"]').click()
    time.sleep(random.randint(5, 8))
    driver.find_element(By.XPATH,'//span[contains(text(),"继续")]').click()
    time.sleep(random.randint(5, 8))
    try:
        driver.find_element(By.XPATH,'//*[contains(text(),"完成，检查名称服务器")]').click()
        time.sleep(random.randint(5, 8))
    except:
        pass
    try:
        driver.find_element(By.XPATH, '//span[contains(text(),"立即检查名称服务器")]').click()
        time.sleep(random.randint(5, 8))
    except:
        pass
    try:
        driver.find_element(By.XPATH, '//span[contains(text(),"继续")]').click()
        time.sleep(random.randint(5, 8))
    except:
        pass
    time.sleep(random.randint(5, 8))
    driver.find_element(By.XPATH,'//span[contains(text(),"开始使用")]').click()
    time.sleep(random.randint(3, 5))
    driver.find_element(By.XPATH,'//span[contains(text(),"保存")]').click()
    time.sleep(random.randint(3, 5))
    driver.find_element(By.XPATH,'//span[contains(text(),"保存")]').click()
    time.sleep(random.randint(3, 5))
    driver.find_element(By.XPATH,'//span[contains(text(),"保存")]').click()
    time.sleep(random.randint(3, 5))
    driver.find_element(By.XPATH,'//span[contains(text(),"完成")]').click()
    time.sleep(random.randint(3, 5))
    driver.find_element(By.XPATH,'//*[@aria-label="返回"]').click()
    time.sleep(random.randint(10, 15))
    print(i)
# print(driver.title)