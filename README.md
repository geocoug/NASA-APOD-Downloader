# nasa_apod_dl

[![Docker](https://github.com/geocoug/nasa-apod-dl/workflows/docker%20build/badge.svg)](https://github.com/geocoug/nasa-apod-dl/actions)
[![GitHub Super-Linter](https://github.com/geocoug/nasa-apod-dl/workflows/lint%20code%20base/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![license](https://img.shields.io/github/license/geocoug/nasa-apod-dl)

Download the NASA Astronomy Picture of the Day (APOD).

## Usage

1. Set the `fpath` variable to the path where to save APOD download.

1. Set the `api_key_file` variable to the file path containing your NASA API key.

1. Run the script:

-   `python3 nasa_apod_dl.py`

**Or**

-   `docker build -t nasa-apod-dl .`

-   `docker run --rm -it -v $(PWD)/nasa.txt:/usr/src/app/nasa.txt nasa-apod-dl`
