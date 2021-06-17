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
############################################################################################        
        self.root = tkinter.Tk()
        self.root.geometry('600x500')
        self.gold = IntVar()
        self.dollar = IntVar()
        self.bitcoin = IntVar()
        self.gold_coin = IntVar()
        self.euro = IntVar()
        self.bors = IntVar()
        self.derham = IntVar()
        self.tether = IntVar()
        self.iqd = IntVar()
        self.shasta = IntVar()
#############################################################################################
        Checkbutton(self.root,text='دلار', variable=self.dollar).grid(column=0, row=1)
        Checkbutton(self.root, text='طلا', variable= self.gold).grid(column=1, row= 1)
        Checkbutton(self.root,text='بیتکوین', variable=self.bitcoin).grid(column=0, row=2)
        Checkbutton(self.root,text='سکه تمام', variable=self.gold_coin).grid(column=1, row=2)
        Checkbutton(self.root,text='یورو', variable=self.euro).grid(column=0, row=5)
        Checkbutton(self.root,text='بورس', variable=self.bors).grid(column=0, row=5)
        Checkbutton(self.root,text='درهم امارات', variable=self.derham).grid(column=0, row=6)
        Checkbutton(self.root,text='تتر', variable=self.tether).grid(column=0, row=7)
        Checkbutton(self.root,text='دینار عراق', variable=self.iqd).grid(column=0, row=8)
        Checkbutton(self.root,text='شستا', variable=self.shasta).grid(column=0, row=9)
