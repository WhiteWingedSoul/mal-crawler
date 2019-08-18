import requests
import os
import json
import datastore
from lxml import html

user_name = os.getenv("MAL_USERNAME")

def execute(event, context):
    page = requests.get(f'https://myanimelist.net/animelist/{user_name}?status=7')
    tree = html.fromstring(page.text)
    html_element = tree.xpath(".//table[@class='list-table']")
    data = json.loads(html_element[0].attrib['data-items'])
    datastore.store_object(data)

if __name__ == "__main__":
    execute(None, None)