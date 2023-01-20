#scraping news from news.ycombinator.com - printing out the most popular article name, votes and link to it

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
if response.status_code != 200:
	print("Error fetching page")
	exit()
else:
	content = response.text
soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())

# finding html items with css  selector
articles = soup.select(selector=".titleline")
article_names = []
article_links = []
votes = []

# parsing and adding to lists all articles names and links
for article in articles:
    name = article.a.string
    link = article.a.get("href")
    article_names.append(name)
    article_links.append(link)

# searching for all elements with score and adding them to a list
upvotes = soup.find_all(name="span", class_="score")
for upvote in upvotes:
    vote = upvote.getText()
    vote = vote.split(" ")
    votes.append(int(vote[0]))

# finding highest score
highest_vote = max(votes)
index = votes.index(highest_vote)

# printing name and link of an article with the highest score
print(article_names[index],"\n", article_links[index], "\n", "Votes:",highest_vote)


