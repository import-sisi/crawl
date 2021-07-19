from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
import time
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
'''https://divar.ir/qom/%D9%82%D9%85/browse/
ht-dfi
cap = DesiredCapabilities().FIREFOX
		cap["marionette"] = False
		binary = FirefoxBinary('/path/to/binary')tps://divar.ir/qom/%D9%82%D9%85/browse/%D8%A7%D9%85%D9%84%D8%A7%DA%A9-%D9%85%D8%B3%DA%A9%D9%86/
https://divar.ir/qom/%D9%82%D9%85/browse/%D8%A7%D8%AC%D8%A7%D8%B1%D9%87-%D9%85%D8%B3%DA%A9%D9%88%D9%86%DB%8C-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86-%D8%AE%D8%A7%D9%86%D9%87-%D8%B2%D9%85%DB%8C%D9%86/%D8%A7%D9%85%D9%84%D8%A7%DA%A9-%D9%85%D8%B3%DA%A9%D9%86/
https://divar.ir/qom/%D9%82%D9%85/browse/%D8%A7%D8%AC%D8%A7%D8%B1%D9%87-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A7%D8%AC%D8%A7%D8%B1%D9%87-%D9%85%D8%B3%DA%A9%D9%88%D9%86%DB%8C-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86-%D8%AE%D8%A7%D9%86%D9%87-%D8%B2%D9%85%DB%8C%D9%86/%D8%A7%D9%85%D9%84%D8%A7%DA%A9-%D9%85%D8%B3%DA%A9%D9%86/
https://divar.ir/v/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86-%D8%B4%D9%87%D8%B1%DA%A9-%D9%82%D8%AF%D8%B3_%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86_%D9%82%D9%85_%D8%B4%D9%87%D8%B1%DA%A9-%D9%82%D8%AF%D8%B3_%D8%AF%DB%8C%D9%88%D8%A7%D8%B1/QX0kAQr7
https://divar.ir/qom/%D9%82%D9%85/browse/%D8%A7%D8%AC%D8%A7%D8%B1%D9%87-%D8%A7%D8%AF%D8%A7%D8%B1%DB%8C-%D8%AA%D8%AC%D8%A7%D8%B1%DB%8C-%D9%85%D8%BA%D8%A7%D8%B2%D9%87-%D8%AF%D9%81%D8%AA%D8%B1-%DA%A9%D8%A7%D8%B1-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C/%D8%A7%D9%85%D9%84%D8%A7%DA%A9-%D9%85%D8%B3%DA%A9%D9%86/
https://divar.ir/tehran/%D8%AA%D9%87%D8%B1%D8%A7%D9%86/browse/%D8%A7%D8%AC%D8%A7%D8%B1%D9%87-%D9%85%D8%B3%DA%A9%D9%88%D9%86%DB%8C-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86-%D8%AE%D8%A7%D9%86%D9%87-%D8%B2%D9%85%DB%8C%D9%86/%D8%A7%D9%85%D9%84%D8%A7%DA%A9-%D9%85%D8%B3%DA%A9%D9%86/
https://divar.ir/tehran/%D8%AA%D9%87%D8%B1%D8%A7%D9%86/browse/%D8%A7%D8%AC%D8%A7%D8%B1%D9%87-%D8%AE%D8%A7%D9%86%D9%87-%D9%88%DB%8C%D9%84%D8%A7/%D8%A7%D8%AC%D8%A7%D8%B1%D9%87-%D9%85%D8%B3%DA%A9%D9%88%D9%86%DB%8C-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86-%D8%AE%D8%A7%D9%86%D9%87-%D8%B2%D9%85%DB%8C%D9%86/%D8%A7%D9%85%D9%84%D8%A7%DA%A9-%D9%85%D8%B3%DA%A9%D9%86/
https://divar.ir/tehran/%D8%AA%D9%87%D8%B1%D8%A7%D9%86/browse/%D8%A7%D8%AC%D8%A7%D8%B1%D9%87-%D8%A7%D8%AF%D8%A7%D8%B1%DB%8C-%D8%AA%D8%AC%D8%A7%D8%B1%DB%8C-%D9%85%D8%BA%D8%A7%D8%B2%D9%87-%D8%AF%D9%81%D8%AA%D8%B1-%DA%A9%D8%A7%D8%B1-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C/%D8%A7%D9%85%D9%84%D8%A7%DA%A9-%D9%85%D8%B3%DA%A9%D9%86/
https://divar.ir/qom/%D9%82%D9%85/browse/%D8%A7%D8%AC%D8%A7%D8%B1%D9%87-%D8%AE%D8%A7%D9%86%D9%87-%D9%88%DB%8C%D9%84%D8%A7/%D8%A7%D8%AC%D8%A7%D8%B1%D9%87-%D9%85%D8%B3%DA%A9%D9%88%D9%86%DB%8C-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86-%D8%AE%D8%A7%D9%86%D9%87-%D8%B2%D9%85%DB%8C%D9%86/%D8%A7%D9%85%D9%84%D8%A7%DA%A9-%D9%85%D8%B3%DA%A9%D9%86/from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
'''

