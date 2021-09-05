import csv
from typing import ItemsView

def save_to_file(items):
    # Create a csv file in the working environment as a write mode.
    file=open("jobs.csv", mode="w")
    
    # This wirter will write on the csv file given as an argument.
    writer = csv.writer(file)

    # Write the first row that contains headers.
    writer.writerow([ "title","image_url", "date", "location", "price"
])
    # Use dictionary function to get only values. 
    for item in items:
        writer.writerow(list(item.values()))
    
    return

