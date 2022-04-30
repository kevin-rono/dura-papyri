import time

from googletrans import Translator
from langdetect import detect

translator = None


def split_years(years):
    if " - " in years:
        start, end = years.split(" - ")
        return int(start), int(end)
    return int(years), int(years)


def parse_date(date):
    date = date.strip()
    for year_type in [" A.D.", " B.C."]:
        if year_type in date:
            years = date.split(year_type)[0]
            start, end = split_years(years)
            if year_type == " B.C.":
                return -start, -end
            return start, end


def to_english(text):
    if detect(text) == "en":
        return text
    global translator
    if translator is None:
        translator = Translator()
    # NOTE: prevent google translate from blocking ip
    time.sleep(0.5)
    return translator.translate(text).text
