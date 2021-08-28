# Craiglist Web Scrapper

- This app scrap data from Craiglist and display to the users. 

*What is web scrapping?*
- Web scrapping is extracting data from the websites. 
- Many firms like Facebook and Google uses it. 
    - when you search the keyword, it scraps some related data on the right panel. 
- It is also called web indexing or data mining. 


# Requirements

Lanuguage:
- Python

Frameworks:
- Flask - python framework to create a website


Libraries:
- Requests - scrap HTML tags.
- BeautifulSoup - extract data from HTML tags.


# Development Process

- Building a web scrapper:

1. Install requests library

```py
pip install requests
```

2. Use requests library to scrap the pages.

```py
import requests

craiglist_result = requests.get("https://losangeles.craigslist.org/")

print(craiglist_result)
# Output: <Response [200]>
```

3. If you want to see the result and the scrapped HTML, use requested_data.text. 

```py
craiglist_result.text
# Gets all the HTML tags in the website. 
```

4. To extract data, use beatifulSoup. 

- Install BeatifulSoup
```py
pip install beautifulsoup4
```

5. Use BeatifulSoup to parse the HTML data. 

```py

```