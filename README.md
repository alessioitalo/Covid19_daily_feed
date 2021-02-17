# Covid19 Daily Feed

This Python script iterates trough the top 10 covid-related articles of the day, collected trough an API call to NEWSAPI. 

A short description of each article is read out loud using the text-to-speech conversion library pyttsx3. After each article iteration, the user can decide to save an article to be read later.

Once all 10 articles have been read, the saved ones are automatically opened in a new Chrome tab launched via Selenium.

You will need:
* an authentication Key for the NEWSAPI endpoint
* a chromedriver executable

These are set as enviroment variables in my script.
