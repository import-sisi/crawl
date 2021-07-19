'''from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://divar.ir/qom/%D9%82%D9%85/browse/%D8%A7%D8%AC%D8%A7%D8%B1%D9%87-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A7%D8%AC%D8%A7%D8%B1%D9%87-%D9%85%D8%B3%DA%A9%D9%88%D9%86%DB%8C-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86-%D8%AE%D8%A7%D9%86%D9%87-%D8%B2%D9%85%DB%8C%D9%86/%D8%A7%D9%85%D9%84%D8%A7%DA%A9-%D9%85%D8%B3%DA%A9%D9%86/")
driver.implicitly_wait(1)
print(driver.get_cookies())'''

import requests

baz_kardan = requests.get('https://divar.ir/qom/%D9%82%D9%85/browse/%D8%A7%D8%AC%D8%A7%D8%B1%D9%87-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A7%D8%AC%D8%A7%D8%B1%D9%87-%D9%85%D8%B3%DA%A9%D9%88%D9%86%DB%8C-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86-%D8%AE%D8%A7%D9%86%D9%87-%D8%B2%D9%85%DB%8C%D9%86/%D8%A7%D9%85%D9%84%D8%A7%DA%A9-%D9%85%D8%B3%DA%A9%D9%86/', timeout=5).encoding

#print(baz_kardan.cookies)
#print(baz_kardan.status_code)
#print(baz_kardan.headers)
print( baz_kardan.url)
#print(baz_kardan.text)
#rint( baz_kardan.conte)
#print(baz_kardan)
