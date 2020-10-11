
import pymongo
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd


conn = 'mongodb://localhost:27017/mars'
client = pymongo.MongoClient(conn)

def scrape():

    mars_info = {}

    news_url = 'https://mars.nasa.gov/news/'

    response = requests.get(news_url)
    soup = BeautifulSoup(response.text, 'html.parser')


    #print(soup.prettify())


    news_title = soup.find('div', class_ ="content_title").text
    


    news_p = soup.find('div', class_ ="rollover_description_inner").text
    


    news_title = news_title.strip()
    news_p = news_p.strip()

    mars_info['news_title'] = news_title
    mars_info['news_p'] = news_p


    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


    response2 = requests.get(image_url)
    soup2 = BeautifulSoup(response2.text, 'html.parser')



    img_url = 'https://www.jpl.nasa.gov'
    img_url += soup2.article['style'][23:-3]
    
    mars_info['img_url'] = img_url


    mars_facts = pd.read_html('https://space-facts.com/mars/')
    mars_facts = mars_facts[0].to_html()
    mars_info['mars_facts'] = mars_facts


    hemisphere_image_urls = [
      {'title':'Cerberus Hemisphere Enhanced','img_url':'https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'},
      {'title':'Schiaparelli Hemisphere Enhanced','img_url':'https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'},
      {'title':'Syrtis Major Hemisphere Enhanced','img_url':'https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'},
      {'title':'Valles Marineris Hemisphere Enhanced','img_url':'https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'}   

    ]

    mars_info['hemisphere_image_urls'] = hemisphere_image_urls

    return mars_info

