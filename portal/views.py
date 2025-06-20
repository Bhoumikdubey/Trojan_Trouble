from django.shortcuts import render
from django.http import HttpResponse
import time
import json
import requests
# Create your views here.

def home(request):
    return render(request,'login.html')

def get_verdict(request):
    try:
        url_to_scan = request.POST.get('url')
        url = 'https://www.virustotal.com/api/v3/urls'

        # Define your API key
        api_key = '1fdbb16b9bcc1357e36b2c9a931ff8d821f76f6ee85b30cd14d490ccc62d592a'

        # Set up the request headers with the API key
        headers = {'x-apikey': api_key}
        data = {"url":url_to_scan}

        # Send a GET request to the API endpoint with the headers
        response = requests.post(url, headers=headers, data = data)
        response = response.json()
        analysis_id = response.get('data', {}).get('id')
        url_analysis = f'https://www.virustotal.com/api/v3/analyses/{analysis_id}'
        response = requests.get(url_analysis, headers=headers)
        result = response.json()
        stats = result['data'].get('attributes', {}).get('stats')
        url_scanned = result['meta']['url_info']['url']
        is_success = insert_to_db(stats, url_scanned)
        result = {'stats':stats, 'status':'success'}
        print(stats)
        
    except Exception as e:
        print(f'exception in getting verdict is: {e}')
        result = {'stats':'NA', 'status':'failed'}

    return result

def insert_to_db(stats, url):
    try:
        #insert to db
        data = {
            "stats":stats,
            "scanned_at": time.time(),
            "url_scanned": url,
            "scanned_by": "kaif"
        }
    except Exception as e:
        print(f'exception in db insertion is: {e}')
        return None

def get_data_from_db():
    try:
        data = db.find()
        # implement correctly
    except:
        pass
    return data
