# Anime Recommandation app based on Mood
# anhang des Values ein Array erstellen
# Wenn keine Data zurückkommt wird ein neuer Request gemacht bis data zurück ist
#
import random
import requests
from jikanpy import Jikan
import time
import pandas as pd
jikan = Jikan()

# 1 Action / 2 Adventure / 3 / 4 Comedy / 8 Drama / 9 Ecchi / 12 Hentai

MOOD_GENRE_MAPPING = {
    "Happy": ['1', '22', '36'],  # Comedy, Romance, Slice of Life
    "Sad": ['8', '22'],          # Drama, Romance
    "Scared": ['14', '49'],      # Horror, Psychological
    "Bored": ["36", '23'],       # Slice of Life, School Life
    "Relaxed": ['36', '1', '22'],  # Slice of Life, Comedy, Romance
    "Inspired": ['30', '2', '8'],  # Sports, Adventure, Drama
    "Confused": ['7', '49']      # Mystery, Psychological
}

def load_data():
    currentLoop = 0
    counter = 0
    anime_data = []
    curr_mood = input("In what mood are you in: ")
    while counter < 10:
        for _ in range(1):
            currentLoop += 1
            if currentLoop % 3 == 0:
                time.sleep(2)
            else:
                try:
                    curr_data = jikan.random('anime')
                    curr_anime = get_genres_for_mood(
                        curr_data["data"], curr_mood)
                    print(curr_anime)
                    if curr_anime != False and curr_anime != None:
                        print(curr_anime)
                        counter += 1
                        anime_data.append(curr_anime)
                except Exception as e:
                    print(f"Error occurred: {
                          e}. Skipping this URL and trying again.")
    result = pd.DataFrame(anime_data)
    return result


def get_genres_for_mood(mood):
    return MOOD_GENRE_MAPPING.get(mood, [])

def convert_arr_to_string(mood):
    modified_list = [s.replace(',', ' ') for s in get_genres_for_mood(mood)]
    final_string = ' '.join(modified_list)
    return final_string


def fetch_anime_data():
    # create an array with all animes based on wished genre then pick 10 Random animes from the created Array
    url = "https://api.jikan.moe/v4/anime/"
    mood = input("In what mood are you in ?: ")
    genres = convert_arr_to_string(mood)
    data = []
    curr = 0
    while len(data) < 40:
        for _ in range(1,2):
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
    test = pick_random_anime(result)
    table = pd.DataFrame(test)
    return table


def create_anime_objects(data):
    anime_list = []
    for anime in data:
        try:
            title = anime['title']
            episodes = anime.get('episodes', 'Unknown')
            genres = [genre['name'] for genre in anime['genres']]
            year = anime.get('year', 'Unknown')
            image_url = anime['images']['webp']['large_image_url']
            anime_list.append({
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


def main():

    print(fetch_anime_data())


if __name__ == "__main__":
    main()
