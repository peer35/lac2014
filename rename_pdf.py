import shutil
from bs4 import BeautifulSoup
import lxml

pdf_path='c:/Users/peter/Documents/lac2014/pdf'

with open("xml/crossref.xml", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "xml")
    doi_data=soup.find_all("doi_data")
    for d in doi_data:
        id = d.doi.string[8:len(d.doi.string)]
        print(id)
        f=d.resource.string[-2:]
        filename=f'{f}-{f}-1-PB.pdf'
        print(filename)
        old_name=f'{pdf_path}/{filename}'
        new_name=f'{pdf_path}/renamed/{id}.pdf'
        shutil.copy(old_name, new_name)
