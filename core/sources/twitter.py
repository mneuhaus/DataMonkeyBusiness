from twython import Twython
import logging
from DataMonkeyBusiness.settings import *

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

twitterApi = Twython(TWITTER_APP_KEY, TWITTER_APP_SECRET, TWITTER_OAUTH_TOKEN, TWITTER_OAUTH_TOKEN_SECRET)

def get_results(search):
    response = twitterApi.search(q=search, lang='en', count=100)
    for status in response['statuses']:
        #print(status['text'])
        logging.info('Processing Tweet: %s' % status['text'])