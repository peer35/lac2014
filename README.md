## Migrate http://lac2014proceedings.nl/ to OSF
1. Copy `config.template.py` to `config.py`, make sure you have an OSF API token and the
guid of your OSF project.  
1. In OJS export issue metadata in crossref and doaj xml formats and store to the paths
 in `config.py` (`DOAJ_FILE` and `CROSSREF_FILE`)
1. Download the article pdf files from the OJS server.
1. Rename article PDF files in `PDF_PATH` with `rename_pdf.py`. This will use the Crossref XML to 
copy to `<PDF_PATH>/renamed/<doi suffix>.pdf`
1. Upload the renamed pdf files to OSF.
1. Run `osf_guid_list.py` to get the OSF file guids. Will be stored in `output/name_guid.json` (`NAME_GUID_FILE`)
1. Run `create_pages_and_toc.py`. This will create wiki pages on OSF with article 
metadata and a link to the pdf and a table of contents in `TOC.md` which can be pasted to
  the wiki home page.
1. Run `modify_crossref.py`. This will create `output/crossref_osf.xml`, a copy
 of `xml/crossref.xml` with the URLs changed to the new OSF locations. 
1. Upload xml-file to Crossref.
