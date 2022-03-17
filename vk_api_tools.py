import requests


def get_upload_url(token, api_version, group_id):
    api_url = 'https://api.vk.com/method/photos.getWallUploadServer'
    payload = {
        'access_token': token,
        'v': api_version,
        'group_id': group_id
    }
    response = requests.get(api_url, params=payload)
    response.raise_for_status()
    if 'error' in response.json():
        raise requests.HTTPError(
            f"Error Code: {response.json()['error']['error_code']}\n"
            f"Error Message: {response.json()['error']['error_msg']}"
        )
    else:
        return response.json()


def upload_picture_to_server(url, picture):
    with open(picture, 'rb') as file:
        files = {
            'photo': file
        }
        response = requests.post(url, files=files)
        response.raise_for_status()
        if 'error' in response.json():
            raise requests.HTTPError(
                f"Error Code: {response.json()['error']['error_code']}\n"
                f"Error Message: {response.json()['error']['error_msg']}"
            )
        else:
            return response.json()


def save_photo_to_album(group_id, photo, server, vk_hash, token, api_version):
    api_url = 'https://api.vk.com/method/photos.saveWallPhoto'
    payload = {
        'group_id': group_id,
        'photo': photo,
        'access_token': token,
        'hash': vk_hash,
        'server': server,
        'v': api_version
    }
    response = requests.post(api_url, params=payload)
    response.raise_for_status()
    if 'error' in response.json():
        raise requests.HTTPError(
            f"Error Code: {response.json()['error']['error_code']}\n"
            f"Error Message: {response.json()['error']['error_msg']}"
        )
    else:
        return response.json()['response'][0]


def publish_photo(
    owner_id, from_group, message, media_id, photo_owner_id, token, api_version
):
    api_url = 'https://api.vk.com/method/wall.post'
    attachments = f'photo{photo_owner_id}_{media_id}'
    payload = {
        'owner_id': owner_id,
        'from_group': from_group,
        'message': message,
        'access_token': token,
        'attachments': attachments,
        'v': api_version
    }
    response = requests.post(api_url, params=payload)
    response.raise_for_status()
    if 'error' in response.json():
        raise requests.HTTPError(
            f"Error Code: {response.json()['error']['error_code']}\n"
            f"Error Message: {response.json()['error']['error_msg']}"
        )
    else:
        return response.json()
