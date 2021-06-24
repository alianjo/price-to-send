from bs4 import BeautifulSoup
import requests
import tkinter
from tkinter import *
from tkinter import ttk
from  pandas import DataFrame
import matplotlib.pyplot as plt
import dataframe_image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
from tkinter import filedialog
import time
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading
import http.client
import dataframe_image as dfi # for save data frame as png file

class price:
    
    def __init__(self):
############################################################################################        
        
        self.root = tkinter.Tk()
        self.root.geometry('900x500')


        self.root.iconbitmap('C:/Users/ali/Desktop/Graphicloads-Colorful-Long-Shadow-Dollar.ico')
        self.l = IntVar()
        menu_bar = Menu(self.root)
        menu_bar2 = Menu(menu_bar, tearoff=0)
        menu_bar2.add_command(label='Exit', command=self.root.destroy)
        menu_bar.add_cascade(label='Option', menu=menu_bar2)
        self.root.config(menu=menu_bar)     
###############################################/////  add Tabs   ###################################
        tabs = ttk.Notebook(self.root)            
        self.first = ttk.Frame(tabs)
        tabs.add(self.first, text='نمودار و قیمت')
        self.second = ttk.Frame(tabs)
        tabs.add(self.second, text='ارسال به دوستان')
        tabs.pack(expand=1, fill="both")

        

        

#############################################################################################
        frame = LabelFrame(self.first, text = 'select one of the checkboxes',bd=3,padx=20,pady=10)
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
#################################### Second page#################
#        Int vars
        self.dollar = IntVar()
        self.gold = IntVar()
        self.bitcoin = IntVar()
        self.coin = IntVar()
        self.euro = IntVar()
        self.bors = IntVar()
        self.derham = IntVar()
        self.tether = IntVar()
        self.iraq = IntVar()
        self.shasta = IntVar()
#           Entries
        frame2 = LabelFrame(self.second, text='مواردی که قصد ارسال دارید', bd = 3, padx=20, pady=20)
        frame2.place(x=20, y =40)
        Checkbutton(frame2, text='دلار',variable=self.dollar).pack()
        Checkbutton(frame2, text='طلا 18',variable=self.gold).pack()
        Checkbutton(frame2, text='بیتکوین',variable=self.bitcoin).pack()
        Checkbutton(frame2, text='سکه تمام',variable=self.coin).pack()
        Checkbutton(frame2, text='یورو',variable=self.euro).pack()
        Checkbutton(frame2, text='شاخص بورس',variable=self.bors).pack()
        Checkbutton(frame2, text='درهم امارات',variable=self.derham).pack()
        Checkbutton(frame2, text='تتر',variable=self.tether).pack()
        Checkbutton(frame2, text='دینار عراق',variable=self.iraq).pack()
        Checkbutton(frame2, text='شستا',variable=self.shasta).pack()
        
        self.frame3 = LabelFrame(self.second, text = 'ارسال ایمیل', bd = 3, padx =20, pady=50)
        self.frame3.place(x =250, y=40)
        self.email = StringVar()
        la1 = Label(self.frame3, text = 'ایمیل').pack()
        self.email_sender = Entry(self.frame3, textvariable=self.email,width=30, bd=2)
        self.email_sender.pack()
        la2 = Label(self.frame3, text='رمز عبور').pack()
        self.password = StringVar()
        self.password= Entry(self.frame3, textvariable=self.password,width=30, bd=2, show="*")
        self.password.pack()
        
        self.one_or_more= IntVar()
        Radiobutton(self.frame3,text='ارسال به یک نفر', variable=self.one_or_more,value=1,command = self.add_entry).pack()
        Radiobutton(self.frame3,text='ارسال به چند نفر', variable=self.one_or_more,value=0,command = self.delete_and_add).pack()
        self.button_explore = Button(self.frame3,text = "انتخاب لیست", command = self.browseFiles)
        self.button_explore.pack()
        label_in_frame=Label(self.frame3, text='دریافت کننده').pack()
        self.entry_for_reciver = Entry(self.frame3,width=30, bd=2,state='readonly')
        self.entry_for_reciver.pack()
        button_explore = Button(self.frame3,text = "ارسال", command = self.send_email).pack()
        self.frame4 = LabelFrame(self.second, text = 'ارسال SMS', bd = 3, padx =20, pady=50)
        self.frame4.place(x =550, y=40)    
        Label(self.frame4, text='فایل تسکتی که دارای شماره تماس ها است را انتخاب کنید').pack()
        self.button_explore2 = Button(self.frame4,text = "انتخاب لیست", command = self.browseFiles)
        self.button_explore2.pack()
        button_explore = Button(self.frame4,text = "ارسال", command = self.send_with_phone).pack()