class DivarlistScraper(object):
	
	def __init__(self, type) :
		self.type = type	
		self.url = f"https://divar.ir/tehran/%D8%AA%D9%87%D8%B1%D8%A7%D9%86/browse/%D8%A7%D8%AC%D8%A7%D8%B1%D9%87-%D8%A7%D8%AF%D8%A7%D8%B1%DB%8C-%D8%AA%D8%AC%D8%A7%D8%B1%DB%8C-%D9%85%D8%BA%D8%A7%D8%B2%D9%87-%D8%AF%D9%81%D8%AA%D8%B1-%DA%A9%D8%A7%D8%B1-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C/{type}/"		
		self.driver = webdriver.Chrome()		
		self.delay = 300
		
#		self.urll = urll
#		self.location = location
#		self.driver = webdriver.Firefox(firefox_binary=binary , capabilities=cap)

	def load_divarlist_url(self):
		self.driver.get(self.url)
		try:
			wait = WebDriverWait(self.driver, self.delay)
			wait.until(EC.presence_of_element_located((By.ID, 'app')))
			
			print("Page is ready")
		except TimeoutException:
		
			print("Loading took too much time")
			
			
	def extract_post_titles(self):
	
		all_title_list = []
		while True:
			all_posts = []
			all_posts = self.driver.find_elements_by_class_name('post-card-link')
			print(len(all_posts))
			print("bbbbbbbbbbbbbbbb")
			
			if all_posts[-1] != 0:
			#self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
				
					
				self.driver.execute_script("arguments[0].scrollIntoView();",all_posts[-1])
				#time.sleep(5)
			if(len(all_posts)==24):
				break
				print("wwwwwwww")
		for post in all_posts:
		
					#self.driver.execute_script("arguments[0].scrollIntoView();", post)
			
			#print(post.get_attribute('href'))
			#print(post.text)
			all_title_list.append(post.text)
			
			print("***********************************************************8")	
			
		return all_title_list
		
		
	def extract_post_url(self):
		parazit = []
		category = []
		place = []
		ad_type = []
		year_of_construction = []
		adver = []
		room_number = []
		area = []
		deposit = []
		lease = []
		#coment = []
		url_list = []
		
		while True:
			all_posts = []
			all_posts = self.driver.find_elements_by_class_name('post-card-link')
			print(len(all_posts))
			print("bbbbbbbbbbbbbbbb")
			
			if all_posts[-1] != 0:
			
				self.driver.execute_script("arguments[0].scrollIntoView();",all_posts[-1])
				#time.sleep(5)
			if (len(all_posts)>=8500):
				break
				
				
		for post in all_posts:
			#print(post.get_attribute('href'))
			url_list.append(post.get_attribute('href'))
				
		#url = pd.DataFrame({'url':	url_list})
		
		for i in url_list:
			
			self.driver.get(i)
			#come = self.driver.find_elements_by_class_name("content")[4]
			
			
			values = self.driver.find_elements_by_class_name("value")
			if(len(values)<10):
				continue
			job=0
			for jj in values:
				
				#if(job == 0):
#					parazit.append(jj.text)
				if(job == 1):
					category.append(jj.text)
				if(job == 2):
					place.append(jj.text)
				if(job == 3):
					ad_type.append(jj.text)
				if(job == 4):
					year_of_construction.append(jj.text)
				if(job == 5):
					adver.append(jj.text)
				if(job == 6):
					room_number.append(jj.text)
				if(job == 7):
					area.append(jj.text)
				if(job == 8):
					deposit.append(jj.text)
				if(job == 9):
					lease.append(jj.text)
				job +=1
			#coment.append(come.text)	
		print(year_of_construction)
		
		information = pd.DataFrame(
		{
		#'comment':	coment,
		'category':category ,
		'place':place ,
		'ad_type':ad_type,
		'year_of_construction': year_of_construction,'Advertiser': adver,
		'Room_number':room_number ,
		'Area': area ,
		'Deposit':deposit ,
		'Lease': lease
		})                    
		
		
		print(information)
		information.to_csv('daftar_tehran.csv')
		#url.to_csv('vila_qom_url.csv')
			
			
		
		
		
		
	def quit(self):
		self.driver.close()
	
		
		
#	def test(self):
#		print(self.driver)

		
		
type="%D8%A7%D9%85%D9%84%D8%A7%DA%A9-%D9%85%D8%B3%DA%A9%D9%86"


scraper = DivarlistScraper(type)
#scraper.test()	
scraper.load_divarlist_url()
#scraper.extract_post_titles()
scraper.extract_post_url()
#scraper.quit()	
		
		
		
		
		
		
		
		