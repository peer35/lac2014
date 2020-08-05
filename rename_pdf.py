import shutil
from bs4 import BeautifulSoup
import lxml
from config import PDF_PATH, CROSSREF_FILE


with open(CROSSREF_FILE, encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "xml")
    doi_data = soup.find_all("doi_data")
    for d in doi_data:
        id = d.doi.string[8:len(d.doi.string)]
        print(id)
        f = d.resource.string[-2:]
        filename = f'{f}-{f}-1-PB.pdf'
        print(filename)
        old_name = f'{PDF_PATH}/{filename}'
        new_name = f'{PDF_PATH}/renamed/{id}.pdf'
        shutil.copy(old_name, new_name)
