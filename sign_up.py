import time
from select import select

import pyautogui

import keyboard
from selenium.webdriver.support.select import Select

import init_chrome
import sign_in
import requests
import pdb
from selenium.webdriver import ActionChains
try:
    url = "http://stagingapp.prowireonline.com/home"
    driver = init_chrome.start()

    emailtemp = "xyz12321332@gmail.com"
    driver.get(url)
    driver.find_element_by_link_text("Sign Up").click()
    sign_in.send_keys_ny_id(driver, 'email', emailtemp)
    print(emailtemp)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(1)
    payload = {
        "email": emailtemp
    }
    response = requests.post("http://65.2.106.231:3000/api/v1/en/users/email-availability", data=payload)
    driver.find_element_by_id("code").send_keys(response.json()["data"]["code"])
    # driver.find_element_by_name()
    time.sleep(3)
    sign_in.send_keys_ny_id(driver, 'firstName', 'murtajiz')
    sign_in.send_keys_ny_id(driver, 'lastName', 'Abbas')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('down', presses=6)
    pyautogui.press('enter')
    driver.find_element_by_name("phoneNumber").send_keys(23123234887)
    sign_in.send_keys_ny_id(driver, 'password', 'HELLOworld12@')
    sign_in.send_keys_ny_id(driver, 'confirmPassword', 'HELLOworld12@')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('down', presses=6)
    pyautogui.press('enter')
    driver.find_element_by_xpath(
        '/html/body/app-root/app-personal-info/div/div/div[2]/div/div/div/form/div[7]/label/span').click()
    pyautogui.hotkey('shift', 'tab', presses=2)
    pyautogui.press('enter')
    pyautogui.press('tab', presses=2)
    pyautogui.press('enter')
    pdb.set_trace()
except Exception as e:
    print(e)
    driver.quit()











