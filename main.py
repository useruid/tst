import os

import requests

from dotenv import load_dotenv
from loguru import logger

load_dotenv()

API_URL = os.getenv('API_URL')

speakers = requests.get(f"""
{API_URL}/items/speakers?fields=id,photo&limit=500
""")

speakers_photos = {speaker['id']: speaker['photo'] for speaker in speakers.json()['data']}

cnt = 0
if __name__ == '__main__':
    for speaker_id, photo in speakers_photos.items():
        if photo:
            asset_url = f'{API_URL}/assets/'
            photo_url = asset_url + photo
            response = requests.get(photo_url)
            logger.info(f'getting photo for {speaker_id} with photo url: {photo_url}')
            try:
                logger.info(f'saving photo for {speaker_id}')
                with open(f'images/{speaker_id}.jpg', 'wb') as file:
                    file.write(response.content)
                cnt += 1
            except Exception as e:
                logger.error(f'error saving photo for {speaker_id}: {e}')
        else:
            logger.warning(f'no photo for {speaker_id}')
        logger.success(f'saved {cnt} photos')


