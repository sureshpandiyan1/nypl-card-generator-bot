from selenium import webdriver
from selenium.webdriver.common.by import By
import time, runpy, configparser
import os


config = configparser.RawConfigParser()
config.read("fakeaddressofnewyork.cfg")


thatdata = {
    "street":    config.get("Fake","street"),
    "city":      config.get("Fake","city"),
    "zip":       config.get("Fake","zip"),
    "streetn":   config.get("alternateFake","street"),
    "cityn" :    config.get("alternateFake","city"),
    "zipn" :     config.get("alternateFake","zip"),
    "fname": config.get("details","fname"),
    "lname": config.get("details","lname"),
    "dob": config.get("details","dob"),
    "mailid": config.get("details","mailid"),
    "uname":  config.get("details","username"),
    "passd": config.get("details","passd")
}



driver = webdriver.Chrome()
driver.get("https://www.nypl.org/library-card/new")


# FIRST PAGE
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Get Started").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/form/div/div[1]/div[1]/div/div/input").send_keys(thatdata["fname"])
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/form/div/div[1]/div[2]/div/div/input").send_keys(thatdata["lname"])
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/form/div/div[2]/div/div/div/input").send_keys(thatdata["dob"])
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/form/div/div[3]/div/div/div/input").send_keys(thatdata["mailid"])
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/form/div/div[6]/div/div/input").click()

# SECOND PAGE
# street
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/form/div/div[1]/div/div/div/input").send_keys(thatdata["street"])
# city
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/form/div/div[3]/div[1]/div/div/input").send_keys(thatdata["city"])
# state
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/form/div/div[3]/div[2]/div/div/input").send_keys("NY")
# postal code
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/form/div/div[4]/div[1]/div/div/input").send_keys(thatdata["zip"])
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/form/div/div[6]/div/div/input").click()


# THIRD PAGE
time.sleep(4)
driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div/form/div/div[1]/div/div/div/input").send_keys(thatdata["streetn"])
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div/form/div/div[3]/div[1]/div/div/input").send_keys(thatdata["cityn"])
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div/form/div/div[3]/div[2]/div/div/input").send_keys("NY")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div/form/div/div[4]/div[1]/div/div/input").send_keys(thatdata["zipn"])
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div/form/div/div[6]/div/div/input").click()
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/form/div/div[3]/div/div/input").click()

# username:
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div/form/div/div[1]/div/div/div/input").send_keys(thatdata["uname"])


# password:
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/form/div/div[4]/div/div/div/input").send_keys(thatdata["passd"])

time.sleep(2)
# verify password
driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/form/div/div[5]/div/div/div/input").send_keys(thatdata["passd"])

time.sleep(2)
# password
driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/form/div/div[8]/label/span[1]").click()
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/form/div/div[10]/div/div/input").click()


time.sleep(7)
driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/form/div/div[2]/div/div/input").click()


with open(os.environ["USERPROFILE"]+ "\Desktop\{0}.txt".format("nypl-"+ thatdata["mailid"])) as wt:
    for y in [thatdata["fname"], thatdata["lname"],thatdata["dob"], thatdata["mailid"], thatdata["uname"], thatdata["passd"]]:
       wt.write(y)

time.sleep(3600)
print("just see your desktop screen and saved as text file what you entered in details")
print("file look like ex: nypl-<yourmailid>.txt")
time.sleep(2)


