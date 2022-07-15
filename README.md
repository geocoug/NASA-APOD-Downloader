# nasa_apod_dl

[![GitHub Super-Linter](https://github.com/geocoug/nasa-apod-dl/workflows/lint%20code%20base/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![license](https://img.shields.io/github/license/geocoug/nasa-apod-dl)

Download the 🚀 NASA 🚀 Astronomy Picture of the Day (APOD).

## Usage

1. Set the `FPATH` variable to the path where to save APOD download.

1. Set the `API_KEY_FILE` variable to the file path containing your NASA API key.

### Using a Python virtual environment

1. Create Python venv: `python3 -m venv venv && source ./venv/bin/activate`

1. Install dependencies: `python -m pip install -r requirements.txt`

1. Run the script: `python nasa_apod_dl.py`
