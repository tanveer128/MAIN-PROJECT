import requests
import pandas as pd
import time

def get_all_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response as JSON
        posts_data = response.json()
        return posts_data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

def display_all_posts(posts_data):
    if posts_data:
        #normalize the data after the get respones
        df = pd.json_normalize(posts_data)
        print(df)

while True:
    # Retrieve and print all posts data
    all_posts_data = get_all_posts()
    #calling function
    display_all_posts(all_posts_data)

    # Wait for 10 seconds 
    time.sleep(10)
