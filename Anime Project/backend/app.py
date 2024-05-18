from flask import Flask, jsonify, request
from flask_cors import CORS

import random
import requests
from jikanpy import Jikan
import time
import pandas as pd

app = Flask(__name__)
CORS(app)  

jikan = Jikan()

MOOD_GENRE_MAPPING = {
    "Happy": ['1', '22', '36'],
    "Sad": ['8', '22'],
    "Scared": ['14', '49'],
    "Bored": ["36", '23'],
    "Relaxed": ['36', '1', '22'],
    "Inspired": ['30', '2', '8'],
    "Confused": ['7', '49']
}


def get_genres_for_mood(mood):
    return MOOD_GENRE_MAPPING.get(mood, [])


def convert_arr_to_string(mood):
    modified_list = [s.replace(',', ' ') for s in get_genres_for_mood(mood)]
    final_string = ' '.join(modified_list)
    return final_string


def fetch_anime_data(mood):
    url = "https://api.jikan.moe/v4/anime/"
    genres = convert_arr_to_string(mood)
    data = []
    curr = 0
    while len(data) < 40:
        for _ in range(1, 2):
            curr += 1
            currentPage = random.randint(1, 50)
            params = {
                'page': currentPage,
                "type": 'tv',
                'genres': genres,
                'min_score': 7,
            }
            try:
                response = requests.get(url, params=params).json()
                data += response['data']
                time.sleep(2)
            except requests.exceptions.RequestException as e:
                print(f"Error occurred: {e}. Retrying...")
                time.sleep(2)
                continue

    result = create_anime_objects(data)
    return pick_random_anime(result)


def create_anime_objects(data):
    anime_list = []
    for anime in data:
        try:
            id = anime['mal_id']
            title = anime['title']
            episodes = anime.get('episodes', 'Unknown')
            genres = [genre['name'] for genre in anime['genres']]
            year = anime.get('year', 'Unknown')
            image_url = anime['images']['webp']['image_url']
            anime_list.append({
                'id': id,                
                'title': title,
                'episodes': episodes,
                'genres': genres,
                'year': year,
                'image_url': image_url
            })
        except KeyError as e:
            print(f"KeyError: {e} in anime {anime}")
    return anime_list


def pick_random_anime(arr):
    final_result = []
    selected_indices = set()
    length = len(arr)

    while len(final_result) < 10:
        random_index = random.randint(0, length - 1)
        if random_index not in selected_indices:
            final_result.append(arr[random_index])
            selected_indices.add(random_index)

    return final_result


@app.route('/api/anime', methods=['GET'])
def get_anime():
    mood = request.args.get('mood')
    anime_list = fetch_anime_data(mood)
    return jsonify(anime_list)





if __name__ == "__main__":
    app.run(debug=True)
