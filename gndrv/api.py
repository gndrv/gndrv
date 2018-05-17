from .const import auth_url, api_url
from getpass import getpass
import requests


def login():
    email = raw_input("Email: ")
    passwd = getpass("Password: ")
    return email, passwd


def get_token():
    email, passwd = login()
    payload = {'email': email, 'password': passwd, 'returnSecureToken': 'true'}
    r = requests.post(auth_url, json=payload)
    return r.json().get('idToken')


def auth_headers():
    token = get_token()
    headers = {'Authorization': 'Bearer {}'.format(token)}
    return headers


def get_parts():
    r = requests.get('{}/parts'.format(api_url), headers=auth_headers())
    return r.json()


def get_part(user, part_name):
    r = requests.get('{}/parts/{}/{}'.format(api_url, user, part_name))
    return r.json()


def post_part(part):
    r = requests.post('{}/parts'.format(api_url),
                      data=part, headers=auth_headers())
    return r.text
