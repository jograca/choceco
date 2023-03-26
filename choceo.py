import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'https://example.com'

# Define the lambda function to scrape the UI
scrape_ui = lambda url: BeautifulSoup(requests.get(url).text, 'html.parser')

# Call the lambda function to scrape the UI
ui_data = scrape_ui(url)

# Print the UI data
print(ui_data.prettify())
