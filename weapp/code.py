import requests
import json
url = "https://shazam.p.rapidapi.com/search"

querystring = {"term":"kiss the rain","locale":"en-US","offset":"0","limit":"5"}

headers = {
    'x-rapidapi-key': "50be966fe8mshb2163444b4be156p108766jsn838dd20bc6e3",
    'x-rapidapi-host': "shazam.p.rapidapi.com"
    }



response = requests.request("GET", url, headers=headers, params=querystring).json()
print(response)
to_search = "Falling"


for hit in response['tracks']['hits']:
    # if hit['track']['title'].find(to_search)!=-1:
    if hit['track']['title'].lower().find(to_search.lower())!=-1:
        print(hit['track']['title'])