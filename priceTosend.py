from bs4 import BeautifulSoup
import requests
import tkinter
from tkinter import *
from  pandas import DataFrame
import matplotlib.pyplot as plt
import dataframe_image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import sys

class price:
    
    def __init__(self):
############################################################################################        
        
        self.root = tkinter.Tk()
        self.root.geometry('900x400')
        '''
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
        '''
        self.root.iconbitmap('C:/Users/ali/Desktop/Graphicloads-Colorful-Long-Shadow-Dollar.ico')
        self.l = IntVar()
        
#############################################################################################
        frame = LabelFrame(self.root, text = 'select one of the checkboxes',bd=3,padx=20,pady=10)
        frame.place(x=20, y = 40)
        Radiobutton(frame,text='دلار', variable=self.l,value= 'dollar', command=self.dollar_price).pack()
        Radiobutton(frame, text='طلا', variable= self.l,value = 'gold', command = self.gold_price).pack()
        Radiobutton(frame,text='بیتکوین', variable=self.l, value='bitcoin', command=self.bitcoin_price).pack()
        Radiobutton(frame,text='سکه تمام', variable=self.l, value='coin',command = self.coin_gold_price).pack()
        Radiobutton(frame,text='یورو', variable=self.l, value='euro', command =self.euro_price).pack()
        Radiobutton(frame,text='بورس', variable=self.l, value = 'bors', command=self.bors_price).pack()
        Radiobutton(frame,text='درهم امارات', variable=self.l, value = 'derham', command = self.derham_price).pack()
        Radiobutton(frame,text='تتر', variable=self.l, value='tether', command=self.tether_price).pack()
        Radiobutton(frame,text='دینار عراق', variable=self.l, value = 'divar', command=self.iqd_price).pack()
        Radiobutton(frame,text='شستا', variable=self.l,value='shasta',command=self.shasta_price).pack()
        #Label(self.root, text = '               ').grid(column=1,row=0)
        
##############################################################################################
        exit_page_1 = Button(self.root, text= 'Exit', command= self.root.destroy, width=20, bd =3).place(x = 30, y =350)

        self.root.title("Have the newest price")
        self.root.mainloop()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
 
    """
    def show(self):
        if self.l.get() == 'dollar':
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
            
            """
            
    def gold_price(self):
        self.gold_price_site = requests.get("https://www.tgju.org/profile/geram18")
        soup = BeautifulSoup(self.gold_price_site.text, 'html.parser')
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
        plt.savefig('data\\gold.png', dpi=90 )
        image1 = Image.open(r"data\gold.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.root, image=test)
        label1.image = test
        label1.place( x=350, y=25)
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
        plt.savefig('data\\dollar.png', dpi=90 )
        image1 = Image.open(r"data\dollar.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.root, image=test)
        label1.image = test
        label1.place( x=350, y=25)
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
        plt.savefig('data\\bitcoin.png', dpi=90 )
        image1 = Image.open(r"data\bitcoin.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.root, image=test)
        label1.image = test
        label1.place( x=350, y=25)
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
        plt.savefig('data\\coin.png', dpi=90 )
        image1 = Image.open(r"data\coin.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.root, image=test)
        label1.image = test
        label1.place( x=350, y=25)
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
        label1.place( x=350, y=25)
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
        label1.place( x=350, y=25)
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
        label1.place( x=350, y=25)
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
        label1.place( x=350, y=25)
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
        label1.place( x=350, y=25)
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
        label1.place( x=350, y=25)
        plt.close()                
        
    
        
c = price()




