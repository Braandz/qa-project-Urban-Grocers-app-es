# sender_stand_request.py
import requests
from configuration import BASE_URL, CREATE_USER_ENDPOINT, CREATE_KIT_ENDPOINT

def post_new_user():
    url = BASE_URL + CREATE_USER_ENDPOINT
    headers = {"Content-Type": "application/json"}
    data = {
        "firstName": "Max",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
    }
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()['authToken']

def post_new_client_kit(kit_body, auth_token):
    url = BASE_URL + CREATE_KIT_ENDPOINT
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=kit_body, headers=headers)
    return response
