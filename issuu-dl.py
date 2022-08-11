#!/usr/bin/python3
# ISSUU downloader

import urllib3

uri = "https://issuu.com/AUTHOR/docs/DOCUMENT"

readerBaseUri = "https://reader3.isu.pub"
readerJsonUri = "reader3_4.json"

parsed = urllib3.util.parse_url(uri)

path = parsed.path.split("/")
author = path[-3]
document = path[-1]

readerFileUri = f"{readerBaseUri}/{author}/{document}/{readerJsonUri}"
http = urllib3.PoolManager()
resp = http.request("GET", readerFileUri)

print(resp.data)