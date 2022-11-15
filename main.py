from cProfile import label
from getopt import getopt
from msilib.schema import ListBox
from random import randint
import tkinter
from turtle import bgcolor
import webbrowser
from tkinter import simpledialog
from tkinter import messagebox, ttk
from numpy import size
import psycopg2
from tkinter import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkcalendar import Calendar, DateEntry
import matplotlib.pyplot as plt0
from matplotlib import style
from datetime import date
import db


t =Tk()
t.geometry("1280x720")
t.configure(bg = "#ffffff")
today = date.today()


def Social_btn_clicked():
    print("Social media page")
    SocialMedia()

def Rate_btn_clicked():
    print("Rate us Button clicked")
    rating()

def AE_btn_clicked():
    print("Add Expense Button Clicked")
    AddExpense()

def Summary_btn_clicked():
    print("Summary Button clicked")
    Summary()

def AI_btn_clicked():
    print("Add Income Button Clicked")
    AddIncome()

def Search_btn_clicked():
    print("Search Button Clicked")
    Search()

def Dashboard_btn_clicked():
    print("Dashboard Button Clicked")
    dashboardF()

def register():

    print("register function")
    registerframe = Frame()
    registerframe.place(x=0, y=0, width=1280, height=720)
    global regglobalemail
    regglobalemail = ""

    def Rbtn_clicked():

        name = entry0.get()
        global user
        user = entry1.get()
        password = entry2.get()
        regglobalemail = entry1.get()

        print("Button Clicked")

        if regglobalemail.__contains__("@gmail.com") :

                global otp
                otp = randint(1000, 5001)
                def check_otp():
                
                    if otp:
                        server_email = "expenzoapsit@gmail.com"
                    user_email = regglobalemail

                    msg = MIMEMultipart('alternative')
                    msg['Subject'] = "OTP"
                    msg['From'] = server_email
                    msg['To'] = user_email

                    html = f"""
                            <html>
                            <head>
                            </head>
                            <body>
                                <H1 style="color:#00c2ff;text-align:center;"> EXPENZO </H1><br><br>
                                <img src="https://i.ibb.co/pLjs3b2/8432.jpg" alt="image" border="0"><br>
                                <H2> OTP for Registration is : {otp} </H2>
                                <H4 style="text-align:left;"> Thanks for Registration,<br><span style="color:#00c2ff;">EXPENZO</span> Team </H4>
                            </body>
                            </html>
                            """

                    part2 = MIMEText(html, 'html')

                    msg.attach(part2)
                    mail = smtplib.SMTP('smtp.gmail.com', 587)
                    mail.ehlo()
                    mail.starttls()
                    mail.login('expenzoapsit@gmail.com', 'qsqwnitnkpmdydtf')
                    mail.sendmail(server_email, user_email, msg.as_string())
                    mail.quit()
                    print("email sent")
                    def get_otp():
                        global USER_INP
                        USER_INP = simpledialog.askstring(title="Test", prompt="Enter OTP recieved in gmail.")
                    get_otp()
                    if USER_INP == str(otp):
                            reg_db()

                    else:
                        messagebox.showinfo('Error', 'Wrong OTP. Try again')
                        register()
                    
                def reg_db():
                    try:
                        db.connection.autocommit = True
                        cursor = db.connection.cursor()
                        cursor.execute('''INSERT INTO Public."User"("name","email","password") VALUES (%s,%s,%s)''',
                                (name, user, password))
                        db.connection.commit()

                        cursor.execute('''INSERT INTO Public."expenseaddtable"("email","amount","category","description","date") VALUES (%s,%s,%s,%s,%s)''',
                                (regglobalemail, 1, "Bonus","Bonus",today))
                        db.connection.commit()

                        db.connection.autocommit = True
                        cursor.execute('''INSERT INTO Public."incomeaddtable"("email","amount","category","description","date") VALUES (%s,%s,%s,%s,%s)''',
                                (regglobalemail, 100,"Bonus","Bonus",today))
                        db.connection.commit()
                    
                        print("Registered : ",name, user, password)

                        messagebox.showinfo("Registration", "Registered successfully")

                    except (Exception, psycopg2.DatabaseError) as error:
                        assert isinstance(error, object)
                        print(error)
                    
                    finally:
                        login()

                check_otp()
        else:
            messagebox.showerror("Registration", "Email should be @gmail.com")

    img0 = PhotoImage(file=f"Rimg0.png")
    b0 = Button(
        registerframe.master,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=Rbtn_clicked,
        relief="flat")

    b0.place(
        x=294, y=493,
        width=151,
        height=52)

    canvas = Canvas(
        registerframe,
        bg="#ffffff",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"Rbackground.png")
    background = canvas.create_image(
                                     640.0, 360.0,
                                     image=background_img)

    entry0_img = PhotoImage(file=f"Rimg_textBox0.png")
    entry0_bg = canvas.create_image(

        370.0, 254.5,
        image=entry0_img)

    entry0 = Entry(
        registerframe,
        bd=0,
        bg="#ffffff",
        highlightthickness=0)

    entry0.place(

        x=230.0, y=233,
        width=280.0,
        height=41)

    entry1_img = PhotoImage(file=f"Rimg_textBox1.png")
    entry1_bg = canvas.create_image(

        370.0, 343.5,
        image=entry1_img)

    entry1 = Entry(
        registerframe,
        bd=0,
        bg="#ffffff",
        highlightthickness=0)

    entry1.place(

        x=230.0, y=322,
        width=280.0,
        height=41)

    entry2_img = PhotoImage(file=f"Rimg_textBox2.png")
    entry2_bg = canvas.create_image(

        370.0, 434.5,
        image=entry2_img)

    entry2 = Entry(
        registerframe,
        bd=0,
        bg="#ffffff",
        highlightthickness=0)

    entry2.place(

        x=230.0, y=413,
        width=280.0,
        height=41)

    registerframe.attributes("-topmost", True)

