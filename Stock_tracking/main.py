import requests
from datetime import date
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_KEY = "39RQ1JXZSZ5WFX6N"
NEWS_KEY ="1b78a6dcce604ac8ae683a94f1b5bc7c"
DAY = date.today()
account_sid = "AC929713b9b1d324e7464028966b691ff5"
auth_token = "4d4c0940d83f6cc0faad45139cb49f6b"

link_stock = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+STOCK+"&apikey="+STOCK_KEY
link_news = "https://newsapi.org/v2/everything?q="+COMPANY_NAME +"&from="+ str(DAY)+ "&language=en&sortBy=publishedAt&apiKey=" + NEWS_KEY

response_news = requests.get(url=link_news)
response_news.raise_for_status()
news = response_news.json()["articles"][:3]

def get_news():
    notification = ""
    for i in range(3):
        notification += f"Title {i + 1}: {news[i]['title']}\nDescription:{news[i]['description']}\n"
    return notification

response = requests.get(url=link_stock)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
day0 = list(stock_data.keys())[0]
day1 = list(stock_data.keys())[1]
price_day0 = stock_data[day0]["4. close"]
price_day1 = stock_data[day1]["4. close"]
price_change = round((abs(float(price_day1) - float(price_day0)))/float(price_day1)*100,1)

icon= ""
if float(price_day1) - float(price_day0) <= 0:
    icon="🔺"
else:
    icon="🔻"


if price_change >= 5:
    message=get_news()
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = f"TSLA: {icon}{price_change}\n{message}",
        from_= "+12347424317",
        to='+61416041302'
    )
    print(message.status)




