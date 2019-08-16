import praw
import pprint
import requests
import re
import yaml
import time
from anyOfListAreInString import anyOfListAreInString
import os


class PrawRequest:

    def __init__(self):
        self.config = yaml.safe_load(open("conf.yml"))

    typesOfImages = ['jpeg', 'jpg', 'png']
    titleLength = 20
    redditLinks = ['reddit', 'redd.it']
    fileRegex = r'[ ":;.,|<>{}+=/\\\'’?!*#@$%()&]'

    def __downloadImageResults(self, submission, r, sub):
        if not os.path.exists("images/" + sub):
            os.makedirs("images/" + sub)
        for imageType in self.typesOfImages:
            if imageType in r.headers.get('content-type').lower():
                name = re.sub(self.fileRegex, "",
                              submission.title.lower())
                open("images/" + sub + "/" + name[0:self.titleLength] + '.' +
                     imageType, 'wb').write(r.content)
                print(submission.title)

    def __downloadSelfTextResults(self, submission, r, sub):
        if not os.path.exists("selfText/" + sub):
            os.makedirs("selfText/" + sub)
        name = re.sub(self.fileRegex, "",
                      submission.title.lower())
        open("selfText/" + sub + "/" + name[0:self.titleLength] + '.' +
             'txt', 'wb').write(submission.selftext)
        print(submission.title)

    def __saveLink(self, submission, sub):
        with open("links.txt", "a") as myfile:
            myfile.write(submission.url + "\n")
        print(submission.title)

    def req(self, sub: str, amount: int, types: list):
        redditRequest = praw.Reddit(
            client_id=self.config['praw_conf']['id'],
            client_secret=self.config['praw_conf']['secret'],
            user_agent=self.config['praw_conf']['user_agent']
        )

        for submission in redditRequest.subreddit(sub).hot(limit=amount):
            r = requests.get(submission.url, headers={
                             'User-agent': self.config['praw_conf']['user_agent']}, allow_redirects=True)
            if 'images' in types and 'image' in r.headers.get('content-type').lower():
                print("-Image- " + sub)
                self.__downloadImageResults(submission, r, sub)
                print("-----------------")
            if 'selfText' in types and submission.selftext != "":
                print("-Self Text- " + sub)
                self.__downloadSelfTextResults(submission, r, sub)
                print("-----------------")
            if 'link' in types and not anyOfListAreInString(submission.url, self.redditLinks):
                print("-Link Post- " + sub)
                self.__saveLink(submission, sub)
                print("-----------------")