def login():
    print("Login function")
    loginframe = Frame()
    loginframe.place(x=0, y=0, width=1280, height=720)

    def btn_clicked():
        user = entry1.get()
        password = entry0.get()

        global globaluseremail
        globaluseremail = entry1.get()

        print("Button Clicked")

        db.connection.autocommit = True
        # Creating a cursor object using the cursor() method
        cursor = db.connection.cursor()
        # inserting data data
        cursor.execute('''select email,password from public."User" where email=%s and password=%s''',(user, password))
        print(cursor.fetchall())
        results=cursor.fetchall()

        # db_cursor.execute(query)
        rowcount =cursor.rowcount
        print(rowcount)

        #try:
        if(cursor.rowcount == 1):
            print("Logged In")
            dashboardF()
        else:
            messagebox.showerror("Login", "Email or Password is Incorrect")
            login()

        db.connection.commit()
        
        print("Logged in by : ")
        print(user)
        print(password)


    img0 = PhotoImage(file=f"Limg0.png")
    b0 = Button(
        loginframe.master,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    b0.place(

        x=294, y=461,
        width=151,
        height=52
    )

    def Registerbtn_clicked():
        register()


    img1 = PhotoImage(file=f"Limg1.png")
    b1 = Button(
        loginframe.master,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=Registerbtn_clicked,
        relief="flat")

    b1.place(
        x=327, y=560,
        width=84,
        height=28)


    canvas = Canvas(
        loginframe,
        bg="#ffffff",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"Lbackground.png")
    background = canvas.create_image(
        640.0, 360.0,
        image=background_img)

    entry0_img = PhotoImage(file=f"Limg_textBox0.png")
    entry0_bg = canvas.create_image(

        370.0, 390.5,
        image=entry0_img)

    entry0 = Entry(
        loginframe,
        bd=0,
        bg="#ffffff",
        highlightthickness=0,
        show="*")

    entry0.place(
        x=230.0, y=369,
        width=280.0,
        height=41)



    entry1_img = PhotoImage(file=f"Limg_textBox1.png")
    entry1_bg = canvas.create_image(

        370.0, 283.5,
        image=entry1_img)

    entry1 = Entry(
        loginframe,
        bd=0,
        bg="#ffffff",
        highlightthickness=0,
        font=('Consolas',12)
        )

    entry1.place(

        x=230.0, y=262,
        width=280.0,
        height=41)


    loginframe.attributes("-topmost", True)

def dashboardF():
    print("Dashboard function")

    dashframe = Frame()
    dashframe.place(x=0, y=0, width=1280, height=720)

    canvas = Canvas(

        bg="#ffffff",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"Dbackground.png")
    background = canvas.create_image(
        640.0, 360.0,
        image=background_img)



    # Setting auto commit false
    db.connection.autocommit = True
    # Creating a cursor object using the cursor() method
    cursor = db.connection.cursor()
    # Retrieving data
    sql2="SELECT SUM(amount) from incomeaddtable WHERE email='" + globaluseremail + "'"
    cursor.execute(sql2)

    result = cursor.fetchall()
    for i in result:
            income = i[0]
            lable_income = Label(dashframe.master,
                         # text="1234567",
                        text=i[0],
                         bg="white",
                         fg='#444444',
                         justify="center",
                         font=("consolas", 14, 'bold'))

            lable_income.place(x=583, y=103)

    # Setting auto commit false
    db.connection.autocommit = True
    # Creating a cursor object using the cursor() method
    cursor = db.connection.cursor()
    # Retrieving data
    sql="SELECT SUM(amount) from expenseaddtable WHERE email='" + globaluseremail + "'"

    print(sql)
    cursor.execute(sql)

    result = cursor.fetchall()

    db.connection.commit()
    for i in result:
        expense = i[0]
        lable_expense = Label(dashframe.master,
                          text=i[0],
                          # text='hehehe',
                          bg="white",
                          fg='#444444',
                          justify="center",
                          font=("consolas", 14, 'bold'))

        lable_expense.place(
                               x=831, y=103)

    Balanceamount = income - expense

    lable_balance_amount = Label(dashframe.master,
                                 text=Balanceamount,
                                 bg="white",
                                 fg='#444444',
                                 justify="center",
                                 font=("consolas", 14, 'bold'))

    lable_balance_amount.place(x=345, y=103)

    summaryratio=getdouble((expense/income)*100)


    lable_summery = Label(dashframe.master,
                          text="%.2f"% round(summaryratio,2)+" %",
                          bg="white",
                          fg='#444444',
                          justify="center",
                          font=("consolas", 14, 'bold'))

    lable_summery.place(
                        x=1074, y=103)

    db.connection.autocommit = True
    # Creating a cursor object using the cursor() method
    cursor1 = db.connection.cursor()
    # inserting data data
    sql2="select date,amount FROM public.incomeaddtable WHERE email='" + globaluseremail + "' ORDER BY date DESC LIMIT 4"
    cursor1.execute(sql2)
    result1 = cursor1.fetchall()

    db.connection.autocommit = True
    # Creating a cursor object using the cursor() method
    cursor = db.connection.cursor()
    # inserting data data
    sql1="select date,amount,category FROM public.expenseaddtable WHERE email='" + globaluseremail + "' ORDER BY date DESC LIMIT 4"
    cursor.execute(sql1)
    result = cursor.fetchall()

    exp_amount = []
    exp_date = []
    in_date = []
    category = []
    in_amount = []

    frame1 = Frame(dashframe.master, width=400, height=400, background='white', highlightbackground='#00c2ff',
                   highlightthickness=3)
    frame1.grid(row=2, column=1, padx=290, pady=170)
    colors = ("#F39237", "#54DEFD", "#CC4BC2", "#53599A", "#FB9F89","#722B8E","#EF1C26","#0087CD","#FDB913","#03A54A","#5DDA00","#7D7F83")

    f = Figure(figsize=(9.6, 4.5))
    plt = f.add_subplot(121)

    c = ['#01295F', '#849324', '#FFB30F', '#FD151B', '#885A5A', '#9CFC97', '#EFD780', '#A379C9', '#A379C9',
         '#5AB1BB',
         '#FC60A8']
    for i in result:
        exp_date.append(i[0])
        exp_amount.append(i[1])
        category.append(i[2])
    for i2 in result1:
        in_date.append(i2[0])
        in_amount.append(i2[1])

    plt.plot(exp_date, exp_amount, label="Expense")
    plt.plot(in_date, in_amount, label="Income")
    plt.scatter(exp_date, exp_amount)
    plt.scatter(in_date, in_amount)


    plt.set_title("Date wise Expense")
    # plt.grid('on')

    plt.legend()
    canvas1 = FigureCanvasTkAgg(f, frame1)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=False)

    print("Expenses  = ", exp_amount)
    print("names = ", category)


    plt2 = f.add_subplot(122)
    y = exp_amount
    wedgeprops = {"linewidth":0.6, "edgecolor":"black"}
    plt2.pie(y, labels=category, colors=colors, autopct='%1.2f%%', startangle=90)


    img0 = PhotoImage(file=f"Dimg0.png")
    b0 = Button(
        # dashframe,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=Social_btn_clicked,
        relief="flat")

    b0.place(
        x=55, y=619,
        width=142,
        height=38)

    img1 = PhotoImage(file=f"Dimg1.png")
    b1 = Button(
        # dashframe,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=Dashboard_btn_clicked,
        relief="flat")

    b1.place(
        x=37, y=185,
        width=192,
        height=38)

    img2 = PhotoImage(file=f"Dimg2.png")
    b2 = Button(
        # dashframe,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=Dashboard_btn_clicked,
        relief="flat")

    b2.place(
        x=38, y=147,
        width=192,
        height=38)

    img3 = PhotoImage(file=f"Dimg3.png")
    b3 = Button(
        # dashframe,
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=Search_btn_clicked,
        relief="flat")

    b3.place(
        x=34, y=183,
        width=192,
        height=38)

    img4 = PhotoImage(file=f"Dimg4.png")
    b4 = Button(
        # dashframe,
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=AI_btn_clicked,
        relief="flat")

    b4.place(
        x=37, y=225,
        width=192,
        height=38)

    logout = PhotoImage(file=f"DLOButton.png")
    lo = Button(
        # dashframe,
        image=logout,
        borderwidth=0,
        highlightthickness=0,
        command=login,
        relief="flat")

    lo.place(
        x=37, y=349,
        width=192,
        height=38)

    img5 = PhotoImage(file=f"Dimg5.png")
    b5 = Button(
        # dashframe,
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=AE_btn_clicked,
        relief="flat")

    b5.place(
        x=37, y=269,
        width=192,
        height=38)

    img6 = PhotoImage(file=f"Dimg6.png")
    b6 = Button(
        # dashframe,
        image=img6,
        borderwidth=0,
        highlightthickness=0,
        command=Summary_btn_clicked,
        relief="flat")

    b6.place(
        x=38, y=306,
        width=192,
        height=38)

    img7 = PhotoImage(file=f"Dimg7.png")
    b7 = Button(
        # dashframe,
        image=img7,
        borderwidth=0,
        highlightthickness=0,
        command=Rate_btn_clicked,
        relief="flat")

    b7.place(
        x=55, y=581,
        width=192,
        height=38)

    def statusf():
        if (0.00 < summaryratio < 25.00):
            GB = Button(
                dashframe.master,
                text="Status - Green", bg='#1bd93a', fg='White', command=green, font=('maindragd', 12, 'bold'))

            GB.place(
                x=554, y=646,
                width=480,
                height=38)
        elif (25.01 < summaryratio < 75.00):
            YB = Button(
                dashframe.master,
                text="Status - Yellow", bg='#FFED65', fg='#465362', command=yellow, font=('maindragd', 12, 'bold'))

            YB.place(
                x=554, y=646,
                width=480,
                height=38)
        elif (75.01 < summaryratio < 100.00):
            RB = Button(
                dashframe.master,
                text="Status - Red", bg='#ED254E', fg='White', command=red, font=('maindragd', 12, 'bold'))

            RB.place(
                x=554, y=646,
                width=480,
                height=38)
    
    db.connection.commit()
    db.connection.commit()

    statusf()
    dashframe.attributes("-topmost", True)

