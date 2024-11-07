import requests
from bs4 import BeautifulSoup
import http.client
import json
import re

def get_actor_metadata(actor_url): #This function scrapes out the movie names and its year of release from the imdb link of the given actor
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(actor_url, headers=headers)
    response.raise_for_status()  
    soup = BeautifulSoup(response.content, 'html.parser')
    span_elements = soup.find_all('span', class_='ipc-metadata-list-summary-item__li')
    a_elements = soup.find_all('a', class_='ipc-metadata-list-summary-item__t')
    span_texts = [span.text for span in span_elements]
    a_texts = [a.text for a in a_elements]
    return span_texts, a_texts

def get_imdb_link(actor_name): #This function will extract the imdb link given the actor's name so that the scraping can be done
    conn = http.client.HTTPSConnection("google-search72.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "ad1fb620f5msh02732fee09b35e1p1e4affjsn56b0c591aa94",
        'x-rapidapi-host': "google-search72.p.rapidapi.com"
    }

    query = f"/search?q={actor_name.replace(' ', '%20')}%20site:imdb.com&lr=en-US&num=10"
    conn.request("GET", query, headers=headers)

    res = conn.getresponse()
    data = res.read()
    result = data.decode("utf-8")
    json_data = json.loads(result)
    imdb_link = None
    for item in json_data.get('items', []):
        link = item.get('link')
        if "imdb.com" in link:
            imdb_link = link
            break
    return imdb_link


def main(actor_name): #main function that intergrates the above two functionalities
    imdb_link = get_imdb_link(actor_name)

    if imdb_link:
        span_texts, a_texts = get_actor_metadata(imdb_link)

        print(f"\nFilms by {actor_name} in Descending order (Years)\n")
        for year, title in zip(span_texts, a_texts):
            if re.match(r'^\d{4}$', year):
                print(f"{title} ({year})")
            else:
                print(f"{title} (upcoming)")
        if len(span_texts) > len(a_texts):
            for year in span_texts[len(a_texts):]:
                if re.match(r'^\d{4}$', year):
                    print(f"({year})")
                else:
                    print("(upcoming)")
        elif len(a_texts) > len(span_texts):
            for title in a_texts[len(span_texts):]:
                print(f"{title} ()")
    else:
        print(f"No IMDb link found for {actor_name}")

#Input-> Name of the Actor 
#Ouput->List of movies in ascending order 

actor_name = input("Enter the name of the Actor:  ")  
main(actor_name)
