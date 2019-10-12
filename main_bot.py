from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
import os

username = "" #Enter your SAP id
password = "" #Enter your password
score = -1 #Enter a score to give from 1 to 7

def start_browser():

	dir = os.path.dirname(__file__)
	chrome_driver_path = dir + "/chromedriver.exe"
	chrome_options = Options()

	return webdriver.Chrome(options=chrome_options)

def login():

	try:
		driver = start_browser()

		driver.get("http://portal.svkm.ac.in/usermgmt/login")

		driver.find_element_by_name('username').send_keys(username)
		driver.find_element_by_name('password').send_keys(password)

		driver.find_element_by_id('userLogin').click()

		sleep(5)
		driver.find_element_by_class_name('feed').click()
		sleep(5)
		driver.find_element_by_xpath("//a[contains(text(),' Faculty Feedback 2019-20 Term. I - B. Tech. Computer Sem. VII')]").click()
		sleep(1)
		driver.find_element_by_link_text('Provide Feedback').click()
		sleep(10)

		for i in range(15):

			for j in range(8):

				select = Select(driver.find_element_by_id('answer'+str(i)+str(j)))
				select.select_by_index(5)

			driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
			print('yes')
			if i==0:
				driver.find_element_by_id('btn'+str(i+1)).click()
			else:
				driver.find_elements_by_id('btn'+str(i+1))[1].click()
			print('doubleyes')
			# driver.execute_script("window.scrollTo(0, 0);")
			sleep(1)


		finish = driver.find_element_by_id('studentFeedbackCommentForm')

		finish.find_elements_by_tag_name('button')[1].click()
		sleep(2)
	except Exception as e:
		print(e)
	finally:
		driver.close()

if __name__ == '__main__':
	login()
