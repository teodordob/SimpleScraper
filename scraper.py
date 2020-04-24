import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/Philips-EP2220-Kaffeevollautomat-Benutzeroberfl%C3%A4che-Schwarz-geb%C3%BCrstet/dp/B07MMSHC4R/ref=sr_1_7?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2G7DK7J59H39Y&dchild=1&keywords=coffee+machine&qid=1587552984&s=kitchen&sprefix=cof%2Ckitchen%2C190&sr=1-7'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:3])
    print(converted_price)
    if (converted_price < 250.0):
        send_mail()
    else:
        print("Price still too high :(")


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('pythwebscrap@gmail.com', 'ajhbaeguedtteoky')
    subject = 'Price fell down for coffee!!!!'
    body = 'Check The Amazon Page https://www.amazon.de/Philips-EP2220-Kaffeevollautomat-Benutzeroberfl%C3%A4che-Schwarz-geb%C3%BCrstet/dp/B07MMSHC4R/ref=sr_1_7?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2G7DK7J59H39Y&dchild=1&keywords=coffee+machine&qid=1587552984&s=kitchen&sprefix=cof%2Ckitchen%2C190&sr=1-7'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'pythwebscrap@gmail.com',
        'teodor.dobrev1901@gmail.com',
        msg
    )
    print('You have sent the email!')
    server.quit()


check_price()
