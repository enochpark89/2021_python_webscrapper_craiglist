from craiglist import extract_craiglist_pages
from craiglist import extract_craiglist_items
from craiglist import extract_craglist_pages
from save import save_to_file

data = extract_craglist_pages()
save_to_file(data)

# # Iterate through an array and send seperate request to each pages. 
# for n in pages:
#     print(n)





# scrapped HTML tags are displayed.
