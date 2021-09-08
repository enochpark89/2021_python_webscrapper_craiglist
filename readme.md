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


# Overview:

1. save.py: 
- Uses python csv library to save the data into csv file.
- 

2. 

# Development Process

# 1.0: Use BeautifulSoup to scrap web pages

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

# 1.1: Setting up Flask environment. 

- Flask is a lightweight Python framework for web applications that provides the basics for URL routing and page rendering.


1. Inside the project environment, set up environment

```shell
python -m venv env
```

*Ctrl+Shift+`: Command Palette, which creates a terminal and automatically activates the virtual environment by running its activation script.*

2. Update pip in the virt environment
```shell
python -m pip install --upgrade pip
```

3. Install flask
```shell
python -m pip install flask
```

4. To run the server, use below code.
```shell
python -m flask run
```

# 1.2: Work on the Flask


## Render the template on the localhost.
1. Import Flask in the app.py and start using.

```py
from flask import Flask
```

2. Use render_template from flask library to render HTML template. 

```py
from flask import Flask, render_template
```

3. Create HTML templates for use and render it in .route()
```
@app.route("/")
def home():
    return render_template('appliance.html')

```

## Create a form

1. Send data from a form

```html
    <form action="/report" method="get">
        <input placeholder='Search for a job' required name="word" />
        <button>Search</button>
        <h3>changed</h3>
    </form>
```
- URL before: http://127.0.0.1:5000/
- URL after: http://127.0.0.1:5000/report?word=dfsfasd

- Pattern: <action word>?<name>=<query argument>
*When you search from the Google, you will notice the query argument also.*

2. Create a new route that correspond with the action word. 
- This particular example: report
```py
@app.route("/report")
def report():
    return "This is the report"

```
- Report will show the return string, but the url keeps the word received from an user. 

3. Get the keyword from the URL. 

- If you want to get the keyword from the URL, you have to simply get the argument from the request. 

@app.route("/report")
def report():
    # Get the word from the url.
    word = request.args.get('word')
    print(word)
    return render_template('report.html')



# 1.3: Deployment with heroku

- Deploy using heroku steps:

1. Create requirements.txt that shows what to install to launch this app. 
```py
pip freeze > requirements.txt
```

2. Create a 'Procfile.txt' in the root directory.

3. Add below to Procfile.txt
```
web: gunicorn app:app
```

4. Install heroku

```bash
npm install -g heroku
```

5. Verify version

```bash
heroku --version
```

6. Login to heroku using the browser login
```bash
heroku login
```

7. Add your project to heroku from github

```bash
 heroku git:remote -a {your-project-name}
```
- this particular case
```
heroku git:remote -a {2021_python_webscrapper_craiglist}

```