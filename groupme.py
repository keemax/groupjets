import requests
import json

BASE_URL = 'https://api.groupme.com/v3'

class GroupMeBot:
    def __init__(self, botId):
        self.botId = botId

    def sendMessage(self, msg):
        params = {}
        params['bot_id'] = self.botId
        params['text'] = msg
        requests.post(BASE_URL + '/bots/post', data=json.dumps(params))