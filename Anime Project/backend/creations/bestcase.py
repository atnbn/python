import random
import time
import requests
import pandas as pd
from jikanpy import Jikan


jikan = Jikan()

MOOD_GENRE_MAPPING = {
    "Happy": ['4', '22', '36'],  # Comedy, Romance, Slice of Life
    "Sad": ['8', '22'],          # Drama, Romance
    "Scared": ['14', '49'],      # Horror, Psychological
    "Bored": ["36", '23'],       # Slice of Life, School Life
    "Relaxed": ['36', '4', '22'],  # Slice of Life, Comedy, Romance
    "Inspired": ['30', '2', '8'],  # Sports, Adventure, Drama
    "Confused": ['7', '49']      # Mystery, Psychological
}


def get_user_mood():
    return input("In what mood are you in? ")


def convert_arr_to_string(mood):
    modified_list = [s.replace(',', ' ') for s in get_genres_for_mood(mood)]
    final_string = ' '.join(modified_list)
    return final_string


def get_genres_for_mood(mood):
    return MOOD_GENRE_MAPPING.get(mood, [])


def fetch_anime_data(genres):
    url = "https://api.jikan.moe/v4/anime/Ha"
    data = []
    while len(data) < 40:
        currentPage = random.randint(1, 50)
        params = {
            'page': currentPage,
            'type': 'tv',
            'genres': ' '.join(genres),
            'min_score': 7,
        }
        try:
            print(genres)
            response = requests.get(url, params=params).json()
            if "data" in requests:
                print('success')
                data.extend(response['data'])
            time.sleep(2)
        except Exception as e:
            print(f"Error occurred: {e}. Retrying...")
            time.sleep(2)
    return data


def create_anime_objects(data):
    return [
        {
            'id': [genre['mal_id'] for genre in anime['genres']],
            'title': anime['titles'][0]['title'],
            'episodes': anime['episodes'],
            'genres': [genre['name'] for genre in anime['genres']],
            'year': anime.get('year', 'Unknown'),
            'image_url': anime['images']['webp']['small_image_url']
        }
        for anime in data
    ]


def pick_random_animes(animes, count=10):
    return random.sample(animes, count)


def main():
    user_mood = get_user_mood()
    genres = get_genres_for_mood(user_mood)
    convert_arr_to_string(mood)
    print(genres)
    if not genres:
        print("Invalid mood or no genres found for the given mood.")
        return

    anime_data = fetch_anime_data(genres)
    anime_objects = create_anime_objects(anime_data)
    selected_animes = pick_random_animes(anime_objects)


    anime_df = pd.DataFrame(selected_animes)
    print(anime_df)


if __name__ == "__main__":
    main()
