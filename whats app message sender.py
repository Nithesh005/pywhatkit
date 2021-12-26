 # importing the pywhatkit module
import pywhatkit 
number=input("enter phone number :") # geting the phone number froum user with country code +91
msg=input("Enter your message :") # geting the input message
pywhatkit.sendwhatmsg(number,msg,7,8)
print("Successfully Sent!")
