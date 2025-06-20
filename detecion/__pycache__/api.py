import requests
import json

# Define the URL of the API endpoint you want to call
url = 'https://www.virustotal.com/gui/home/url'

# Define your API key
api_key = '1fdbb16b9bcc1357e36b2c9a931ff8d821f76f6ee85b30cd14d490ccc62d592a'

# Set up the request headers with the API key
headers = {'Authorization': f'Bearer {api_key}'}

# Send a GET request to the API endpoint with the headers
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.text)
# Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the JSON response into a Python dictionary
#     data = response.json()
    
#     # Now you can work with the data returned by the API
#     print(data)
# else:
#     # If the request was not successful, print an error message
#     print('Error:', response.status_code)
