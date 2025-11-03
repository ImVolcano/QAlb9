from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

o = Options()
o.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=o)

driver.get('http://localhost:5173')

username = driver.find_element(By.ID, 'emailInput')
password = driver.find_element(By.ID, 'passwordInput')
submit = driver.find_element(By.XPATH, '//button[@type="submit"]')

username.send_keys('max@mail.ru')
password.send_keys('123456')
submit.click()

while True:
    if EC.alert_is_present()(driver):
        alert = driver.switch_to.alert
        print(alert.text)

        break