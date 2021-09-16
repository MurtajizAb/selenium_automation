# import time
# from select import select
#
# import pyautogui
#
# import keyboard
# from selenium.webdriver.support.select import Select
#
# import init_chrome
# import sign_in
# import requests
# import pdb
# from selenium.webdriver import ActionChains
# url="http://stagingapp.prowireonline.com/home"
#
#
# driver=init_chrome.start()
#
#
# emailtemp="xyz124@gmail.com"
# driver.get(url)
# driver.find_element_by_link_text("Sign Up").click()
# sign_in.send_keys_ny_id(driver,'email',emailtemp)
# print(emailtemp)
# pyautogui.press('tab')
# pyautogui.press('enter')
# time.sleep(20)
# # payload={
# #     "email":emailtemp
# # }
# # response = requests.post("http://65.2.106.231:3000/api/v1/en/users/email-availability",data=payload)
# # ver_code=response.json()["data"]["code"]
# # sign_in.send_keys_ny_id(driver,'code',ver_code)
# # keyboard.press('tab')
# # keyboard.press('enter')
# # print(ver_code)
# sign_in.send_keys_ny_id(driver,'firstName','murtajiz')
# sign_in.send_keys_ny_id(driver,'lastName','Abbas')
# pyautogui.press('tab')
# pyautogui.press('enter')
# pyautogui.press('down',presses=6)
# pyautogui.press('enter')
# # select = Select(driver.find_element_by_id('countryCode'))
# # select.select_by_index(6)
# # a = select(driver.find_element_by_name("countryCode"))
# driver.find_element_by_name("phoneNumber").send_keys(23123235)
# sign_in.send_keys_ny_id(driver,'password','HELLOworld12@')
# sign_in.send_keys_ny_id(driver,'confirmPassword','HELLOworld12@')
# pyautogui.press('tab')
# pyautogui.press('enter')
# pyautogui.press('down',presses=6)
# pyautogui.press('enter')
# driver.find_element_by_xpath('/html/body/app-root/app-personal-info/div/div/div[2]/div/div/div/form/div[7]/label/span').click()
# pyautogui.hotkey('shift','tab',presses=2)
# pyautogui.press('enter')
# pyautogui.press('tab',presses=2)
# pyautogui.press('enter')
# pdb.set_trace()
# # print('i am working')
# # pyautogui.press('tab')
# # print('still working')
# # sign_in.click_by_xpath(driver,'/html/body/app-root/app-personal-info/div/div/div[2]/div/div/div/form/div[6]/mat-form-field')
# # pyautogui.press('down', press=6)
# # pyautogui.press('enter')
# # s = select(driver.find_element_by_name ("country"))
# # s.select_by_visible_text ('Pakistan')
# # pyautogui.press('tab')
# # driver.find_element_by_name('termsAndConditions').click()
#
#
#
#
# #pdb.set_trace()
#
#
# # driver= send_keys_ny_id(driver,'email','xyz123@gmail.com')
# #keyboard.press('tab')
# #keyboard.press('enter')
# #driver.switch_to_frame(driver.find_elements_by_xpath('//*[@id="navbarSupportedContent"]/form/a[2]')).click()
#
# #driver.click_by_xpath(driver,'/html/body/app-root/app-home-page/app-header/div/nav/a/img' )
# #keyboard.press('tab')
# #keyboard.press('tab')
# #keyboard.press('tab')
#
# # signup= driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/form/a[2]')
# # actions = ActionChains(driver)
# # actions.move_to_element(signup)
# #keyboard.press('enter')
# # git commit -m "first commit"
# # git branch -M main
# # git remote add origin https://github.com/MurtajizAb/selenium_automation.git
# # git push -u origin main
#
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

    emailtemp = "xyz1098@gmail.com"
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
    driver.find_element_by_name("phoneNumber").send_keys(38600200887)
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
