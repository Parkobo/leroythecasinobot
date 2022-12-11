import time
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def server_restart():
    print('Restarting the server via website')
    chrome_options = Options()

    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")

    server_website = config('server_website', default='')
    file_driver_path = config('file_path_driver', default='')
    email_username = config('broccoli_email', default='')
    broc_password = config('broccoli_password', default='')

    s = Service(file_driver_path)
    web_form = webdriver.Chrome(service=s, options=chrome_options)
    web_form.get(server_website)
    web_form.maximize_window()

    time.sleep(1)
    web_form.find_element(by=By.XPATH, value='/html/body/div/div[1]/div/div/nav/a[2]').click()
    time.sleep(1)
    web_form.find_element(by=By.XPATH, value='/html/body/div/div/form/div[1]/div[1]/input').send_keys(email_username)
    web_form.find_element(by=By.XPATH, value='/html/body/div/div/form/div[1]/div[2]/input').send_keys(broc_password)
    web_form.find_element(by=By.XPATH, value='/html/body/div/div/form/div[3]/button').click()
    web_form.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/main/div/div/nav/div[2]/div[2]/form/input[4]').click()
    print('Server restarted successfully!')
    web_form.quit()