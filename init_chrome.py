from sys import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from sys import platform
from selenium.webdriver.common.keys import Keys
import pdb
#*def max_window():

 #   driver = webdriver.chrome(executable_path='C:\Downloads\chromedriver.exe')
  #  driver.max_window()
# driver.get('https://www.webassign.net/question_assets/unccolphysmechl1/measurements/manual.html')
#def start():
   # driver = webdriver.Chrome(executable_path='chromedriver.exe')
   # driver.get("https://prowireonline.com/")
    # driver.get('https://www.webassign.net/question_assets/unccolphysmechl1/measurements/manual.html')

#start()


def start():
    if platform=="linux":
        driver = webdriver.Chrome(executable_path='drivers/linux/chromedriver')
    else:
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.maximize_window()

    return driver




# driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/form/a[1]').click()
# driver.
if __name__ == '__main__':
    start()