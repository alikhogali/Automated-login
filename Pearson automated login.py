from selenium import webdriver

username = ("exampleusername")
password = ("examplepassword")

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
driver.get("https://login.pearson.com/v1/piapi/piui/signin?client_id=dN4bOBG0sGO9c9HADrifwQeqma5vjREy&okurl=https:%2F%2Fportal.mypearson.com%2Fcourse-home&siteid=8313")

username_textbox = driver.find_element_by_name("username")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_name("password")
password_textbox.send_keys(password)

login_button = driver.find_element_by_id('mainButton')

login_button.submit()
