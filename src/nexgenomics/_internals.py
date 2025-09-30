
import os


def _get_api_url_stem():
    return os.getenv("API_URL_STEM", "https://agentstore.nexgenomics.ai")
def _get_api_auth_token():
    if a := os.getenv("API_AUTH_TOKEN"):
        return a
    return "not_a_valid_token"

def _handle_api_error(resp):
    if resp.status_code != 200:
        try:
            msg = resp.json()["msg"]
        except:
            msg = ""
        raise Exception (f"status code {resp.status_code} {msg}")

