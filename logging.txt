#logging is a very useful tool in a programmers toolbox. it can be help you to develope a
#better understanding of the flow of a program and discover
# scenarios that you might not even have thought while
# developing   log levels
#debug
#info
#warning
#error
#critical

import logging
#setting for debug and info messages

logging.basicConfig(filename="D:/appium/selenium with python/logs/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',                  #this will change the format to time,level and message
                    level=logging.DEBUG
                    )  #this will create a log file
logging.debug("This is debug message ")
logging.info("This is info message ")

logging.warning("This is warning message ")  #if you run it without any code warning errror and critical run but debug and info doesnt
logging.error("This is error message ")
logging.critical("This is critical message ")