def AddExpense():

    def Add_btn_clicked():
        print("Adding Expence to Data")
        print(globaluseremail)

        amount=entry3.get()
        category=mycomboC.get()
        description=entry1.get()
        date=entry0.get_date()

        try:
            # Setting auto commit false
            db.connection.autocommit = True
            # Creating a cursor object using the cursor() method
            cursor = db.connection.cursor()
            # inserting data data
            cursor.execute('''INSERT INTO Public."expenseaddtable"("email","amount","category","description","date") VALUES (%s,%s,%s,%s,%s)''',
                           (globaluseremail, amount, category,description,date))
            # Commit your changes in the database
            db.connection.commit()
            # Closing the connection
            # db.connection.close()

            print(globaluseremail,amount, category,description,date)

            print('data inserted to table')

            messagebox.showinfo("Data", "Data Added")


        except (Exception, psycopg2.DatabaseError) as error:
            assert isinstance(error, object)
            print(error)

    print("Add Expence function")
    AEframe = Frame()
    AEframe.place(x=0, y=0, width=1280, height=720)

    options1 = [
        "Necessary",
        "Grocery",
        "Bills",
        "Entertaintment",
        "Gadgets",
        "Others" ]

    mycomboC = ttk.Combobox(AEframe.master,
                            state='readonly',
                            value=options1,
                            width=28,
                            font=("maindra", 11, 'bold'),
                            justify="center")

    mycomboC.place(x=366, y=264)
    mycomboC.current(0)
    mycomboC.bind("<<ComboboxSelected>>")

    canvas = Canvas(
        AEframe,
        bg="#FFFFFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"AEbackground.png")
    background = canvas.create_image(
        640.5, 360.5,
        image=background_img)

    entry0_img = PhotoImage(file=f"AEimg_textBox0.png")
    entry0_bg = canvas.create_image(
        456.5, 513.5,
        image=entry0_img)

    entry0 = DateEntry(
        AEframe,
        selectmode='day',
        bd=0,
        bg="#fdf9f9",
        highlightthickness=0)

    entry0.place(
        x=377.0, y=490,
        width=159.0,
        height=45)

    entry1_img = PhotoImage(file=f"AEimg_textBox1.png")
    entry1_bg = canvas.create_image(
        677.0, 395.0,
        image=entry1_img)

    entry1 = Entry(
        AEframe,
        bd=0,
        bg="#fdf9f9",
        highlightthickness=0)

    entry1.place(
        x=377.0, y=355,
        width=600.0,
        height=78)

    entry3_img = PhotoImage(file=f"AEimg_textBox3.png")
    entry3_bg = canvas.create_image(
        454.0, 174.5,
        image=entry3_img)

    entry3 = Entry(
        AEframe,
        bd=0,
        bg="#fdf9f9",
        highlightthickness=0)

    entry3.place(
        x=375.0, y=151,
        width=158.0,
        height=45)

    img0 = PhotoImage(file=f"AEimg0.png")
    b0 = Button(
        AEframe.master,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=Social_btn_clicked,
        relief="flat")

    b0.place(
        x=55, y=619,
        width=142,
        height=38)

    img1 = PhotoImage(file=f"AEimg1.png")
    b1 = Button(
        AEframe.master,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=Search_btn_clicked,
        relief="flat")

    b1.place(
        x=38, y=183,
        width=192,
        height=38)

    img2 = PhotoImage(file=f"AEimg2.png")
    b2 = Button(
        AEframe.master,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=Dashboard_btn_clicked,
        relief="flat")

    b2.place(
        x=38, y=147,
        width=192,
        height=38)

    img3 = PhotoImage(file=f"AEimg3.png")
    b3 = Button(
        AEframe.master,
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=AI_btn_clicked,
        relief="flat")

    b3.place(
        x=38, y=222,
        width=192,
        height=38)

    img4 = PhotoImage(file=f"AEimg4.png")
    b4 = Button(
        AEframe.master,
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=AE_btn_clicked,
        relief="flat")

    b4.place(
        x=38, y=264,
        width=192,
        height=38)

    img5 = PhotoImage(file=f"AEimg5.png")
    b5 = Button(
        AEframe.master,
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=Add_btn_clicked,
        relief="flat")

    b5.place(
        x=610, y=565,
        width=99,
        height=41)

    img6 = PhotoImage(file=f"AEimg6.png")
    b6 = Button(
        AEframe.master,
        image=img6,
        borderwidth=0,
        highlightthickness=0,
        command=Summary_btn_clicked,
        relief="flat")

    b6.place(
        x=38, y=306,
        width=192,
        height=38)

    img7 = PhotoImage(file=f"AEimg7.png")
    b7 = Button(
        AEframe.master,
        image=img7,
        borderwidth=0,
        highlightthickness=0,
        command=Rate_btn_clicked,
        relief="flat")

    b7.place(
        x=55, y=581,
        width=192,
        height=38)

    AEframe.attributes("-topmost", True)

def AddIncome():

    def IncomeAdd_btn_clicked():
        print("Adding Income to Data")
        print(globaluseremail)

        amount=entry3.get()
        category=mycomboC.get()
        description=entry1.get()
        date=entry0.get_date()

        try:
            # Setting auto commit false
            db.connection.autocommit = True
            # Creating a cursor object using the cursor() method
            cursor = db.connection.cursor()
            # inserting data data
            cursor.execute('''INSERT INTO Public."incomeaddtable"("email","amount","category","description","date") VALUES (%s,%s,%s,%s,%s)''',
                           (globaluseremail, amount, category,description,date))
            # Commit your changes in the database
            db.connection.commit()
            # Closing the connection
            # db.connection.close()

            print(globaluseremail,amount, category,description,date)

            print('data inserted to table')

            messagebox.showinfo("Data", "Data Added")


        except (Exception, psycopg2.DatabaseError) as error:
            assert isinstance(error, object)
            print(error)

    def Add_btn_clicked():
        print("Adding income to Data")

    print("Add Income function")
    AIframe = Frame()
    AIframe.place(x=0, y=0, width=1280, height=720)


    mycomboC = ttk.Combobox(AIframe.master,
                            state='readonly',
                            value=['Work',
                                   'Business',
                                    'Others'],
                            width=28,
                            font=("maindra", 11, 'bold'),

                            justify="center")

    mycomboC.place(x=366, y=264)
    # mycomboC.current(0)
    mycomboC.bind("<<ComboboxSelected>>")

    mycomboC.place(x=366, y=264)
    mycomboC.current(0)
    mycomboC.bind("<<ComboboxSelected>>")

    canvas = Canvas(
        AIframe,
        bg="#ffffff",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"AIbackground.png")
    background = canvas.create_image(
        640.5, 360.5,
        image=background_img)

    entry0_img = PhotoImage(file=f"AIimg_textBox0.png")
    entry0_bg = canvas.create_image(
        456.5, 513.5,
        image=entry0_img)

    entry0 = DateEntry(
        selectmode='day',
        bd = 0,
        bg = "#fdf9f9",
        highlightthickness = 0
    )

    entry0.place(
        x=378.0, y=492,
        width=159.0,
        height=45)

    entry1_img = PhotoImage(file=f"AIimg_textBox1.png")
    entry1_bg = canvas.create_image(
        677.0, 395.0,
        image=entry1_img)

    entry1 = Entry(
        AIframe,
        bd=0,
        bg="#fdf9f9",
        highlightthickness=0)

    entry1.place(
        x=377.0, y=355,
        width=600.0,
        height=78)

    entry3_img = PhotoImage(file=f"AIimg_textBox3.png")
    entry3_bg = canvas.create_image(
        454.0, 174.5,
        image=entry3_img)

    entry3 = Entry(
        AIframe,
        bd = 0,
        bg = "#fdf9f9",
        highlightthickness = 0
        )

    entry3.place(
        x=375.0, y=151,
        width=158.0,
        height=45)

    img0 = PhotoImage(file=f"AIimg0.png")
    b0 = Button(
        AIframe.master,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=IncomeAdd_btn_clicked,
        relief="flat")

    b0.place(
        x=610, y=565,
        width=99,
        height=41)

    img1 = PhotoImage(file=f"AIimg1.png")
    b1 = Button(
        AIframe.master,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=Social_btn_clicked,
        relief="flat")

    b1.place(
        x=55, y=619,
        width=142,
        height=38)

    img2 = PhotoImage(file=f"AIimg2.png")
    b2 = Button(
        AIframe.master,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=Rate_btn_clicked,
        relief="flat")

    b2.place(
        x=55, y=581,
        width=192,
        height=38)

    img3 = PhotoImage(file=f"AIimg3.png")
    b3 = Button(
        AIframe.master,
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=Summary_btn_clicked,
        relief="flat")

    b3.place(
        x=38, y=310,
        width=192,
        height=38)

    img4 = PhotoImage(file=f"AIimg4.png")
    b4 = Button(
        AIframe.master,
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=AE_btn_clicked,
        relief="flat")

    b4.place(
        x=38, y=268,
        width=192,
        height=38)

    img5 = PhotoImage(file=f"AIimg5.png")
    b5 = Button(
        AIframe.master,
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=AI_btn_clicked,
        relief="flat")

    b5.place(
        x=38, y=226,
        width=192,
        height=38)

    img6 = PhotoImage(file=f"AIimg6.png")
    b6 = Button(
        AIframe.master,
        image=img6,
        borderwidth=0,
        highlightthickness=0,
        command=Search_btn_clicked,
        relief="flat")

    b6.place(
        x=38, y=185,
        width=192,
        height=38)

    img7 = PhotoImage(file=f"AIimg7.png")
    b7 = Button(
        AIframe.master,
        image=img7,
        borderwidth=0,
        highlightthickness=0,
        command=Dashboard_btn_clicked,
        relief="flat")

    b7.place(
        x=38, y=147,
        width=192,
        height=38)

    AIframe.attributes("-topmost", True)

def Search():
    print("Search Function ")
    Searchframe = Frame()
    Searchframe.place(x=0, y=0, width=1280, height=720)

    canvas = Canvas(
        Searchframe,
        bg="#ffffff",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"Sbackground.png")
    background = canvas.create_image(
        640.0, 360.0,
        image=background_img)


    img0 = PhotoImage(file=f"Simg0.png")
    b0 = Button(
        Searchframe.master,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=Social_btn_clicked,
        relief="flat")

    b0.place(
        x=55, y=619,
        width=142,
        height=38)

    img1 = PhotoImage(file=f"Simg1.png")
    b1 = Button(
        Searchframe.master,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=Rate_btn_clicked,
        relief="flat")

    b1.place(
        x=55, y=581,
        width=192,
        height=38)

    img2 = PhotoImage(file=f"Simg2.png")
    b2 = Button(
        Searchframe.master,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=Summary_btn_clicked,
        relief="flat")

    b2.place(
        x=38, y=307,
        width=192,
        height=38)

    img3 = PhotoImage(file=f"Simg3.png")
    b3 = Button(
        Searchframe.master,
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=AE_btn_clicked,
        relief="flat")

    b3.place(
        x=38, y=265,
        width=192,
        height=38)

    img4 = PhotoImage(file=f"Simg4.png")
    b4 = Button(
        Searchframe.master,
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=AI_btn_clicked,
        relief="flat")

    b4.place(
        x=38, y=223,
        width=192,
        height=38)

    img5 = PhotoImage(file=f"Simg5.png")
    b5 = Button(
        Searchframe.master,
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=Search_btn_clicked,
        relief="flat")

    b5.place(
        x=38, y=184,
        width=192,
        height=38)

    img6 = PhotoImage(file=f"Simg6.png")
    b6 = Button(
        Searchframe.master,
        image=img6,
        borderwidth=0,
        highlightthickness=0,
        command=Dashboard_btn_clicked,
        relief="flat")

    b6.place(
        x=38, y=146,
        width=192,
        height=38)


    options1 = [
        "Necessary",
        "Grocery",
        "Bills",
        "Entertaintment",
        "Gadgets",
        "Others",
        "Work",
        "Business",
        "Others"]

    mycomboC1 = ttk.Combobox(Searchframe.master,
                            state='readonly',
                            value=options1,
                            width=22,
                            font=("maindra", 11, 'bold'),
                            justify="center")

    mycomboC1.place(x=685, y=163)
    mycomboC1.current(0)
    mycomboC1.bind("<<ComboboxSelected>>")

    entry01 = DateEntry(
        Searchframe,
        selectmode='day',
        bd=0,
        bg="#fdf9f9",
        highlightthickness=0)

    entry01.place(
        x=460.0, y=154,
        width=159.0,
        height=43)


    def showexp():

        # listBox.delete("","end")


        category1 = mycomboC1.get()
        date1 = entry01.get_date()
        print (date1)
        
        db.connection.autocommit = True
        # Creating a cursor object using the cursor() method
        cursor = db.connection.cursor()
        cursor.execute("SELECT amount,description,date,category FROM public.expenseaddtable WHERE email ='" + globaluseremail + "'AND category='" + category1 + "' AND date='" + str(date1) + "' ")
        records = cursor.fetchall()
        print(records)

        for i, (amount, description, date ,category) in enumerate(records, start=1):
            listBox.insert("", "end", values=(amount, description ,date,category))


    cols = ('amount', 'description', 'date','category')
    global listBox
    listBox = ttk.Treeview(Searchframe, columns=cols, show='headings')

    for col in cols:
        listBox.heading(col, text=col)
        listBox.place(x=440, y=240,
                        width=680,
                        height=340)


    # showexp()

    img8 = PhotoImage(file=f"Simg7.png")
    b8 = Button(
        Searchframe.master,
        image=img8,
        borderwidth=0,
        highlightthickness=0,
        command=showexp,
        relief="flat")

    b8.place(
        x=924, y=151,
        width=187,
        height=49)
    ttk.Treeview.destroy



    # back = Button(Searchframe.master, text="Back", bg='#683ad0', fg='White', command=Home)
    # back.place(
    #     Searchframe,
    #     x=550, y=300,
    #     width=192,
    #     height=38)

    Searchframe.attributes("-topmost", True)

def Summary():
    print("Summary function")
    Summaryframe=Frame()
    Summaryframe.place(x=0, y=0, width=1280, height=720)

    canvas = Canvas(
        Summaryframe,
        bg="#ffffff",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)
    def showexp():
        db.connection.autocommit = True
            # Creating a cursor object using the cursor() method
        cursor = db.connection.cursor()
        cursor.execute("SELECT amount,date FROM public.expenseaddtable WHERE email = '" + globaluseremail + "' ")
        records = cursor.fetchall()
        print(records)

        for i, (amount,date) in enumerate(records, start=1):
             explistBox.insert("", "end", values=(amount,date))

    cols = ('amount','date')
    explistBox = ttk.Treeview(Summaryframe, columns=cols, show='headings')

    for col in cols:
        explistBox.heading(col, text=col)    
        explistBox.place(x=796, y=119, height=467, width=425)


    showexp()

    def showicm():
        db.connection.autocommit = True
            # Creating a cursor object using the cursor() method
        cursor = db.connection.cursor()
        cursor.execute("SELECT amount,date FROM public.incomeaddtable WHERE email = '" + globaluseremail + "' ")
        records = cursor.fetchall()
        print(records)

        for i, (amount,date) in enumerate(records, start=1):
             icmlistBox.insert("", "end", values=(amount, date))


    cols = ('amount','date')
    icmlistBox = ttk.Treeview(Summaryframe, columns=cols, show='headings')

    for col in cols:
        icmlistBox.heading(col, text=col)   
        icmlistBox.place(x=331, y=119, height=467, width=425)

    


    showicm()

    def getrptmail():
        server_email = "expenzoapsit@gmail.com"
        user_email = globaluseremail

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "REPORT"
        msg['From'] = server_email
        msg['To'] = user_email

        db.connection.autocommit = True
        # Creating a cursor object using the cursor() method
        cursor = db.connection.cursor()
        # Retrieving data
        incamount1="SELECT SUM(amount) from incomeaddtable WHERE email='" + globaluseremail + "'  "
        cursor.execute(incamount1)
        incresult = cursor.fetchall()
        db.connection.commit()
        for i in incresult:
            global tincome
            tincome = i[0]


        db.connection.autocommit = True
        # Creating a cursor object using the cursor() method
        cursor = db.connection.cursor()
        # Retrieving data
        expamount1="SELECT SUM(amount) from expenseaddtable WHERE email='" + globaluseremail + "'  "
        cursor.execute(expamount1)
        expresult = cursor.fetchall()
        db.connection.commit()
        for i in expresult:
            global texpense
            texpense = i[0]

        balanceavail = tincome - texpense

        html = f"""
        <html>
        <head>
        </head>
        <body>
            <H1 style="color:#00c2ff;text-align:center;"> EXPENZO </H1><br><br>
            <img src="https://i.ibb.co/pLjs3b2/8432.jpg" alt="image" border="0"><br>
            <H2> Total Balance : {balanceavail} </H2>
            <H2> Total Income : {tincome} </H2>
            <H2> Total Expense : {texpense} </H2>
            <H4 style="text-align:left;"> Thanks for being with us,<br><span style="color:#00c2ff;">EXPENZO</span> Team </H4>
        </body>
        </html>
        """

        part1 = MIMEText(html, 'html')

        msg.attach(part1)
        
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('expenzoapsit@gmail.com', 'qsqwnitnkpmdydtf')
        mail.sendmail(server_email, user_email, msg.as_string())
        mail.quit()
        print("email sent")
        messagebox.showinfo("","Report sent on your email")

    getmailimg = PhotoImage(file=f"Summaryimg7.png")
    getmailbtn = Button(
        Summaryframe.master,
        image=getmailimg,
        command=getrptmail,
        bg='white',
        relief="flat"
    )
    getmailbtn.place(
        x=714,
        y=615,
        height=42,
        width=137,
    )


    background_img = PhotoImage(file=f"Summarybackground1.png")
    background = canvas.create_image(
        640.0, 360.0,
        image=background_img)

    img0 = PhotoImage(file=f"Summaryimg0.png")
    b0 = Button(
        Summaryframe.master,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=Social_btn_clicked,
        relief="flat")

    b0.place(
        x=55, y=619,
        width=142,
        height=38)

    img1 = PhotoImage(file=f"Summaryimg1.png")
    b1 = Button(
        Summaryframe.master,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=Rate_btn_clicked,
        relief="flat")

    b1.place(
        x=55, y=581,
        width=192,
        height=38)

    img2 = PhotoImage(file=f"Summaryimg2.png")
    b2 = Button(
        Summaryframe.master,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=Summary_btn_clicked,
        relief="flat")

    b2.place(
        x=37, y=310,
        width=192,
        height=38)

    img3 = PhotoImage(file=f"Summaryimg3.png")
    b3 = Button(
        Summaryframe.master,
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=AE_btn_clicked,
        relief="flat")

    b3.place(
        x=37, y=268,
        width=192,
        height=38)

    img4 = PhotoImage(file=f"Summaryimg4.png")
    b4 = Button(
        Summaryframe.master,
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=AI_btn_clicked,
        relief="flat")

    b4.place(
        x=37, y=226,
        width=192,
        height=38)

    img5 = PhotoImage(file=f"Summaryimg5.png")
    b5 = Button(
        Summaryframe.master,
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=Search_btn_clicked,
        relief="flat")

    b5.place(
        x=38, y=186,
        width=192,
        height=38)

    img6 = PhotoImage(file=f"Summaryimg6.png")
    b6 = Button(
        Summaryframe.master,
        image=img6,
        borderwidth=0,
        highlightthickness=0,
        command=Dashboard_btn_clicked,
        relief="flat")

    b6.place(
        x=37, y=147,
        width=192,
        height=38)

    Summaryframe.attributes("-topmost", True)

def SocialMedia():
    print("Social Media function")

    SocialMediaWindow = Toplevel(t)
    SocialMediaWindow.geometry("574x328")
    SocialMediaWindow.configure(bg="#ffffff")

    SMframe = Frame(SocialMediaWindow)
    SMframe.place(x=4, y=4, width=574, height=328)


    def fb_btn_clicked():
        print("Facebook Link Copied")
        webbrowser.open("https://instagram.com/expenzoapsit?utm_medium=copy_link")

    def ig_btn_clicked():
        print("Instagram Link Copied")
        webbrowser.open("https://instagram.com/expenzoapsit?utm_medium=copy_link")

    def twit_btn_clicked():
        print("Twitter Link Copied")
        webbrowser.open("https://mobile.twitter.com/Expenzoapsit")

    def ty_btn_clicked():
        print("Thank You")
        dashboardF()
        SocialMediaWindow.destroy()


    canvas = Canvas(
        SMframe,
        # SocialMediaWindow,
        bg="#ffffff",
        height=328,
        width=574,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"SMbackground.png")
    background = canvas.create_image(
        287.0, 164.0,
        image=background_img)

    img0 = PhotoImage(file=f"SMimg0.png")
    b0 = Button(
        SMframe,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=fb_btn_clicked,
        relief="flat")

    b0.place(
        x=379, y=124,
        width=69,
        height=65)

    img1 = PhotoImage(file=f"SMimg1.png")
    b1 = Button(
        SMframe,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=ig_btn_clicked,
        relief="flat")

    b1.place(
        x=252, y=124,
        width=69,
        height=65)

    img2 = PhotoImage(file=f"SMimg2.png")
    b2 = Button(
        SMframe.master,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=twit_btn_clicked,
        relief="flat")

    b2.place(
        x=125, y=124,
        width=69,
        height=65)

    img3 = PhotoImage(file=f"SMimg3.png")
    b3 = Button(
        SMframe.master,
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=ty_btn_clicked,
        state=DISABLED,
        relief="flat")

    b3.place(
        x=236, y=239,
        width=101,
        height=36)

    SocialMediaWindow.resizable(False, False)
    SocialMediaWindow.mainloop()

    SMframe.attributes("-topmost", True)

def rating():

    RUWindow = Toplevel(t)
    RUWindow.geometry("730x400")
    RUWindow.configure(bg="#ffffff")

    RUframe = Frame(RUWindow)
    RUframe.place(x=4, y=4, width=574, height=328)

    def btn_clicked_b0():
        print("Button 0 Clicked")
        messagebox.showinfo("Rating", "\t1 Star \n Thanks For Rating Us!")
        RUWindow.destroy()

    def btn_clicked_b1():
        print("Button 1 Clicked")
        messagebox.showinfo("Rating", "\t5 Star \n Thanks For Rating Us!")
        RUWindow.destroy()

    def btn_clicked_b2():
        print("Button 2 Clicked")
        messagebox.showinfo("Rating", "\t3 Star \n Thanks For Rating Us!")
        RUWindow.destroy()

    def btn_clicked_b3():
        print("Button 3 Clicked")
        messagebox.showinfo("Rating", "\t4 Star \n Thanks For Rating Us!")
        RUWindow.destroy()

    def btn_clicked_b4():
        print("Button 4 Clicked")
        messagebox.showinfo("Rating", "\t2 Star \n Thanks For Rating Us!")
        RUWindow.destroy()

    canvas = Canvas(
        RUWindow,
        bg="#ffffff",
        height=400,
        width=730,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"RAbackground.png")
    background = canvas.create_image(
        365.0, 200.0,
        image=background_img)

    img0 = PhotoImage(file=f"RAimg0.png")
    imgC0 = PhotoImage(file=f"RACimg0.png")
    b0 = Button(
        RUframe.master,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked_b0,
        relief="flat")

    b0.place(
        x=160, y=151,
        width=65,
        height=65)

    img1 = PhotoImage(file=f"RAimg1.png")
    imgC1 = PhotoImage(file=f"RACimg1.png")
    b1 = Button(
        RUframe.master,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked_b1,
        relief="flat")

    b1.place(
        x=499, y=151,
        width=65,
        height=65)

    img2 = PhotoImage(file=f"RAimg2.png")
    imgC2 = PhotoImage(file=f"RACimg2.png")
    b2 = Button(
        RUframe.master,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked_b2,
        relief="flat")

    b2.place(
        x=329, y=151,
        width=65,
        height=65)

    img3 = PhotoImage(file=f"RAimg3.png")
    imgC3 = PhotoImage(file=f"RACimg3.png")
    b3 = Button(
        RUframe.master,
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked_b3,
        relief="flat")

    b3.place(
        x=414, y=151,
        width=65,
        height=65)

    img4 = PhotoImage(file=f"RAimg4.png")
    imgC4 = PhotoImage(file=f"RACimg4.png")
    b4 = Button(
        RUframe.master,
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked_b4,
        relief="flat")

    b4.place(
        x=244, y=151,
        width=65,
        height=65)

    RUWindow.resizable(False, False)
    RUWindow.mainloop()

    RUframe.attributes("-topmost", True)

def green():
    greenframe = Frame()
    greenframe.place(x=0, y=0, width=1280, height=720)

    def Vdo1_btn_clicked():
        webbrowser.open("https://youtu.be/icyXl7B-s-4")

    def Vdo2_btn_clicked():
        webbrowser.open("https://youtu.be/z83Rd160YGs")

    def Vdo3_btn_clicked():
        webbrowser.open("https://youtu.be/w8A4mDbdGp0")

    canvas = Canvas(

        bg="#ffffff",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"Greenbackground.png")
    background = canvas.create_image(
        640.0, 354.5,
        image=background_img)

    img0 = PhotoImage(file=f"Greenimg0.png")
    b0 = Button(
        greenframe.master,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=Vdo1_btn_clicked,
        relief="flat")

    b0.place(
        x=212, y=576,
        width=158,
        height=59)

    img1 = PhotoImage(file=f"Greenimg1.png")
    b1 = Button(
        greenframe.master,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=Vdo2_btn_clicked,
        relief="flat")

    b1.place(
        x=212, y=462,
        width=266,
        height=59)

    img2 = PhotoImage(file=f"Greenimg2.png")
    b2 = Button(
        greenframe.master,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=Vdo3_btn_clicked,
        relief="flat")

    b2.place(
        x=212, y=354,
        width=162,
        height=62)

    img3 = PhotoImage(file=f"Greenimg3.png")
    b3 = Button(
        greenframe.master,
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=Dashboard_btn_clicked,
        relief="flat")

    b3.place(
        x=20, y=6,
        width=158,
        height=38)

    greenframe.attributes("-topmost", True)

def red():
    redframe = Frame()
    redframe.place(x=0, y=0, width=1280, height=720)

    def Vdo1_btn_clicked():
        webbrowser.open("https://youtu.be/20IjthX-XcU")

    def Vdo2_btn_clicked():
        webbrowser.open("https://youtu.be/HQzoZfc3GwQ")

    def Vdo3_btn_clicked():
        webbrowser.open("https://youtu.be/DfveM69yimo")


    canvas = Canvas(
        bg="#ffffff",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"Redbackground.png")
    background = canvas.create_image(
        599.5, 343.5,
        image=background_img)

    img0 = PhotoImage(file=f"Redimg0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=Vdo1_btn_clicked,
        relief="flat")

    b0.place(
        x=212, y=579,
        width=225,
        height=54)

    img1 = PhotoImage(file=f"Redimg1.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=Vdo2_btn_clicked,
        relief="flat")

    b1.place(
        x=212, y=465,
        width=270,
        height=59)

    img2 = PhotoImage(file=f"Redimg2.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=Vdo3_btn_clicked,
        relief="flat")

    b2.place(
        x=212, y=354,
        width=162,
        height=59)

    img3 = PhotoImage(file=f"Redimg3.png")
    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=Dashboard_btn_clicked,
        relief="flat")

    b3.place(
        x=20, y=6,
        width=158,
        height=38)

    redframe.attributes("-topmost", True)

