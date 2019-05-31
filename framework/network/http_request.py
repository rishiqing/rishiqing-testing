#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json

def post (url, parameters = {}, header = {}):
    response = send('POST', url, parameters, header)
    return response

def get (url, parameters = {}, header = {}):
    response = send('GET', url, parameters, header)
    return response

def send (type, url, parameters = {}, header = {}):
    if  any(header) == False:
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cache-control': "no-cache"
        }
    response = requests.request(type, url, data=parameters, headers=headers)
    return response

def getJson (response):
    body = json.loads(response.text)
    return body