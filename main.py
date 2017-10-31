from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as u_req

twitter_name = input("Enter the twitter username: ")
url          = "https://twitter.com/" + twitter_name

# Opens the connection and grabs the page
u_client  = u_req(url)
page_html = u_client.read()
u_client.close()

# Converts the page to html (parsing)
page_soup  = soup(page_html, "html.parser")
containers = page_soup.find_all("div", {"class": "content"})

with open("Twitter-Info.csv", "w") as f:
    headers = twitter_name + ", Their Tweet\n"
    f.write(headers)

    for counter, current_tweet in enumerate(containers):
        tweet = containers[counter].p.text
        f.write( str(counter) + "," + tweet.replace(",", ";") + "\n")
        print("----------")
        print(counter + 1, ": " , tweet)
