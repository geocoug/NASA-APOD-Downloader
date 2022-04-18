#!/usr/bin/env python
# coding: utf-8
# NASA APOD Downloader
# https://github.com/geocoug/NASA-APOD-Downloader.git


import os

import requests

# Local path to save APOD download
fpath = "/Users/cgrant/Pictures/Wallpaper"

# File containing NASA API key
api_key_file = "/Users/cgrant/OneDrive/GitHub/nasa.txt"

with open(api_key_file, "r") as f:
    API_KEY = f.readlines()[0]

# API endpoint
apod = "https://api.nasa.gov/planetary/apod?api_key={}".format(API_KEY)


def GetRequest(url: str):
    """Send a GET request"""
    response = requests.get(url)
    if not response.ok:
        raise Exception(response)
    return response


def GetAPOD() -> str:
    """Retrieve POD url from payload"""
    response = GetRequest(apod)

    if response.json()["media_type"] == "image":
        if "hdurl" in response.json():
            img_url = response.json()["hdurl"]
        elif "url" in response.json():
            img_url = response.json()["url"]
    else:
        raise Exception("POD not in image format.")
    return img_url


def SaveImg(url: str) -> None:
    """Retrieve the iamge and save it locally."""
    img_name = url.split("/")[-1]
    img_data = GetRequest(url).content
    with open(os.path.join(fpath, img_name), "wb") as handler:
        handler.write(img_data)


if __name__ == "__main__":
    SaveImg(GetAPOD())
