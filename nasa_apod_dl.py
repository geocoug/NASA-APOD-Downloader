#!/usr/bin/env python
# NASA APOD Downloader
# https://github.com/geocoug/NASA-APOD-Downloader.git


import argparse
import logging
import os

import requests

logging.basicConfig(level=logging.INFO, format="%(msg)s")
log = logging.getLogger(__name__)
log.propagate = False


def clparser() -> argparse.ArgumentParser:
    """Create a parser to handle input arguments and displaying.

    a script specific help message.
    """
    desc_msg = """Download the NASA Astronomy Picture of the Day (APOD)."""
    parser = argparse.ArgumentParser(
        description=desc_msg,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "api_token",
        help="""NASA API token. Either a filename containing the token or the raw string.""",
    )
    parser.add_argument("img_path", help="""Path to store the downloaded image file.""")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="""Control the amount of verbosity.""",
    )
    return parser


def get_request(request: str):
    """Send a GET request."""
    response = requests.get(request)
    if not response.ok:
        raise Exception(response)
    return response


def get_apod(request: str):
    """Retrieve POD url from payload."""
    response = get_request(request)

    if response.json()["media_type"] == "image":
        if "hdurl" in response.json():
            img_url = response.json()["hdurl"]
            log.info("Retrieved HD image URL: %s", img_url)
        elif "url" in response.json():
            img_url = response.json()["url"]
            log.info("Retrieved image URL: %s", img_url)
        else:
            img_url = None
            log.info("No image URL retrieved.")
    else:
        raise Exception("POD not in image format.")
    return img_url


def save_img(response: str, save_dir: str) -> None:
    """Retrieve the iamge and save it locally."""
    img_name = response.split("/")[-1]
    img_data = get_request(response).content
    if os.path.isdir(save_dir):
        save_path = os.path.join(save_dir, img_name)
    else:
        raise Exception(f"Save directory does not exist: {save_dir}")
    log.info("Saving image at: %s", save_path)
    with open(save_path, "wb") as handler:
        handler.write(img_data)


def get_token(parameter: str) -> str:
    """Return a token string."""
    if os.path.exists(parameter):
        try:
            with open(parameter, encoding="utf-8") as file:
                _token = file.readlines()[0]
        except Exception as error:
            raise error
    else:
        _token = parameter
    return _token


if __name__ == "__main__":
    args = clparser().parse_args()
    api_token = args.api_token
    img_path = args.img_path
    verbose = args.verbose
    if verbose:
        log.addHandler(logging.StreamHandler())

    token = get_token(api_token)
    endpoint = f"https://api.nasa.gov/planetary/apod?api_key={token}"
    url = get_apod(endpoint)
    if url:
        save_img(url, img_path)
