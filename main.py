from tkinter import *
import random,math,os
from tkinter import messagebox
import sqlite3


class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1250x700+0+0")
        self.root.title("FAST FOOD CENTRE")
        bg_color= "#17202A"
        title = Label(self.root,text ="FAST FOOD CENTRE ",bd=12,relief=GROOVE,bg=bg_color,fg = "white",font=("times new roman",30,"bold")).pack(fill=X)
        # ======variables=======
        self.a1_txtt = IntVar()
        self.a2_txtt = IntVar()
        self.a3_txtt= IntVar()
        self.a4_txtt= IntVar()
        self.a5_txtt = IntVar()

        self.b1_txtt = IntVar()
        self.b2_txtt = IntVar()
        self.b3_txtt = IntVar()
        self.b4_txtt = IntVar()
        self.b5_txtt = IntVar()

        self.c1_txtt = IntVar()
        self.c2_txtt = IntVar()
        self.c3_txtt = IntVar()
        self.c4_txtt = IntVar()
        self.c5_txtt = IntVar()

        # =======Total price and tax variables
        self.a_price = StringVar()
        self.b_price = StringVar()
        self.c_price = StringVar()

        self.a_tax = StringVar()
        self.b_tax = StringVar()
        self.c_tax = StringVar()

        # =====Customer=======
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))


        #Customer details
        F1 = LabelFrame(self.root,text ="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg = bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lb1 = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl = Label(F1, text="Phone Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,column=3,padx=5,pady=10)


        # ========MAIN FRAME=======

        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Mains", font=("times new roman", 15, "bold"), fg="gold",
                        bg=bg_color)
        F2.place(x=5, y=170, width=340, height=335)

        a1_lbl = Label(F2, text="Burger", font=("times new roman", 16, "bold"), bg=bg_color, fg="#5DADE2").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        a1_txt = Entry(F2, width=15, textvariable=self.a1_txtt,font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=0, column=1,
                                                                                                     padx=10, pady=10)

        a2_lbl = Label(F2, text="Pizza", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="#5DADE2").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        a2_txt = Entry(F2, width=15, textvariable=self.a2_txtt,font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=1,column=1,padx=5,pady=10)

        a3_lbl = Label(F2, text="Shawarma", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="#5DADE2").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        a3_txt = Entry(F2, width=15, textvariable=self.a3_txtt,font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        a4_lbl = Label(F2, text="Momos", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="#5DADE2").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        a4_txt = Entry(F2, width=15, textvariable=self.a4_txtt,font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        a5_lbl = Label(F2, text="Wraps", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="#5DADE2").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        a6_txt = Entry(F2, width=15, textvariable=self.a5_txtt,font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        # ========SIDE FRAME=======

        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Sides", font=("times new roman", 15, "bold"),
                        fg="gold",
                        bg=bg_color)
        F3.place(x=340, y=170, width=340, height=335)

        b1_lbl = Label(F3, text="Fries", font=("times new roman", 16, "bold"), bg=bg_color, fg="#5DADE2").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        b1_txt = Entry(F3, width=15, textvariable=self.b1_txtt,font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=0, column=1,
                                                                                                       padx=10, pady=10)

        b2_lbl = Label(F3, text="Nuggets", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="#5DADE2").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        b2_txt = Entry(F3, width=15, textvariable=self.b2_txtt,font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=1,column=1,padx=5, pady=10)

        b3_lbl = Label(F3, text="Garlic Bread", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="#5DADE2").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        b3_txt = Entry(F3, width=15, textvariable=self.b3_txtt,font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=2,column=1, padx=10, pady=10)

        b4_lbl = Label(F3, text="Chi-Popcorn", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="#5DADE2").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        b4_txt = Entry(F3, width=15, textvariable=self.b4_txtt,font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        b5_lbl = Label(F3, text="Chi-Peri-Peri", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="#5DADE2").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        b5_txt = Entry(F3, width=15, textvariable=self.b5_txtt,font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=4,column=1,padx=10, pady=10)

        # ========BEVERAGE FRAME=======

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Beverages", font=("times new roman", 15, "bold"), fg="gold",bg=bg_color)
        F4.place(x=670, y=170, width=340, height=335)

        c1_lbl = Label(F4, text="Coke", font=("times new roman", 16, "bold"), bg=bg_color, fg="#5DADE2").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        c1_txt = Entry(F4, width=15, textvariable=self.c1_txtt,font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        c2_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="#5DADE2").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=15, textvariable=self.c2_txtt,font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=1,column=1,padx=5,pady=10)

        c3_lbl = Label(F4, text="Mazza", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="#5DADE2").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=15, textvariable=self.c3_txtt,font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl = Label(F4, text="7up", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="#5DADE2").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=15, textvariable=self.c4_txtt,font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=3,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

        c5_lbl = Label(F4, text="Mirinda", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="#5DADE2").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        c5_txt = Entry(F4, width=15, textvariable=self.c5_txtt,font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=4,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)


        # billing System
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=330)

        bill_title = Label(F5, text="Bill", font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)


        # Button frame
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu",font=("times new roman", 15, "bold"), fg ="gold", bg=bg_color)
        F6.place(x=0, y=510, relwidth=1, height=140)

        m1 = Label(F6, text="Total Mains Price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.a_price,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        m2 = Label(F6, text="Total Sides Price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.b_price,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3 = Label(F6, text="Total Beverages Price", bg=bg_color, fg="white",
                   font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.c_price,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        s1 = Label(F6, text="Mains Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=0, column=2,padx=20,pady=1,sticky="w")
        s1_txt = Entry(F6, width=18, textvariable=self.a_tax,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        s2 = Label(F6, text="Sides Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        s2_txt = Entry(F6, width=18, textvariable=self.b_tax,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        s3 = Label(F6, text="Beverages Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=2, column=2, padx=20, pady=1, sticky="w")
        s3_txt = Entry(F6, width=18, textvariable=self.c_tax,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=750, width=580, height=105)

        total_btn = Button(btn_F, text="Total", bg="#5DADE2", fg="white", bd=2, pady=15, width=10,command=self.total,
                           font="arial 15 bold").grid(row=0, column=0, padx=5, pady=5)
        GBill_btn = Button(btn_F, text="Generate Bill", bg="#5DADE2", fg="white", bd=2, pady=15, width=10,command=self.bill_area,
                           font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_F, text="Clear", bg="#5DADE2", fg="white", bd=2, pady=15, width=10,command=self.clear_data,
                           font="arial 15 bold").grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_F, text="Exit", bg="#5DADE2", fg="white", bd=2, pady=15, width=10,command=self.Exit_app,
                          font="arial 15 bold").grid(row=0, column=3, padx=5, pady=5)

    def total(self):

        self.a_a1 = (self.a1_txtt.get() * 80)
        self.a_a2 = (self.a2_txtt.get() * 120)
        self.a_a3 = (self.a3_txtt.get() * 70)
        self.a_a4 = (self.a4_txtt.get() * 60)
        self.a_a5 = (self.a5_txtt.get() * 130)

        self.total_mains_price = float(
            (self.a_a1) +
            (self.a_a2) +
            (self.a_a3) +
            (self.a_a4) +
            (self.a_a5)
        )
        self.a_price.set("Rs. " + str(self.total_mains_price))
        self.x_tax = round((self.total_mains_price * 0.05), 2)
        self.a_tax.set("Rs. " + str(self.x_tax))

        self.b_b1 = (self.b1_txtt.get() * 80)
        self.b_b2 = (self.b2_txtt.get() * 90)
        self.b_b3 = (self.b3_txtt.get() * 60)
        self.b_b4 = (self.b4_txtt.get() * 70)
        self.b_b5 = (self.b5_txtt.get() * 80)

        self.total_sides_price = float(
            (self.b_b1) +
            (self.b_b2) +
            (self.b_b3) +
            (self.b_b4) +
            (self.b_b5)
        )
        self.b_price.set("Rs. " + str(self.total_sides_price))
        self.y_tax= round((self.total_sides_price * 0.1), 2)
        self.b_tax.set("Rs. " + str(self.y_tax))

        self.c_c1 = (self.c1_txtt.get() * 45)
        self.c_c2 = (self.c2_txtt.get() * 60)
        self.c_c3 = (self.c3_txtt.get() * 50)
        self.c_c4 = (self.c4_txtt.get() * 70)
        self.c_c5 = (self.c5_txtt.get() * 40)

        self.total_beverages_price = float(
            (self.c_c1) +
            (self.c_c2) +
            (self.c_c3) +
            (self.c_c4) +
            (self.c_c5)
        )
        self.c_price.set("Rs. " + str(self.total_beverages_price))
        self.z_tax= round((self.total_beverages_price * 0.05), 2)
        self.c_tax.set("Rs. " + str(self.z_tax))

        self.Total_bill=float( self.total_mains_price+
                               self.total_sides_price+
                               self.total_beverages_price+
                               self.x_tax+
                               self.y_tax+
                               self.z_tax
                             )



    def welcome_bill(self):
        self.txtarea.insert(END, "\tWELCOME TO FASTFOOD CENTER")
        self.txtarea.insert(END, f"\n BILL NUMBER : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()} ")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phone.get()} ")
        self.txtarea.insert(END, f"\n======================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\t\t Price")
        self.txtarea.insert(END, f"\n======================================")


    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        else:
            self.welcome_bill()

            # ===cosmetics======
            if self.a1_txtt.get() != 0:
                self.txtarea.insert(END, f"\n Burger\t\t{self.a1_txtt.get()}\t\t{self.a_a1}")
            if self.a2_txtt.get() != 0:
                self.txtarea.insert(END, f"\n Pizza\t\t{self.a2_txtt.get()}\t\t{self.a_a2}")
            if self.a3_txtt.get() != 0:
                self.txtarea.insert(END, f"\n Shawarna\t\t{self.a3_txtt.get()}\t\t{self.a_a3}")
            if self.a4_txtt.get() != 0:
                self.txtarea.insert(END, f"\n Momos\t\t{self.a4_txtt.get()}\t\t{self.a_a4}")
            if self.a5_txtt.get() != 0:
                self.txtarea.insert(END, f"\n Wraps\t\t{self.a5_txtt.get()}\t\t{self.a_a5}")

            # ===grocery======
            if self.b1_txtt.get() != 0:
                self.txtarea.insert(END, f"\n Fries\t\t{self.b1_txtt.get()}\t\t{self.b_b1}")
            if self.b2_txtt.get() != 0:
                self.txtarea.insert(END, f"\n Nuggets\t\t{self.b2_txtt.get()}\t\t{self.b_b2}")
            if self.b3_txtt.get() != 0:
                self.txtarea.insert(END, f"\n Garlic  Bread\t\t{self.b3_txtt.get()}\t\t{self.b_b3}")
            if self.b4_txtt.get() != 0:
                self.txtarea.insert(END, f"\n Chi-Popcorn\t\t{self.b4_txtt.get()}\t\t{self.b_b4}")
            if self.b5_txtt.get() != 0:
                self.txtarea.insert(END, f"\n Chi-Peri-Peri\t\t{self.b5_txtt.get()}\t\t{self.b_b5}")

            # ===Drinks======
            if self.c1_txtt.get() != 0:
                self.txtarea.insert(END, f"\n Coke\t\t{self.c1_txtt.get()}\t\t{self.c_c1}")
            if self.c2_txtt.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.c2_txtt.get()}\t\t{self.c_c2}")
            if self.c3_txtt.get() != 0:
                self.txtarea.insert(END, f"\n Mazza\t\t{self.c3_txtt.get()}\t\t{self.c_c3}")
            if self.c4_txtt.get() != 0:
                self.txtarea.insert(END, f"\n 7up\t\t{self.c4_txtt.get()}\t\t{self.c_c4}")
            if self.c5_txtt.get() != 0:
                self.txtarea.insert(END, f"\n Mirinda\t\t{self.c5_txtt.get()}\t\t{self.c_c5}")

            self.txtarea.insert(END, f"\n-------------------------------------")
            if self.a_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Mains Tax\t\t\t{self.a_tax.get()}")
            if self.b_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Sides Tax\t\t\t{self.b_tax.get()}")
            if self.c_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Beverages Tax\t\t\t{self.c_tax.get()}")

            self.txtarea.insert(END, f"\n Total Bill:\t\t\t Rs. {self.Total_bill}")
            self.txtarea.insert(END, f"\n-------------------------------------")
            self.save_bill()

    def save_bill(self):
        '''op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("Invoice/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
        else:
            return'''

        conn = sqlite3.connect('C:\\Users\\uniya\\PycharmProjects\\pythonProject2\\Receipt.db')
        c = conn.cursor()

        #c.execute(
         #   "CREATE TABLE INVOICE(bill_no integer,c_name text,c_phone integer,Total_bill integer);")
        c.execute("INSERT INTO INVOICE(bill_no,c_name,c_phone,Total_bill) VALUES(?,?,?,?)",
                  (str(self.bill_no.get()), str(self.c_name.get()), str(self.c_phone.get()),str(self.Total_bill)))
        conn.commit()
        print("data entered")
        conn.close()



    def clear_data(self):
        # ======variables=======
        self.a1_txtt.set(0)
        self.a2_txtt.set(0)
        self.a3_txtt.set(0)
        self.a4_txtt.set(0)
        self.a5_txtt.set(0)

        self.b1_txtt.set(0)
        self.b2_txtt.set(0)
        self.b3_txtt.set(0)
        self.b4_txtt.set(0)
        self.b5_txtt.set(0)

        self.c1_txtt.set(0)
        self.c2_txtt.set(0)
        self.c3_txtt.set(0)
        self.c4_txtt.set(0)
        self.c5_txtt.set(0)

        # =======Total price and tax variables
        self.a_price.set("")
        self.b_price.set("")
        self.c_price.set("")

        self.a_tax.set("")
        self.b_tax.set("")
        self.c_tax.set("")

        # =====Customer=======
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.txtarea.delete('1.0', END)
        #self.welcome_bill.clear()

    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()