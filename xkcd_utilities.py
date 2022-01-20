import requests
import os


# def save_spacex_last_launch(urls, files_extensions):
#     for url_index, url_value in enumerate(urls):
#         response = requests.get(url_value)
#         response.raise_for_status()
#         filepath = 'images/spacex{}.{}'.format(
#             url_index,
#             files_extensions[url_index]
#         )
#         with open(filepath, 'wb') as file:
#             file.write(response.content)


def get_xckd_comics_meta(comics_number):
    url = f'https://xkcd.com/{comics_number}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    comics_meta = response.json()
    return comics_meta


def save_xckd_pic_file(comics_meta):
    pic_title = comics_meta['title']
    pic_extension = comics_meta['img'].split('.')[-1]
    response = requests.get(url=comics_meta['img'])
    response.raise_for_status()
    filepath = f'{pic_title}.{pic_extension}'
    with open(filepath, 'wb') as file:
        file.write(response.content)
