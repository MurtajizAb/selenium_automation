import pyautogui
import sign_in
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pdb
# url='http://stagingapp.prowireonline.com/buyer/services/view?searchText=all'
# driver= init_chrome.start()
# driver.get(url)
def do_seller_sign_up():
    driver = sign_in.login("mahirakhan@gmail.com", "Arsal@123#")
    print("I am at line 9 of sign up selelr")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-service/div/div/div[2]/button"))
    )
    element.click()
    # driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[2]/li').click()
    # driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[2]/li/div/a[3]').click()
    # driver.find_element_by_tag('button').click()




do_seller_sign_up()
# sign_in.click_by_id('')
# driver.find_element_by_xpath(driver,'//*[@id="navbarSupportedContent"]/ul[2]/li')
# pyautogui.press('enter')
# sign_in.click_by_xpath(driver,
#                        '//*[@id="navbarSupportedContent"]/ul[2]/li/div/a[3]')