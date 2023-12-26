import requests
import os
from env import APIKEY


def fetch_images(query, count, api_key):
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    params = {"q": query, "license": "public", "imageType": "photo", "count": count}

    search_url = "https://api.bing.microsoft.com/v7.0/images/search"
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def save_images(images, folder="downloaded_images"):
    if not os.path.exists(folder):
        os.makedirs(folder)

    for i, image in enumerate(images["value"]):
        image_data = requests.get(image["contentUrl"])
        if image_data.status_code == 200:
            with open(os.path.join(folder, f"image_{i}.jpg"), "wb") as file:
                file.write(image_data.content)


def main():
    query = "single"  # Your search query
    count = 10  # Number of images to fetch
    api_key = APIKEY  # Replace with your Bing Search API key

    images = fetch_images(query, count, api_key)
    save_images(images)


if __name__ == "__main__":
    main()
