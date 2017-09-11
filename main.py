import bs4

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

twitterName = input("Enter the twitter userName: ")
url = "https://twitter.com/" + twitterName

#Opens the connection and grabs the page
uClient = uReq(url)
page_html = uClient.read()
uClient.close()


#Converts the page to html (parsing)
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "content"})
filename = "Twitter-Info.csv"
f = open(filename, "w")
headers = twitterName + ", Their Tweet\n"

f.write(headers)
counter = 0
for currentTweet in containers:

    tweet = containers[counter].p.text
    f.write( str(counter) + "," + tweet.replace(",", ";") + "\n")
    print("----------")
    print(counter + 1, ": " , tweet)
    counter = counter + 1



f.close()