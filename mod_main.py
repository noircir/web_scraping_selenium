from mod_sqlite import *
from mode_scrape import *
from mod_selenium import *

def main():
    num_pages_to_search = 2
    url = 'https://hidemyna.me/en/proxy-list/'
    db = "proxy001.dbf"

    create_table(db)
    navigate_to_page(url)
    proxy_list = do_scraping(num_pages_to_search)
    insert_into_table(db, proxy_list)


if __name__ == '__main__':
    main()

