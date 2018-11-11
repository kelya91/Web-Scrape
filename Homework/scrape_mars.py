from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

    
def scrape_mars_news():
    
    mars_info ={}
    

        # Initialize browser 
    browser = init_browser()

        

        # Visit Nasa news url through splinter module
    url1 = 'https://mars.nasa.gov/news/'
    browser.visit(url1)
        #collect the latest News Title and Paragraph Text

    html = browser.html
    soup = BeautifulSoup(html, 'lxml')
    article = soup.find("div", class_="list_text")
    news_title = article.find("div", class_="content_title").text
    news_paragraph = article.find("div", class_="article_teaser_body").text

        # Dictionary entry from MARS NEWS
    mars_info['news_title'] = news_title
    mars_info['news_paragraph'] = news_paragraph

    #return mars_info


    #browser.quit()
        # IMAGE
#def scrape_mars_image():
 

        # Initialize browser 
    browser = init_browser()

        #browser.is_element_present_by_css("img.jpg", wait_time=1)

        # Visit Mars Space Images through splinter module
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    #Visit the url for JPL Featured Space Image
    browser.visit(url2)
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')
    browser.find_by_id('full_image').click()
    featured_image_url = browser.find_by_css('.fancybox-image').first['src']

    # Display full link to featured image
    featured_image_url 

    # Dictionary entry from FEATURED IMAGE
    mars_info['featured_image_url'] = featured_image_url 

    #return mars_info


    #browser.quit()
# Mars Weather 
#def scrape_mars_weather():

   

    # Initialize browser 
    browser = init_browser()


    # Visit Mars Weather Twitter through splinter module
    url3 = 'https://twitter.com/marswxreport?lang=en'
            #scrape the latest Mars weather tweet
    browser.visit(url3)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    weather_tweet=soup.find('p',class_='TweetTextSize').text
    weather_tweet=weather_tweet.replace("\n","")
    weather_tweet


    # Dictionary entry from WEATHER TWEET
    mars_info['weather_tweet'] = weather_tweet

   # return mars_info


   # browser.quit()
# Mars Facts
#def scrape_mars_facts():
    browser = init_browser()
    # Visit Mars facts url 
    url4 = 'http://space-facts.com/mars/'
    #scrape the table containing facts about the planet including Diameter, Mass, etc.
    mars_df=pd.read_html(url4)[0]
    mars_df.columns=["Mars","Data"]
    mars_df



    # Dictionary entry from MARS FACTS
    mars_info['mars_facts'] = mars_df

    #return mars_info

#def scrape_mars_hemispheres():
    browser = init_browser()

   # Visit the USGS Astrogeology site
    url5="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url5)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # Retreive all items that contain mars hemispheres information
    items = soup.find_all('div', class_='item')

    # Create empty list for hemisphere urls 
    hemisphere_image_urls = []


    # Loop through the items previously stored
    for x in items: 
        # Store title
        title = x.find('h3').text

        # Store link that leads to full image website
        img_url = x.find('a', class_='itemLink product-item')['href']


        # Append the retreived information into a list of dictionaries 
        hemisphere_image_urls.append({"title" : title, "img_url" :img_url})

        mars_info['hemispheres'] = hemisphere_image_urls


        # Return mars_data dictionary 

    return mars_info


    browser.quit()



