print("hello new puppy")
import urllib.request
import os 

if not os.path.exists("html_file"):
	os.mkdir("html_file")

f = open("html_file/userid_file", "wb" )
response = urllib.request.urlopen("http://45.79.253.243/index.html/")  #request a webpage
html = response.read()
f.write(html)
f.close()
	

print("hello little buddy")
