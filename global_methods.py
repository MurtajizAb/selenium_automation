from selenium import webdriver
from selenium.webdriver.support.ui import Select


def print_success(status=True, e=None):
    if status:
        print('✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓')
    else:
        print("Exepection body")
        print(e)
        print("Expeption body ending" + "   " + "Failed******************************************************")


def click_by_id(driver, id):
    try:
        driver.find_element_by_id(id).click()
        print_success(True)
        return driver
    except Exception as e:
        print_success(False, e)
        print("Something went wrong with the" + " " + str(id))
        return driver


def click_by_name(driver, name):
    try:
        driver.find_element_by_name(name).click()
        print_success(True)
        return driver
    except Exception as e:
        print_success(False, e)
        print("Something went wrong with the" + " " + str(id))
        return driver


def click_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath).click()
        print_success(True)
        return driver
    except Exception as e:
        print_success(False, e)
        print("Something went wrong with the" + " " + str(id))
        return driver


def send_keys_by_name(driver, name, key="test"):
    try:
        driver.find_element_by_name(name).send_keys(key)
        print_success(True)
        return driver
    except Exception as e:
        print_success(False, e)
        print("Something went wrong with the" + " " + str(id))
        return driver



def click_by_link_text(driver, text):
    try:
        driver.find_element_by_partial_link_text(text).click()
        print_success(True)
        return driver
    except Exception as e:
        print_success(False, e)
        print("Something went wrong with the" + " " + str(id))
        return driver
    finally:
        return driver


def click_by_selector(selector):
    pass


def select_dropdown_by_visibletext(driver, id, visible_text):
    try:
        select = Select(driver.find_element_by_id(id))
        select.select_by_visible_text(visible_text)
        print_success(True)
        return driver
    except Exception as e:
        print_success(False, e)
        print("Something went wrong with the" + " " + str(id))
        return driver


def select_dropdown_by_index(driver, id, index):
    try:
        select = Select(driver.find_element_by_id(id))
        select.select_by_value(index)
        print_success(True)
        return driver
    except Exception as e:
        print_success(False, e)
        print("Something went wrong with the" + " " + str(id))
        return driverddd
