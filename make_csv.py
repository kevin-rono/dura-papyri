import json
import os

import pandas as pd


def get_subject(xml):
    subject = xml["TEI"]["teiHeader"]["profileDesc"]["textClass"]["keywords"]["term"]
    if isinstance(subject, str):
        return subject
    result = recurse(subject)
    assert len(result) > 0
    return " ".join(result)
    # return " ".join([x for x in result if x not in {"literature", "classical", "prose"}])


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
    divs = xml["TEI"]["text"]["body"]["div"]
    for d in divs:
        if d["@type"] == "figure":
            try:
                return d["p"]["figure"]["graphic"]["@url"]
            except:
                return d["p"]["figure"][0]["graphic"]["@url"]


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
    for id_, xml in xmls.items():
        data = {"id": id_}
        data["content"] = get_content(xml)
        data["name"] = get_name(xml)
        data["subject"] = get_subject(xml)
        data["date"] = get_date(xml)
        data["image_url"] = get_image_url(xml)
        data["material"] = get_material(xml)
        data["origin"] = get_origin(xml)
        fields.append(data)
    df = pd.DataFrame(fields)
    df.to_csv(os.path.join("raw", "data.csv"))


if __name__ == "__main__":
    main()
