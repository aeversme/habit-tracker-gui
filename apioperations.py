import requests
import secrets

PIXELA_ENDPOINT_ROOT = 'https://pixe.la/v1/users'


def post_new_pixel():
    print('New pixel posted.')
    return 'true'


def put_pixel_modification():
    print('Pixel modified.')
    return 'true'


def delete_existing_pixel():
    print('Pixel deleted.')
    return 'true'
