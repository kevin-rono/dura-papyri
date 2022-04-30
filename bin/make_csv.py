import base64
import json
import os

import pandas as pd
import requests
import xmltodict
from bs4 import BeautifulSoup
from tqdm.auto import tqdm


def get_subject(xml):
    subject = xml["TEI"]["teiHeader"]["profileDesc"]["textClass"]["keywords"]["term"]
    if isinstance(subject, str):
        return subject
    result = recurse(subject)
    assert len(result) > 0
    return " ".join(result)


def recurse(data):
    result = []
    if isinstance(data, list) and all([isinstance(x, str) for x in data]):
        return data
    for x in data:
        if isinstance(x, dict):
            subresult = recurse(x)
            result.extend(subresult)
        elif x == "#text":
            result.append(data[x])
    return result


def get_name(xml):
    return xml["TEI"]["teiHeader"]["fileDesc"]["publicationStmt"]["idno"][3]["#text"]


def get_date(xml):
    date = xml["TEI"]["teiHeader"]["fileDesc"]["sourceDesc"]["msDesc"]["history"][
        "origin"
    ]["origDate"]
    if isinstance(date, list):
        date = " ".join([x["#text"] for x in date])
    else:
        date = date["#text"]
    return date


def get_content(xml):
    return xml["TEI"]["teiHeader"]["fileDesc"]["titleStmt"]["title"]


def get_image_url(xml):
    image_url = ""
    divs = xml["TEI"]["text"]["body"]["div"]
    for div in divs:
        if div["@type"] == "figure":
            try:
                image_url = div["p"]["figure"]["graphic"]["@url"]
            except:
                image_url = div["p"]["figure"][0]["graphic"]["@url"]
    try:
        _, suffix = image_url.split("&key=")
        xml_url = f"https://papyri.info/apis/{suffix}/source"
        response = requests.get(xml_url)
        xml = xmltodict.parse(response.content)
    except:
        return image_url
    for div in xml["TEI"]["text"]["body"]["div"]:
        if isinstance(div, dict) and div["@type"] == "figure":
            image_url = div["p"]["figure"]["graphic"]["@url"]
            break
    assert image_url
    response = requests.get(image_url)
    soup = BeautifulSoup(response.content, "html.parser")
    try:
        return soup.find("div", class_="showComplex").find("a").find("img")["src"]
    except:
        return image_url


def get_image(image_url):
    if isinstance(image_url, str) and "imageserver" in image_url:
        return base64.b64encode(requests.get(image_url).content)
    return ""


def get_material(xml):
    return xml["TEI"]["teiHeader"]["fileDesc"]["sourceDesc"]["msDesc"]["physDesc"][
        "objectDesc"
    ]["supportDesc"]["support"]["material"]


def get_origin(xml):
    return xml["TEI"]["teiHeader"]["fileDesc"]["sourceDesc"]["msDesc"]["history"][
        "origin"
    ]["origPlace"]


def main():
    fields = []
    with open(os.path.join("raw", "xmls.json")) as f:
        xmls = json.load(f)
    for id_, xml in tqdm(xmls.items()):
        data = {"id": id_}
        data["content"] = get_content(xml)
        data["name"] = get_name(xml)
        data["subject"] = get_subject(xml)
        data["date"] = get_date(xml)
        data["image_url"] = get_image_url(xml)
        data["image"] = get_image(data["image_url"])
        data["material"] = get_material(xml)
        data["origin"] = get_origin(xml)
        fields.append(data)
    df = pd.DataFrame(fields)
    df.to_csv(os.path.join("raw", "data.csv"))


if __name__ == "__main__":
    main()
