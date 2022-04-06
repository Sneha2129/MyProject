from tkinter import *
import random,math,os
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('C:\\Users\\ritik\\PycharmProjects\\tkinter_project\\Reciept.db')
c = conn.cursor()

c.execute('SELECT * FROM INVOICE where bill_no="1548"')
print(c.fetchall())
conn.commit()
conn.close()