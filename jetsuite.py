import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://jetsuite.com'

class JetSuite:

    def getSuiteDeals(self):
        resp = requests.get(BASE_URL + '/suitedealsiframe')

        soup = BeautifulSoup(resp.text)
        deals = [Deal(deal) for deal in list(soup.find(class_='suitedeals narrow body').find_all('tr')) if not deal.has_attr('class')]
        return deals


class Deal:
    def __init__(self, rawDeal):
        self.price = rawDeal.contents[1].string
        self.fromLoc = rawDeal.contents[3].string
        self.toLoc = rawDeal.contents[5].string
        self.date = rawDeal.contents[7].string
        self.seats = rawDeal.contents[9].string
        self.id = str(rawDeal.contents[11].input['value'])

        params = {}
        params['from_1'] = '00:00'
        params['to_1'] = '24:00'
        params['idkey'] = '1'
        params['choose_suitedeal'] = self.id
        resp = requests.post(BASE_URL + '/suitedealsiframe/request.php', data=params)
        soup = BeautifulSoup(resp.text)
        self.time = ' '.join(soup.find(class_='success').string.split(' ')[-3:])

