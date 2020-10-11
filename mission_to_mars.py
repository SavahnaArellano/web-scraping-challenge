#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymongo
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd


# In[2]:


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# In[3]:


news_url = 'https://mars.nasa.gov/news/'


# In[4]:


response = requests.get(news_url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[5]:


print(soup.prettify())


# In[10]:


news_title = soup.find('div', class_ ="content_title").text
print(news_title)


# In[11]:


news_p = soup.find('div', class_ ="rollover_description_inner").text
print(news_p)


# In[12]:


news_title = news_title.strip()
news_p = news_p.strip()


# In[13]:


image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


# In[14]:


response2 = requests.get(image_url)
soup2 = BeautifulSoup(response2.text, 'html.parser')


# In[15]:


print(soup2.prettify())


# In[17]:


img_url = 'https://www.jpl.nasa.gov'
img_url += soup2.article['style'][23:-3]
print(img_url)


# In[21]:


mars_facts = pd.read_html('https://space-facts.com/mars/')
mars_facts = mars_facts[0].to_html()
print(mars_facts)


# In[22]:


hemisphere_image_urls = [
    {'title':'Cerberus Hemisphere Enhanced','img_url':'https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'},
    {'title':'Schiaparelli Hemisphere Enhanced','img_url':'https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'},
    {'title':'Syrtis Major Hemisphere Enhanced','img_url':'https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'},
    {'title':'Valles Marineris Hemisphere Enhanced','img_url':'https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'}   
    
]


# In[ ]:




