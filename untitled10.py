# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:02:54 2019

@author: xxx
"""

from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.rottentomatoes.com/tv/travelers/s01/reviews/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html5lib")


Allcomments = soup.findAll("div", class_ = "the_review")
Allcommenters = soup.findAll("a", class_ = "unstyled bold articleLink")

CCP = []
CMP = []

for comment in Allcomments:
        CC = comment.get_text(strip=True)
        CCP.append(CC)
        
for commenter in Allcommenters:
        CM = commenter.get_text(strip=True)
        CMP.append(CM)

dict1= dict(zip(CCP,CMP))

print(dict1)


keys = dict1.keys()
with open('mycsvfile.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, keys)
    w.writeheader()
    w.writerow(dict1)
