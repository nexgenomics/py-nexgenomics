# src/nexgenomics/images.py


import requests
from . import _internals


def get_images():
    url = f"{_internals._get_api_url_stem()}/api/v0/images"
    headers = {"Authorization": f"Bearer {_internals._get_api_auth_token()}"}
    resp = requests.get(url,headers=headers)
    _internals._handle_api_error(resp)
    return resp.json()
