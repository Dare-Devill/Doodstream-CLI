#MIT License

#Copyright (c) 2022 PRATHXM

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.






from doodstream import DoodStream
from doodstream_api import doodstream_conf
import os
import time
import asyncio
from colorama import Fore, Back, Style
#API_KEY


def api_key():
	k = int()
	if (k==0):
		k = k + 1
		global d,ds
	
		apikey = input("Enter Your Api Key: ")
		d = DoodStream(f"{apikey}")
		ds = doodstream_conf(f"{apikey}")
		print("checking Key.....")
		res = d.account_info()
		#print(res['msg'])
		if(res['msg']=='OK'):
			print("Connection Established Successfully to DoodStream..")
			time.sleep(2)
			os.system('cls' if os.name == 'nt' else 'clear')
		elif(res['status']==403):
			print("WRONG KEY...!!")
			print("Try Again...!!")
			time.sleep(2)
			os.system('cls' if os.name == 'nt' else 'clear')
			api_key()
		elif(res['status']==400):
				print("INVALID KEY...!!")
				print("Try Again...!!")
				time.sleep(2)
				os.system('cls' if os.name == 'nt' else 'clear')
				api_key()
		else:
				exit()
		




api_key()	
def graphic():
	
	print(Fore.RED + '''
=======================================
|                                     |
|                                     |
|PRATHAM'S DOODSTREAM SCRIPT          |
|                                     |
|       version 0.1                   |
=======================================''')

def options():
	print(Fore.YELLOW + '''
######################################
Select an option from given below...
1. Account Info
2. Account Reports
3. Remote Upload
4. File Info
5. Rename File
6. Copy Videos
7. Remote Upload List
8. File List
######################################
''')
	resp = int(input())
	if(resp == 1):
		#ACCOUNT INFO
		e = d.account_info()
		print(e)
		back = int(input(Fore.GREEN + "Type 0 to go back: "))
		if(back == 0):
			os.system('cls' if os.name == 'nt' else 'clear')
			graphic()
			options()
	elif(resp == 2):
		#DMCA REPORTS
		e2 = d.account_reports()
		print(e2)
		back = int(input(Fore.GREEN +"Type 0 to go back: "))
		if(back == 0):
			os.system('cls' if os.name == 'nt' else 'clear')
			graphic()
			options()
	elif(resp == 3):
		remote_link = input("Enter a Direct Link: ")
		#REMOTE UPLOAD
		e3 = d.remote_upload(f"{remote_link}")
		print(e3)
		back = int(input(Fore.GREEN +"Type 0 to go back: "))
		if(back == 0):
			os.system('cls' if os.name == 'nt' else 'clear')
			graphic()
			options()
	elif(resp == 4):
		#FILE_INFO
		file_id = input("Enter the file id: ")
		e4 = d.file_info(f"{file_id}")
		print(e4)
		back = int(input(Fore.GREEN + "Type 0 to go back: "))
		if(back == 0):
			os.system('cls' if os.name == 'nt' else 'clear')
			graphic()
			options()
	elif(resp == 5):
		#RENAME_FILE
		file_id = input("Enter The File Id: ")
		new_name = input("Enter New Name: ")
		e5  = d.rename_file(f"{file_id}", f"{new_name}")
		print(e5)
		back = int(input(Fore.GREEN +"Type 0 to go back: "))
		if(back == 0):
			os.system('cls' if os.name == 'nt' else 'clear')
			graphic()
			options()
	elif(resp == 6):
		#COPY_VIDEOS
		dlink = input("Enter A Doodstream File Id to copy in your account: ")
		e6 = d.copy_video(f"{dlink}")
		print(e6)
		back = int(input(Fore.GREEN +"Type 0 to go back: "))
		if(back == 0):
			os.system('cls' if os.name == 'nt' else 'clear')
			graphic()
			options()
	elif(resp == 7):
			e7 = ds.remote_upload_list()
			print(e7)
			back = int(input(Fore.GREEN +"Type 0 to go back: "))
			if(back == 0):
				os.system('cls' if os.name == 'nt' else 'clear')
				graphic()
				options()
	elif(resp == 8):
			page_number= int(input("Enter Page Number: "))
			per_page = int(input("Enter Per Page Limit: "))
			e8 = ds.file_list(f"{page_number}",f"{per_page}",'/')
			print(e8)
			back = int(input(Fore.GREEN +"Type 0 to go back: "))
			if(back == 0):
				
				os.system('cls' if os.name == 'nt' else 'clear')
				graphic()
				options()
			
			
	else:
		print(Fore.RED +"∆∆∆ YOU'VE CHOSEN INVALID OPTION ∆∆∆")
		time.sleep(2.5)
		os.system('cls' if os.name == 'nt' else 'clear')
		graphic()
		options()
graphic()
options()
