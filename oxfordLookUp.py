import requests
from pprint import pprint as print


def oxfordLookUp(word):
    # word = 'Great'
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    response = requests.get(url)
    resp = response.json()
    list_of_resp = []

    if not response.status_code == 200:
        list_of_resp.append('xatolik qaytadan kiriting')
    else:
        audio = resp[0]['phonetics'][0]['audio']
        defin = resp[0]['meanings'][0]['definitions'][0]['definition']

        list_of_resp.append(audio)
        list_of_resp.append(defin)
        # print(audio)
        # print(defin)

    return list_of_resp
# nev = oxfordLookUp('Great')