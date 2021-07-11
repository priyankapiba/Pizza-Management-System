from tkinter import *
import time
from sqlite3 import * #to connect database
import random  #to generate random number between specified range
from tkinter import messagebox
class Pizza: #m
    cartlist = []
    amount = 0
    # --  page 1------
    def main(sf):                       #sf is parameter as same as self
        try:                            #is used for error handling
            sf.scr.destroy()            #it is used to destroy widgets(labels ,etc)
            sf.scr=Tk()                 # Tk() isclass in which there is main window
        except:
            try:
                sf.scr=Tk()
            except:
                pass
        sf.scr.geometry("1366x768")     #window resize at specified location
        sf.scr.title("big slice pizza")
        sf.mainf1=Frame(sf.scr,height=15,width=1380)
        sf.logo=PhotoImage(file="")
        sf.l=Label(sf.mainf1,image=sf.logo)
        sf.l.place(x=0,y=0)
        sf.mainf1.pack(fill=BOTH,expand=1)
        sf.mainf2=Frame(sf.scr,height=690,width=1400)
        sf.c=Canvas(sf.mainf2,height=690,width=1400)
        sf.c.pack()
        sf.back=PhotoImage(file="mlogo.png")
        sf.c.create_image(720,305,image=sf.back)
        sf.lab=Button(sf.mainf2,text= "Click Here to enter the World of Pizzas",command=lambda:sf.Login(),cursor="hand2", bd=5 ,font=("cooper black",20, 'bold'),fg="white",bg="#0b1335")
        sf.lab.place(x=420,y=550)
        sf.mainf2.pack(fill=BOTH,expand=0)
        sf.scr.mainloop()
    # ------ page 2------
    def Login(sf): #(P)
        sf.scr.destroy()
        sf.scr = Tk() #main window
        sf.scr.title("Big Slice Pizza")
        sf.scr.geometry("1366x768")
        sf.loginf1 = Frame(sf.scr, height=150, width=1366)
        sf.logo = PhotoImage(file="logo.PNG")
        sf.ba = Label(sf.loginf1, image=sf.logo, height=150).place(x=0, y=0)
        sf.home = Button(sf.loginf1, text="Home", command=lambda: sf.main(), bg="#0b1335", cursor="hand2", bd=4,
                         fg="white", font=("cooper black", 16))
        sf.home.place(x=800, y=100)
        sf.localtime = time.asctime(time.localtime(time.time()))
        sf.tim = Label(sf.loginf1, text=sf.localtime, fg="white", font=("default", 16), bg="#0b1335")
        sf.tim.place(x=925, y=50)
        sf.loginf1.pack(fill=BOTH, expand=1)
        sf.loginf2 = Frame(sf.scr, height=618, width=1366)
        sf.c = Canvas(sf.loginf2, height=618, width=1366)  #shapes
        sf.c.pack()
        sf.logo1 = PhotoImage(file="pizzamain.png")
        sf.c.create_image(683, 309, image=sf.logo1)
        sf.c.create_rectangle(50, 100, 700, 450, fill="#d3ede6", outline="white", width=6)
        sf.log = Label(sf.loginf2, text="LOGIN", fg="white", bg="#0b1335", width=26, font=("cooper black", 27))
        sf.log.place(x=59, y=105)
        sf.lab1 = Label(sf.loginf2, text="UserName", bg="#d3ede6", font=("cooper black", 22))
        sf.lab1.place(x=100, y=180)
        sf.user = Entry(sf.loginf2, bg="white", font=("cooper black", 22), bd=6, justify='left')
        sf.user.place(x=320, y=180)
        sf.lab2 = Label(sf.loginf2, text="Password", bg="#d3ede6", font=("cooper black", 22))
        sf.lab2.place(x=105, y=250)
        sf.pasd = Entry(sf.loginf2, bg="white", font=("cooper black", 22), bd=6, justify='left')
        sf.pasd.place(x=320, y=250)
        sf.lg = Button(sf.loginf2, text="Login", cursor="hand2", command=lambda: sf.logindatabase(), fg="white",
                       bg="#0b1335", font=("cooper black", 20), bd=4)
        sf.lg.place(x=180, y=320)
        sf.cl = Button(sf.loginf2, text="Clear", cursor="hand2", command=lambda: clear(sf), fg="white", bg="#0b1335",
                       font=("cooper black", 20), bd=4)
        sf.cl.place(x=450, y=320)
        def clear(sf):
            sf.user.delete(0, END)
            sf.pasd.delete(0, END)
        sf.rg = Button(sf.loginf2, text="New to Big Slice Pizza", command=lambda: sf.Register(), fg="white",
                       cursor="hand2", bg="#8c68c1", font=("cooper black", 20), bd=6)
        sf.rg.place(x=200, y=390)
        sf.c.create_rectangle(795, 120, 1310, 480, fill="#d3ede6", outline="white", width=4)
        sf.ext = PhotoImage(file="p4.png")
        sf.url = Label(sf.loginf2, image=sf.ext, cursor="hand2").place(x=805, y=125)
        sf.loginf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()
    def resultlog(sf):
        sf.loguser = sf.user.get() #to retrieve
        sf.logpass = sf.pasd.get()
        return sf.loguser, sf.logpass
