import requests
from bs4 import BeautifulSoup
import argparse

def fetch_open_graph_tags(url):
    # Fetch the content of the webpage
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve the page: {e}")
        return
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all meta tags with property attribute starting with "og:"
    og_tags = soup.find_all('meta', attrs={'property': lambda x: x and x.startswith('og:')})
    
    # Display found Open Graph tags
    if og_tags:
        print(f"Found Open Graph tags for {url}:\n")
        for tag in og_tags:
            print(f"{tag['property']}: {tag['content']}")
    else:
        print(f"No Open Graph tags found on {url}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Fetch Open Graph tags from a webpage.')
    parser.add_argument('--urlToCheck', required=True, help='URL of the webpage to check')
    args = parser.parse_args()
    
    # Call the function with the provided URL
    fetch_open_graph_tags(args.urlToCheck)
