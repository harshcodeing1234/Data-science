import concurrent.futures
import requests #type:ignore
from bs4 import BeautifulSoup #type:ignore

# List of URLs
urls = [
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.w3schools.com"
]

def fetch_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "No title found"
        print(f"Title of {url}: {title}")
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")

# Using ThreadPoolExecutor for concurrent scraping
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(fetch_title, urls)
