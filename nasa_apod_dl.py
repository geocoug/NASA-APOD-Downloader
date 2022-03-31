#!/usr/bin/env python
# coding: utf-8
# NASA APOD Downloader
# https://github.com/geocoug/NASA-APOD-Downloader.git

import os
import sys
import requests
import json
import datetime


fpath = "/Users/cgrant/Pictures/Wallpaper"

with open('/Users/cgrant/OneDrive/GitHub/nasa.txt', 'r') as f:
    API_KEY = f.readlines()[0]

apod = "https://api.nasa.gov/planetary/apod?api_key={}".format(API_KEY)

def GetRequest(url):
    response = requests.get(url)
    if not response.ok:
        print(response.text)
        sys.exit()
    else:
        return response

def GetAPOD():
    response = GetRequest(apod)

    if response.json()['media_type'] == 'image':
        if 'hdurl' in response.json():
            img_url = response.json()['hdurl']
        elif 'url' in response.json():
            img_url = response.json()['url']
    else:
        sys.exit()
    return img_url

def SaveImg(url):
    img_name = url.split("/")[-1]
    img_data = GetRequest(url).content
    with open(os.path.join(fpath, img_name), 'wb') as handler:
        handler.write(img_data)

if __name__ == "__main__":
    SaveImg(GetAPOD())