##############################################################################################
        exit_page_1 = Button(self.first, text= 'Exit', command= self.root.destroy, width=20, bd =3).place(x = 30, y =400)

        self.root.title("Have the newest price")
        self.root.mainloop()
        

    def send_with_phone(self):
        prices = []
        if self.gold.get():
            prices.append(self.gold_price())
        if self.dollar.get():
            prices.append(self.dollar_price())
        if self.bitcoin.get():
            prices.append(self.bitcoin_price())
        if self.coin.get():
            prices.append(self.coin_gold_price())
        if self.bors.get():
            prices.append(self.bors_price()) 
        if self.euro.get():
            prices.append(self.euro_price())
        if self.derham.get():
            prices.append(self.derham_price())
        if self.tether.get():
            prices.append(self.tether_price())
        if self.iraq.get():
            prices.append(self.iqd_price())
        if self.shasta.get():
            prices.append(self.shasta_price())
            prices = ''.join(str(i) + '\n' for i in prices)
        with open(self.filename,'r') as f:
                first = f.readline()
                while True:
                    if first :
                        threading.Thread(target=self.send_message_with_ghasedak, args=(first.split('\n')[0],prices,)).start()
                        first= f.readline()
                    else: break
                
                
    def send_message_with_ghasedak(self,phone,msg):
        conn = http.client.HTTPSConnection("api.ghasedak.me")
        payload = f"message={msg}&receptor={phone}&linenumber=10008566"
        headers = { 'content-type': "application/x-www-form-urlencoded",
                   'apikey': "02bb8697d495c8c10257bfd8083b1990e595f4b891677cfb85dd7dca121e7623",
                   'cache-control': "no-cache",}
        conn.request("POST", "/v2/sms/send/simple", payload, headers)
        res = conn.getresponse()
        data = res.read()
        Label(self.frame4,text = data,fg='blue').pack()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
    def add_entry(self):
        self.entry_for_reciver.config(state='normal')
        self.button_explore.config(state='disabled')

            

    def delete_and_add(self):
        self.button_explore.config(state='normal')
        self.entry_for_reciver.config(state='readonly')
        
    def browseFiles(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select text or xls file",filetypes = (("Text file","*.txt*"),))
              
    def send_email(self):
        if self.one_or_more.get() == 1:
            if '@' in self.entry_for_reciver.get() and '@' in self.email_sender.get() and self.password.get() !='':
                prices = []
                if self.gold.get():
                    prices.append(self.gold_price())
                if self.dollar.get():
                    prices.append(self.dollar_price())
                if self.bitcoin.get():
                    prices.append(self.bitcoin_price())
                if self.coin.get():
                    prices.append(self.coin_gold_price())
                if self.bors.get():
                    prices.append(self.bors_price()) 
                if self.euro.get():
                    prices.append(self.euro_price())
                if self.derham.get():
                    prices.append(self.derham_price())
                if self.tether.get():
                    prices.append(self.tether_price())
                if self.iraq.get():
                    prices.append(self.iqd_price())
                if self.shasta.get():
                    prices.append(self.shasta_price()) 
    
                self.mailSender(self.email_sender.get(),self.entry_for_reciver.get(),self.password.get(),prices)
                
            else:
                try:
                    self.blue_err.destroy()
                    self.err = Label(self.frame3, text='complete your information correctly',fg='red')
                    self.err.pack()
                    self.root.mainloop()
                except:
                    self.err = Label(self.frame3, text='complete your information correctly',fg='red')  
                    self.err.pack()
                    self.root.mainloop()
        else:
            try:
                if  self.filename:
                    prices = []
                    if self.gold.get():
                        prices.append(self.gold_price())
                    if self.dollar.get():
                        prices.append(self.dollar_price())
                    if self.bitcoin.get():
                        prices.append(self.bitcoin_price())
                    if self.coin.get():
                        prices.append(self.coin_gold_price())
                    if self.bors.get():
                        prices.append(self.bors_price()) 
                    if self.euro.get():
                        prices.append(self.euro_price())
                    if self.derham.get():
                        prices.append(self.derham_price())
                    if self.tether.get():
                        prices.append(self.tether_price())
                    if self.iraq.get():
                        prices.append(self.iqd_price())
                    if self.shasta.get():
                        prices.append(self.shasta_price()) 
                    with open (self.filename,'r') as f :
                        email = f.readline()
                        while True:
                            if not email:
                                break
                            threading.Thread(target=self.mailSender, args=(self.email_sender.get(),email,self.password.get(),prices,)).start()
                            email = f.readline()
            except Exception:
                try:
                    self.err.destroy()
                    self.blue_err = Label(self.frame3, text='No selection', fg='blue')
                    self.blue_err.pack()
                    self.root.mainloop()
                except Exception:
                    self.blue_err = Label(self.frame3, text='No selection', fg='blue')
                    self.blue_err.pack()
                    self.root.mainloop()
            

 
            
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
            'date':dates[:10],
            'price':prices[:10]
            }, columns=(['date', 'price']))

        #save data frame as png
        try:
            self.label2.destroy()
        except Exception:
            pass
        ##################### Chart
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\gold.png', dpi=80 )
        image1 = Image.open(r"data\gold.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.first, image=test)
        label1.image = test
        label1.place( x=400, y=40)
        ######################## tabel
        dfi.export(data_frame,'data\\gold_dataframe.png')
        image2 = Image.open('data\\gold_dataframe.png')
        test2 = ImageTk.PhotoImage(image2)
        self.label2 = tkinter.Label(self.first,image=test2)
        self.label2.image=test2
        self.label2.place(x = 200,y =40)
        
        plt.close()
        return(f'''Gold price at : {dates[0]} is : {prices[0]} (Rial) ''')
        
        
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
            
        data_frame = DataFrame({
            'date':dates[:10],
            'price':prices[:10]
            }, columns=(['date', 'price']))
        try:
            self.label2.destroy()
        except Exception:
            pass
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\dollar.png', dpi=80 )
        image1 = Image.open(r"data\dollar.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.first, image=test)
        label1.image = test
        label1.place( x=400, y=40)
        ######################## tabel
        dfi.export(data_frame,'data\\dollar_dataframe.png')
        image2 = Image.open('data\\dollar_dataframe.png')
        test2 = ImageTk.PhotoImage(image2)
        self.label2 = tkinter.Label(self.first,image=test2)
        self.label2.image=test2
        self.label2.place(x = 200,y =40)
        
        plt.close()
        return(f'''Dollor price at : {dates[0]} is : {prices[0]} (Rial) ''')
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
        
        data_frame = DataFrame({
            'date':dates[:10],
            'price':prices[:10]
            }, columns=(['date', 'price']))

        try:
            self.label2.destroy()
        except Exception:
            pass            
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\bitcoin.png', dpi=80 )
        image1 = Image.open(r"data\bitcoin.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.first, image=test)
        label1.image = test
        label1.place( x=400, y=40)
        ######################## tabel
        dfi.export(data_frame,'data\\bitcoin_dataframe.png')
        image2 = Image.open('data\\bitcoin_dataframe.png')
        test2 = ImageTk.PhotoImage(image2)
        self.label2 = tkinter.Label(self.first,image=test2)
        self.label2.image=test2
        self.label2.place(x = 200,y =40)
        plt.close()
        return(f'''Bitcoin price at : {dates[0]} is : {prices[0]} (Dollar) ''')
        
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
        
        data_frame = DataFrame({
            'date':dates[:10],
            'price':prices[:10]
            }, columns=(['date', 'price']))        
        try:
            self.label2.destroy()
        except Exception:
            pass        
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\coin.png', dpi=80 )
        image1 = Image.open(r"data\coin.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.first, image=test)
        label1.image = test
        label1.place( x=400, y=40)
        ######################## tabel
        dfi.export(data_frame,'data\\coin_dataframe.png')
        image2 = Image.open('data\\coin_dataframe.png')
        test2 = ImageTk.PhotoImage(image2)
        self.label2 = tkinter.Label(self.first,image=test2)
        self.label2.image=test2
        self.label2.place(x = 200,y =40)
        plt.close()
        return(f'''Coin price at : {dates[0]} is : {prices[0]} (Rial) ''')        
        
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

        data_frame = DataFrame({
            'date':dates[:10],
            'price':prices[:10]
            }, columns=(['date', 'price'])) 
        try:
            self.label2.destroy()
        except Exception:
            pass        
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\euro.png', dpi=80 )
        image1 = Image.open(r"data\euro.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.first, image=test)
        label1.image = test
        label1.place( x=400, y=40)
        ######################## tabel
        dfi.export(data_frame,'data\\euro_dataframe.png')
        image2 = Image.open('data\\euro_dataframe.png')
        test2 = ImageTk.PhotoImage(image2)
        self.label2 = tkinter.Label(self.first,image=test2)
        self.label2.image=test2
        self.label2.place(x = 200,y =40)
        plt.close()
        return(f'''Euro price at : {dates[0]} is : {prices[0]} (Rial) ''') 
        
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
        data_frame = DataFrame({
            'date':dates[:10],
            'index':prices[:10]
            }, columns=(['date', 'index'])) 
        try:
            self.label2.destroy()
        except Exception:
            pass        
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\bors.png', dpi=80 )
        image1 = Image.open(r"data\bors.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.first, image=test)
        label1.image = test
        label1.place( x=400, y=40)
        ######################## tabel
        dfi.export(data_frame,'data\\bors_dataframe.png')
        image2 = Image.open('data\\bors_dataframe.png')
        test2 = ImageTk.PhotoImage(image2)
        self.label2 = tkinter.Label(self.first,image=test2)
        self.label2.image=test2
        self.label2.place(x = 200,y =40)
        plt.close()
        return(f'''Bors index at : {dates[0]} is : {prices[0]}''')
        
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
        data_frame = DataFrame({
            'date':dates[:10],
            'price':prices[:10]
            }, columns=(['date', 'price']))      
        try:
            self.label2.destroy()
        except Exception:
            pass
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\derham.png', dpi=80 )
        image1 = Image.open(r"data\derham.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.first, image=test)
        label1.image = test
        label1.place( x=400, y=40)
        ######################## tabel
        dfi.export(data_frame,'data\\bors_dataframe.png')
        image2 = Image.open('data\\bors_dataframe.png')
        test2 = ImageTk.PhotoImage(image2)
        self.label2 = tkinter.Label(self.first,image=test2)
        self.label2.image=test2
        self.label2.place(x = 200,y =40)
        plt.close()
        return(f'Derham Emirates price at : {dates[0]} is : {prices[0]} (Rial) ')
        
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
        data_frame = DataFrame({
            'date':dates[:10],
            'price':prices[:10]
            }, columns=(['date', 'price']))        
        try:
            self.label2.destroy()
        except Exception:
            pass
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\tether.png', dpi=80 )
        image1 = Image.open(r"data\tether.png")
        test = ImageTk.PhotoImage(image1)
        self.label2.destroy()
        label1 = tkinter.Label(self.first, image=test)
        label1.image = test
        label1.place( x=400, y=40)
        ######################## tabel
        dfi.export(data_frame,'data\\bors_dataframe.png')
        image2 = Image.open('data\\bors_dataframe.png')
        test2 = ImageTk.PhotoImage(image2)
        self.label2 = tkinter.Label(self.first,image=test2)
        self.label2.image=test2
        self.label2.place(x = 200,y =40)
        plt.close() 
        return(f'''Tether price at : {dates[0]} is : {prices[0]} (Rial) ''')
        
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
        data_frame = DataFrame({
            'date':dates[:10],
            'price':prices[:10]
            }, columns=(['date', 'price']))         
        try:
            self.label2.destroy()
        except Exception:
            pass
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\iqd.png', dpi=80 )
        image1 = Image.open(r"data\iqd.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.first, image=test)
        label1.image = test
        label1.place( x=400, y=40)
        ######################## tabel
        dfi.export(data_frame,'data\\iqr_dataframe.png')
        image2 = Image.open('data\\iqr_dataframe.png')
        test2 = ImageTk.PhotoImage(image2)
        self.label2 = tkinter.Label(self.first,image=test2)
        self.label2.image=test2
        self.label2.place(x = 200,y =40)
        plt.close()
        return(f'Iraq Dinar price at : {dates[0]} is : {prices[0]} (Rial) ')         
        
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
        data_frame = DataFrame({
            'date':dates[:10],
            'price':prices[:10]
            }, columns=(['date', 'price']))         
        price_int = []
        for i in prices:
            b = i.split(',')
            price_int.append(float(''.join( j for j in b)))
        try:
            self.label2.destroy()
        except Exception:
            pass
        plt.plot(dates[5::-1], price_int[5::-1])
        plt.xlabel('date')
        plt.ylabel('price (Rial)')
        plt.savefig('data\\shasta.png', dpi=80 )
        image1 = Image.open(r"data\shasta.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(self.first, image=test)
        label1.image = test
        label1.place( x=400, y=40)
        ######################## tabel
        dfi.export(data_frame,'data\\shasta_dataframe.png')
        image2 = Image.open('data\\shasta_dataframe.png')
        test2 = ImageTk.PhotoImage(image2)
        self.label2 = tkinter.Label(self.first,image=test2)
        self.label2.image=test2
        self.label2.place(x = 200,y =40)
        plt.close()
        return(f'shasta price at  : {dates[0]} is : {prices[0]} (Rial)')                
    def mailSender(self,mail_sender, mail_reciver,password_sender,prices):
        
        if 'gmail' in mail_reciver:
            smtp_server = "smtp.gmail.com"
        elif 'yahoo' in mail_sender:
            smtp_server = 	"smtp.mail.yahoo.com"
        
        port = 587  

        # Create a secure SSL context
        context = ssl.create_default_context()
        
        prices = ''.join(str(i) + '\n' for i in prices)
        
        message = MIMEMultipart()
        message["From"] = mail_sender
        message["To"] = mail_reciver
        message["Subject"] = 'Daily prices'
        message["Bcc"] = mail_reciver
        message.attach(MIMEText(prices, "plain"))

        
        try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(mail_sender, password=password_sender)
            server.sendmail(mail_sender,mail_reciver, msg=message.as_string())
            # TODO: Send email here
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit() 
    
        
c = price()




