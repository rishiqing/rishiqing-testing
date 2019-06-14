#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json

def post_json(url, parameters, header = {}):
    response = post(url, json.dumps(parameters), header)
    return response

def post (url, parameters, header = {}):
    response = send('POST', url, parameters, header)
    return response

def get (url, parameters, header = {}):
    response = send('GET', url, parameters, header)
    return response

def send(type, url, parameters, header={}):
    if  any(header) == False:
        default = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cache-control': "no-cache"
        }
        header.update(default)
    response = requests.request(type, url, data=parameters, headers=header)
    return response

def getJson (response):
    body = json.loads(response.text)
    return body