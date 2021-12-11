#encoding:utf-8
# ########################################## #
#                   21/11/2020               #
#   Otamatik YTBS Verileri Giren Program     #
#               ABA Çelik Demir A.Ş          #
#                   Version 2.0              #
# ########################################## #

import time
import logger
from browser import Browser
from excel import Excel

loggerText = logger.TextLoging()
loggerConsole = logger.ConsoleLoging()
browser = Browser(loggerText)
excel = Excel(loggerText)

# Yük Tevzi Bilgi Sisteminden sıradaki saat bilgisini alan fonksiyon
def veriGirisEkraniSaatVerisiAlma():
    try:
        browser.loginBrowser()
        req = browser.veriGirisIslemleri()
        time.sleep(10)
        if(req):
            req = browser.hourControl()
            if(req):
                return browser.dateTimeObj
            else:
                browser.browserClose()
                veriGirisEkraniSaatVerisiAlma()
        else:
            browser.browserClose()
            veriGirisEkraniSaatVerisiAlma()
    except:
        veriGirisEkraniSaatVerisiAlma()
        loggerText.log("Saat verisi alma ekranı açılırken hata oluştu.")

# Yük Tevzi Bilgi Sistemine endex verilerinin girilmesini sağlayan fonksiyon
def veriGirisEkraniVeriGirme(counter):
    print(counter)
    counter += 1
    if(counter < 20):
        try:
            browser.browserClose()
            browser.loginBrowser()
            req = browser.veriGirisIslemleri()
            if(req):
                browser.veriUpload(listExcel)
            else:
                veriGirisEkraniVeriGirme(counter)
        except:
            veriGirisEkraniVeriGirme(counter)
            loggerText.log("Veri Girme Ekranı açılırken hata oluştu.")
    else:
        loggerText.log("timeout")


#Uygulama ana döngüsü
while(True):
    veriGirisEkraniSaatVerisiAlma()
    while(True):
        try:
            localDay = time.strftime("%Y-%m-%d")
            localTime = time.strftime('%H:%M')
        
            if localTime == browser.dateTimeObj.strftime("%H:%M"):
                loggerText.log("Saatler esit")
                listExcel = excel.read()
                excel.save(browser.dateTimeObj.strftime("%H,%M"))
                veriGirisEkraniVeriGirme(counter = 0)
                break
            elif localTime > browser.dateTimeObj.strftime("%H:%M"):
                loggerText.log("Saat bilisi tekrar giriliyor : " + browser.dateTimeObj.strftime("%H:%M"))
                time.sleep(1)
                listExcel = excel.readFile(browser.dateTimeObj.strftime("%H,%M"))
                browser.veriUploadPast(listExcel)
                break 
            else :
                browser.browserClose()
                loggerText.log("Siradaki saat bekleniyor: " + browser.dateTimeObj.strftime("%H:%M"))
                time.sleep(20)
        except :
            try:
                loggerText.log("Bilinmeyen bir hata olustu.")
                browser.browserClose()
                break
            except:
                break



