from flask import Flask, render_template, request
from craiglist import extract_craiglist_pages
from craiglist import extract_craiglist_items
from craiglist import extract_craglist_pages
from save import save_to_file
from datetime import datetime
import re

# flash app created.
app = Flask(__name__)

db = {}


# create a route to home or localhost.
@app.route("/")
def home():
    return render_template('appliance.html')

@app.route("/report")
def report():
    # Get the word from the url.
    word = request.args.get('word')
    data = extract_craglist_pages(word)
    return render_template('report.html', items=data)


if __name__ == '__main__':
    app.run('0.0.0.0', 8085)