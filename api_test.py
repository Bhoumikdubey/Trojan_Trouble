import requests
import json

# Define the URL of the API endpoint you want to call
import json

# Define the URL of the API endpoint you want to call
url = 'https://www.virustotal.com/api/v3/urls'

# Define your API key
api_key = '1fdbb16b9bcc1357e36b2c9a931ff8d821f76f6ee85b30cd14d490ccc62d592a'

# Set up the request headers with the API key
headers = {'x-apikey': api_key}
data = {"url":"googlle.com"}

# Send a GET request to the API endpoint with the headers
response = requests.post(url, headers=headers, data = data)
response = response.json()
analysis_id = response.get('data', {}).get('id')
url_analysis = f'https://www.virustotal.com/api/v3/analyses/{analysis_id}'
response = requests.get(url_analysis, headers=headers)
result = response.json()
stats = result['data'].get('attributes', {}).get('stats')
print(stats)
# Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the JSON response into a Python dictionary
#     data = response.json()
    
#     # Now you can work with the data returned by the API
#     print(data)
# else:
#     # If the request was not successful, print an error message
#     print('Error:', response.status_code)