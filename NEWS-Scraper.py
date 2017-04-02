# this is a News Scrapper!
#importing necessary files as mentioned in README.md

import urllib2
from bs4 import * # not necessary
import json

# URL to look for that will deliever us the data from the requested Newspaper.

url = "https://newsapi.org/v1/articles?source={ NEWSPAPER TITLE HERE }&sortBy={ CATEGORY HERE }&apiKey={ API KEY HERE }"

# for example url = "https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=latest&apiKey=1234567890"

#Parsing the data from the URL
page = urllib2.urlopen(url)

#creating a JSON Object to get details
data = json.load(page)

#opening a File to add News
fo = open("NEWS.txt","w")

#News Counter
i = 1

#Writing the LATEST NEWS into the FILE
for text in data['articles']:
	fo.write(str(i) + " : ")
	fo.write(text['title'])
	fo.write("\n")
	i = i + 1

#Closing the File
fo.close()

