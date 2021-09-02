import requests
from bs4 import BeautifulSoup

CRAIGLIST_URL = "https://losangeles.craigslist.org/d/appliances/search/ppa"

def extract_craiglist_pages():
        
    # Retrieve HTML tags with requests lib.
    result = requests.get(CRAIGLIST_URL)

    # Parse HTML tags to BeautifulSoup format.
    soup = BeautifulSoup(result.text, 'html.parser')

    # Extract the total page of the query results
    total_page = soup.find("span", {"class": "totalcount"})
    total_page = total_page.text

    # Parse the extracted total page into an integer
    total_page = int(total_page)

    # Extract class called row from the soup.
    search_container = soup.find("ul", {"class":"rows"})
    result_rows = search_container.find_all('li')

    # Divide the total_page by number of maximum pages (120)
    # Then, store divided numbers into pages array.
    pages =[]
    i = 0
    while i <= total_page:
        pages.append(i)
        i+=120

    return pages

def extract_craiglist_items():
   result = requests.get(CRAIGLIST_URL)
   soup = BeautifulSoup(result.text, 'html.parser')
   search_container = soup.find("ul", {"class":"rows"})
   result_rows = search_container.find_all('li')
   # Iterate each result_row
   for result in result_rows:
       print(result.find("a").find("span"))
       print(result.findAll("a"))

   return result_rows
