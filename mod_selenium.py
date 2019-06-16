from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/local/bin/chromedriver')


def navigate_to_page(url):
    driver.get(url)


def wait_until_visible(xpath):
    driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(
                              EC.element_to_be_clickable((By.XPATH, xpath))))


def find_element(xpath):
    return driver.find_element_by_xpath(xpath)


def navigate_to_the_next_page(counter):
    driver.find_element_by_xpath("//li[@class='arrow__right']/a").click()
    print("Navigating to Page {}".format(counter + 1))
    return counter + 1


def quit_selenium_driver():
    driver.quit()