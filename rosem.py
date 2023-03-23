#import all the modules
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import tkinter.messagebox
import datetime
import math

date=datetime.datetime.now().date()
cnx = mysql.connector.connect(user='root', password='', host='localhost', database='inventory_system2')
# Create a cursor object
cursor = cnx.cursor()


class Application():
    def __init__(self,master,*args,**kwargs):
        self.master=master

        self.left=Frame(self.master,width=666,height=768,bg='#F9F9F9')
        self.left.pack(side=LEFT)

        self.right = Frame(self.master, width=666, height=768)
        self.right.pack(side=RIGHT)

        #components
        self.date_l=Label(self.left,text="Today's Date: "+str(date),font=('arial 10 bold'),bg='#F9F9F9',fg='black')
        self.date_l.place(x=460,y=50)
        self.heading=Label(self.left,text="ROSEM DESIGNERS",font=('arial 20 bold'),fg='black',bg='#F9F9F9')
        self.heading.place(x=0,y=0)

        self.style=ttk.Style()
        self.style.theme_use('clam')

        # Add a Treeview widget
        self.cols = ('item', 'price', 'qty', 'total')
        self.tree = ttk.Treeview(self.right, column=self.cols, show='headings', height=10)

        # Add a Treeview widget

        #self.tree = ttk.Treeview(self.right, column=("c1", "c2", "c3", 'c4'), show='headings', height=10).place(x=880, y=165)

        self.tree.column("# 1", anchor=CENTER, stretch=NO, width=100)
        self.tree.heading("# 1", text="item")
        self.tree.column("# 2", anchor=CENTER, stretch=NO, width=100)
        self.tree.heading("# 2", text="price")
        self.tree.column("# 3", anchor=CENTER, stretch=NO, width=100)
        self.tree.heading("# 3", text='qty')
        self.tree.column("# 4", anchor=CENTER, stretch=NO, width=100)
        self.tree.heading("# 4", text='total')
        
        self.tree.pack()
        
        self.totText = StringVar()
        self.var = IntVar()
        self.cb = Checkbutton(self.left, text="African Dresses", variable=self.var,bg='#F9F9F9').place(x=10, y=50)
        

        self.var1 = IntVar()
        self.cb = Checkbutton(self.left, text="African Hand Bags", variable=self.var1,bg='#F9F9F9').place(x=10, y=80)
        

        self.var2 = IntVar()
        self.cb = Checkbutton(self.left, text="African Shoes", variable=self.var2,bg='#F9F9F9').place(x=10, y=110)
        

        self.var3 = IntVar()
        self.cb = Checkbutton(self.left, text="African shrits", variable=self.var3,bg='#F9F9F9').place(x=10, y=140)
        

        self.var4 = IntVar()
        self.cb = Checkbutton(self.left, text="African Material", variable=self.var4,bg='#F9F9F9').place(x=10, y=170)
        

        self.var5 = IntVar()
        self.cb = Checkbutton(self.left, text="Bras", variable=self.var5,bg='#F9F9F9').place(x=10, y=200)
        

        self.var6 = IntVar()
        self.cb = Checkbutton(self.left, text="Carftana", variable=self.var6,bg='#F9F9F9').place(x=10, y=230)
        

        self.var7 = IntVar()
        self.cb = Checkbutton(self.left, text="Dresses", variable=self.var7,bg='#F9F9F9').place(x=10, y=260)
        

        self.var8 = IntVar()
        self.cb = Checkbutton(self.left, text="Ear Rings", variable=self.var8,bg='#F9F9F9').place(x=10, y=290)
        

        self.var9 = IntVar()
        self.cb = Checkbutton(self.left, text="Jewelry", variable=self.var9,bg='#F9F9F9').place(x=10, y=320)
        

        self.var10 = IntVar()
        self.cb = Checkbutton(self.left, text="Lady Bags", variable=self.var10,bg='#F9F9F9').place(x=10, y=350)
        

        self.var11 = IntVar()
        self.cb = Checkbutton(self.left, text="Leggings", variable=self.var11,bg='#F9F9F9').place(x=10, y=380)
        

        self.var12 = IntVar()
        self.cb = Checkbutton(self.left, text="Skirts", variable=self.var12,bg='#F9F9F9').place(x=10, y=410)
        

        self.var13 = IntVar()
        self.cb = Checkbutton(self.left, text="Tops", variable=self.var13,bg='#F9F9F9').place(x=10, y=440)
        

        self.var14 = IntVar()
        self.cb = Checkbutton(self.left, text="Underwear", variable=self.var14,bg='#F9F9F9').place(x=10, y=470)
                
        #enteries for window
        self.e1 = Entry(self.master)
        self.e1.place(x=140, y=50)
        
        self.e2 = Entry(self.master)
        self.e2.place(x=140, y=80)
        
        self.e3 = Entry(self.master)
        self.e3.place(x=140, y=110)
        
        self.e4 = Entry(self.master)
        self.e4.place(x=140, y=140)
        
        self.e5 = Entry(self.master)
        self.e5.place(x=140, y=170)
        
        self.e6 = Entry(self.master)
        self.e6.place(x=140, y=200)
        
        self.e7 = Entry(self.master)
        self.e7.place(x=140, y=230)
        
        self.e8 = Entry(self.master)
        self.e8.place(x=140, y=260)
        
        self.e9 = Entry(self.master)
        self.e9.place(x=140, y=290)
        
        self.e10 = Entry(self.master)
        self.e10.place(x=140, y=320)

        self.e11 = Entry(self.master)
        self.e11.place(x=140, y=350)
        
        self.e12 = Entry(self.master)
        self.e12.place(x=140, y=380)
        
        self.e13 = Entry(self.master)
        self.e13.place(x=140, y=410)
        
        self.e14 = Entry(self.master)
        self.e14.place(x=140, y=440)
        
        self.e15 = Entry(self.master)
        self.e15.place(x=140, y=470)
        
        self.e16 = Entry(self.master)
        self.e16.place(x=300, y=50)
        
        self.e17 = Entry(self.master)
        self.e17.place(x=300, y=80)
        
        self.e18 = Entry(self.master)
        self.e18.place(x=300, y=110)
        
        self.e19 = Entry(self.master)
        self.e19.place(x=300, y=140)
        
        self.e20 = Entry(self.master)
        self.e20.place(x=300, y=170)
        
        self.e21 = Entry(self.master)
        self.e21.place(x=300, y=200)
        
        self.e22 = Entry(self.master)
        self.e22.place(x=300, y=230)
        
        self.e23 = Entry(self.master)
        self.e23.place(x=300, y=260)
        
        self.e24 = Entry(self.master)
        self.e24.place(x=300, y=290)
        
        self.e25 = Entry(self.master)
        self.e25.place(x=300, y=320)

        self.e26 = Entry(self.master)
        self.e26.place(x=300, y=350)
        
        self.e27 = Entry(self.master)
        self.e27.place(x=300, y=380)
        
        self.e28 = Entry(self.master)
        self.e28.place(x=300, y=410)
        
        self.e29 = Entry(self.master)
        self.e29.place(x=300, y=440)
        
        self.e30 = Entry(self.master)
        self.e30.place(x=300, y=470)
        
        self.btn_deselect = Button(self.left, text="Uncheck", bg='steelblue',fg='white',command=self.deselect, height=3, width=13).place(x=10,y=540)
        self.btn_refresh = Button(self.left, text="Clear Entry", bg='red',fg='white',command=self.delete, height=3, width=13).place(x=300,y=540)  
        
        self.btn_add=Button(self.master, text="Add", command=self.Show, height=3, width=13).place(x=880, y=155)
        self.btn_print=Button(self.master, text="Print", command=self.print, height=3, width=13).place(x=980,y=155) 
        
        self.btn_order = Button(self.master, text ="Orders", command = self.openNewWindow, height=3, width=13).place(x=1080,y=155)
        self.btn_statement = Button(self.master, text ="Statement", command = self.statement, height=3, width=13).place(x=1180,y=155)
        
        self.btn_save = Button(self.master, text="Add to Database", bg='steelblue',fg='white',command=self.get_items, height=3, width=13).place(x=880,y=480)

        self.delete_button = Button(self.master, text="Delete", command=self.delete_record, height=3, width=13).place(x=1080,y=480)

    
               
    
    def get_items(self):
        self.check_values = [self.var.get(), self.var1.get(), self.var2.get(), self.var3.get(), self.var4.get(), 
                             self.var5.get(), self.var6.get(), self.var7.get(), self.var8.get(), self.var9.get(), 
                             self.var10.get(), self.var11.get(), self.var12.get(), self.var13.get(), self.var14.get()]

        self.data_values = [self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(), self.e5.get(), 
                            self.e6.get(), self.e7.get(), self.e8.get(), self.e9.get(), self.e10.get(), 
                            self.e11.get(), self.e12.get(), self.e13.get(), self.e14.get(), self.e15.get(), 
                            self.e16.get(), self.e17.get(), self.e18.get(), self.e19.get(), self.e20.get(), 
                            self.e21.get(), self.e22.get(), self.e23.get(), self.e24.get(), self.e25.get(), 
                            self.e26.get(), self.e27.get(), self.e28.get(), self.e29.get(), self.e30.get()]
        
        self.collections = ["African Dresses", "African Hand Bags", "African Shoes", "African Shirts", "African Material", 
                "Bras", "Carftana", "Dresses", "Ear Rings", "Jewelry", "Lady Bags", "Leggings", "Skirts", "Tops", "Underwear"]
        
        self.query = "INSERT INTO inventory (Item, Price, Qty) VALUES (%s,%s,%s)"

        self.values_list = []

        for i, item in enumerate(self.collections):
            if self.check_values[i] == 1:
                self.values_list.append((item, self.data_values[i], self.data_values[i + 15]))

        for collin in self.values_list:
            cursor.execute(self.query, collin)
            cnx.commit()
            tkinter.messagebox.showinfo("Success","Update Database successfully")
        
    def deselect(self):
        self.var.set(0)
        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        self.var7.set(0)
        self.var8.set(0)
        self.var9.set(0)
        self.var10.set(0)
        self.var11.set(0)
        self.var12.set(0)
        self.var13.set(0)
        self.var14.set(0)
          
    def delete(self):
        # retrieve data from entry widget
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e5.delete(0, END)
        self.e6.delete(0, END)
        self.e7.delete(0, END)
        self.e8.delete(0, END)
        self.e9.delete(0, END)
        self.e10.delete(0, END)
        self.e11.delete(0, END)
        self.e12.delete(0, END)
        self.e13.delete(0, END) 
        self.e14.delete(0, END) 
        self.e15.delete(0, END)
        self.e16.delete(0, END) 
        self.e17.delete(0, END)
        self.e18.delete(0, END)
        self.e19.delete(0, END)
        self.e20.delete(0, END)
        self.e21.delete(0, END) 
        self.e22.delete(0, END) 
        self.e23.delete(0, END) 
        self.e24.delete(0, END) 
        self.e25.delete(0, END)
        self.e26.delete(0, END) 
        self.e27.delete(0, END) 
        self.e28.delete(0, END)
        self.e29.delete(0, END)
        self.e30.delete(0, END)

    def delete_record(self):
        self.selected_item = self.tree.focus()
        self.tree.delete(self.selected_item)
        
    def print(self):
        self.tott = float(self.totText.get())
        self.top = Toplevel()
        self.top.geometry("300x300")
        self.top.config(bg="white")
        self.l = Label(self.top, text='---------RECIEPT----------')
        self.l.pack()
        self.l.config(bg="white")
        self.heading = Label(self.top, text='\tItem\tPRICE\tQTY\tTOTAL')
        self.heading.pack()
        self.heading.config(bg="white")

        for child in self.tree.get_children():
            self.item = (self.tree.item(child, 'values')[0])
            self.price = float(self.tree.item(child, 'values')[1])
            self.qty = float(self.tree.item(child, 'values')[2])
            self.tot = float(self.tree.item(child, 'values')[3])
            self.item1 = Label(self.top, text=f'{self.item}\t{self.price}\t{self.qty}\t{self.tot}')
            self.item1.config(bg="white")
            self.item1.pack()

        self.tot = Label(self.top, text=f'Total\t{self.tott}')
        self.tot.config(bg="white")
        self.tot.pack()

    def openNewWindow(self):
        # Toplevel object which will
        # # be treated as a new window
        self.newWindow = Toplevel()
        # sets the title of the
        # Toplevel widget
        self.newWindow.geometry("600x600")
        self.newWindow.title("Orders")
        self.newWindow.config(bg="#FCF9BE")
        self.name_l=Label(self.newWindow,text="Customer's Name", bg='#FCF9BE', font=('arial 10 bold'))
        self.name_l.place(x=0,y=70)

        self.stock_l=Label(self.newWindow,text="Phone number", bg='#FCF9BE', font=('arial 10 bold'))
        self.stock_l.place(x=0,y=120)

        self.cp_l = Label(self.newWindow, text="Picking Date ", bg='#FCF9BE', font=('arial 10 bold'))
        self.cp_l.place(x=0, y=170)

        self.name_2=Label(self.newWindow,text="Amount", bg='#FCF9BE', font=('arial 10 bold'))
        self.name_2.place(x=0,y=220)

        self.stock_2=Label(self.newWindow,text="Deposit", bg='#FCF9BE', font=('arial 10 bold'))
        self.stock_2.place(x=0,y=270)

        self.cp_2 = Label(self.newWindow, text="Balance", bg='#FCF9BE', font=('arial 10 bold'))
        self.cp_2.place(x=0, y=320)

        #enteries for window

        self.name_e=Entry(self.newWindow,width=25,font=('arial 10 bold'))
        self.name_e.place(x=380,y=70)

        self.stock_e = Entry(self.newWindow, width=25, font=('arial 10 bold'))
        self.stock_e.place(x=380, y=120)

        self.cp_e = Entry(self.newWindow, width=25, font=('arial 10 bold'))
        self.cp_e.place(x=380, y=170)
        
        self.name_e2=Entry(self.newWindow,width=25,font=('arial 10 bold'))
        self.name_e2.place(x=380,y=220)

        self.stock_e2 = Entry(self.newWindow, width=25, font=('arial 10 bold'))
        self.stock_e2.place(x=380, y=270)

        self.cp_e2 = Entry(self.newWindow, width=25, font=('arial 10 bold'))
        self.cp_e2.place(x=380, y=320)

        #button to add to the database
        self.btn_add=Button(self.newWindow,text='Add to Database',width=25,height=2,bg='steelblue',fg='white',command=self.retrieve_data)
        self.btn_add.place(x=380,y=370)  
        self.btn_clear=Button(self.newWindow,text="Clear All Fields",width=18,height=2,bg='red',fg='white',command=self.clear_all)
        self.btn_clear.place(x=3,y=370)
        
        
        # mainloop, runs infinitely
        mainloop()

    def clear_all(self):
        self.name = self.name_e.delete(0, END)
        self.stock = self.stock_e.delete(0, END)
        self.cp = self.cp_e.delete(0, END)
        self.name2 = self.name_e2.delete(0, END)
        self.stock2 = self.stock_e2.delete(0, END)
        self.cp2 = self.cp_e2.delete(0, END) 

    def retrieve_data(self):
        # get from entries
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.name2 = self.name_e2.get()
        self.stock2 = self.stock_e2.get()
        self.cp2 = self.cp_e2.get() 
        
        # dynamic entries
        if self.name == '' or self.stock == '' or self.cp == '' or self.name2 == '' or  self.stock2 == '' or self.cp2 =='':
                tkinter.messagebox.showinfo("Error", "Please Fill all the entries.")
        else:
                cursor.execute("INSERT INTO orders (Name, Phone, Picking_Date, Amount, Deposit, Balance) VALUES (%s,%s,%s,%s,%s,%s)", (self.name, self.stock, self.cp, self.name2 , self.stock2, self.cp2))
                 
                cnx.commit()
                tkinter.messagebox.showinfo("Success", "Successfully added to the database")
                self.newWindow.destroy()

    # Add a function to delete data from the orders table
    def delete_order(self):
        # Get the selected row
        selected_item = self.tree1.selection()[0]
        values = self.tree1.item(selected_item)['values']

        # Delete the selected row from the database
        query = "DELETE FROM orders WHERE Name=? AND Phone=? AND Picking_Date=? AND Amount=? AND Deposit=? AND Balance=?"
        self.cursor.execute(query, values)
        self.conn.commit()

        # Delete the selected row from the Treeview
        self.tree1.delete(selected_item)

    # Add a function to delete data from the inventory table
    def delete_inventory(self):
        # Get the selected row
        selected_item = self.tree2.selection()[0]
        values = self.tree2.item(selected_item)['values']

        # Delete the selected row from the database
        query = "DELETE FROM inventory WHERE Item=? AND Price=? AND Qty=?"
        self.cursor.execute(query, values)
        self.conn.commit()

        # Delete the selected row from the Treeview
        self.tree2.delete(selected_item)
    
    # Connect to the database
    def statement(self):
        self.window = tk.Tk()
        self.window.geometry("1000x1000")
        self.window.config(bg="#EB455F")
        self.window.title("Database Results")

        # Execute SQL query to select data
        query = ("SELECT orders.Name, orders.Phone, orders.Picking_Date, orders.Amount, orders.Deposit, orders.Balance FROM orders")

        cursor.execute(query)
        self.table1_data = cursor.fetchall()

        # Create a label for Orders Table
        self.table1 = tk.Label(self.window, text="Orders Table", bg="#EB455F", font=("TkDefaultFont", 16))
        self.table1.pack()

        # Create Tkinter window and Treeview widget
        self.tree1 = ttk.Treeview(self.window)
        
        # Insert columns into Treeview
        self.tree1["columns"] = ("Name", "Phone", "Picking_Date", "Amount", "Deposit", "Balance")
        self.tree1.column("Name", anchor=CENTER, stretch=NO, width=100)
        self.tree1.column("Phone", anchor=CENTER, stretch=NO, width=100)
        self.tree1.column("Picking_Date", anchor=CENTER, stretch=NO, width=100)
        self.tree1.column("Amount", anchor=CENTER, stretch=NO, width=100)
        self.tree1.column("Deposit", anchor=CENTER, stretch=NO, width=100)
        self.tree1.column("Balance", anchor=CENTER, stretch=NO, width=100)
        self.tree1.heading("Name", text="Name")
        self.tree1.heading("Phone", text="Number")
        self.tree1.heading("Picking_Date", text="Picking Date")
        self.tree1.heading("Amount", text="Amount")
        self.tree1.heading("Deposit", text="Deposit")
        self.tree1.heading("Balance", text="Balance")
        
        # Insert data into Treeview
        for i, row in enumerate(self.table1_data):
            self.tree1.insert("", i, text=i, values=row)
            self.tree1.pack()

        # Create a label for table1
        self.table1 = tk.Label(self.window, text="Inventory Table", bg="#EB455F", font=("TkDefaultFont", 16))
        self.table1.pack()

        # Execute SQL query to select data
        query = ("SELECT inventory.Item, inventory.Price, inventory.Qty FROM inventory")
        cursor.execute(query)
        self.table2_data = cursor.fetchall()

        # Create Tkinter window and Treeview widget
        self.tree2 = ttk.Treeview(self.window)
        self.tree2["columns"] = ("Item", "Price", "Qty")
        self.tree2.column("Item", anchor=CENTER, stretch=NO, width=100)
        self.tree2.column("Price", anchor=CENTER, stretch=NO, width=100)
        self.tree2.column("Qty", anchor=CENTER, stretch=NO, width=100)
        self.tree2.heading("Item", text="Item")
        self.tree2.heading("Price", text="Price")
        self.tree2.heading("Qty", text="Quantity")

        # Insert data into Treeview
        for i, row in enumerate(self.table2_data):
            self.tree2.insert("", i, text=i, values=row)
            self.tree2.pack()

        # Run the Tkinter event loop
        self.window.mainloop()


    def Show(self):
        self.tot = 0
        if (self.var.get()):
            self.price = int(self.e1.get())
            self.qty = int(self.e16.get())
            self.tot = int(self.price * self.qty)
            self.tempList = [['African Dresses', self.e1.get(), self.e16.get(), self.tot]]
            self.tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (self.item, self.price, self.qty, self.tot) in enumerate(self.tempList, start=1):
                self.tree.insert("", "end", values=(self.item, self.price, self.qty, self.tot))

        if (self.var1.get()):
             self.price = int(self.e2.get())
             self.qty = int(self.e17.get())
             self.tot = int(self.price * self.qty)
             self.tempList = [['African Hand Bags', self.e2.get(), self.e17.get(), self.tot]]
             self.tempList.sort(key=lambda e: e[1], reverse=True)
             for i, (self.item, self.price, self.qty, self.tot) in enumerate(self.tempList, start=1):
                self.tree.insert("", "end", values=(self.item, self.price, self.qty, self.tot))

        if (self.var2.get()):
             self.price = int(self.e3.get())
             self.qty = int(self.e18.get())
             self.tot = int(self.price * self.qty)
             self.tempList = [['African Shoes', self.e3.get(), self.e18.get(), self.tot]]
             self.tempList.sort(key=lambda e: e[1], reverse=True)
             for i, (self.item, self.price, self.qty, self.tot) in enumerate(self.tempList, start=1):
                self.tree.insert("", "end", values=(self.item, self.price, self.qty, self.tot))

        if (self.var3.get()):
             self.price = int(self.e4.get())
             self.qty = int(self.e19.get())
             self.tot = int(self.price * self.qty)
             self.tempList = [['African Shrit', self.e4.get(), self.e19.get(), self.tot]]
             self.tempList.sort(key=lambda e: e[1], reverse=True)
             for i, (self.item, self.price, self.qty, self.tot) in enumerate(self.tempList, start=1):
                self.tree.insert("", "end", values=(self.item, self.price, self.qty, self.tot))

        if (self.var4.get()):
             self.price = int(self.e5.get())
             self.qty = int(self.e20.get())
             self.tot = int(self.price * self.qty)
             self.tempList = [['African Material', self.e5.get(), self.e20.get(), self.tot]]
             self.tempList.sort(key=lambda e: e[1], reverse=True)
             for i, (self.item, self.price, self.qty, self.tot) in enumerate(self.tempList, start=1):
                self.tree.insert("", "end", values=(self.item, self.price, self.qty, self.tot))

        if (self.var5.get()):
             self.price = int(self.e6.get())
             self.qty = int(self.e21.get())
             self.tot = int(self.price * self.qty)
             self.tempList = [['Bras', self.e6.get(), self.e21.get(), self.tot]]
             self.tempList.sort(key=lambda e: e[1], reverse=True)
             for i, (self.item, self.price, self.qty, self.tot) in enumerate(self.tempList, start=1):
                self.tree.insert("", "end", values=(self.item, self.price, self.qty, self.tot))

        if (self.var6.get()):
             self.price = int(self.e7.get())
             self.qty = int(self.e22.get())
             self.tot = int(self.price * self.qty)
             self.tempList = [['Carftana', self.e7.get(), self.e22.get(), self.tot]]
             self.tempList.sort(key=lambda e: e[1], reverse=True)
             for i, (self.item, self.price, self.qty, self.tot) in enumerate(self.tempList, start=1):
                self.tree.insert("", "end", values=(self.item, self.price, self.qty, self.tot))

        if (self.var7.get()):
             self.price = int(self.e8.get())
             self.qty = int(self.e23.get())
             self.tot = int(self.price * self.qty)
             self.tempList = [['Dresses', self.e8.get(), self.e23.get(), self.tot]]
             self.tempList.sort(key=lambda e: e[1], reverse=True)
             for i, (self.item, self.price, self.qty, self.tot) in enumerate(self.tempList, start=1):
                self.tree.insert("", "end", values=(self.item, self.price, self.qty, self.tot))
        
        if (self.var8.get()):
             self.price = int(self.e9.get())
             self.qty = int(self.e24.get())
             self.tot = int(self.price * self.qty)
             self.tempList = [['Ear Rings', self.e9.get(), self.e24.get(), self.tot]]
             self.tempList.sort(key=lambda e: e[1], reverse=True)
             for i, (self.item, self.price, self.qty, self.tot) in enumerate(self.tempList, start=1):
                self.tree.insert("", "end", values=(self.item, self.price, self.qty, self.tot))

        if (self.var9.get()):
             self.price = int(self.e10.get())
             self.qty = int(self.e25.get())
             self.tot = int(self.price * self.qty)
             self.tempList = [['Jewelry', self.e10.get(), self.e25.get(), self.tot]]
             self.tempList.sort(key=lambda e: e[1], reverse=True)
             for i, (self.item, self.price, self.qty, self.tot) in enumerate(self.tempList, start=1):
                self.tree.insert("", "end", values=(self.item, self.price, self.qty, self.tot))

        if (self.var10.get()):
             self.price = int(self.e11.get())
             self.qty = int(self.e26.get())
             self.tot = int(self.price * self.qty)
             self.tempList = [['Lady Bags', self.e11.get(), self.e26.get(), self.tot]]
             self.tempList.sort(key=lambda e: e[1], reverse=True)
             for i, (self.item, self.price, self.qty, self.tot) in enumerate(self.tempList, start=1):
                self.tree.insert("", "end", values=(self.item, self.price, self.qty, self.tot))

        if (self.var11.get()):
             self.price = int(self.e12.get())
             self.qty = int(self.e27.get())
             self.tot = int(self.price * self.qty)
             self.tempList = [['Leggings', self.e12.get(), self.e27.get(), self.tot]]
             self.tempList.sort(key=lambda e: e[1], reverse=True)
             for i, (self.item, self.price, self.qty, self.tot) in enumerate(self.tempList, start=1):
                self.tree.insert("", "end", values=(self.item, self.price, self.qty, self.tot))

        if (self.var12.get()):
             self.price = int(self.e13.get())
             self.qty = int(self.e28.get())
             self.tot = int(self.price * self.qty)
             self.tempList = [['Skirts', self.e13.get(), self.e28.get(), self.tot]]
             self.tempList.sort(key=lambda e: e[1], reverse=True)
             for i, (self.item, self.price, self.qty, self.tot) in enumerate(self.tempList, start=1):
                self.tree.insert("", "end", values=(self.item, self.price, self.qty, self.tot))

        if (self.var13.get()):
             self.price = int(self.e14.get())
             self.qty = int(self.e29.get())
             self.tot = int(self.price * self.qty)
             self.tempList = [['Tops', self.e14.get(), self.e29.get(), self.tot]]
             self.tempList.sort(key=lambda e: e[1], reverse=True)
             for i, (self.item, self.price, self.qty, self.tot) in enumerate(self.tempList, start=1):
                self.tree.insert("", "end", values=(self.item, self.price, self.qty, self.tot))
        
        if (self.var14.get()):
             self.price = int(self.e15.get())
             self.qty = int(self.e30.get())
             self.tot = int(self.price * self.qty)
             self.tempList = [['Underwear', self.e15.get(), self.e30.get(), self.tot]]
             self.tempList.sort(key=lambda e: e[1], reverse=True)
             for i, (self.item, self.price, self.qty, self.tot) in enumerate(self.tempList, start=1):
                self.tree.insert("", "end", values=(self.item, self.price, self.qty, self.tot))

        
        self.name_e=Label(self.master, text="Total").place(x=750, y=70)
        self.tot =Label(self.master, text="", font="arial 22 bold", textvariable=self.totText)
        self.tot.place(x=850, y=70)

        
        self.sum1 = 0.0
        for child in self.tree.get_children():
            self.sum1 += float(self.tree.item(child, 'values')[3])
            self.totText.set(self.sum1)

root=Tk()
Application(root)
root.geometry("1366x768+0+0")
root.title("Rosem Designers")
root.mainloop()