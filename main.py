import requests
import xkcd_tools
import vk_api_tools
import os
from dotenv import load_dotenv
import random


def main():
    load_dotenv()
    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    vk_api_version = 5.131
    vk_group_id = os.getenv('VK_GROUP_ID')
    post_sender = {'user': 0, 'group': 1}
    latest_comics = xkcd_tools.get_latest_comics_number()
    comics = xkcd_tools.get_xckd_comics(
        random.randint(1, latest_comics)
    )
    comics_filepath = xkcd_tools.save_xckd_pic_file(comics)
    comics_comment = comics['alt']
    try:
        upload_url = vk_api_tools.get_upload_url(
            vk_access_token, vk_api_version, vk_group_id
        )
        uploaded_photo = vk_api_tools.upload_picture_to_server(
            upload_url['response']['upload_url'], comics_filepath)
        saved_photo = vk_api_tools.save_photo_to_album(
            vk_group_id, uploaded_photo['photo'], uploaded_photo['server'],
            uploaded_photo['hash'], vk_access_token, vk_api_version
        )
        vk_api_tools.publish_photo(
            f'-{vk_group_id}', post_sender['group'], comics_comment,
            saved_photo['id'], saved_photo['owner_id'], vk_access_token,
            vk_api_version
        )
    except requests.HTTPError as error:
        print(error)
    finally:
        os.remove(comics_filepath)


if __name__ == '__main__':
    main()
