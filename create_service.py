import sign_in
import global_methods as globals
from selenium.webdriver.common.keys import Keys
email = "arsal.azeem@vizteck.com"
password = "Arsal@123#"
driver=sign_in.login(email,password)
driver = globals.click_by_xpath(driver, '//button[@size="normal"]')
driver=globals.send_keys_by_xpath(driver,'//input[@id="ibm-label-0"]',"create service")
driver=globals.click_by_xpath(driver,'//button[@id="dropdown-0"]')
driver=driver.find_element_by_id("dsaf").send_keys(Keys.ENTER)