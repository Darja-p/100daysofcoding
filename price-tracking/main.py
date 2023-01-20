# web scraping the price of a bookcase from amazon and if it's below 110$, sending an email

import requests
from bs4 import BeautifulSoup
import smtplib
import os


url = "https://www.amazon.com/Sauder-Coral-Cape-Bookcase-Finish/dp/B08XY8L16V?ref_=Oct_DLandingS_D_2258ae19_374&smid=ATVPDKIKX0DER"


headers = {
"Accept-Language":"cs-CZ,cs;q=0.9,en;q=0.8,ru;q=0.7,sk;q=0.6",
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
}

response = requests.get(url=url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

title = soup.select(selector="#productTitle")
title = title[0].getText().strip()

price_whole = soup.find(name="span", class_="a-price-whole").getText()
price_fraction = soup.find(name="span", class_="a-price-fraction").getText()
price = f"{price_whole}{price_fraction}"
price = float(price)
print(price)

#--------------------CHECKING IF PRICE IS BELOW TARGET AND SENDING EMAIL--------------------------

my_email = os.environ.get("MAIL_USERNAME")
password = os.environ.get("MAIL_PASSWORD")

if price <100:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(password=password, user=my_email)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject: Price decrease on Amazon \n\n The price of {title} is below 100$ and is {price} now. \n Here is the link "
                                f"{url}")
