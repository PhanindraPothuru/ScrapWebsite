import bs4,requests
url="https://appbrewery.github.io/instant_pot/"
response=requests.get(url=url)
content=response.text
soup=bs4.BeautifulSoup(content,"html.parser")
details_3=soup.find(class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay")
print(details_3.getText())

import smtplib
my_email=to_Email="*******YOUR EMAIL ADDRESS HERE******"
password_email="*****YOUR EMAIL APP PASSWORD HERE*******"
connection=smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email,password=password_email)
connection.sendmail(from_addr=my_email,to_addrs=to_Email,msg=(f"Price Drop Alert \n\n Today price of the product which you have kept is {details_3.getText()}"))
connection.close()