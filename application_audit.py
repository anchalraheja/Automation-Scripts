import win32api
import win32net
from socket import *
import wmi
import os
import wmi, time
from shutil import copyfile
import getpass


username = ("")
password = ("")

def check_ps(ip):

	try:
		connection = wmi.WMI(ip, user=username, password=password)
		print "Connection established"
		process_id, return_value = connection.Win32_Process.Create(CommandLine="notepad.exe")
		if ( process_id > 0):
			print str(ip) + " " +"Working"
			update_sheet(ip,"enabled")
		else:
			print str(ip) +" " +"Disabled"
			update_sheet(ip,"disabled")
			
			if (return_value == 0 ):
				print str(ip) +" " +"Working"
				update_sheet(ip,"enabled")
			else:
				print str(ip) +" " +"Disabled"
				# update_sheet(ip,"disabled")
			
	except wmi.x_wmi:
		print "Your Username and Password of "+getfqdn(ip)+" are wrong."
		update_sheet(ip,"failed")



def update_sheet(ip,result):
	f = open("result.csv","ab")
	line = str(ip) + "," + str(result)
	f.write(line)
	f.write("\n")
	f.close()


server_list = open("ip_list.txt")
for x in server_list.readlines():
	ip = x.rstrip()
	print ip
	check_ps(ip)