# --  page 3------
    def Register(sf):#H
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("Big Slice Pizza")
        sf.scr.geometry("1366x768")
        sf.regf1 = Frame(sf.scr, height=150, width=1366)
        sf.logo = PhotoImage(file="logo.PNG")
        sf.ba = Label(sf.regf1, image=sf.logo, height=150).place(x=0, y=0)
        sf.home = Button(sf.regf1, text="Home", command=lambda: sf.main(), bg="#0b1335", cursor="hand2", fg="white",
                         font=("default", 16))
        sf.home.place(x=800, y=100)
        sf.localtime = time.asctime(time.localtime(time.time()))
        sf.tim = Label(sf.regf1, text=sf.localtime, fg="white", font=("default", 16), bg="#0b1335")
        sf.tim.place(x=925, y=50)
        sf.regf1.pack(fill=BOTH, expand=1)
        sf.regf2 = Frame(sf.scr, height=618, width=1366)
        sf.c = Canvas(sf.regf2, height=618, width=1366)
        sf.c.pack()
        sf.logo1 = PhotoImage(file="pizzamain.png")
        sf.c.create_image(683, 309, image=sf.logo1)
        sf.c.create_rectangle(150, 100, 1216, 450, fill="#d3ede6", outline="white", width=6)
        sf.log = Label(sf.regf2, text="REGISTRATION", fg="white", bg="#0b1335", width=20, font=("cooper black", 27))
        sf.log.place(x=480, y=120)
        sf.lab1 = Label(sf.regf2, text="FirstName", bg="#d3ede6", font=("cooper black", 18))
        sf.lab1.place(x=190, y=200)
        sf.first = Entry(sf.regf2, bg="white", width=15, font=("cooper black", 18), bd=5)
        sf.first.place(x=430, y=200)
        sf.lab2 = Label(sf.regf2, text="LastName", bg="#d3ede6", font=("cooper black", 18))
        sf.lab2.place(x=730, y=200)
        sf.last = Entry(sf.regf2, bg="white", width=15, font=("cooper black", 18), bd=5)
        sf.last.place(x=920, y=200)
        sf.lab3 = Label(sf.regf2, text="Username", bg="#d3ede6", font=("cooper black", 18))
        sf.lab3.place(x=190, y=250)
        sf.usern = Entry(sf.regf2, bg="white", width=15, font=("cooper black", 18), bd=5)
        sf.usern.place(x=430, y=250)
        sf.lab4 = Label(sf.regf2, text="Password", bg="#d3ede6", font=("cooper black", 18))
        sf.lab4.place(x=730, y=250)
        sf.passd = Entry(sf.regf2, bg="white", width=15, font=("cooper black", 18), bd=5)
        sf.passd.place(x=920, y=250)
        sf.lab5 = Label(sf.regf2, text="Email", bg="#d3ede6", font=("cooper black", 18))
        sf.lab5.place(x=190, y=300)
        sf.email = Entry(sf.regf2, bg="white", width=15, font=("cooper black", 18), bd=5)
        sf.email.place(x=430, y=300)
        sf.lab6 = Label(sf.regf2, text="Mobile No.", bg="#d3ede6", font=("cooper black", 18))
        sf.lab6.place(x=730, y=300)
        sf.mob = Entry(sf.regf2, bg="white", width=15, font=("cooper black", 18), bd=5)
        sf.mob.place(x=920, y=300)
        sf.bc = Button(sf.regf2, text="Back", cursor="hand2", command=lambda: sf.Login(), fg="white", bg="#0b1335",
                       font=("cooper black", 18), bd=5)
        sf.bc.place(x=370, y=370)
        sf.rg = Button(sf.regf2, text="Register", cursor="hand2", fg="white", bg="#0b1335",
                       command=lambda: sf.Regdatabase(), font=("cooper black", 18), bd=5)
        sf.rg.place(x=610, y=370)
        def clear(sf):
            sf.usern.delete(0, END)
            sf.passd.delete(0, END)
            sf.first.delete(0, END)
            sf.last.delete(0, END)
            sf.email.delete(0, END)
            sf.mob.delete(0, END)
        sf.cl = Button(sf.regf2, text="Clear", cursor="hand2", fg="white", bg="#0b1335", command=lambda: clear(sf),
                       font=("cooper black", 18), bd=5)
        sf.cl.place(x=910, y=370)
        sf.regf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()
    def resultreg(sf):
        sf.reguser = sf.usern.get()
        sf.regpasd = sf.passd.get()
        sf.firstname = sf.first.get()
        sf.lastname = sf.last.get()
        sf.Email = sf.email.get()
        sf.Mob = sf.mob.get()
        return sf.reguser, sf.regpasd, sf.firstname, sf.lastname, sf.Email, sf.Mob
    # --  page 4------#M
        def Ref(sf):
            sf.con = connect("pizza.db")
            try:
                sf.cur.execute(
                    "create table orderdetail(id integer primary key,username varchar(50),name varchar(50),mobile varchar(50),money varchar(10) not null,address varchar ,orderdet varchar not null)")          #table is being created
                sf.con.commit()         #to connect database
            except:
                pass
            x = sf.cur.execute("select count(*) from orderdetail")
            ordno = list(x)[0][0] + 1
            sf.order.set(ordno)   #is used to display data
            sf.v1 = sf.vp1.get()
            if sf.v1 == "Medium":
                sf.p1 = float(sf.Deluxe_Veggie.get()) * 450
            elif sf.v1 == "Large":
                sf.p1 = float(sf.Deluxe_Veggie.get()) * 650
            else:
                sf.p1 = float(sf.Deluxe_Veggie.get()) * 250
            sf.v2 = sf.vp2.get()
            if sf.v2 == "Medium":
                sf.p2 = float(sf.Veg_Vaganza.get()) * 400
            elif sf.v2 == "Large":
                sf.p2 = float(sf.Veg_Vaganza.get()) * 600
            else:
                sf.p2 = float(sf.Veg_Vaganza.get()) * 250
            sf.v3 = sf.vp3.get()
            if sf.v3 == "Medium":
                sf.p3 = float(sf.Pepper.get()) * 385
            elif sf.v3 == "Large":
                sf.p3 = float(sf.Pepper.get()) * 550
            else:
                sf.p3 = float(sf.Pepper.get()) * 225
            sf.v4 = sf.vp4.get()
            if sf.v4 == "Medium":
                sf.p4 = float(sf.Margherita.get()) * 195
            elif sf.v4 == "Large":
                sf.p4 = float(sf.Margherita.get()) * 385
            else:
                sf.p4 = float(sf.Margherita.get()) * 99
            sf.v5 = sf.vp5.get()
            if sf.v5 == "Medium":
                sf.p5 = float(sf.Non_Veg_Supreme.get()) * 450
            elif sf.v5 == "Large":
                sf.p5 = float(sf.Non_Veg_Supreme.get()) * 650
            else:
                sf.p5 = float(sf.Non_Veg_Supreme.get()) * 250
            sf.v6 = sf.vp6.get()
            if sf.v6 == "Medium":
                sf.p6 = float(sf.Chicken_Tikka.get()) * 400
            elif sf.v6 == "Large":
                sf.p6 = float(sf.Chicken_Tikka.get()) * 600
            else:
                sf.p6 = float(sf.Chicken_Tikka.get()) * 225
            sf.v7 = sf.vp7.get()
            if sf.v7 == "Medium":
                sf.p7 = float(sf.Chicken_Sausage.get()) * 385
            elif sf.v7 == "Large":
                sf.p7 = float(sf.Chicken_Sausage.get()) * 550
            else:
                sf.p7 = float(sf.Chicken_Sausage.get()) * 225
            sf.v8 = sf.vp8.get()
            if sf.v8 == "Medium":
                sf.p8 = float(sf.Chicken_Peri.get()) * 195
            elif sf.v8 == "Large":
                sf.p8 = float(sf.Chicken_Peri.get()) * 385
            else:
                sf.p8 = float(sf.Chicken_Peri.get()) * 99
            sf.costofmeal = "Rs.", str('%.2f' % (
                        sf.p1 + sf.p2 + sf.p3 + sf.p4 + sf.p5 + sf.p6 + sf.p7 + sf.p8 ))
            sf.PayTax = ((
                                     sf.p1 + sf.p2 + sf.p3 + sf.p4 + sf.p5 + sf.p6 + sf.p7 + sf.p8 ) * .05)
            sf.Totalcost = (
                        sf.p1 + sf.p2 + sf.p3 + sf.p4 + sf.p5 + sf.p6 + sf.p7 + sf.p8 )
            sf.Ser_Charge = ((
                                         sf.p1 + sf.p2 + sf.p3 + sf.p4 + sf.p5 + sf.p6 + sf.p7 + sf.p8 ) / 99)
            sf.Service = "Rs." + str('%.2f' % sf.Ser_Charge)
            sf.OverAllCost = "Rs." + str(int(sf.PayTax + sf.Totalcost + sf.Ser_Charge))
            sf.PaidTax = "Rs." + str('%.2f' % sf.PayTax)
            sf.money = int(sf.PayTax + sf.Totalcost + sf.Ser_Charge)
            sf.Service_Charge.set(sf.Service)
            sf.cost.set(sf.costofmeal)
            sf.Tax.set(sf.PaidTax)
            sf.Total.set(sf.OverAllCost)
        def reset(sf):
            sf.Deluxe_Veggie.set("0")
            sf.Veg_Vaganza.set("0")
            sf.Pepper.set("0")
            sf.Margherita.set("0")
            sf.Non_Veg_Supreme.set("0")
            sf.Chicken_Tikka.set("0")
            sf.Chicken_Sausage.set("0")
            sf.Chicken_Peri.set("0")
            sf.Total.set("0")
            sf.Service_Charge.set("0")
            sf.Tax.set("0")
            sf.cost.set("0")
            sf.order.set("0")
            sf.Cutomer_name.set("")
            sf.cusmob.set("")
            sf.vp1.set("Medium")
            sf.vp2.set("Medium")
            sf.vp3.set("Medium")
            sf.vp4.set("Medium")
            sf.vp5.set("Medium")
            sf.vp6.set("Medium")
            sf.vp7.set("Medium")
            sf.vp8.set("Medium")
        def price(sf):#P
            sf.roo = Tk()
            sf.roo.geometry("600x768+0+0")
            sf.roo.title("Price List")
            sf.lblinfo = Label(sf.roo, font=('aria', 18, 'bold'), text="ITEM", fg="black", bd=5)
            sf.lblinfo.grid(row=0, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Veg Pizza", fg="black", anchor=W)
            sf.lblinfo.grid(row=1, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15), text="(Medium/Large/Regular)", fg="black", anchor=W)
            sf.lblinfo.grid(row=1, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 18, 'bold'), text="PRICE", fg="black", anchor=W)
            sf.lblinfo.grid(row=0, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Deluxe Veggie", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=2, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹450/₹650/₹250", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=2, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Veg Vaganza", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=3, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹400/₹600/₹250", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=3, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="5 sf.Pepper", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=4, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹385/₹550/₹225", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=4, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="sf.Margherita", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=5, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹195/₹385/₹99", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=5, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Non-Veg Pizza", fg="black", anchor=W)
            sf.lblinfo.grid(row=6, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15), text="(Medium/Large/Regular)", fg="black", anchor=W)
            sf.lblinfo.grid(row=6, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Non-Veg Supreme", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=7, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹450/₹650/₹250", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=7, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Tikka", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=8, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹400/₹600/₹250", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=8, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Suasage", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=9, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹385/₹550/₹225", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=9, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Peri", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=10, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹195/₹385/₹99", fg="steel blue", anchor=W)          #anchor is alignment (W=text wrapping)
            sf.lblinfo.grid(row=10, column=2)
            sf.roo.mainloop()
    # customer (H)
        sf.non = Label(sf.admainf2, pady=2, text=(" "), font=('Cooper Black', 20), bg="#f2e8b8", bd=10, anchor='w')
        sf.non.grid(row=0, column=8)
        sf.lbl6 = Label(sf.admainf2, pady=2, font=('Cooper Black', 22, 'bold', 'underline'), bg="#f2e8b8",
                        text="Customer Detail", bd=10, anchor='w')
        sf.lbl6.place(x=970, y=0)

        sf.lblnam = Label(sf.admainf2, pady=2, font=('aria', 16, 'bold'), width=10, text="    Name:", bg="#f2e8b8",
                          fg="#7769ad", bd=6, anchor='w')
        sf.lblnam.grid(row=1, column=7)
        sf.txtnam = Entry(sf.admainf2, font=('ariel', 16, 'bold'), textvariable=sf.Cutomer_name, bd=6, width=14,
                          bg="powder blue", justify='left')
        sf.txtnam.grid(row=1, column=8)

        sf.lblmob = Label(sf.admainf2, pady=2, font=('aria', 16, 'bold'), text="Mobile No:", bg="#f2e8b8", fg="#7769ad",
                          bd=6, anchor='w')
        sf.lblmob.grid(row=2, column=7)
        sf.txtmob = Entry(sf.admainf2, font=('ariel', 16, 'bold'), textvariable=sf.cusmob, width=14, bd=6,
                          bg="powder blue", justify='left')
        sf.txtmob.grid(row=2, column=8)

        # bill H
        sf.non = Label(sf.admainf2, pady=2, text=(" "), font=('Cooper Black', 20), bg="#f2e8b8", bd=10, anchor='w')
        sf.non.grid(row=3, column=8)
        sf.lbl5 = Label(sf.admainf2, pady=2, font=('Cooper Black', 22, 'bold', 'underline'), bg="#f2e8b8",
                        text="Bill Payment", bd=10, anchor='w')
        sf.lbl5.place(x=1000, y=140)

        sf.non = Label(sf.admainf2, pady=2, text=(" "), font=('Cooper Black', 20), width=5, bg="#f2e8b8", bd=10,
                       anchor='w')
        sf.non.grid(row=4, column=6)
        sf.lblord = Label(sf.admainf2, pady=2, font=('aria', 16, 'bold'), width=10, text="    Order No:", bg="#f2e8b8",
                          fg="#7769ad", bd=6, anchor='w')
        sf.lblord.grid(row=4, column=7)
        sf.txtord = Entry(sf.admainf2, font=('ariel', 16, 'bold'), textvariable=sf.order, bd=6, width=14,
                          bg="powder blue", justify='right')
        sf.txtord.grid(row=4, column=8)

        sf.lblco = Label(sf.admainf2, pady=2, font=('aria', 16, 'bold'), text="Subtotal:", bg="#f2e8b8", fg="#7769ad",
                         bd=6, anchor='w')
        sf.lblco.grid(row=5, column=7)
        sf.txtco = Entry(sf.admainf2, font=('ariel', 16, 'bold'), textvariable=sf.cost, width=14, bd=6,
                         bg="powder blue", justify='right')
        sf.txtco.grid(row=5, column=8)

        sf.lblser = Label(sf.admainf2, pady=2, font=('aria', 16, 'bold'), text="Service Charge:", bg="#f2e8b8",
                          fg="#7769ad", bd=6, anchor='w')
        sf.lblser.grid(row=6, column=7)
        sf.txtser = Entry(sf.admainf2, font=('ariel', 16, 'bold'), textvariable=sf.Service_Charge, width=14, bd=6,
                          bg="powder blue", justify='right')
        sf.txtser.grid(row=6, column=8)

        sf.lbltax = Label(sf.admainf2, pady=2, font=('aria', 16, 'bold'), text="Tax:", bg="#f2e8b8", fg="#7769ad", bd=6,
                          anchor='w')
        sf.lbltax.grid(row=7, column=7)
        sf.txttax = Entry(sf.admainf2, font=('ariel', 16, 'bold'), textvariable=sf.Tax, bd=6, width=14,
                          bg="powder blue", justify='right')
        sf.txttax.grid(row=7, column=8)

        sf.lbltot = Label(sf.admainf2, pady=2, font=('aria', 16, 'bold'), text="Total:", bg="#f2e8b8", fg="#7769ad",
                          bd=6, anchor='w')
        sf.lbltot.grid(row=8, column=7)
        sf.txttot = Entry(sf.admainf2, font=('ariel', 16, 'bold'), textvariable=sf.Total, bd=6, width=14,
                          bg="powder blue", justify='right')
        sf.txttot.grid(row=8, column=8)

        sf.btnprice = Button(sf.admainf2, pady=2, bd=6, fg="black", font=('ariel', 16, 'bold'), width=6, text="PRICE",
                             bg="powder blue", command=lambda: price(sf))
        sf.btnprice.place(x=970, y=440)

        sf.btnTotal = Button(sf.admainf2, pady=2, bd=6, fg="black", font=('ariel', 16, 'bold'), width=6, text="TOTAL",
                             bg="powder blue", command=lambda: Ref(sf))
        sf.btnTotal.place(x=1160, y=440)

        sf.btnreset = Button(sf.admainf2, pady=2, bd=6, fg="black", font=('ariel', 16, 'bold'), width=6, text="RESET",
                             bg="powder blue", command=lambda: reset(sf))
        sf.btnreset.place(x=970, y=500)

        sf.btnpay = Button(sf.admainf2, pady=2, bd=6, fg="black", font=('ariel', 16, 'bold'), width=6, text="PAY",
                           bg="powder blue", command=lambda: sf.adminorderdetail())
        sf.btnpay.place(x=1160, y=500)

        sf.scr.mainloop()
    # --  page 5------
    def menulist(sf, x):  #M
        sf.x = x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("Big Slice Pizza")
        sf.scr.geometry("1366x768")
        sf.menuf1 = Frame(sf.scr, height=150, width=1366)
        sf.c = Canvas(sf.menuf1, height=150, width=1300)
        sf.c.pack()
        sf.logo = PhotoImage(file="logo.PNG")
        sf.c.create_image(683, 75, image=sf.logo)
        sf.home = Button(sf.menuf1, text="Log Out", command=lambda: sf.Login(), bg="#0b1335", cursor="hand2",
                         fg="white", bd=5, font=("default", 16, 'bold'))
        sf.home.place(x=1000, y=90)
        sf.localtime = time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000, 50, text=sf.localtime, fill="white", font=("default", 16))
        sf.menuf1.pack(fill=BOTH, expand=1)
        sf.menuf2 = Frame(sf.scr, height=618, width=1366)
        sf.c = Canvas(sf.menuf2, height=618, width=1366)
        sf.c.pack()
        sf.logo1 = PhotoImage(file="pizzamain.png")
        sf.c.create_image(683, 309, image=sf.logo1)
        sf.c.create_rectangle(300, 100, 1000, 420, fill="orange", outline="white", width=6)
        sf.veg = PhotoImage(file="veg.png")
        sf.c.create_image(500, 250, image=sf.veg)
        sf.vegbut = Button(sf.menuf2, text="Veg Pizza", cursor="hand2", fg="white", command=lambda: sf.vegpizza(sf.x),
                           bg="#0b1335", bd=5, font=("default", 18, 'bold'))
        sf.vegbut.place(x=400, y=350)
        sf.nonveg = PhotoImage(file="Non.png")
        sf.c.create_image(800, 250, image=sf.nonveg)

        sf.nonvegbut = Button(sf.menuf2, text="Non-Veg Pizza", cursor="hand2", fg="white",
                              command=lambda: sf.nonvegpiz(sf.x), bg="#0b1335", bd=5, font=("default", 18, 'bold'))
        sf.nonvegbut.place(x=700, y=350)
        sf.menuf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()
    # --  page 6------
    def pizmain(sf):#P
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("Big Slice Pizza")
        sf.scr.geometry("1366x768")
        sf.pizf1 = Frame(sf.scr, height=150, width=1366)
        sf.c = Canvas(sf.pizf1, height=150, width=1366)
        sf.c.pack()
        sf.logo = PhotoImage(file="logo.PNG")
        sf.c.create_image(683, 75, image=sf.logo)
        sf.c.create_text(950, 80, text="WELCOME", fill="white", font=("default", 20))
        sf.out = Button(sf.pizf1, text="Log Out", command=lambda: sf.Login(), bg="#0b1335", cursor="hand2", fg="white",
                        font=("default", 16))
        sf.out.place(x=1200, y=100)
        sf.localtime = time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000, 40, text=sf.localtime, fill="white", font=("default", 16))
        sf.pizf1.pack(fill=BOTH, expand=1)
        sf.pizf2 = Frame(sf.scr, height=618, width=1366)
        sf.c = Canvas(sf.pizf2, height=618, width=1366)
        sf.c.pack()
        sf.logo1 = PhotoImage(file="pizzamain.png")
        sf.c.create_image(683, 309, image=sf.logo1)
        sf.c.create_rectangle(400, 120, 966, 470, fill="#d3ede6", outline="white", width=2)
        sf.deli = PhotoImage(file="delivery.png")
        sf.c.create_image(540, 260, image=sf.deli)
        sf.pic = PhotoImage(file="pick.png")
        sf.c.create_image(825, 260, image=sf.pic)
        sf.de = Button(sf.pizf2, text="Delivery", cursor="hand2", fg="white", command=lambda: sf.menulist("deli"),
                       bg="#0b1335", font=("default", 20), bd=5)
        sf.de.place(x=480, y=400)
        sf.pu = Button(sf.pizf2, text="Pick Up", cursor="hand2", fg="white", command=lambda: sf.menulist("pick"),
                       bg="#0b1335", font=("default", 20), bd=5)
        sf.pu.place(x=770, y=400)
        sf.c.create_rectangle(405, 125, 678, 465, outline="black", width=2)
        sf.c.create_rectangle(688, 125, 960, 465, outline="black", width=2)
        sf.pizf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()
    # --  page 7------
    def vegpizza(sf, x):#H
        sf.x = x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("BIG SLICE PIZZA")
        sf.scr.geometry("1366x768")
        sf.vegf1 = Frame(sf.scr, height=150, width=1366)
        sf.c = Canvas(sf.vegf1, height=150, width=1366)
        sf.c.pack()
        sf.logo = PhotoImage(file="logo.PNG")
        sf.c.create_image(683, 75, image=sf.logo)
        sf.home = Button(sf.vegf1, text="Log Out", command=lambda: sf.Login(), bg="#0b1335", cursor="hand2", fg="white",
                         bd=5, font=("default", 16, 'bold'))
        sf.home.place(x=1000, y=90)
        sf.localtime = time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000, 50, text=sf.localtime, fill="white", font=("default", 16))
        sf.vegf1.pack(fill=BOTH, expand=1)
        sf.vegf2 = Frame(sf.scr, height=618, width=1366)
        sf.c = Canvas(sf.vegf2, height=618, width=1366)
        sf.c.pack()
        sf.logo1 = PhotoImage(file="pizzamain.png")
        sf.c.create_image(683, 309, image=sf.logo1)
        sf.log = Label(sf.vegf2, text="VEG PIZZA", bg="#9db1f2", font=("Cooper Black", 22))
        sf.log.place(x=600, y=4)
        sf.c.create_rectangle(400, 40, 966, 540, fill="#d3ede6", outline="white", width=6)
        sf.q1 = StringVar()
        sf.q2 = StringVar()
        sf.q3 = StringVar()
        sf.q4 = StringVar()
        sf.q1.set("0")
        sf.q2.set("0")
        sf.q3.set("0")
        sf.q4.set("0")
        # pizza 1
        sf.c.create_rectangle(405, 50, 960, 170, width=2)
        sf.delu = PhotoImage(file="deluxe.png")
        sf.c.create_image(470, 110, image=sf.delu)
        sf.c.create_text(650, 80, text="Deluxe Veggie", fill="#000000", font=("Cooper Black", 20))
        sf.c.create_text(860, 80, text="₹450/₹650/₹250", fill="#ff3838", font=("default", 17, 'bold'))
        sf.v1 = IntVar()
        sf.C11 = Radiobutton(sf.vegf2, text="Medium", value=10, variable=sf.v1)
        sf.C11.place(x=550, y=100)
        sf.C12 = Radiobutton(sf.vegf2, text="Large", value=20, variable=sf.v1)
        sf.C12.place(x=650, y=100)
        sf.C13 = Radiobutton(sf.vegf2, text="Regular", value=30, variable=sf.v1)
        sf.C13.place(x=750, y=100)
        sf.C11.select()
        sf.C11.deselect()
        sf.C11.invoke()
        sf.c.create_text(590, 150, text="Quantity : ", fill="#000000", font=("default", 12))
        sf.qty1 = Entry(sf.vegf2, textvariable=sf.q1, bg="#aae2d7", font=("default", 12), width=4, )
        sf.qty1.place(x=650, y=140)
        sf.add1 = Button(sf.vegf2, text="ADD", command=lambda: addch1(), bg="#0b1335", cursor="hand2", fg="white", bd=4,
                         font=("default", 12, 'bold'))
        sf.add1.place(x=850, y=120)
        def addch1():
            if sf.v1.get() == 10:
                ch1 = "Medium"
                pric1 = 450
            elif sf.v1.get() == 20:
                ch1 = "Large"
                pric1 = 650
            else:
                ch1 = "Regular"
                pric1 = 250
            sf.addlist(["Deluxe Veggie", ch1, sf.q1.get(), pric1 * int(sf.q1.get())])
        # pizza 2
        sf.c.create_rectangle(405, 170, 960, 290, width=2)
        sf.vag = PhotoImage(file="extravaganza.png")
        sf.c.create_image(470, 230, image=sf.vag)
        sf.c.create_text(650, 200, text="Veg Vaganza", fill="#000000", font=("Cooper Black", 20))
        sf.c.create_text(860, 200, text="₹400/₹600/₹250", fill="#ff3838", font=("default", 17, 'bold'))
        sf.v2 = IntVar()
        sf.C21 = Radiobutton(sf.vegf2, text="Medium", value=10, variable=sf.v2)
        sf.C21.place(x=550, y=220)
        sf.C22 = Radiobutton(sf.vegf2, text="Large", value=20, variable=sf.v2)
        sf.C22.place(x=650, y=220)
        sf.C23 = Radiobutton(sf.vegf2, text="Regular", value=30, variable=sf.v2)
        sf.C23.place(x=750, y=220)
        sf.C21.select()
        sf.C21.deselect()
        sf.C21.invoke()
        sf.c.create_text(590, 270, text="Quantity : ", fill="#000000", font=("default", 12))
        sf.qty2 = Entry(sf.vegf2, textvariable=sf.q2, bg="#aae2d7", font=("default", 12), width=4, )
        sf.qty2.place(x=650, y=260)
        sf.add2 = Button(sf.vegf2, text="ADD", command=lambda: addch2(), bg="#0b1335", cursor="hand2", fg="white", bd=4,
                         font=("default", 12, 'bold'))
        sf.add2.place(x=850, y=240)
        def addch2():
            if sf.v2.get() == 10:
                ch2 = "Medium"
                pric2 = 400
            elif sf.v2.get() == 20:
                ch2 = "Large"
                pric2 = 600
            else:
                ch2 = "Regular"
                pric2 = 250
            sf.addlist(["Veg Vaganza", ch2, sf.q2.get(), pric2 * int(sf.q2.get())])
    # pizza 3
        sf.c.create_rectangle(405, 290, 960, 410, width=2)
        sf.pep = PhotoImage(file="5-pepper-veg-pizza.png")
        sf.c.create_image(470, 350, image=sf.pep)
        sf.c.create_text(650, 320, text="5 Pepper", fill="#000000", font=("Cooper Black", 20))
        sf.c.create_text(860, 320, text="₹385/₹550/₹225", fill="#ff3838", font=("default", 17, 'bold'))
        sf.v3 = IntVar()
        sf.C31 = Radiobutton(sf.vegf2, text="Medium", value=10, variable=sf.v3)
        sf.C31.place(x=550, y=340)
        sf.C32 = Radiobutton(sf.vegf2, text="Large", value=20, variable=sf.v3)
        sf.C32.place(x=650, y=340)
        sf.C33 = Radiobutton(sf.vegf2, text="Regular", value=30, variable=sf.v3)
        sf.C33.place(x=750, y=340)
        sf.C31.select()
        sf.C31.deselect()
        sf.C31.invoke()
        sf.c.create_text(590, 390, text="Quantity : ", fill="#000000", font=("default", 12))
        sf.qty3 = Entry(sf.vegf2, textvariable=sf.q3, bg="#aae2d7", font=("default", 12), width=4, )
        sf.qty3.place(x=650, y=380)
        sf.add3 = Button(sf.vegf2, text="ADD", command=lambda: addch3(), bg="#0b1335", cursor="hand2", fg="white", bd=4,
                         font=("default", 12, 'bold'))
        sf.add3.place(x=850, y=360)
        def addch3():
            if sf.v3.get() == 10:
                ch3 = "Medium"
                pric3 = 385
            elif sf.v3.get() == 20:
                ch3 = "Large"
                pric3 = 550
            else:
                ch3 = "Regular"
                pric3 = 225
            sf.addlist(["5 Pepper     ", ch3, sf.q3.get(), pric3 * int(sf.q3.get())])
        # pizza 4
        sf.c.create_rectangle(405, 410, 960, 530, width=2)
        sf.mag = PhotoImage(file="Margherit.png")
        sf.c.create_image(470, 470, image=sf.mag)
        sf.c.create_text(650, 440, text="Margherita", fill="#000000", font=("Cooper Black", 20))
        sf.c.create_text(860, 440, text="₹195/₹385/₹99", fill="#ff3838", font=("default", 17, 'bold'))
        sf.v4 = IntVar()
        sf.C41 = Radiobutton(sf.vegf2, text="Medium", value=10, variable=sf.v4)
        sf.C41.place(x=550, y=460)
        sf.C42 = Radiobutton(sf.vegf2, text="Large", value=20, variable=sf.v4)
        sf.C42.place(x=650, y=460)
        sf.C43 = Radiobutton(sf.vegf2, text="Regular", value=30, variable=sf.v4)
        sf.C43.place(x=750, y=460)
        sf.C41.select()
        sf.C41.deselect()
        sf.C41.invoke()
        sf.c.create_text(590, 500, text="Quantity : ", fill="#000000", font=("default", 12))
        sf.qty4 = Entry(sf.vegf2, textvariable=sf.q4, bg="#aae2d7", font=("default", 12), width=4, )
        sf.qty4.place(x=650, y=500)
        sf.add4 = Button(sf.vegf2, text="ADD", command=lambda: addch4(), bg="#0b1335", cursor="hand2", fg="white", bd=4,
                         font=("default", 12, 'bold'))
        sf.add4.place(x=850, y=480)
        def addch4():
            if sf.v4.get() == 10:
                ch4 = "Medium"
                pric4 = 195
            elif sf.v4.get() == 20:
                ch4 = "Large"
                pric4 = 385
            else:
                ch4 = "Regular"
                pric4 = 99
            sf.addlist(["Margherita  ", ch4, sf.q4.get(), pric4 * int(sf.q4.get())])
        sf.con = Button(sf.vegf2, text="Confirm Order", command=lambda: sf.Orderde(sf.x), bg="#0b1335", cursor="hand2",
                        fg="white", bd=5, font=("default", 18, 'bold'))
        sf.con.place(x=1050, y=250)
        sf.more = Button(sf.vegf2, text="Add More..", command=lambda: sf.menulist(sf.x), bg="#0b1335", cursor="hand2",
                         fg="white", bd=5, font=("default", 18, 'bold'))
        sf.more.place(x=1050, y=350)
        sf.vegf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()
    ##----page 8 ------
    def addlist(sf, q):
        if q[-2] != "0" and q[-2].isdigit():
            sf.cartlist.append(q)
            sf.amount = sf.amount + q[-1]
            messagebox.showinfo("Cart", "Item Successfully added")
        else:
            messagebox.showinfo("Cart", "Enter Valid Quantity to add")
        print(sf.cartlist, sf.amount)
    # --  page 9------
    def nonvegpiz(sf, x):#M
        sf.x = x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("BIG SLICE PIZZA")
        sf.scr.geometry("1366x768")
        sf.nonvegf1 = Frame(sf.scr, height=150, width=1366)
        sf.c = Canvas(sf.nonvegf1, height=150, width=1366)
        sf.c.pack()
        sf.logo = PhotoImage(file="logo.PNG")
        sf.c.create_image(683, 75, image=sf.logo)
        sf.home = Button(sf.nonvegf1, text="Log Out", command=lambda: sf.Login(), bg="#0b1335", cursor="hand2",
                         fg="white", bd=5, font=("default", 16, 'bold'))
        sf.home.place(x=1000, y=90)
        sf.localtime = time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000, 50, text=sf.localtime, fill="white", font=("default", 16))
        sf.nonvegf1.pack(fill=BOTH, expand=1)
        sf.nonvegf2 = Frame(sf.scr, height=618, width=1366)
        sf.c = Canvas(sf.nonvegf2, height=618, width=1366)
        sf.c.pack()
        sf.logo1 = PhotoImage(file="pizzamain.png")
        sf.c.create_image(683, 309, image=sf.logo1)
        sf.log = Label(sf.nonvegf2, text="NON-VEG PIZZA", bg="#9db1f2", font=("Cooper Black", 22))
        sf.log.place(x=580, y=4)
        sf.c.create_rectangle(400, 40, 966, 540, fill="#d3ede6", outline="white", width=6)
        sf.q5 = StringVar()
        sf.q6 = StringVar()
        sf.q7 = StringVar()
        sf.q8 = StringVar()
        sf.q5.set("0")
        sf.q6.set("0")
        sf.q7.set("0")
        sf.q8.set("0")
        # pizza 1
        sf.c.create_rectangle(405, 50, 960, 170, width=2)
        sf.delu = PhotoImage(file="Non-Veg_Supreme.png")
        sf.c.create_image(470, 110, image=sf.delu)
        sf.c.create_text(650, 80, text="Non-Veg Supreme", fill="#000000", font=("Cooper Black", 20))
        sf.c.create_text(860, 80, text="₹450/₹650/₹250", fill="#ff3838", font=("default", 17, 'bold'))
        sf.v5 = IntVar()
        sf.C51 = Radiobutton(sf.nonvegf2, text="Medium", value=10, variable=sf.v5)
        sf.C51.place(x=550, y=100)
        sf.C52 = Radiobutton(sf.nonvegf2, text="Large", value=20, variable=sf.v5)
        sf.C52.place(x=650, y=100)
        sf.C53 = Radiobutton(sf.nonvegf2, text="Regular", value=30, variable=sf.v5)
        sf.C53.place(x=750, y=100)
        sf.C51.select()
        sf.C51.deselect()
        sf.C51.invoke()
        sf.c.create_text(590, 150, text="Quantity : ", fill="#000000", font=("default", 12))
        sf.qty5 = Entry(sf.nonvegf2, textvariable=sf.q5, bg="#aae2d7", font=("default", 12), width=4, )
        sf.qty5.place(x=650, y=140)
        sf.add5 = Button(sf.nonvegf2, text="ADD", command=lambda: addch5(), bg="#0b1335", cursor="hand2", fg="white",
                         bd=4, font=("default", 12, 'bold'))
        sf.add5.place(x=850, y=120)
        def addch5():
            if sf.v5.get() == 10:
                ch5 = "Medium"
                pric5 = 450
            elif sf.v5.get() == 20:
                ch5 = "Large"
                pric5 = 650
            else:
                ch5 = "Regular"
                pric5 = 250
            sf.addlist(["Non-Veg Supreme", ch5, sf.q5.get(), pric5 * int(sf.q5.get())])
        # pizza 2
        sf.c.create_rectangle(405, 170, 960, 290, width=2)
        sf.vag = PhotoImage(file="nonChicken_Tikka.png")
        sf.c.create_image(470, 230, image=sf.vag)
        sf.c.create_text(650, 200, text="Chicken Tikka", fill="#000000", font=("Cooper Black", 20))
        sf.c.create_text(860, 200, text="₹400/₹600/₹250", fill="#ff3838", font=("default", 17, 'bold'))
        sf.v6 = IntVar()
        sf.C61 = Radiobutton(sf.nonvegf2, text="Medium", value=10, variable=sf.v6)
        sf.C61.place(x=550, y=220)
        sf.C62 = Radiobutton(sf.nonvegf2, text="Large", value=20, variable=sf.v6)
        sf.C62.place(x=650, y=220)
        sf.C63 = Radiobutton(sf.nonvegf2, text="Regular", value=30, variable=sf.v6)
        sf.C63.place(x=750, y=220)
        sf.C61.select()
        sf.C61.deselect()
        sf.C61.invoke()
        sf.c.create_text(590, 270, text="Quantity : ", fill="#000000", font=("default", 12))
        sf.qty6 = Entry(sf.nonvegf2, textvariable=sf.q6, bg="#aae2d7", font=("default", 12), width=4, )
        sf.qty6.place(x=650, y=260)
        sf.add6 = Button(sf.nonvegf2, text="ADD", command=lambda: addch6(), bg="#0b1335", cursor="hand2", fg="white",
                         bd=4, font=("default", 12, 'bold'))
        sf.add6.place(x=850, y=240)
        def addch6():
            if sf.v6.get() == 10:
                ch6 = "Medium"
                pric6 = 400
            elif sf.v6.get() == 20:
                ch6 = "Large"
                pric6 = 600
            else:
                ch6 = "Regular"
                pric6 = 250
            sf.addlist(["Chicken Tikka", ch6, sf.q6.get(), pric6 * int(sf.q6.get())])
        sf.c.create_rectangle(405, 290, 960, 410, width=2)
        sf.pep = PhotoImage(file="non-Chicken_Sausage.png")
        sf.c.create_image(470, 350, image=sf.pep)
        sf.c.create_text(650, 320, text="Chicken Sausage", fill="#000000", font=("Cooper Black", 20))
        sf.c.create_text(860, 320, text="₹385/₹550/₹225", fill="#ff3838", font=("default", 17, 'bold'))
        sf.v7 = IntVar()
        sf.C71 = Radiobutton(sf.nonvegf2, text="Medium", value=10, variable=sf.v7)
        sf.C71.place(x=550, y=340)
        sf.C72 = Radiobutton(sf.nonvegf2, text="Large", value=20, variable=sf.v7)
        sf.C72.place(x=650, y=340)
        sf.C73 = Radiobutton(sf.nonvegf2, text="Regular", value=30, variable=sf.v7)
        sf.C73.place(x=750, y=340)
        sf.C71.select()
        sf.C71.deselect()
        sf.C71.invoke()
        sf.c.create_text(590, 390, text="Quantity : ", fill="#000000", font=("default", 12))
        sf.qty7 = Entry(sf.nonvegf2, textvariable=sf.q7, bg="#aae2d7", font=("default", 12), width=4, )
        sf.qty7.place(x=650, y=380)
        sf.add7 = Button(sf.nonvegf2, text="ADD", command=lambda: addch7(), bg="#0b1335", cursor="hand2", fg="white",
                         bd=4, font=("default", 12, 'bold'))
        sf.add7.place(x=850, y=360)
        def addch7():
            if sf.v7.get() == 10:
                ch7 = "Medium"
                pric7 = 385
            elif sf.v7.get() == 20:
                ch7 = "Large"
                pric7 = 550
            else:
                ch7 = "Regular"
                pric7 = 225
            sf.addlist(["Chicken Sausage", ch7, sf.q7.get(), pric7 * int(sf.q7.get())])
        # pizza 4
        sf.c.create_rectangle(405, 410, 960, 530, width=2)
        sf.mag = PhotoImage(file="no-LoadedL.png")
        sf.c.create_image(470, 470, image=sf.mag)
        sf.c.create_text(650, 440, text="Chicken Peri", fill="#000000", font=("Cooper Black", 20))
        sf.c.create_text(860, 440, text="₹195/₹385/₹99", fill="#ff3838", font=("default", 17, 'bold'))
        sf.v8 = IntVar()
        sf.C81 = Radiobutton(sf.nonvegf2, text="Medium", value=10, variable=sf.v8)
        sf.C81.place(x=550, y=460)
        sf.C82 = Radiobutton(sf.nonvegf2, text="Large", value=20, variable=sf.v8)
        sf.C82.place(x=650, y=460)
        sf.C83 = Radiobutton(sf.nonvegf2, text="Regular", value=30, variable=sf.v8)
        sf.C83.place(x=750, y=460)
        sf.C81.select()
        sf.C81.deselect()
        sf.C81.invoke()
        sf.c.create_text(590, 500, text="Quantity : ", fill="#000000", font=("default", 12))
        sf.qty8 = Entry(sf.nonvegf2, textvariable=sf.q8, bg="#aae2d7", font=("default", 12), width=4, )
        sf.qty8.place(x=650, y=500)
        sf.add8 = Button(sf.nonvegf2, text="ADD", command=lambda: addch8(), bg="#0b1335", cursor="hand2", fg="white",
                         bd=4, font=("default", 12, 'bold'))
        sf.add8.place(x=850, y=480)
        def addch8():
            if sf.v8.get() == 10:
                ch8 = "Medium"
                pric8 = 195
            elif sf.v8.get() == 20:
                ch8 = "Large"
                pric8 = 385
            else:
                ch8 = "Regular"
                pric8 = 99
            sf.addlist(["Chicken Peri", ch8, sf.q8.get(), pric8 * int(sf.q8.get())])
        sf.con = Button(sf.nonvegf2, text="Confirm Order", command=lambda: sf.Orderde(sf.x), bg="#0b1335",
                        cursor="hand2", fg="white", bd=5, font=("default", 18, 'bold'))
        sf.con.place(x=1050, y=250)
        sf.more = Button(sf.nonvegf2, text="Add More..", command=lambda: sf.menulist(sf.x), bg="#0b1335",
                         cursor="hand2", fg="white", bd=5, font=("default", 18, 'bold'))
        sf.more.place(x=1050, y=350)
        sf.nonvegf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()
    # --  page 10---
        sf.con = Button(sf.sidef2, text="Confirm Order", command=lambda: sf.Orderde(sf.x), bg="#0b1335", cursor="hand2",
                        fg="white", bd=5, font=("default", 18, 'bold'))
        sf.con.place(x=600, y=430)
        sf.more = Button(sf.sidef2, text="Add More..", command=lambda: sf.menulist(sf.x), bg="#0b1335", cursor="hand2",
                         fg="white", bd=5, font=("default", 16, 'bold'))
        sf.more.place(x=630, y=500)
        sf.sidef2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()
    # --  page 11------
    def Address(sf, x):#P
        sf.x = x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("BIG SLICE PIZZA")
        sf.scr.geometry("1366x768")
        sf.addf1 = Frame(sf.scr, height=150, width=1366)
        sf.c = Canvas(sf.addf1, height=150, width=1366)
        sf.c.pack()
        sf.logo = PhotoImage(file="logo.PNG")
        sf.c.create_image(683, 75, image=sf.logo)
        sf.out = Button(sf.addf1, text="Log Out", command=lambda: sf.Login(), bg="#0b1335", cursor="hand2", fg="white",
                        font=("default", 16))
        sf.out.place(x=1200, y=100)
        sf.addf1.pack(fill=BOTH, expand=1)
        sf.addf2 = Frame(sf.scr, height=618, width=1366)
        sf.c = Canvas(sf.addf2, height=618, width=1366)
        sf.c.pack()
        sf.logo1 = PhotoImage(file="pizzamain.png")
        sf.c.create_image(683, 309, image=sf.logo1)
        sf.log = Label(sf.addf2, text="Address", fg="white", bg="#0b1335", width=20, font=("default", 27))
        sf.log.place(x=480, y=110)
        sf.c.create_rectangle(150, 100, 1216, 450, fill="#d3ede6", outline="white", width=6)
        sf.lab1 = Label(sf.addf2, text="City", bg="#d3ede6", font=("cooper black", 18))
        sf.lab1.place(x=190, y=200)
        sf.city = Entry(sf.addf2, bg="white", width=15, font=("default", 18), bd=5)
        sf.city.place(x=430, y=200)
        sf.lab2 = Label(sf.addf2, text="Locality", bg="#d3ede6", font=("cooper black", 18))
        sf.lab2.place(x=730, y=200)
        sf.loc = Entry(sf.addf2, bg="white", width=15, font=("default", 18), bd=5)
        sf.loc.place(x=918, y=200)
        sf.lab3 = Label(sf.addf2, text="Building Name", bg="#d3ede6", font=("cooper black", 18))
        sf.lab3.place(x=190, y=250)
        sf.buil = Entry(sf.addf2, bg="white", width=15, font=("default", 18), bd=5)
        sf.buil.place(x=430, y=250)
        sf.lab4 = Label(sf.addf2, text="House No.", bg="#d3ede6", font=("cooper black", 18))
        sf.lab4.place(x=730, y=250)
        sf.hou = Entry(sf.addf2, bg="white", width=15, font=("default", 18), bd=5)
        sf.hou.place(x=918, y=250)
        sf.lab5 = Label(sf.addf2, text="Landmark", bg="#d3ede6", font=("cooper black", 18))
        sf.lab5.place(x=190, y=300)
        sf.lan = Entry(sf.addf2, bg="white", width=15, font=("default", 18), bd=5)
        sf.lan.place(x=430, y=300)
        sf.bc = Button(sf.addf2, text="Back", command=lambda: sf.Orderde(sf.x), cursor="hand2", fg="white",
                       bg="#0b1335", font=("default", 18), bd=5)
        sf.bc.place(x=370, y=370)
        sf.rg = Button(sf.addf2, text="Order Now", command=lambda: sf.orderpay(sf.x), cursor="hand2", fg="white",
                       bg="#0b1335", font=("default", 18), bd=5)
        sf.rg.place(x=610, y=370)
        def clear(sf):
            sf.city.delete(0, END)
            sf.loc.delete(0, END)
            sf.buil.delete(0, END)
            sf.hou.delete(0, END)
            sf.lan.delete(0, END)
        sf.cl = Button(sf.addf2, text="Clear", command=lambda: clear(sf), cursor="hand2", fg="white", bg="#0b1335",
                       font=("default", 18), bd=5)
        sf.cl.place(x=910, y=370)
        sf.addf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()
    # --  page 12------
    def Orderde(sf, x):#H
        sf.x = x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("BIG SLICE PIZZA")
        sf.scr.geometry("1366x768")
        sf.ordf1 = Frame(sf.scr, height=150, width=1366)
        sf.c = Canvas(sf.ordf1, height=150, width=1366)
        sf.c.pack()
        sf.logo = PhotoImage(file="logo.PNG")
        sf.c.create_image(683, 75, image=sf.logo)
        sf.home = Button(sf.ordf1, text="Log Out", command=lambda: sf.Login(), bg="#0b1335", cursor="hand2", fg="white",
                         bd=5, font=("default", 16, 'bold'))
        sf.home.place(x=1000, y=90)
        sf.localtime = time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000, 50, text=sf.localtime, fill="white", font=("default", 16))
        sf.ordf1.pack(fill=BOTH, expand=1)
        sf.ordf2 = Frame(sf.scr, height=618, width=1366)
        sf.c = Canvas(sf.ordf2, height=618, width=1366)
        sf.c.pack()
        sf.logo1 = PhotoImage(file="pizzamain.png")
        sf.c.create_image(683, 309, image=sf.logo1)
        sf.log = Label(sf.ordf2, text="YOUR ORDER", bg="#9db1f2", font=("Cooper Black", 22))
        sf.log.place(x=450, y=4)
        sf.c.create_rectangle(250, 50, 800, 500, fill="#d3ede6", outline="white", width=6)
        sf.amt = sf.amount
        sf.text = "Total : " + str(sf.amt)
        sf.tot = Label(sf.ordf2, text=sf.text, bg="#f2da9d", width=12, font=("Cooper Black", 22))
        sf.tot.place(x=900, y=250)
        if sf.x == "deli":
            sf.y = sf.Address
        if sf.x == "pick":
            sf.y = sf.orderpay
        sf.pay = Button(sf.ordf2, text="Pay", command=lambda: sf.y(sf.x), bg="#0b1335", cursor="hand2", fg="white",
                        bd=5, font=("default", 18, 'bold'))
        sf.pay.place(x=900, y=300)
        sf.exi = Button(sf.ordf2, text="Add more", command=lambda: sf.menulist(sf.x), bg="#0b1335", cursor="hand2",
                        fg="white", bd=5, font=("default", 18, 'bold'))
        sf.exi.place(x=1070, y=300)
        sf.c.create_text(525, 80, text="Items\tSize\tQty\tPrice", font=("cooper black", 18))
        sf.c.create_text(525, 90, text="_______________________________________", font=("cooper black", 18))
        y = 100
        for i in sf.cartlist:
            y += 30
            s = i[0] + "\t" + i[1] + "\t" + i[2] + "\t" + str(i[3])
            sf.c.create_text(525, y, text=s, font=("default", 16))
        sf.ordf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()
    # -----  database-------
    def logindatabase(sf):#M
        sf.credlog = sf.resultlog()
        sf.con = connect("pizza.db")
        sf.cur = sf.con.cursor()
        try:
            sf.cur.execute(
                "create table customer(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,email varchar(50),mob varchar(50) not null)")
        except:
            pass
        x = sf.cur.execute(
            "select count(*) from customer where username=%r and password=%r" % (sf.credlog[0], sf.credlog[1]))
        messagebox.showinfo("Login", "You have Successfully Log In\nWelcome to the BIG SLICE PIZZA")
        sf.pizmain()
    def Regdatabase(sf):
        sf.credreg = sf.resultreg()
        sf.con = connect("pizza.db")
        sf.cur = sf.con.cursor()
        try:
            sf.cur.execute(
                "create table customer(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,email varchar(50),mob varchar(50) not null)")
        except:
            pass
        x = sf.cur.execute(
            "select count(*) from customer where username=%r and mob=%r " % (sf.credreg[0], sf.credreg[5]))
        if list(x)[0][0] == 0:
            if sf.credreg[0] == "" or sf.credreg[1] == "" or sf.credreg[2] == "" or sf.credreg[3] == "" or sf.credreg[
                5] == "":
                messagebox.showinfo("Register", "Empty Entry is not Allowed(except Email)")
            else:
                sf.cur.execute("insert into customer values(%r,%r,%r,%r,%r,%r)" % (
                sf.credreg[0], sf.credreg[1], sf.credreg[2], sf.credreg[3], sf.credreg[4], sf.credreg[5]))
                sf.con.commit()
                messagebox.showinfo("Register", "You are Successfully Registered")
                sf.Login()
        else:
            messagebox.showinfo("Register", "Username Already Exist \nEnter New Username")
    def orderpay(sf, x):
       messagebox.showinfo("Pay", "Payment Done!!")
x = Pizza()
x.main()
