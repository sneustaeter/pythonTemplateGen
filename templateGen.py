#!/usr/bin/python3
#Date: April 12, 2020
#File: templateGen.py
#Author: Saxon Neustaeter
import os
from datetime import date

today = date.today()
createDate = today.strftime("%B %d, %Y")

os.system("clear")

print("Welcome to the Python template generator!\n")
fileName = input("Enter the name of the file to be generated WITHOUT an extention: ")
fileName += ".py"

author = input("Enter the authors name: ")

fileContents = ('#!/usr/bin/python3', '#Date: ' + createDate ,'#File: ' + fileName, '#Author: ' + author , 'import os')

with open(fileName, 'w') as outfile:
	index = 0
	for index in range(0,len(fileContents),1):
		outfile.write(fileContents[index])
		outfile.write("\n")
