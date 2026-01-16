# WAP to scraping data or downloading multiple pages using multithreading.
import threading
import requests
import time

# Function to download a web pag
def download_page(url):
    print(f"starting downloading {url}", flush = True)
    response = requests.get(url)
    print(f"finished download {url} - size: {len(response.content)}")

def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/delay/2", 
        "https://httpbin.org/delay/3",
        "https://www.wikipedia.org",

    ]
    start = time.perf_counter()

    # Create and start a thread for each URL
    threads = []
    for url in urls:
        t = threading.Thread(target=download_page, args = (url,))
        threads.append(t)
        t.start()
    
    # Wait for all threads to finish
    for t in threads:
        t.join()

    end = time.perf_counter()
    print(f"Download all pages in {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
