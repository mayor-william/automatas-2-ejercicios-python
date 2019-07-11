from bs4 import BeautifulSoup
from collections import Counter
import requests

soup = BeautifulSoup(requests.get("https://itcolima.edu.mx/www/").text, "html.parser")

foundUrls = Counter([link["href"] for link in soup.find_all("a", href=lambda href: href and not href.startswith("#"))])
foundUrls = foundUrls.most_common()

for item in foundUrls:
    print ("%s: %d" % (item[0], item[1]))