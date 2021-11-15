import requests

from src.shared.logger import with_logging

DEFAULT_TIMEOUT = 2


# Can also wrap this function to send Influx DB metrics and such
@with_logging
def get(url: str, **kwargs):
    response = requests.get(url, **kwargs, timeout=DEFAULT_TIMEOUT)
    response.raise_for_status()
    return response
