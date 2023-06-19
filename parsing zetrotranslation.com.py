import requests
from bs4 import BeautifulSoup
import re

url = input() # url of chapter, like https://zetrotranslation.com/novel/the-case-in-which-streaming-in-another-world-led-to-the-creation-of-a-massive-yandere-following/01-im-a-streamer/
answer = requests.get(url=url)
number_chapter = re.findall(r"\d?\d", url)[0]
status_code_site = answer.status_code  # 200
bs = BeautifulSoup(answer.text, "lxml")
text1 = bs.find("div", "text-left")
work_text = text1.text.split("\n")
with open(f"chapter_{number_chapter}.txt", "w", encoding="utf-8") as file:
    for item in work_text:
        item = re.sub(" ", "", item)
        file.write(item)
        file.write("\n")
