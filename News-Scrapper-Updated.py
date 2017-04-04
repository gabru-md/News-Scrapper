import os
import time
import urllib2
import json

url = "https://newsapi.org/v1/articles?source=the-hindu&sortBy={ CATEGORY HERE }&apiKey={ API KEY HERE }"
url1 = "https://newsapi.org/v1/articles?source=the-times-of-india&sortBy={ CATEGORY HERE }&apiKey={ API KEY HERE }"


page = urllib2.urlopen(url1)
page1 = urllib2.urlopen(url)
print "Establishing Connection"

time.sleep(1)



data = json.load(page)
data1 = json.load(page1)
print "Parsing Data"


fo = open("NEWS-FEED.txt","w")


time.sleep(1)

#for p in range(100):
#	print "\n"
 
i = 1

print "\n"

print "------------------------NEWS FROM THE TIMES OF INDIA------------------------"
raw_input()
fo.write("------------------------NEWS FROM THE TIMES OF INDIA------------------------\n\n")

for text in data['articles']:
	print str(i) + " : " + text['title'].encode('utf-8') + "\nDescription : " + text['description'].encode('utf-8') + "\n"
	raw_input()
	fo.write( str(i) + " : " + text['title'].encode('utf-8') + "\nDescription : " + text['description'].encode('utf-8') + "\n\n" )
	i= i + 1
i = 1

print "------------------------NEWS FROM THE HINDU------------------------"
raw_input()
fo.write("\n------------------------NEWS FROM THE HINDU------------------------\n\n")

for text in data1['articles']:
	print str(i) + " : " + text['title'].encode('utf-8') + "\nDescription : " + text['description'].encode('utf-8') + "\n"
	raw_input()
	fo.write( str(i) + " : " + text['title'].encode('utf-8') + "\nDescription : " + text['description'].encode('utf-8') + "\n\n" )
	i = i + 1
temp = raw_input()
