from boto.dynamodb2.exceptions import ItemNotFound
from jetsuite import JetSuite
from boto.dynamodb2.table import Table
import secrets
from groupme import GroupMeBot

dealsTable = Table('suitedeals')

def main():
    jetsuite = JetSuite()
    bot = GroupMeBot(secrets.BOT_ID)
    deals = jetsuite.getSuiteDeals()
    for deal in deals:
        try:
            dealsTable.get_item(id=deal.id)
        except ItemNotFound:
            if 'Vegas' in deal.fromLoc:
                bot.sendMessage(getMessageFromDeal(deal))
            storeDeal(deal)


def getMessageFromDeal(deal):
    return 'from {} to {} | {} passengers | {}'.format(deal.fromLoc, deal.toLoc, deal.seats, deal.time)

def storeDeal(deal):
    item = {
        'id': deal.id,
        'from': deal.fromLoc,
        'to': deal.toLoc,
        'date': deal.date,
        'time': deal.time,
        'seats': deal.seats,
        'price': deal.price
    }
    dealsTable.put_item(data=item, overwrite=True)


if __name__ == '__main__':
    main()