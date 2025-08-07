# Login test case generation
import requests

def test_login(endpoint, username, password):
    try:
        response = requests.post(endpoint, json={'username': username, 'password': password})
        return response.status_code == 200, response.json().get('token')
    except Exception as e:
        return False, str(e)

def test_invalid_login(endpoint, username, password):
    try:
        response = requests.post(endpoint, json={'username': username, 'password': password})
        return response.status_code != 200, response.json().get('error', 'No error message')
    except Exception as e:
        return True, str(e)