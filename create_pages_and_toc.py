from bs4 import BeautifulSoup
import lxml
from config import LAC_NODE_ID

def stripSpaces(str):
    return " ".join(str.split())

def parsePubmed(xmlFile="xml/pubmed.xml"):
    with open(xmlFile, encoding="utf8") as fp:
        soup = BeautifulSoup(fp, "xml")
        articles = []
        for a in soup.find_all("Article"):
            authors = []
            for au in a.find_all("Author"):
                affiliation=''
                if au.Affiliation!=None:
                    affiliation=au.Affiliation.string
                authors.append({'name': f'{au.LastName.string}, {au.FirstName.string}', 'affiliation': stripSpaces(affiliation)})
            abstract=''
            if a.Abstract!=None:
                abstract=stripSpaces(a.Abstract.string)
            articles.append({
                'title': stripSpaces(a.ArticleTitle.string),
                'doi': a.ELocationID.string,
                'abstract': abstract,
                'authors': authors
            })
        return articles

articles=parsePubmed('xml/pubmed.xml')

TOC=''
for a in articles:
    names=[]
    for au in a['authors']:
        names.append(au['name'])
    id = a['doi'].string[8:len(a['doi'])]
    TOC=f"{TOC}\n\n [{a['title']}](https://osf.io/{LAC_NODE_ID}/wiki/{id}).\n {', '.join(names)}"

print(TOC)
with open("TOC.md", 'w', encoding="utf8") as f:
    f.write(TOC)