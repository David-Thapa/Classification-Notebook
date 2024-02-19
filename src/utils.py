import requests
from bs4 import BeautifulSoup
import os
import urllib

# Function to download images
def download_images(image_urls, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, url in enumerate(image_urls):
        response = requests.get(url)
        with open(os.path.join(output_folder, f"pigeon_image_{i + 1}.jpg"), 'wb') as f:
            f.write(response.content)

# Function to scrape image URLs from Unsplash
def scrape_unsplash_images(search_query, num_pages=1):
    base_url = 'https://unsplash.com/s/photos/'
    image_urls = []

    for page in range(1, num_pages + 1):
        url = f"{base_url}{search_query}?page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find image URLs on the page
        images = soup.find_all('img', class_='_2UpQX')
        image_urls.extend([img['src'] for img in images])

    return image_urls
