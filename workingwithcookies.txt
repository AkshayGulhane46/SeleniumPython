from selenium import webdriver
driver=webdriver.Chrome(executable_path="D:/appium\chromedriver.exe")

driver.get("https://www.amazon.in/")

#capture all the cookies created by browser

cookies = driver.get_cookies()
print(len(cookies))   #print number of cookies created
print(cookies)  #here all the cookies are saved in dictionary format
                #all cookies will be printed
#[{'domain': '.amazon.in', 'expiry': 2192684444.14099,
# 'httpOnly': False, 'name': 'session-token',
# 'path': '/', 'secure': False, 'value':
# '/up+T44pBl8zsxUILKP3o7d3xASQTdkQciTPihyMwj/
# AWJ0FZaSJdUwUsmkRGPZOPcpIcZOr7xqzbxILuXiHmh7HSXVANFe
# /4vKh2K0G0d1E83T8aEwfJavCHTEeFl74+8/pw0/i/p+rgtbK8U5
# dkWPHugm45+V//OFrMNOgjYB9y3OApDgUHPhdGo2cLYSTGCEOYS
# EiiHhI4TLVs2A1RSHqYJmWSCbxb+8gnZEGEOJOgpBCDXo+aw=='},
# {'domain': '.amazon.in', 'expiry': 2082758396.141025, '
# httpOnly': False, 'name': 'session-id-time', 'path': '
# /', 'secure': False, 'value': '2082758401l'}, {'domain':
# '.amazon.in', 'expiry': 2082758396.140887, 'httpOnly': Fal
# se, 'name': 'ubid-acbin', 'path': '/', 'secure': False, 'valu
# e': '262-7690374-2427550'}, {'domain': '.amazon.in', 'expiry':
# 2082758396.141058, 'httpOnly': False, 'name': 'session-id', '
# path': '/', 'secure': False, 'value': '260-6534839-5006762'}, {'d
# omain': '.amazon.in', 'expiry': 2082787195.603126, 'httpOnly': False
# , 'name': 'i18n-prefs', 'path': '/', 'secure': False, 'value': 'INR'},
# {'domain': '.amazon.in', 'expiry': 2082758396.140951, 'httpOnly': False,
# 'name': 'x-wl-uid', 'path': '/', 'secure': False, 'value': '1HPUi4i7ZyhMP
# Ox7N++kStSe16s/y9Sbb0R2tNVbBUNXNKISmNXkP2oVf4cACtUiXw+rStX468Sw='}, {'doma

cookie={'name':'Mycookie','value':'1234567890'}  #adding a cookie in browser
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))   #print number of cookies created
print(cookies)


#deleting cookie

driver.delete_cookie('Mycookie')
cookies = driver.get_cookies()
print(len(cookies))   #print number of cookies after deleting the cookie
print(cookies)from selenium import webdriver
driver=webdriver.Chrome(executable_path="D:/appium\chromedriver.exe")

driver.get("https://www.amazon.in/")

#capture all the cookies created by browser

cookies = driver.get_cookies()
print(len(cookies))   #print number of cookies created
print(cookies)  #here all the cookies are saved in dictionary format
                #all cookies will be printed
#[{'domain': '.amazon.in', 'expiry': 2192684444.14099,
# 'httpOnly': False, 'name': 'session-token',
# 'path': '/', 'secure': False, 'value':
# '/up+T44pBl8zsxUILKP3o7d3xASQTdkQciTPihyMwj/
# AWJ0FZaSJdUwUsmkRGPZOPcpIcZOr7xqzbxILuXiHmh7HSXVANFe
# /4vKh2K0G0d1E83T8aEwfJavCHTEeFl74+8/pw0/i/p+rgtbK8U5
# dkWPHugm45+V//OFrMNOgjYB9y3OApDgUHPhdGo2cLYSTGCEOYS
# EiiHhI4TLVs2A1RSHqYJmWSCbxb+8gnZEGEOJOgpBCDXo+aw=='},
# {'domain': '.amazon.in', 'expiry': 2082758396.141025, '
# httpOnly': False, 'name': 'session-id-time', 'path': '
# /', 'secure': False, 'value': '2082758401l'}, {'domain':
# '.amazon.in', 'expiry': 2082758396.140887, 'httpOnly': Fal
# se, 'name': 'ubid-acbin', 'path': '/', 'secure': False, 'valu
# e': '262-7690374-2427550'}, {'domain': '.amazon.in', 'expiry':
# 2082758396.141058, 'httpOnly': False, 'name': 'session-id', '
# path': '/', 'secure': False, 'value': '260-6534839-5006762'}, {'d
# omain': '.amazon.in', 'expiry': 2082787195.603126, 'httpOnly': False
# , 'name': 'i18n-prefs', 'path': '/', 'secure': False, 'value': 'INR'},
# {'domain': '.amazon.in', 'expiry': 2082758396.140951, 'httpOnly': False,
# 'name': 'x-wl-uid', 'path': '/', 'secure': False, 'value': '1HPUi4i7ZyhMP
# Ox7N++kStSe16s/y9Sbb0R2tNVbBUNXNKISmNXkP2oVf4cACtUiXw+rStX468Sw='}, {'doma

cookie={'name':'Mycookie','value':'1234567890'}  #adding a cookie in browser
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))   #print number of cookies created
print(cookies)


#deleting cookie

driver.delete_cookie('Mycookie')
cookies = driver.get_cookies()
print(len(cookies))   #print number of cookies after deleting the cookie
print(cookies)