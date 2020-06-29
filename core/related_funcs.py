import requests
from bs4 import BeautifulSoup

from core.models import LostDocuments


def process_file():
    r = requests.get("https://data.gov.ua/dataset/ab09ed00-4f51-4f6c-a2f7-1b2fb118be0f")
    soup = BeautifulSoup(r.text, 'html.parser')

    for s in soup.find_all("th"):
        if s.get_text() == "Структура набору данних":
            url = s.next_sibling.next_sibling.contents[1].get("href")

            r = requests.get(f"https://data.gov.ua/{url}")
            data = r.json()["resources"]
            for d in data[:1]:
                if "Shema" not in d["name"]:
                    req = requests.get(d["path"])
                    return req.json()


def upload_docs():
    for doc in process_file():
        LostDocuments.objects.create(identifier=doc["ID"],
                                     series=doc["D_SERIES"],
                                     doc_num=doc["D_NUMBER"],
                                     type=doc["D_TYPE"],
                                     status=doc["D_STATUS"],
                                     loss_date=doc["THEFT_DATA"],
                                     reg_date=doc["INSERT_DATE"],
                                     authority=doc["OVD"])