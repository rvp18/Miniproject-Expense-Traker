import optparse
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import random
# from tkinter.messagebox import showinfo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def getmail():
    global rptopt
    rptotp = random.randint(100000,600001)
    if rptotp:
        
        server_email = "expenzoapsit@gmail.coml"
        user_email = "omchavan35@gmail.com"

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Report"
        msg['From'] = server_email
        msg['To'] = user_email

        html = f"""
        <html>
        <head>
        </head>
        <body>
            <H1 style="color:#00c2ff;text-align:center;"> EXPENZO-report </H1><br><br>
            <img src="https://i.ibb.co/pLjs3b2/8432.jpg" alt="image" border="0"><br>
            <H2 style="color:ff0000;"> Report : </H2>
            <H3> Total Income  : 50000 </H3>
            <H3> Total Expense : 30000 </H3>
            <H3> Total Balance : 20000 </H3><br>
            <h3> OTP : {rptotp} </H3>
            <H4 style="text-align:left;"> Thanks for being with us,<br><span style="color:#00c2ff;">EXPENZO</span> Team </H4>
        </body>
        </html>
        """
    # moneybag image == <img src="https://i.ibb.co/wSkMR8W/et-img.png" alt="et-img" style="width:100px;height:100px;">


        part1 = MIMEText(html, 'html')

        msg.attach(part1)
        
        mail = smtplib.SMTP('smtp.gmail.com', 587)

        mail.ehlo()

        mail.starttls()

        mail.login('expenzoapsit@gmail.com', 'qsqwnitnkpmdydtf')
        mail.sendmail(server_email, user_email, msg.as_string())
        mail.quit()
        print("email sent")
        def checkrptotp():
            global USER_INP
            USER_INP = simpledialog.askstring(title='get report', prompt="You want to get report mailed to you ?")
        checkrptotp()

        if USER_INP==str(rptotp):
            messagebox.showinfo(title="",message="Report Sent")

        else:
            messagebox.showinfo('Error', 'Wrong OTP')
        
getmail()






















# import smtplib
# import random
# otp = random.randint(1000,9999)
# var = 1
# if var==1:
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()

#     server.login('expenzoapsit@gmail.com', 'qsqwnitnkpmdydtf')

#     recievers = ['a.r.malegave@gmail.com','purvesh1543@gmail.com','rahulvpatil2003@gmail.com','omchavan35@gmail.com']

#     server.sendmail('expenzoapsit@gmail.com', recievers)
#     server.send_message('''
#     DOCTYPE html!
    
    
    
    
    
    
    
    
#     '''
#     )
#     print("Sent")
# else:
#     print("not sent")
