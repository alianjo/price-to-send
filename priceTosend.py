from bs4 import BeautifulSoup
import requests
import tkinter
from tkinter import *
from  pandas import DataFrame
import matplotlib.pyplot as plt
import dataframe_image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

class price:
    
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('1300x700')
        self.gold = IntVar()
        self.dollor = IntVar()
        Checkbutton(self.root,text='dollor', variable=self.dollor).grid(column=0, row=1)
        Checkbutton(self.root, text='Gold', variable= self.gold).grid(column=0, row= 0)
        b = Button(self.root, text= 'show price', command= self.show).grid(column=1, row=1)
        self.root.mainloop()
        
    def show(self):
        if self.gold.get():
            self.gold_price()
    
    
    def gold_price(self):
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
            'date':dates[:20:3],
            'price':price_int[:20:3]
            }, columns=(['date', 'price']))
        print(data_frame)
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price')
        plt.savefig('data\\gold.png', dpi=100 )
        image1 = Image.open(r"data\gold.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.root, image=test)
        label1.image = test
        label1.grid(column=4, row=1)
c = price()





