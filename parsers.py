import json
from config import NAME_GUID_FILE
from bs4 import BeautifulSoup
import lxml


def stripSpaces(str):
    return " ".join(str.split())


def parseDoaj(xmlFile="xml/doaj.xml"):
    with open(xmlFile, encoding="utf8") as fp:
        soup = BeautifulSoup(fp, "xml")
        articles = []
        for r in soup.find_all("record"):
            authors = []
            for au in r.find_all("author"):
                if au.affiliationId != None:
                    affiliation = r.find('affiliationName', {'affiliationId': au.affiliationId.string}).string
                # name is reserved word
                authors.append({'name': f'{au.find("name").string}', 'affiliation': stripSpaces(affiliation)})
            abstract = '\-'
            if r.abstract != None:
                abstract = stripSpaces(r.abstract.string)
            articles.append({
                'title': stripSpaces(r.title.string),
                'doi': r.doi.string,
                'abstract': abstract,
                'authors': authors
            })
        return articles


def parsePubmed(xmlFile="xml/pubmed.xml"):
    with open(xmlFile, encoding="utf8") as fp:
        soup = BeautifulSoup(fp, "xml")
        articles = []
        for a in soup.find_all("Article"):
            authors = []
            for au in a.find_all("Author"):
                affiliation = ''
                if au.Affiliation != None:
                    affiliation = au.Affiliation.string
                authors.append(
                    {'name': f'{au.LastName.string}, {au.FirstName.string}', 'affiliation': stripSpaces(affiliation)})
            abstract = '\-'
            if a.Abstract != None:
                abstract = stripSpaces(a.Abstract.string)
            articles.append({
                'title': stripSpaces(a.ArticleTitle.string),
                'doi': a.ELocationID.string,
                'abstract': abstract,
                'authors': authors
            })
        return articles


def getGuid(id):
    with open(NAME_GUID_FILE) as json_file:
        data = json.load(json_file)
        for d in data:
            if d['name'] == f'{id}.pdf':
                return d['guid']
