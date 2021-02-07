import requests
import secrets

PIXELA_ENDPOINT_ROOT = 'https://pixe.la/v1/users'
HEADERS = {
    'X-USER-TOKEN': secrets.token,
}


def post_new_pixel(username, graph_id, date, quantity):
    pixel_creation_endpoint = f'{PIXELA_ENDPOINT_ROOT}/{username}/graphs/{graph_id}'
    pixel_create_parameters = {
        'date': date,
        'quantity': quantity,
    }
    response = requests.post(url=pixel_creation_endpoint, headers=HEADERS, json=pixel_create_parameters)
    response_json = response.json()
    return response.status_code, response_json['message']


def put_pixel_modification():
    print('Pixel modified.')
    return 'Success.'


def delete_existing_pixel():
    print('Pixel deleted.')
    return 'Success.'
