import requests
from bs4 import BeautifulSoup


# Global variable that is frequently used.
CRAIGLIST_URL = "https://losangeles.craigslist.org/d/appliances/search/ppa"
CRAIGLIST_SUB = ""


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


# This function will extract items from the page. 
def extract_craiglist_items(row):
    # new query of HTML elements on the sub_page.
    CRAIGLIST_SUB= row.find("a")['href']
    sub_result = requests.get(CRAIGLIST_SUB)
    sub_soup = BeautifulSoup(sub_result.text, 'html.parser')

    # From top to bottom - scrap img URL, Title(heading), date, location, price
    try:
        image_url = sub_soup.find('img')['src']
        
    except:
        image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/No-Image-Placeholder.svg/330px-No-Image-Placeholder.svg.png"
    title = row.find("div", {"class":"result-info"}).find("h3").text
    date = row.find("div", {"class":"result-info"}).find("time")['datetime']
    location = row.find("div", {"class":"result-info"}).find("span",{"class":"result-hood"}).text
    price = row.find("div", {"class":"result-info"}).find("span",{"class":"result-price"}).text 
    
    # remove whitespaces from the data
    image_url= image_url.strip()
    title = title.strip()
    date = date.strip()
    location = location.strip()
    price = price.strip()

    
    return { 'title': title,'image_url':image_url, 'date':date, 'location':location, 'price':price}



# This function will extract pages. 
def extract_craglist_pages():
    print("Scrapping the page......")
    result = requests.get(CRAIGLIST_URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    search_container = soup.find("ul", {"class":"rows"})
    item_lists = search_container.find_all('li')
    data = []
    row_counter = 0
    # Iterate each result_row
    for row in item_lists:
        item_data= extract_craiglist_items(row)
        data.append(item_data)
        row_counter+=1
        print(f"Scrapping row {row_counter}")
    return data

