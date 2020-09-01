from forecasterScrapper import Forecaster
import yagmail

def sendEmail(myForecaster, emails, senderDetails):
    status = "["+myForcaster.lootIndex+"/10] Current Loot Status: " + myForcaster.lootStatus + ", for: " + myForcaster.lootStatusLeft
    yag = yagmail.SMTP(senderDetails[0], senderDetails[1])
    with yagmail.SMTP(senderDetails[0]) as yag:
        for reciever in emails:
            yag.send(reciever, status, myForcaster.lootForecast)

def getSenderDetails():
    try:
        f = open("senderDetails.txt", "r")
        senderDetails = f.readlines()
        f.close()
        return(senderDetails)
    except:
        f = open("senderDetails.txt", "w")
        f.write("senderEmail\nsenderPassword")
        f.close()

def getRecieverDetails():
    try:
        f = open("recieverDetails.txt", "r")
        emails = f.readlines()
        f.close()
        return(emails)
    except:
        f = open("recieverDetails.txt", "w")
        f.write("recieverEmail[for multiple, enter emails on new line]")
        f.close()

lastLootStatus = "null"
myForcaster = Forecaster()
senderDetails = getSenderDetails()
yagmail.register(senderDetails[0],senderDetails[1])
while True:
    myForcaster.defaultScrape()
    if myForcaster.lootStatus != lastLootStatus:
        lastLootStatus = myForcaster.lootStatus
        sendEmail(myForcaster, getRecieverDetails(),getSenderDetails())