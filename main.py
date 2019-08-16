import prawRequest
import time
import yaml

repeatInterval = 86400
amountOfImages = 1
config = yaml.safe_load(open("conf.yml"))


# conf.yml take precedence over passed parameters
if 'repeating' in config['praw_conf'] and config['praw_conf']['repeating'] is True:
    repeating = True

if 'repeat_interval' in config['praw_conf']:
    repeatInterval = config['praw_conf']['repeat_interval']

if 'amount' in config['praw_conf']:
    amountOfImages = config['praw_conf']['amount']


def requests():
    prawRequest.PrawRequest().req("art", amountOfImages, ["images"])
    prawRequest.PrawRequest().req("pics", amountOfImages, ["images"])
    prawRequest.PrawRequest().req("pic", amountOfImages, ["images"])
    prawRequest.PrawRequest().req("pictures", amountOfImages, ["images"])
    prawRequest.PrawRequest().req("images", amountOfImages, ["images"])

    if repeating:
        print("Repeating in " + str(repeatInterval) + " seconds")
        time.sleep(repeatInterval)
        requests()


requests()
