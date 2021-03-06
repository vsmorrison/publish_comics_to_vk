import requests
from os import path


def get_xckd_comics(comics_number):
    url = f'https://xkcd.com/{comics_number}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    comics = response.json()
    return comics


def save_xckd_pic_file(comics_title, comics_path):
    pic_title = comics_title
    pic_extension = path.splitext(comics_path)[-1]
    response = requests.get(url=comics_path)
    response.raise_for_status()
    filepath = f'{pic_title}{pic_extension}'
    with open(filepath, 'wb') as file:
        file.write(response.content)
    return filepath


def get_latest_comics_number():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['num']
