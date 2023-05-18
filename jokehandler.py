import requests

#https://foolishdeveloper.com/random-joke-generator-using-javascript-api/
#https://v2.jokeapi.dev/#url-parameters

#Hämtar giltiga personnummer frå skatteverket 
#Anväder Thunder client för att testa request
#pip install requests
#python.exe -m pip install --upgrade pip

class Jokehandler:

    def __init__(self, adress):
        self.adress = adress

    def get_joke(self):
        req = requests.get(self.adress)
        json_data = req.json()
        joke = json_data['joke']

        return joke

        #personnummer = list_results[0]['testpersonnummer'] 