from selenium import webdriver
from bs4 import BeautifulSoup


class DVDscraper(object):
    def __init__(self):
        browser = webdriver.PhantomJS('./phantomjs/bin/phantomjs')
        browser.set_window_size(1024, 768)
        browser.get('http://www.dvdsreleasedates.com')
        browser.implicitly_wait(1)
        self.content = browser.page_source
        browser.quit()

    def page_scrape(self):
        if self.content is not None:
            soup = BeautifulSoup(self.content, 'html.parser')
            if soup is not None:
                tables = soup.find_all('table', {'class': 'fieldtable-inner'})
                if tables is not None:
                    try:
                        for table in tables:
                            try:
                                print table.tr.td
                            except AttributeError:
                                print '<table><tr><td> Tag not found'
                    except TypeError:
                        print "err: <tables> object not iterable"

if __name__ == '__main__':
    scraper = DVDscraper()
    scraper.page_scrape()