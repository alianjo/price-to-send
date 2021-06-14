from bs4 import BeautifulSoup
import requests
import tkinter
from  pandas import DataFrame
import matplotlib.pyplot as plt
import dataframe_image

def gold_price():
    site = requests.get("https://www.tgju.org/profile/geram18")
    soup = BeautifulSoup(site.text, 'html.parser')
    data = soup.select('#main > div.stocks-profile > div.fs-row.bootstrap-fix.widgets.full-w-set > div > div.tgju-widgets-block.col-12.col-md-6.mobile-hide > div:nth-child(1) > div.tables-default.normal > table > tbody > tr ')
  #  print(len(data))
    dates = []
    prices = []
    for i in range(len(data)):
        dates.append(data[i].td.text)
        
    for i in range(len(data)):
        child = list(data[i].children)
        prices.append(child[9].text)
    price_int= []
    for i in prices:
       b = i.split(',')
       price_int.append(int(''.join( j for j in b)))

    data_frame = DataFrame({
        'date':dates[:9],
        'price':prices[:9]
        }, columns=(['date', 'price']))
 #   plt.plot([2,3,4,5,6,6,21], [1,2,3,4,5,6,7])
  #  plt.savefig('C:/Users/ali/Desktop/sample.png')
   # dataframe_image.export(data_frame, 'C:/Users/ali/Desktop/thisisframe.png')
    #print(data_frame)
   # data_frame.plot(x = 'date', y='price', kind='line')

    plt.plot(dates[::-5], price_int[::-5])
    plt.show()
gold_price()





