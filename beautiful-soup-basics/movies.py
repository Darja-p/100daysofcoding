# scraping 100 best movies from empire magazine and saving them in txt file (in an ascending order)

import requests
from bs4 import BeautifulSoup

url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=url)
if response.status_code != 200:
	print("Error fetching page")
	exit()
else:
    content = response.text

soup = BeautifulSoup(content, "html.parser")

# getting all the title from the webpage (ordered descending)
titles =[title.getText().split(") ")[-1] for title in soup.find_all(name="h3", class_="title")]
#print(titles)

# sorting list so we have movies in ascending order
titles_sorted = [x for x in titles[::-1]]
#print(titles_sorted)

# saving titles to the separate file
with open("100_best_movies.txt", "w") as f:
    for i, title in enumerate(titles_sorted):
        f.writelines(f"{i+1}. {title}\n")


