import time

from selenium import webdriver
from sys import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from sys import platform
from selenium.webdriver.support.ui import Select
from inspect import currentframe


def get_linenumber():
    cf = currentframe()
    return cf.f_back.f_lineno



wait = 40


def print_success(status=True, e=None):
    if status:
        print('✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓')
    else:
        print("Exepection body")
        print(e)
        print("Expeption body ending" + "   " + "Failed******************************************************")


def click_by_id(driver, id):
    try:
        element = WebDriverWait(driver, wait).until(
            EC.presence_of_element_located((By.ID, id))
        )
        driver.find_element_by_id(id).click()
        print_success(True)
        return driver
    except Exception as e:
        print(get_linenumber())
        print_success(False, e)
        print("Something went wrong with the" + " " + str(id))
        return driver


def click_by_name(driver, name):
    try:
        element = WebDriverWait(driver, wait).until(
            EC.presence_of_element_located((By.NAME, name))
        )
        driver.find_element_by_name(name).click()
        print_success(True)
        return driver
    except Exception as e:
        print(get_linenumber())
        print_success(False, e)
        print("Something went wrong with the" + " " + str(id))
        return driver



def click_by_xpath(driver, xpath):
    try:
        time.sleep(1)
        element = WebDriverWait(driver, wait).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        driver.find_element_by_xpath(xpath).click()
        print_success(True)
        return driver
    except Exception as e:
        print(get_linenumber())
        print_success(False, e)
        print("Something went wrong with the" + " " + str(id))
        return driver


def send_keys_by_name(driver, name, key="test"):
    try:
        element = WebDriverWait(driver, wait).until(
            EC.presence_of_element_located((By.NAME, name))
        )
        driver.find_element_by_name(name).send_keys(key)
        print_success(True)
        return driver
    except Exception as e:
        print(get_linenumber())
        print_success(False, e)
        print("Something went wrong with the" + " " + str(id))
        return driver


def click_by_link_text(driver, text):
    try:
        element = WebDriverWait(driver, wait).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, text))
        )
        driver.find_element_by_partial_link_text(text).click()
        print_success(True)
        return driver
    except Exception as e:
        print(get_linenumber())
        print_success(False, e)
        print("Something went wrong with the" + " " + str(id))
        return driver
    finally:
        return driver


def click_by_selector(selector):
    pass


def select_dropdown_by_visibletext(driver, id, visible_text):
    try:
        element = WebDriverWait(driver, wait).until(
            EC.presence_of_element_located((By.ID, id))
        )
        select = Select(driver.find_element_by_id(id))
        select.select_by_visible_text(visible_text)
        print_success(True)
        return driver
    except Exception as e:
        print(get_linenumber())
        print_success(False, e)
        print("Something went wrong with the" + " " + str(id))
        return driver

def select_dropdown_by_visibletext_xpath(driver, xpath, visible_text):
    try:
        element = WebDriverWait(driver, wait).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        # select = Select(driver.find_element_by_xpath(xpath))
        element.select_by_visible_text(visible_text)
        print_success(True)
        return driver
    except Exception as e:
        print(get_linenumber())
        print_success(False, e)
        print("Something went wrong with the" + " " + str(id))
        return driver

def select_dropdown_by_index(driver, id, index):
    try:
        element = WebDriverWait(driver, wait).until(
            EC.presence_of_element_located((By.ID, id))
        )
        select = Select(driver.find_element_by_id(id))
        select.select_by_value(index)
        print_success(True)
        return driver
    except Exception as e:
        print(get_linenumber())
        print_success(False, e)
        print("Something went wrong with the" + " " + str(id))
        return driverddd


def send_keys_by_xpath(driver, xpath,text):
    try:
        time.sleep(1)
        element = WebDriverWait(driver, wait).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        driver.find_element_by_xpath(xpath).send_keys(text)
        print_success(True)
        return driver
    except Exception as e:
        print(get_linenumber())
        print_success(False, e)
        print("Something went wrong with the" + " " + str(id))
        return driver