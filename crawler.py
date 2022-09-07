import seaborn as sns
import matplotlib.pyplot as plt
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from collections import Counter
import re
import os

data = {}
url_queue = ["https://www.python.org/"]
pages = 0
total_words = 0
total_pages_found = 0

while len(url_queue) > 0 and pages < 20:
    try:
        html = urllib.request.urlopen(url_queue.pop(0)).read()
    except:
        continue
    soup = BeautifulSoup(html,"html.parser",from_encoding="iso-8859-1")
    words = re.sub(r'[^a-zA-Z0-9_\']+', ' ', soup.get_text().lower()).split(" ")
    
    for word in words:
        total_words += 1
        if word not in data:
            data[word] = 1
        else:
            data[word] += 1

    for link in soup.find_all('a'):
        try:
            if re.match("^http", link.get('href')) != None:
                total_pages_found += 1
                url_queue.append(link.get('href'))
        except:
            continue
    
    os.system('cls||clear')
    print(f'Words found: {"{:,}".format(total_words)}{chr(10)}Pages found: {"{:,}".format(total_pages_found)}')
    
    pages += 1

top = dict(Counter(data).most_common(15))
words = list(top.keys())
vals = [top[word] for word in words]
sns.barplot(x=words, y=vals)

plt.show()
