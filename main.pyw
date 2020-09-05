from forecasterScrapper import Forecaster
import yagmail
import re


def valid_email(email):
  return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

def writeToSendertxt():
    with open("senderDetails.txt", "w") as file:
            userEmail = input("Enter sender's email:\n")
            userPass = input("Enter sender's password:\n")
            file.write(userEmail+"\n"+userPass)

def writeToRecievertxt():
    with open("recieverDetails.txt", "w") as file:
            userEmail = input("Enter reciever's email:\n")
            file.write(userEmail)

def sendEmail(myForecaster, emails, senderDetails):
    status = "["+myForcaster.lootIndex+"/10] Current Loot Status: " + myForcaster.lootStatus + ", for: " + myForcaster.lootStatusLeft
    if valid_email(senderDetails[0]):
        yag = yagmail.SMTP(senderDetails[0], senderDetails[1])
        with yagmail.SMTP(senderDetails[0]) as yag:
            for reciever in emails:
                if valid_email(reciever):
                    yag.send(reciever, status, myForcaster.lootForecast)
                else:
                    print("ERROR with emails. Please check and re-edit the txt files.")
                    writeToRecievertxt()
                    sendEmail(myForecaster, emails, senderDetails)
    else:
        print("ERROR with emails. Please check and re-edit the txt files.")
        writeToSendertxt()
        sendEmail(myForecaster, emails, senderDetails)

def getSenderDetails():
    try:
        with open("senderDetails.txt", "r") as file:
            senderDetails = file.readlines()
        return(senderDetails)
    except:
        writeToSendertxt()


def getRecieverDetails():
    try:
        with open("recieverDetails.txt", "r") as file:
            emails = file.readlines()
        return(emails)
    except:
        writeToRecievertxt()

lastLootStatus = "null"
myForcaster = Forecaster()
senderDetails = getSenderDetails()
yagmail.register(senderDetails[0],senderDetails[1])
while True:
    myForcaster.defaultScrape()
    if myForcaster.lootStatus != lastLootStatus:
        lastLootStatus = myForcaster.lootStatus
        sendEmail(myForcaster, getRecieverDetails(),getSenderDetails())