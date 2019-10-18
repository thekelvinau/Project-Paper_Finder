# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:23:27 2019

@author: Kelvin
"""
##https://gazpacho.xyz
#from gazpacho import get,Soup
#
#url = 'https://ui.adsabs.harvard.edu/search/q=hello%20world&sort=date%20desc%2C%20bibcode%20desc&p_=0'
#html = get(url)
##print(html)
#
#soup = Soup(html)
#str(soup)
##print(soup.prettify())
#
## Original HTML: <span class="mw-headline" id="Ingredients_and_preparation">Ingredients and preparation</span>
###results = soup.find('span', {'class': 'mw-headline'})
#results = soup.find('div', {'class': 'hidden-xs hidden-sm col-md-3 s-top-row-col identifier s-identifier'})
#print(results)
##results = soup.find('h3', {'class': 's-results-title'})

#<div class="hidden-xs hidden-sm col-md-3 s-top-row-col identifier s-identifier">
#<h3 class="s-results-title">Stain/Arcp-Py: Arcp 0.2.0</h3>


##https://docs.python.org/3.7/howto/urllib2.html
#import urllib.request
##https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#from bs4 import BeautifulSoup
#
#with urllib.request.urlopen('https://ui.adsabs.harvard.edu/search/q=hello%20world&sort=date%20desc%2C%20bibcode%20desc&p_=0') as response:
#   html_doc = response.read()
#   print(html_doc)
#   
##with urllib.request.urlopen('https://ui.adsabs.harvard.edu/') as response:
##   html_doc = response.read()
###   print(html_doc)
#   
#
#soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.prettify())


#import requests
##response = requests.get('http://hiscore.runescape.com/index_lite.ws?player=zezima')
##print (response.status_code)
##print (response.content)


#import requests
##search_term = what_are_you_searching_for()
#search_term = 'pewdiepie'
##search_url = "https://www.youtube.com/results?search_query=" + search_term
#search_url = 'https://ui.adsabs.harvard.edu/search/q=hello%20world&sort=date%20desc%2C%20bibcode%20desc&p_=0'
#r=requests.get(search_url)
#print (r.status_code)
#print (r.content)



###https://docs.python-guide.org/scenarios/scrape/
##from lxml import html
##import requests
##
##page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
##tree = html.fromstring(page.content)
##
##These are the two elements of interest
##<div title="buyer-name">Carson Busses</div>
##<span class="item-price">$29.95</span>
###This will create a list of buyers:
##buyers = tree.xpath('//div[@title="buyer-name"]/text()')
###This will create a list of prices
##prices = tree.xpath('//span[@class="item-price"]/text()')
##
###print 'Buyers: ', buyers
###print 'Prices: ', prices
##
##print(buyers)
##print(prices)
#
#from lxml import html
#import requests
#
#page = requests.get('https://ui.adsabs.harvard.edu/search/q=hello%20world&sort=date%20desc%2C%20bibcode%20desc&p_=0')
#tree = html.fromstring(page.content)
#print(tree)
#
##This will create a list of buyers:
#buyers = tree.xpath('//h3[@class="s-results-title"]/text()')
###This will create a list of prices
##prices = tree.xpath('//span[@class="item-price"]/text()')
#
##/html/body/div[3]/div/div/div[3]/div/div/div/div[4]/div/div/div/div[2]/div/div[1]/div/div/div[2]/ul/li[1]/div/div[2]/div/a
##//*[@id="main-content"]/div[1]/div/div/div[2]/ul/li[1]/div/div[2]/div/a
##//*[@id="main-content"]/div[1]/div/div/div[2]/ul/li[2]/div/div[2]/div
##<div class="col-xs-10 col-xs-offset-1">
##            <a href="#abs/2019arXiv190705457B/abstract" class="abs-redirect-link">
##                <h3 class="s-results-title">Schatten Norms in Matrix Streams: Hello Sparsity, Goodbye Dimension</h3>
##            </a>
##    </div>
#
##print 'Buyers: ', buyers
##print 'Prices: ', prices
#
#print(buyers)
##print(prices)



### Import etree class from lxml
##
##from lxml import etree
##
### Example html content
##
##html = '''<div class="container"> 
##<p class="row"> 
##<a href="#123333" class="box"> I love xpath </a> 
##</p> 
##</div>'''
##
### Use etree to process html text and return an _Element object which is a dom object.
##dom = etree.HTML(html)
##
### Get a tag's text. Please Note: The _Element's xpath method always return a list of html nodes.Because there is only one a tag's text, so we can do like below.
##a_tag_text = dom.xpath('//div/p/a/text()')
##
##print(a_tag_text)
##
### Import etree class from lxml
#
#from lxml import etree
#
## Example html content
#
#html = '''<div class="container"> 
#<p class="row"> 
#<a href="#123333" class="box"> I love xpath </a> 
#</p> 
#</div>'''
#
## Use etree to process html text and return an _Element object which is a dom object.
#dom = etree.HTML(html)
#
## Get a tag's text. Please Note: The _Element's xpath method always return a list of html nodes.Because there is only one a tag's text, so we can do like below.
#a_tag_text = dom.xpath('//div/p/a/text()')
#
#print(a_tag_text)


##https://docs.python.org/3.4/library/xml.etree.elementtree.html
#https://pybit.es/download-xml-file.html
#import requests
#
#URL = "http://insert.your/feed/here.xml"
#
#response = requests.get(URL)
#with open('feed.xml', 'wb') as file:
#    file.write(response.content)



###https://stackoverflow.com/questions/3075550/how-can-i-get-href-links-from-html-using-python
##from BeautifulSoup import BeautifulSoup
##import urllib2
##import re
##
##html_page = urllib2.urlopen("http://www.yourwebsite.com")
##soup = BeautifulSoup(html_page)
##for link in soup.findAll('a'):
##    print(link.get('href'))
#
#from bs4 import BeautifulSoup
#import urllib2
#import re
#
#html_page = urllib2.urlopen("http://www.yourwebsite.com")
#soup = BeautifulSoup(html_page)
#for link in soup.findAll('a'):
#    print(link.get('href'))
    



###https://stackoverflow.com/questions/3075550/how-can-i-get-href-links-from-html-using-python
##from bs4 import BeautifulSoup, SoupStrainer
##import requests
##
##url = "https://ui.adsabs.harvard.edu/search/p_=0&q=hello%20world&sort=date%20desc%2C%20bibcode%20desc"
##
##page = requests.get(url)    
##data = page.text
##soup = BeautifulSoup(data)
##
##for link in soup.find_all('a'):
##    print(link.get('href'))
#    
#from bs4 import BeautifulSoup, SoupStrainer
#import requests
#
#url = "https://ui.adsabs.harvard.edu/search/p_=0&q=hello%20world&sort=date%20desc%2C%20bibcode%20desc"
#
#page = requests.get(url)    
#data = page.text
#print(data)
#soup = BeautifulSoup(data, features = "lxml")
#
#for link in soup.find_all('a'):
#    print(link.get('href'))
    

#https://stackoverflow.com/questions/34759787/fetch-all-href-link-using-selenium-in-python
#https://www.programcreek.com/python/example/88681/selenium.webdriver.support.expected_conditions.presence_of_element_located
#https://selenium-python.readthedocs.io/waits.html
#https://www.seleniumhq.org/docs/04_webdriver_advanced.jsp
#https://stackoverflow.com/questions/29858752/error-message-chromedriver-executable-needs-to-be-available-in-the-path
##https://enginebai.com/2017/04/12/advanced-web-scraping-in-python/
#from selenium import webdriver
#from bs4 import BeautifulSoup
#
#url = "https://medium.com/dualcores-studio/make-an-android-custom-view-publish-and-open-source-99a3d86df228"	
#driver = webdriver.Chrome(executable_path="./driver/chromedriver")
#driver.get(url)
#content_element = driver.find_element_by_class_name("postArticle-content")
#content_html = content_element.get_attribute("innerHTML")	
#soup = BeautifulSoup(content_html, "html.parser")
#p_tags = soup.find_all("p")
#for p in p_tags:	   
#    print(p.prettify())
#driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

#url = "https://medium.com/dualcores-studio/make-an-android-custom-view-publish-and-open-source-99a3d86df228"	
url = "https://ui.adsabs.harvard.edu/search/p_=0&q=hello%20world&sort=date%20desc%2C%20bibcode%20desc"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
#elems = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "main-content")))
elems = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[1]/div/div/div[2]/ul/li[1]/div/div[2]/div/a')))
elems = driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[3]/div/div/div/div[4]/div/div/div/div[2]/div/div[1]/div/div/div[2]/ul/li[1]/div/div[2]/div/a[@href]')
#elems = driver.find_element_by_partial_link_text('https://ui.adsabs.harvard.edu/#abs/')
for elem in elems:
    print(elem.get_attribute("href"))
driver.close()
##elems = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID, "0846 [href]")))
##links = [elem.get_attribute('href') for elem in elems]
#content_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "0846")))
##print(content_element)
###try:
####    content_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[1]/div/div/div[2]/ul/li[1]/div/div[2]/div/a')))
###    content_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "0846")))
###    print(content_element)
###finally:
###    driver.quit()
####content_element = driver.find_element_by_class_name("0846")
#content_html = content_element.get_attribute("innerHTML")
##print(content_html)	
#
#soup = BeautifulSoup(content_html, "html.parser")
#a_tags = soup.find_all("a")
#for a in a_tags:	   
#    print(a.prettify())
#driver.close()
#print(a)




#https://github.com/urllib3/urllib3/issues/869
##import ssl, urllib3
##r = urllib3.PoolManager().connection_from_url('http://en.wikipedia.org/wiki/Main_Page').request('GET', 'http://en.wikipedia.org/wiki/Main_Page', assert_same_host=False)
##print(r.status)
#
#import ssl, urllib3
#r = urllib3.PoolManager(maxsize=10, block=False).connection_from_url('http://en.wikipedia.org/wiki/Main_Page').request('GET', 'http://en.wikipedia.org/wiki/Main_Page', assert_same_host=False)
#print(r.status)