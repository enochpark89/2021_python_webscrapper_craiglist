import requests
from bs4 import BeautifulSoup


# Retrieve HTML tags with requests lib.
craiglist_result = requests.get("https://losangeles.craigslist.org/d/appliances/search/ppa")

# Parse HTML tags to BeautifulSoup format.
craiglist_soup = BeautifulSoup(craiglist_result.text, 'html.parser')

# Extract the total page of the query results
total_page = craiglist_soup.find("span", {"class": "totalcount"})
total_page = total_page.text
  
# Extract class called row from the soup.
search_container = craiglist_soup.find("ul", {"class":"rows"})


result_rows = search_container.find_all('li')

# Iterate each result_row
# for result in result_rows:
#     print(result.find("a"))

# scrapped HTML tags are displayed.
