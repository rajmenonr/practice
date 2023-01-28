import requests
import json

url = "https://test-mobile-configuration-files.s3.eu-central-1.amazonaws.com/stories-test/shelf.json"

resp = requests.get(url)
print(resp.status_code)
jresp = resp.json()['_embedded']
count = 0
ti = []
for i in jresp.values():


    for j in i:
        x = isinstance(j['content'],dict)
        if x == True:
                if 'title' in (j['content'].keys()):
                    ti.append(j['content']['title'])

assert "Frühplaner sind klar im Vorteil!" in ti
assert "Top Angebote" in ti