def yellow():
    yellowframe = Frame()
    yellowframe.place(x=0, y=0, width=1280, height=720)

    def Vdo1_btn_clicked():
        webbrowser.open("https://youtu.be/zYGzemJSP8U")

    def Vdo2_btn_clicked():
        webbrowser.open("https://youtu.be/luVdqOQRCfU")

    def Vdo3_btn_clicked():
        webbrowser.open("https://youtu.be/yNaN5kYTNLY")


    canvas = Canvas(
        bg="#ffffff",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"Yellowbackground.png")
    background = canvas.create_image(
        640.0, 351.5,
        image=background_img)

    img0 = PhotoImage(file=f"Yellowimg0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=Vdo1_btn_clicked,
        relief="flat")

    b0.place(
        x=212, y=579,
        width=198,
        height=54)

    img1 = PhotoImage(file=f"Yellowimg1.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=Vdo2_btn_clicked,
        relief="flat")

    b1.place(
        x=212, y=354,
        width=261,
        height=54)

    img2 = PhotoImage(file=f"Yellowimg2.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=Vdo3_btn_clicked,
        relief="flat")

    b2.place(
        x=212, y=466,
        width=255,
        height=52)

    img3 = PhotoImage(file=f"Yellowimg3.png")
    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=Dashboard_btn_clicked,
        relief="flat")

    b3.place(
        x=20, y=6,
        width=158,
        height=38)

    yellowframe.attributes("-topmost", True)

def Home():
    f1 = Frame()
    f1.place(x=0, y=0, width=1280, height=720)

    b1 = Button(f1, text="Expenzo", bg='#05752a', fg='White', command=login)
    b1.place(
        x=550, y=200,

        width=192,
        height=38)

Home()


t.resizable(False, False)
t.mainloop()