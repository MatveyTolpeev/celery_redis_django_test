import uuid
import requests

from celery import shared_task
from django.conf import settings

IMAGE_URL = "https://thecatapi.com/api/images/get?format=src&type=gif"

@shared_task
def load_image():
    response = requests.get(IMAGE_URL)
    file_ext = response.headers.get('Content-Type').split('/')[1]
    file_name = settings.BASE_DIR / 'photos' / (str(uuid.uuid4()) + "." + file_ext)
    print('[+] start_d in ' + str(file_name))
    with open(file_name, 'wb') as f:
        for chunk in response.iter_content(chunk_size=128):
            f.write(chunk)
    print('[+] end_d')
    return True
