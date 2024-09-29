import requests

NINJA_API = "LPBDCymlX3maYlUMhd7GDA==EiLvpCDgS6M3aQTJ"

def import_quote(category = ""):
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': NINJA_API})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        print("Error:", response.status_code, response.text, flush=True)
        

def import_riddle():
    api_url = 'https://api.api-ninjas.com/v1/riddles'
    response = requests.get(api_url, headers={'X-Api-Key': NINJA_API})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        print("Error:", response.status_code, response.text, flush=True)
        

def import_trivia(category = ""):
    api_url = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': NINJA_API})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        print("Error:", response.status_code, response.text, flush=True)

def import_joke():
    api_url = 'https://api.api-ninjas.com/v1/jokes'
    response = requests.get(api_url, headers={'X-Api-Key': NINJA_API})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        print("Error:", response.status_code, response.text, flush=True)

def import_dad_joke():
    api_url = 'https://api.api-ninjas.com/v1/dadjokes'
    response = requests.get(api_url, headers={'X-Api-Key': NINJA_API})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        print("Error:", response.status_code, response.text, flush=True)
        
def import_fact():
    api_url = 'https://api.api-ninjas.com/v1/facts'
    response = requests.get(api_url, headers={'X-Api-Key': NINJA_API})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        print("Error:", response.status_code, response.text, flush=True)
        