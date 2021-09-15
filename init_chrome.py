from selenium import webdriver

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
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.implicitly_wait(40)
    return driver

# driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/form/a[1]').click()
# driver.