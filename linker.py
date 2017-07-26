import requests
import json
from bs4 import BeautifulSoup

def songwhip_it(url):
    html = requests.get('https://songwhip.com/'+url).content
    soup = BeautifulSoup(html, 'html.parser')
    links_text = list(soup.findAll('script'))[2].get_text()
    links_json = json.loads(links_text[links_text.index('{'):-1])['links']
    return links_json

songwhip_it("https://open.spotify.com/track/4Aep3WGBQlpbKXkW7kfqcU")
