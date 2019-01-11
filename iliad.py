#!/usr/bin/python

import requests
import json
from collections import defaultdict
from bs4 import BeautifulSoup

class Iliad:
    BASE_URL =   "https://www.iliad.it/account/consumi-e-credito"
    page =  ''
    trafficPercent =  0
    residuoEuro =  0


    
    def getData(self):
        r = requests.get(BASE_URL)
	#print r.headers
        resSession = r.cookies['ACCOUNT_SESSID']
        myCookies = dict(ACCOUNT_SESSID=resSession)
        r2 = requests.get(URL, cookies=myCookies)
        page =  r2.text
    
    def getTraffic(self):
        soup = BeautifulSoup(page, 'html.parser')
        price_box = soup.find('div', attrs={'class':'progressbar'})
        price = price_box.text
        trafficPercent =  price_box['data-progress-value']
        return trafficPercent

    def getMoney(self):
        soup = BeautifulSoup(page, 'html.parser')
        residuo = soup.find('div', attrs={'class':'red montant'})
        residuoEuro =  residuo.text
        return residuoEuro
        

if __name__ == '__main__':
    print("**** test iliad **** ")
    iliad = Iliad()
    iliad.getData()
    
    print "TRAFFICO: " + iliad.getTraffic()
    print "RESIDUO: " + iliaa.getMoney()