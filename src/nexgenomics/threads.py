# src/nexgenomics/threads.py

import os
import requests


def _get_api_url_stem():
    return os.getenv("API_URL_STEM", "https://agenstore.nexgenomics.ai")
def _get_api_auth_token():
    return os.getenv("API_AUTH_TOKEN", "not_a_valid_token")


class Thread:
    """
    """
    def __init__(self, *, threadid):
        self.threadid = threadid
    def __repr__(self):
        return f"Thread({self.threadid!r})"

def ping():
    """
    """
    url = f"{_get_api_url_stem()}/api/v0/ping"
    headers = {
        "Authorization": f"Bearer {_get_api_auth_token()}",
    }
    resp = requests.get(url,headers=headers)
    if resp.status_code != 200:
        raise Exception (f"status code {resp.status_code}")
    return resp.json()

def new(*,metadata={},title):
    """
    """
    #url = "https://agentstore.nexgenomics.ai/api/v0/threads"
    url = f"{_get_api_url_stem()}/api/v0/thread"
    data = {
        "metadata":metadata,
        "title":title,
    }
    headers = {
        "Authorization": f"Bearer {_get_api_auth_token()}",
    }
    resp = requests.put(url,json=data,headers=headers)
    if resp.status_code != 200:
        raise Exception (f"status code {resp.status_code} {resp.json()["msg"]}")
    t = resp.json()
    return Thread(threadid=t["thread_id"])
