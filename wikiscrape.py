import lxml.html as lh
from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.PhantomJS('./phantomjs/bin/phantomjs')
browser.set_window_size(1024, 768)
browser.get('http://www.dvdsreleasedates.com/')
content = browser.page_source
#print content
if content is not None:
    soup = BeautifulSoup(content, "html.parser")
    if soup is not None:
        dvds = soup.find_all('table', {'class': 'fieldtable-inner'})
        if dvds is not None:
            try:
                for dvd in dvds:
                    if dvd is not None:
                        if dvd.parent is not None:
                            if dvd.parent.parent is not None:
                                print dvd.parent.parent.tr.td
                                break
                            # if dvd.parent.tr is not None:
                            #     if dvd.parent.tr.td is not None:
                            #         print dvd.parent.tr.td
                    #print (dvd)
            except TypeError, e:
                print "err: something went wrong"

browser.quit()

