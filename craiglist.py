import requests
from bs4 import BeautifulSoup

CRAIGLIST_URL = "https://losangeles.craigslist.org/d/appliances/search/ppa"
CRAIGLIST_SUB = "";

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

   arr_of_items = []

   # Iterate each result_row
   for result in result_rows:
       # new query of HTML elements on the sub_page.
       CRAIGLIST_SUB= result.find("a")['href']
       sub_result = requests.get(CRAIGLIST_SUB)
       sub_soup = BeautifulSoup(sub_result.text, 'html.parser')
       

       # From top to bottom - scrap img URL, Title(heading), date, location, price
       try:
           image_url = sub_soup.find('img')['src']
           
       except:
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/No-Image-Placeholder.svg/330px-No-Image-Placeholder.svg.png"
       title = result.find("div", {"class":"result-info"}).find("h3").text
       date = result.find("div", {"class":"result-info"}).find("time")['datetime']
       location = result.find("div", {"class":"result-info"}).find("span",{"class":"result-hood"}).text
       price = result.find("div", {"class":"result-info"}).find("span",{"class":"result-price"}).text 
       
       # remove whitespaces from the data
       image_url= image_url.strip()
       title = title.strip()
       date = date.strip()
       location = location.strip()
       price = price.strip()

       print(image_url, title, date, location, price)

#    return result_rows
