import xkcd_utilities
import vk_utilities
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    vk_access_token = os.getenv('vk_access_token')
    vk_api_version = 5.131
    vk_group_id = os.getenv('vk_group_id')
    comics_meta = xkcd_utilities.get_xckd_comics_meta(353)
    xkcd_utilities.save_xckd_pic_file(comics_meta)
    comics_comment = xkcd_utilities.get_author_comment(comics_meta)
    upload_data = vk_utilities.get_upload_url(
        vk_access_token, vk_api_version, vk_group_id
    )
    uploaded_photo = vk_utilities.upload_picture_to_server(
        upload_data['response']['upload_url'], 'Python.png')
    saved_photo = vk_utilities.save_photo_to_album(
        vk_group_id, uploaded_photo['photo'], uploaded_photo['server'],
        uploaded_photo['hash'], vk_access_token, vk_api_version
    )
    vk_utilities.publish_photo(
        f'-{vk_group_id}', 1, comics_comment, saved_photo['id'],
        saved_photo['owner_id'], vk_access_token, vk_api_version
    )


if __name__ == '__main__':
    main()
