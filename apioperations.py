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


def put_pixel_modification(username, graph_id, date, quantity):
    pixel_mod_endpoint = f'{PIXELA_ENDPOINT_ROOT}/{username}/graphs/{graph_id}/{date}'
    pixel_mod_parameters = {
        'quantity': quantity,
    }
    response = requests.put(url=pixel_mod_endpoint, headers=HEADERS, json=pixel_mod_parameters)
    response_json = response.json()
    return response.status_code, response_json['message']


def delete_existing_pixel(username, graph_id, date):
    pixel_mod_endpoint = f'{PIXELA_ENDPOINT_ROOT}/{username}/graphs/{graph_id}/{date}'
    response = requests.delete(url=pixel_mod_endpoint, headers=HEADERS)
    response_json = response.json()
    return response.status_code, response_json['message']
