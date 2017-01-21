import datetime
from functions import *
import blagconfig
title = blagconfig.title
name = blagconfig.name
fdir = blagconfig.fdir
from sys import argv

if argv[1] == "-build":
	stuff = updateMainPage(title, name)
	f = open(fdir+"/index.html", "w")
	f.write(stuff)
	f.close()
	print "success"
elif argv[1] == "-publish":
	if argv[2].split(".")[1] == "txt":
		gtitle = raw_input("Title of this post?: ")
		gdesc = raw_input("Description?: ")
		now = datetime.datetime.now()
		year = now.year
		month = now.month
		day = now.day
		#put it in the thing file
		f = open(fdir+"/fname2title.txt", "a")
		entry_string = argv[2].split(".")[0]+".html|"+str(month)+" "+str(day)+" "+str(year)+"|"+gtitle+"|"+gdesc+"\n" #dyingorangutan.jpg
		f.write(entry_string)
		f.close()
		#now make the html page
		content = open(argv[2]).read()
		date=str(month)+" "+str(day)+" "+str(year)
		post = buildPost(content, title, name, date, gtitle)
		f = open(fdir+"/"+argv[2].split(".")[0]+".html", "w")
		f.write(post)
		f.close()
		print "Published"
		
		