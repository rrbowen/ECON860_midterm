from bs4 import BeautifulSoup
import pandas
import os
import glob
import json

file_name = "html_file/userid_file"

#print(file_name)	
	
f = open(file_name, "r")
soup = BeautifulSoup(f.read(), "html.parser")
f.close()