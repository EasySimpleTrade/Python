#Required Libraries
import requests

#Function to send payload as JSON
def post_request(url, headers, payload):
    response = requests.post(url, headers=headers, json=payload)
    response_data = response.json()
    return response_data

#Function to send payload as data
def post_request(url, headers, payload):
    response = requests.post(url, headers=headers, data=payload)
    response_data = response.json()
    return response_data

#Function to send without headers
def post_request(url, payload):
    response = requests.post(url, data=payload)
    response_data = response.json()
    return response_data


#All above in one
def post_request(url, payload, headers=None, is_json=True):
    if headers is None:
        headers = {}
        
    if is_json:
        response = requests.post(url, headers=headers, json=payload) 
    else:
        response = requests.post(url, headers=headers, data=payload)  

    response_data = response.json()
    return response_data
