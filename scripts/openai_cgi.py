#!/usr/bin/env python

import cgi
import json
import traceback
import os
import sys
sys.path.insert(0, "/home/zhenqi/.local/lib/python3.10/site-packages")

import requests

try:
    # Set the content type to plain text
    print("Content-type: text/plain\n")
    
    # Parse the input data
    if os.environ.get('CONTENT_TYPE') == "application/json":
        input_data = sys.stdin.read()
        data = json.loads(input_data)
        prompt = data.get("command", "")
    else:
        form = cgi.FieldStorage()
        prompt = form.getvalue("command")
    
    openai_api_key = "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"
    
    # Set up the OpenAI API request
    #url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}",
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500,
    }

    # Send the request to the OpenAI API
    response = requests.post(url, headers=headers, json=data)
    
    #print(response.content)
    #exit(0)
    # Parse the response and extract the top choice
    json = response.json()
    choice = json["choices"][0]['message']["content"]
    
    # Output the choice only
    print(choice)
    
except Exception as e:
    print(json)
    print(traceback.format_exc())
