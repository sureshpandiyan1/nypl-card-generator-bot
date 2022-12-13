import requests
from bs4 import BeautifulSoup
import time
from configparser import RawConfigParser

def intro():
    graphicz = """


                      __                       __                     
   ____  __  ______  / /  _________ __________/ /                     
  / __ \/ / / / __ \/ /  / ___/ __ `/ ___/ __  /                      
 / / / / /_/ / /_/ / /  / /__/ /_/ / /  / /_/ /                       
/_/ /_/\__, / .___/_/   \___/\__,_/_/__ \__,_/         __          __ 
   __________/____  ___  _________ _/ /_____  _____   / /_  ____  / /_
  / __ `/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/  / __ \/ __ \/ __/
 / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /     / /_/ / /_/ / /_  
 \__, /\___/_/ /_/\___/_/   \__,_/\__/\____/_/     /_.___/\____/\__/  
/____/                                                                


Copyright @ 2022 nypl card generator | Created By Suresh P
Made with love for everyone :) |  The Unlicense

"""
    print(graphicz)


def clctfakedata():
    url = "https://www.fakexy.com/us-fake-address-generator-nm"
    time.sleep(0.2)
    res = requests.get(url)
    l = BeautifulSoup(res.text, features="html.parser")

    clctfakedata = {}
    ls = []
    for x in ['\n']:
        for y in l.find_all('table')[0].find_all('tr'):
            spt1 = str(y).replace(x,"").split("<tr><td>")
            spt2 = str(spt1).split("</td><td>")
            spt3 = str(spt2[1:][0]).split("</td></tr>")
            gotcha = str(spt3[0]).split("\n")
            ls.append(gotcha[0])
            clctfakedata |= {n : k for n, k in zip(["street","city","state","zip"],ls)}
    return clctfakedata


def get_data(section="alternateFake",name="fakeaddressofnewyork.cfg",modez="a"):
    config = RawConfigParser(); config.add_section(section)
    for x,y in clctfakedata().items(): config.set(section,x,y)
    with open(name, modez) as fakezz: config.write(fakezz)

def followingthingsneed():
    myconfig = RawConfigParser()
    myconfig.add_section("details")
    print("we need a following details for the nypl card:")
    print("no worries..we don't collect any personal information from your side")
    print("*" * 30)
    print("read this instruction when you type in details")
    print("DOB format: MM/DD/YYYY | username should be letters contains a numbers")
    print("password should contains letter and lowercase and one special characters..atleast 8 characters")
    print("*" * 30)
    fname, lname, dob, mailid, username, passd = input("firstname: "),input("lastname: "),input("dob: "),input("email: "),input("username: "),input("password: ")
    clct = [fname,lname,dob,mailid,username,passd]
    clctd = ["fname","lname","dob","mailid","username","passd"]
    for x, y in zip(clctd, clct):
        myconfig.set("details",x,y)
    with open("fakeaddressofnewyork.cfg","a") as clt: myconfig.write(clt)
    print("thank you for give all information :)..")
    time.sleep(2)
    print("processing..don't close any windows")
    time.sleep(2)
    print("just sit back and watch..until you see a membership card")
    time.sleep(2)


getdatas = {
    'intro': intro(),
    'fkdata1': get_data(section="Fake",name="fakeaddressofnewyork.cfg",modez="w"),
    'fkdata2': get_data(section="alternateFake",name="fakeaddressofnewyork.cfg",modez="a"),
    'fkdata3': followingthingsneed()
}


stopme = True
while stopme:
    for justcollectthat in getdatas.values():
        if len(getdatas) == 4:
            justcollectthat
            stopme = False

