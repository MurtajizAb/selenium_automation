import keyboard

import init_chrome
url= "http://stagingapp.prowireonline.com/home"

def click_by_xpath(driver,x_path):
    driver.find_element_by_xpath(x_path).click()
    return driver

def click_by_name(driver,name):
    driver.find_element_by_name(name).click()
    return driver


def click_by_class(driver,clas):
    driver.find_element_by_class(clas).click()
    return driver


def click_by_id():
    driver.find_element_by_id(id).click()
    return driver

def send_keys_ny_id(driver,id,text) -> object:
    driver.find_element_by_id(id).send_keys(text)
    return driver

def send_keys_ny_name(driver,id,text):
    driver.find_element_by_name(id).send_keys(text)
    return driver


def click_element_by_css(driver,sele):
    driver.find_element_by_css(sele).click()
    return driver

def send_keys_by_link_text(driver,link_text,text):
    driver.find_element_by_link_text(link_text).send_keys(text)





def login(email,password):
    driver = init_chrome.start()
    driver.get(url)
    driver = click_by_xpath(driver, '//*[@id="navbarSupportedContent"]/form/a[1]')
    # driver = send_keys_ny_id(driver, 'email', 'absdf')
    driver = send_keys_ny_name(driver, 'email', email)
    driver = send_keys_ny_name(driver, 'password', password)
    driver.find_element_by_xpath('//button[@name="continue"]').click()
    driver.find_element_by_xpath('//button[@size="normal"]').click()
    return driver




    # print('i am here')
    # keyboard.press('tab')
    # keyboard.press("enter")
if __name__ == '__main__':
    email = "arsal.azeem@vizteck.com"
    password = "Arsal@123#"
    login(email,password)





# keyboard.press()
