import pyttsx3
import requests
import os
from selenium import webdriver

engine = pyttsx3.init()
engine.setProperty('rate', 140)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

response = requests.get(f"https://newsapi.org/v2/everything?q=covid&apiKey={os.environ['API_KEY']}")
articles = response.json()['articles'][:9]

CHROMEDRIVER = os.environ['CHROME_DRIVER']

urls = []

for article in articles:
    engine.say(f'The following article is from {article["source"]["name"]} and its title is')
    engine.say(f'{article["title"]}')
    engine.say(f'Here is a preview: {article["description"]}')
    engine.say('Enter 1 to save the article. Any other key to continue')
    engine.runAndWait()
    save = input("")
    if save == "1":
        engine.say('Article saved.')
        urls.append(article['url'])
    else:
        continue

driver = webdriver.Chrome(CHROMEDRIVER)
for url in urls:
    driver.execute_script(f"window.open('{url}');")
