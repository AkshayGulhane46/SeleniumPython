from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions=Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory":"c:\Downloadedfiles"})




driver= webdriver.Chrome(executable_path="C:/Users\Android - PC\Downloads\drivers\chromedriver.exe",chrome_options=chromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

driver.find_element_by_id("textbox").send_keys("testing download textffile")
driver.find_element_by_id("createTxt").click()         #generate link
driver.find_element_by_id("link-to-download").click()  # download link

#download pdf file

driver.find_element_by_id("pdfbox").send_keys("testing pdf")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()

#driver.close()

