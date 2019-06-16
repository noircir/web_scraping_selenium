from mod_class_proxy import Proxy
from mod_class_proxy_list import ListOfProxies

from mod_selenium import *
from mod_string_manipulation import *
from selenium.common.exceptions import TimeoutException, WebDriverException


def do_scraping(num_pages_to_search):
    counter = 1
    proxy_list = ListOfProxies()

    while counter <= num_pages_to_search:
        try:
            wait_until_visible("//li[@class='arrow__right']/a")
            table = find_element("//table[@class='proxy__t']")

            for row in table.find_elements_by_xpath(".//tr"):
                line = [td.text.strip() for td in row.find_elements_by_xpath(".//td")]
                line = remove_special_char_and_compress(line)
                if line != '':
                    print(line)
                    record = Proxy(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3],
                                   line.split(',')[4], line.split(',')[5], line.split(',')[6])
                    proxy_list.add_proxy(record)

            counter = navigate_to_the_next_page(counter)

        except (TimeoutException, WebDriverException) as e:
            print("Last page reached")
            break

    quit_selenium_driver()
    return proxy_list

