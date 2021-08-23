import requests

ip = 'ip of the rest api container in docker'
BASE = f'http://{ip}:5000/predict'


class BUTTON:
    def __init__(self, click):
        self.click = click

    def isNew(self, newClick):
        if (self.click == newClick):
            return False
        elif ((newClick == 0) | (newClick == None)):
            return False
        else:
            self.click = newClick
            return True

predictBUTTON = BUTTON(0)



def restPred(age, mil, bodytype, spoiler, trim):
    response = requests.post(BASE, json={
                'age': age,
                'Mil': mil,
                'Bodytype' : bodytype,
                'Spoiler': spoiler,
                'Trim' : trim,
        })

    prediction = response.json()
    return prediction['Price']