##############################################################################################
        b = Button(self.root, text= 'show price', command= self.show).grid(column=1, row=1)
        self.root.mainloop()
        
    def show(self):
        if self.gold.get():
            self.gold_price()
        elif self.dollar.get():
            self.dollar_price()
        elif self.bitcoin.get():
            self.bitcoin_price()
        elif self.gold_coin.get():
            self.coin_gold_price()
        elif self.euro.get():
            self.euro_price()
        elif self.bors.get():
            self.bors_price()
        elif self.derham.get():
            self.derham_price()
        elif self.tether.get():
            self.tether_price()
        elif self.iqd.get():
            self.iqd_price()
        elif self.shasta.get():
            self.shasta_price()
            
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


        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\gold.png', dpi=100 )
        image1 = Image.open(r"data\gold.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.root, image=test)
        label1.image = test
        label1.grid(column=6, row=6)
        plt.close()
        
        
    def dollar_price(self):
        site = requests.get('https://www.tgju.org/profile/price_dollar_rl')
        soup= BeautifulSoup(site.text, 'html.parser')
        data = soup.select('#main > div.stocks-profile > div.fs-row.bootstrap-fix.widgets.full-w-set > div > div.tgju-widgets-block.col-12.col-md-6.mobile-hide > div:nth-child(1) > div.tables-default.normal > table > tbody > tr ')
        dates= []
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
        
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\dollar.png', dpi=100 )
        image1 = Image.open(r"data\dollar.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.root, image=test)
        label1.image = test
        label1.grid(column=6, row=6)
        plt.close()
    def bitcoin_price(self):
        site = requests.get('https://www.tgju.org/profile/crypto-bitcoin')
        soup = BeautifulSoup(site.text, 'html.parser')
        data = soup.select('#main > div.stocks-profile > div.fs-row.bootstrap-fix.widgets.full-w-set > div > div.tgju-widgets-block.col-12.col-md-6.mobile-hide > div:nth-child(1) > div.tables-default.normal > table > tbody > tr')
        dates= []
        prices = []
        for i in range(len(data)):
            dates.append(data[i].td.text)
            
        for i in range(len(data)):
            child = list(data[i].children)
            prices.append(child[9].text)
        
        price_int= []
        for i in prices:
            b = i.split(',')
            price_int.append(float(''.join( j for j in b)))
          
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\bitcoin.png', dpi=100 )
        image1 = Image.open(r"data\bitcoin.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.root, image=test)
        label1.image = test
        label1.grid(column=6, row=6)
        plt.close()
        
    def coin_gold_price(self):
        site = requests.get('https://www.tgju.org/profile/sekeb')
        soup = BeautifulSoup(site.text, 'html.parser')
        data = soup.select('#main > div.stocks-profile > div.fs-row.bootstrap-fix.widgets.full-w-set > div > div.tgju-widgets-block.col-12.col-md-6.mobile-hide > div:nth-child(1) > div.tables-default.normal > table > tbody > tr')
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
        
        
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\coin.png', dpi=100 )
        image1 = Image.open(r"data\coin.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.root, image=test)
        label1.image = test
        label1.grid(column=6, row=6)
        plt.close()        
        
    def euro_price(self):
        site = requests.get('https://www.tgju.org/profile/price_eur')
        soup = BeautifulSoup(site.text, 'html.parser')
        data = soup.select('#main > div.stocks-profile > div.fs-row.bootstrap-fix.widgets.full-w-set > div > div.tgju-widgets-block.col-12.col-md-6.mobile-hide > div:nth-child(1) > div.tables-default.normal > table > tbody > tr')
        
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
     
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\euro.png', dpi=90 )
        image1 = Image.open(r"data\euro.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.root, image=test)
        label1.image = test
        label1.grid(column=6, row=6)
        plt.close() 
        
    def bors_price(self):
        site = requests.get('https://www.tgju.org/profile/bourse')
        soup = BeautifulSoup(site.text, 'html.parser')
        data = soup.select('#main > div.stocks-profile > div.fs-row.bootstrap-fix.widgets.full-w-set > div > div.tgju-widgets-block.col-12.col-md-6.mobile-hide > div:nth-child(1) > div.tables-default.normal > table > tbody > tr')
        
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
           price_int.append(float(''.join( j for j in b))) 
     
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\bors.png', dpi=90 )
        image1 = Image.open(r"data\bors.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.root, image=test)
        label1.image = test
        label1.grid(column=7, row=1)
        plt.close()         
        
    def derham_price(self):
        site = requests.get('https://www.tgju.org/profile/price_aed')
        soup = BeautifulSoup(site.text, 'html.parser')
        data = soup.select('#main > div.stocks-profile > div.fs-row.bootstrap-fix.widgets.full-w-set > div > div.tgju-widgets-block.col-12.col-md-6.mobile-hide > div:nth-child(1) > div.tables-default.normal > table > tbody > tr')

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
     
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\derham.png', dpi=90 )
        image1 = Image.open(r"data\derham.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.root, image=test)
        label1.image = test
        label1.grid(column=7, row=1)
        plt.close() 
        
    def tether_price(self):
        site = requests.get('https://www.tgju.org/profile/crypto-tether')
        soup = BeautifulSoup(site.text, 'html.parser')
        data = soup.select('#main > div.stocks-profile > div.fs-row.bootstrap-fix.widgets.full-w-set > div > div.tgju-widgets-block.col-12.col-md-6.mobile-hide > div:nth-child(1) > div.tables-default.normal > table > tbody > tr')
        
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
           price_int.append(float(''.join( j for j in b)))
     
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\tether.png', dpi=90 )
        image1 = Image.open(r"data\tether.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.root, image=test)
        label1.image = test
        label1.grid(column=7, row=1)
        plt.close() 
        
    def iqd_price(self):
        site = requests.get('https://www.tgju.org/profile/price_iqd')
        soup = BeautifulSoup(site.text, 'html.parser')
        data = soup.select('#main > div.stocks-profile > div.fs-row.bootstrap-fix.widgets.full-w-set > div > div.tgju-widgets-block.col-12.col-md-6.mobile-hide > div:nth-child(1) > div.tables-default.normal > table > tbody > tr')
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
           price_int.append(float(''.join( j for j in b)))
        
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\iqd.png', dpi=90 )
        image1 = Image.open(r"data\iqd.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.root, image=test)
        label1.image = test
        label1.grid(column=7, row=1)
        plt.close()         
        
    def shasta_price(self):
        site = requests.get('https://www.shakhesban.com/markets/stock/%D8%B4%D8%B3%D8%AA%D8%A7')
        soup = BeautifulSoup(site.text, 'html.parser')
        data = soup.select('#stocks-page > div > div.tabs-contents > div > div > div > div:nth-child(11) > div.tgju-widget.light.has-icon.t-mb-2.history-widget > div.tables-default.normal > table > tbody > tr')
        dates = []
        prices = []
        for i in range(len(data)):
            dates.append(data[i].td.text.split()[-1])
        for i in range(1,11):
            b = soup.select('#stocks-page > div > div.tabs-contents > div > div > div > div:nth-child(11) > div.tgju-widget.light.has-icon.t-mb-2.history-widget > div.tables-default.normal > table > tbody > tr:nth-child(%s) > td:nth-child(2) ' %str(i))
            prices.append( b[0].text.split()[-1])
        
        price_int = []
        for i in prices:
            b = i.split(',')
            price_int.append(float(''.join( j for j in b)))
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\shasta.png', dpi=90 )
        image1 = Image.open(r"data\shasta.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.root, image=test)
        label1.image = test
        label1.grid(column=7, row=1)
        plt.close()                
        
    
        
c = price()





