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

df = pandas.DataFrame()

body = soup.find("body")
userid_rows = body.find_all("div")



for i in range(4,734):
	string_test = str(userid_rows[i])
	hold_a = (string_test[26:])
	scalar_hardway = int(len(string_test)/2-17)
	hold_b = hold_a[:scalar_hardway]
	print(hold_b)
	df = df.append({
		"userid_test": hold_b
		}, ignore_index=True)




df.to_csv("userid_list_simple.csv")
