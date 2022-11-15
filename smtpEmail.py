from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import random
# from tkinter.messagebox import showinfo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def check_otp():
    USER_INP = simpledialog.askstring(title="Test", prompt="Enter OTP recieved in gmail.")
    if USER_INP == "abc":

        server_email = "sender email"
        user_email = "receivr email"

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Link"
        msg['From'] = server_email
        msg['To'] = user_email

        otp = random.randint(1001, 5001)

        html = f"""
        <html>
        <head>
        </head>
        <body>
            <H1 style="color:#00c2ff;text-align:center;"> EXPENZO </H1><br><br>
            <img src="https://i.ibb.co/pLjs3b2/8432.jpg" alt="image" border="0"><br>
            <H2> OTP for registration is : {otp} </H2>
            <H4 style="text-align:left;"> Thanks for Registration,<br><span style="color:#00c2ff;">EXPENZO</span> Team </H4>
        </body>
        </html>
        """
    # moneybag image == <img src="https://i.ibb.co/wSkMR8W/et-img.png" alt="et-img" style="width:100px;height:100px;">


        part1 = MIMEText(html, 'html')

        msg.attach(part1)
        
        mail = smtplib.SMTP('smtp.gmail.com', 587)

        mail.ehlo()

        mail.starttls()

        mail.login('email', 'app password')
        mail.sendmail(server_email, user_email, msg.as_string())
        mail.quit()
        print("email sent")
    else:
        messagebox.showinfo('Error', 'Wrong OTP')
        check_otp()
        
check_otp()






















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
