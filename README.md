# groupjets
GroupMe bot to get [suitedeals](https://www.jetsuite.com/suitedeals) posted to your group automatically.
Uses dynamoDB for persistence.



## groupme.py
Simple bot class that can post messages to whatever group the bot is currently in.

## jetsuite.py
Scraper for jetsuite that grabs information about all the suitedeals

## usage
```python
myBot = GroupMeBot(BOT_KEY)
jetsuiteAPI = JetSuite()

deals = jetsuiteAPI.getSuiteDeals()

for deal in deals:
  myBot.sendMessage("jetsuite from {} to {} at {}!".format(deal.fromLoc, deal.toLoc, deal.time))
```
