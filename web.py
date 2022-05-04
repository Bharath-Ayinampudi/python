from bs4 import BeautifulSoup
import requests
import connect

web_url="web.html"
req=requests.get(web_url)

content=req.content

soup=BeautifulSoup(content,"html.parser")

Login=soup.find("div",{"class:Login"})

if Login=="Admin":
    if Password="1234":
        print("Loged in sucessfully")
    else:
        print("Emtered password is wrong")
else:
    print("Entered username is wrong")
    
