from bs4 import BeautifulSoup
import requests


def fetch_page(url):
    try:
        req = requests.get(url)
        if req.status_code != 200:
            req.raise_for_status()
        else:
            return req
    except requests.exceptions.HTTPError as e:
        raise e
    except requests.RequestException as e:
        raise e


def parse(url, **settings):
    req = fetch_page(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    test = {field: ''.join(
        map(lambda x: str(x.text), soup.select(selector=selector)) if soup.select(selector=selector)
        else ["None"]) for (field, selector) in settings.items()}
    return test
