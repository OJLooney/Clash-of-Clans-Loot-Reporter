import re
import requests
from bs4 import BeautifulSoup

class Forecaster():
    def __init__(self):
        self.URL = "http://clashofclansforecaster.com/"
        self.brewScript()
    
    def brewScript(self):
        response = requests.get(self.URL)
        soup = BeautifulSoup(response.text,'lxml')
        
        self.script = str(soup.select("script")[9])

    def scrapeFarmersForecast(self):
        currentLootAvailabiltyRegex = re.compile(r'(Loot available is )(\w+)( right now\.  This will continue for the next )([\w ]+)')
        currentLootForecastRegex = re.compile(r'(Loot available is )([\w\d \.]+)')
        #regexv1 = '(Loot available is )(\w+)( right now\.  This will continue for the next )([\w ]+)'
        #regexv2 = '.+(TERRIBLE|OKAY|DECENT|GOOD|GREAT).+(\d+ hours \d{0,2} minutes)|(\d+ hours \d{0,2} minutes)'
        #regexv3 = 'Loot available is \w\\",'
        mo = currentLootAvailabiltyRegex.search(self.script)
        mo2 = currentLootForecastRegex.search(self.script)
        self.outputString1 = ("Loot status: " + mo.group(2) + " for next: " +  mo.group(4))
        self.lootStatus = mo.group(2)
        self.lootStatusLeft = mo.group(4)
        self.lootForecast = mo2.group()
    
    def scrapeLootIndex(self):
        currentLootIndexRegex = re.compile(r'"lootIndexString.{5}(\d\.\d)')
        mo = currentLootIndexRegex.search(self.script)
        
        self.lootIndex = mo.group(1)
    
    def defaultScrape(self):
        self.brewScript()
        self.scrapeFarmersForecast()
        self.scrapeLootIndex()