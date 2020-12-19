#!/usr/bin/python3.8
# pyTemplateGen.py
# Author: Saxon Neustaeter
# Date: 12/18/2020
# Description: Simple script to produce a template file for a new python project
import os
import datetime
os.system("clear")

# Path to Executable
shebang = "#!/usr/bin/python3.8"

# Collect Information about File, etc.
filename = input("What is the filename without extension: ")
filename += ".py"
author = input("What is the authors name: ")
desc = input("Enter a breif description of the project: ")

# Get and format date
today = datetime.datetime.now()
today = (today.strftime("%m/%d/%Y"))

with open(filename, 'w') as outfile:
	outfile.write(shebang + "\n# " + filename + "\n# Author: " + author + "\n# Date: " + today + "\n# Description: " + desc + "\nimport os\nos.system(\"clear\")\n")
