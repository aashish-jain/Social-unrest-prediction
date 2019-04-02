#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import date, timedelta, datetime
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
from newspaper import Article
from multiprocessing import Pool, cpu_count
from tqdm import tqdm_notebook as tqdm
import pickle
import pandas as pd
import time


# In[ ]:


startDate = date(2016, 1, 1)
endDate = date(2016, 12, 31)
# endDate = datetime.now().date() + timedelta(days=1)
offset = 36892
newsStartDate = date(2001, 1, 1)


# In[ ]:


def generateLinkForDate(dateGiven):
    def startTime(x): return (x - newsStartDate).days + offset
    stringDate = str(dateGiven).replace('-', '/')
    return "https://timesofindia.indiatimes.com/%s/archivelist/year-%d,month-%d,starttime-%d.cms" % (stringDate, dateGiven.year, dateGiven.month,  startTime(dateGiven))


# In[ ]:


'''
    Returns the links that have the given queryWords in
    their headlines be used for scrapping
'''
def fetchRelevantNewsLinks(tagSet, queryWords):
    links = []
    for tag in tagSet:
        occurs = False
        headline = tag.text
        link = tag.get('href')
        
        if headline == None or link == None:
            continue
        headlineLower = headline.lower()
        for query in queryWords:
            if query in headline:
                occurs = True
                break

        if occurs:
            # Fix for links that don't start with http
            if not link.startswith("http"):
                link = "http://timesofindia.indiatimes.com/" + link
            links.append(link)
    return links


# In[ ]:


def getArticle(url, beginsWithLocation = True):
    try:
        article = Article(url)
        article.download()
        article.parse()
        #Return the location too
        if beginsWithLocation:
            location = article.text.find(':')
            if 0 < location < 26:
                location = article.text[:location].strip()
                text = article.text.strip()
                return article.title, article.text, location
            else:
                return None
        return article.title, article.text
    except:
        return None


# In[ ]:


queryWords = 'protest, riot, violence, violent, unrest, clash, bandh, rally, election, rule ,law, policy, demonstration, congress, INC, BJP, guv ,govt, government, political, politics, party, PM, CM, minister, polls'
queryWords = [word.strip().lower() for word in queryWords.split(',')]


# In[ ]:


# currDate = startDate
# newsLinks = {}
# while currDate != endDate:
#     print(currDate, end=' ')
#     link = generateLinkForDate(currDate)
#     request = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
#     soup = BeautifulSoup(request.text, 'lxml')
#     tagSet = soup.find_all('a')
#     foundLinks = fetchRelevantNewsLinks(tagSet, queryWords)
#     print(len(foundLinks))
#     newsLinks[str(currDate)] = foundLinks
#     currDate += timedelta(days=1)


# In[ ]:


# len(newsLinks.keys())


# In[ ]:


newsLinks = pickle.load(open('TOI-dump.pkl', 'rb'))


# In[ ]:





# In[ ]:


df = None
total_skipped = 0
for key in newsLinks.keys():
    full_news = []
    param = newsLinks[key]
    print(key ,end = " ")
    skipped = 0
    for i, p in enumerate(tqdm(param)):
        scraped = getArticle(p)
        if scraped==None or 'Download' in scraped[1]:
            skipped += 1
        else:
            full_news.append(scraped)

    print('Skipped %d articles' % skipped)
    total_skipped += skipped
    df = pd.DataFrame(data=full_news, columns=['title', 'text', 'location'])
    df.to_csv('TOI/%s.csv' % key)
print(total_skipped)


# In[ ]:




