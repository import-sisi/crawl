import requests
from bs4 import BeautifulSoup

page=requests.get('https://divar.ir/v/آپارتمان-۸۵-متری-پردیسان_آپارتمان_قم_پردیسان_دیوار/QXwUAktQ')
soup=BeautifulSoup(page.content,'html.parser')
count=soup.find(id="app")
#print(count)
#ui fluid card post-card-detailed
count1=count.find_all(class_="ui fluid card post-fields")
#items=count.find_all(class_="item")
#print(count1.div)
#print(count1.find(class_="value"))
#print(count1.find(calss_="item__titel").get_text())
count2=soup.find(class_="ui fluid card post-fields")
for item in count2.select('.value'):
 print(item.get_text())