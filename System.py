#coding=utf-8
#This Script is Written by Arbab Ali
#Do not edit this code without permission
#If you edit this without permission then 
#You have to pay for this Code.
import os, sys, time
logo=""" \033[1;97m _    _                  _                  
 | |  | |                | |                 
 | |__| |   __ _    ___  | | __   ___   _ __ 
 |  __  |  / _` |  / __| | |/ /  / _ \ | '__|
 | |  | | | (_| | | (__  |   <  |  __/ | |   
 |_|  |_|  \__,_|  \___| |_|\_\  \___| |_|"""  
logo1=('══════════════════════════════════════════════════')     
def outing(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


def password():
	os.system('clear')
	print (logo)  
	print (logo1)       
	print('             Owner   :- Beta Nam To Suna Hi Hoga')
	print('             Author  :- Arbab Ali Memon')
	print('             Youtube :- Cyber Gange Hidden Tricker')
	print('             Whatsapp:- +923003023263')
	print(logo1)
	username= input(' Username:- ')
	if username =="":
		print('\033[1;91m[!] Invalid Username\033[1;97m')
		os.system('xdg-open https://m.youtube.com/channel/UC23obpgnG79fUSXS7QnEnTA')
		time.sleep(2)
		os.system('clear')
		password()
	elif username =="Admin" or username =="Im" or username =="Owner":
		outing(' Welcome back sir,')
		outing(' Hello sir, How are you Today..?')
		time.sleep(1)
		os.system('python2 System.py')
	elif username =="Million" or username =="2BU": #Defalut username
		pswd= input(' Password:- ')
		if pswd =="":
			print('\033[1;91m[!]  Invalid Password\033[1;97m')
			os.system('xdg-open https://m.youtube.com/channel/UC23obpgnG79fUSXS7QnEnTA')
			time.sleep(1)
			os.system('clear')
			password()
		elif pswd =="03003023263" or pswd =="Arbab": #Defalut pass
			outing(' Logged Successful as Anonymous')
			os.system('python2 System.py')
		else:
			print('\033[1;91m[!]  Invalid Password\033[1;97m')
			os.system('xdg-open https://m.youtube.com/channel/UC23obpgnG79fUSXS7QnEnTA')
			time.sleep(1)
			os.system('clear')
			password()
	else:
		print('\033[1;91m[!] Invalid Username\033[1;97m')
		time.sleep(1)
		os.system('xdg-open https://m.youtube.com/channel/UC23obpgnG79fUSXS7QnEnTA')
		os.system('clear')	
		password()	
password()				                                                                   
                                             
