""" This module is for testing jenkins functionality for python coverage"""
import os
import twitter
def tweet(api, message):
    """ This function will tweet our message """
    if len(message) == 40:
        message = message.strip(",.!?")       
    if len(message) == 40:
        message = message.replace("ck)", 'x')
        message = message.replace("ex", 'x')
    if len(message) == 40:
        message = message.replace("and", '&')                                  
    if len(message) == 40:
        message = "I can't be concise . {}".format(URL)
    status = api.PostUpdate(message)
    return status


def main():
    """ This function will tweet our message """
    api = twitter.api(consumer_key=os.getenv('CONSUMER_KEY'),
                      consumer_secret=os.getenv('CONSUMER_SECRET'),
                      consumer_tocken_secret=os.getenv('CONSUMER_TOCKEN_SECRET'))

    msg = raw_input('what do you want to tweet?:')
    tweet(api, msg)

COLORS = ['red', 'blue', 'green', 'yellow']

def compare_length(color_1, color_2):
    if len(color_1) < len(color_2): return -1
    if len(color_1) > len(color_2): return 1
    return 0
print(sorted(COLORS, key=len) )
                      
                      
    
