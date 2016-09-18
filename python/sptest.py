from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.title
    except AttributeError as e:
        return None
    return title
# title = getTitle("http://www.baidu.com")
# if title == None :
#     print("not found")
# else:
#     print(title)

import re
html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for img in images:
    print(img["src"])
