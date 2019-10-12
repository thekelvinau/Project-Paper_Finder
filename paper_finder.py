# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:23:27 2019

@author: Kelvin
"""

#https://docs.python.org/3.7/howto/urllib2.html
import urllib.request
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup

with urllib.request.urlopen('https://ui.adsabs.harvard.edu/search/q=hello%20world&sort=date%20desc%2C%20bibcode%20desc&p_=0') as response:
   html_doc = response.read()
#   print(html_doc)
   

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
