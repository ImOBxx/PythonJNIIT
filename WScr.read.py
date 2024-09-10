from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ssl._create_default_https_context = ssl._create_unverified_context

try:
    # URL of the website to scrape
    url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"

    # Open the URL and read the data
    response = urlopen(url)
    data = response.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(data, "html.parser")

    # Print the title of the webpage
    print(soup.title.text)

except Exception as e:
    print(f"An error occurred: {e}")
