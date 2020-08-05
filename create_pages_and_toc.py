from config import LAC_NODE_ID
from parsers import parseDoaj, getGuid

articles=parseDoaj('xml/doaj.xml')
print(articles)

TOC=''
for a in articles:
    names=[]
    authors_list=[]
    for au in a['authors']:
        names.append(au['name'])
        authors_list.append(f"*{au['name']}*  \n{au['affiliation']}")
    author_block='\n\n'.join(authors_list)
    id = a['doi'].string[8:len(a['doi'])]

    TOC=f"{TOC}\n\n [{a['title']}](https://osf.io/{LAC_NODE_ID}/wiki/{id}).\n {', '.join(names)}"

    article_md=f"*{a['title']}.* LAC 2014 proceedings, [S.l.], oct. 2016. doi: https://dx.doi.org/{a['doi']}\n\n" \
               f"### Abstract ###\n{a['abstract']}\n\n" \
               f"[pdf](https://osf.io/{getGuid(id)})\n\n" \
               f"### Authors ####\n{author_block}"

    with open(f"output/{id}.md", 'w', encoding="utf8") as f:
        f.write(article_md)


with open("output/TOC.md", 'w', encoding="utf8") as f:
    f.write(TOC)