import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from variable import *

class Browser:
    def __init__(self, loggerService):
        self.loggerService = loggerService

    # Yük Tevzi sistemine giriş işlemi yapılıyor.
    def loginBrowser(self):
        self.browser    = webdriver.Chrome(executable_path = driverPath)
        self.browser.get(browserAdress)
        time.sleep(2)
        kadiText = self.browser.find_element_by_xpath(browserKullaniciAdi)
        passText = self.browser.find_element_by_xpath(browserPassword)
        kadiText.send_keys(username)
        passText.send_keys(password)
        self.browser.find_element_by_xpath(browserLoginClick).click()
        time.sleep(5)

    # Yük Tevzi sisteminde veri giriş ekranı açılıyor.
    def veriGirisIslemleri(self):
        try:
            try:
                time.sleep(2)
                self.browser.find_element_by_xpath(browserDialogClose).click()
            except:
                self.loggerService.log("Diyalog penceresi bulunamadi")
            self.browser.find_element_by_xpath(browserVeriGirisEkranı).click()
            time.sleep(0.5)
            return True
        except:
            self.loggerService.log(" Veri Giris Alanina Erisilemedi. Tekrar Deneniyor... ")
            time.sleep(7)
            return False

    # Veri giriş alanından sıradaki saat bilgisi alınıyor.
    def hourControl(self):
        try:
            nextTime = self.browser.find_element_by_xpath(browserNextHour).text
            if nextTime == "24:00":
                nextTime = "23:59"
            self.dateTimeObj = datetime.datetime.strptime(nextTime, '%H:%M')
            self.loggerService.log("Saat Bilgisi alindi: " + nextTime)
            return True
        except:
            self.loggerService.log("Saat Bilgisi alinamadi. Browser kapatılacak.")
            self.browserClose()
            time.sleep(15)
            return False

    # Excelden okunan değerler liste formatında alınıyor,
    # Alınan değerler ytbs veri giriş ekranında uygun yerlere yazılıyor.
    def veriUpload(self, excelList):
        try:
            #self.browserXPath()
            time.sleep(2)

            d1 = str(excelList[0]).split(".") # kV
            d2 = str(excelList[1]).split(".") # MVAr Payas
            d3 = str(excelList[2]).split(".") # MW   Payas
            d4 = str(excelList[3]).split(".") # MVAr TR-A
            d5 = str(excelList[4]).split(".") # MW   TR-A
            # d6 = 17 kademe sabit
            d7 = str(excelList[6]).split(".") # MVAr TR-B
            d8 = str(excelList[7]).split(".") # MW   TR-B
            # d9 = 17 kademe sabit

            self.v1.send_keys(d1[0]+","+d1[1])
            time.sleep(0.1)
            self.v2.send_keys(d2[0]+","+d2[1])
            time.sleep(0.1)
            self.v3.send_keys(d3[0]+","+d3[1])
            time.sleep(0.1)
            self.v4.send_keys(d4[0]+","+d4[1])
            time.sleep(0.1)
            self.v5.send_keys(d5[0]+","+d5[1])
            time.sleep(0.1)
            self.v6.send_keys("17")
            time.sleep(0.1)
            self.v7.send_keys(d7[0]+","+d7[1])
            time.sleep(0.1)
            self.v8.send_keys(d8[0]+","+d8[1])
            time.sleep(0.1)
            self.v9.send_keys("17")
            time.sleep(5)

            self.browser.find_element_by_xpath(browserVeriEkle).click()
            self.loggerService.log("*** Saat verisi girildi. ***")
            self.browserClose()
        except:
            try:
                d3 = str(excelList[2]).split(".") # MW   Payas
                d5 = str(excelList[4]).split(".") # MW   TR-A
                d8 = str(excelList[7]).split(".") # MW   TR-B

                self.v3.send_keys(d3[0]+","+d3[1])
                time.sleep(0.1)
                self.v5.send_keys(d5[0]+","+d5[1])
                time.sleep(0.1)
                self.v8.send_keys(d8[0]+","+d8[1])
                time.sleep(5)

                self.browser.find_element_by_xpath(browserVeriEkle).click()
                self.loggerService.log("Puant saati girildi.")
                self.browserClose()
            except:
                self.loggerService.log("Bilinmeyen bir hata olustu. Veri girilemedi. Tekrar Deneniyor...")
                time.sleep(5)

    # Geçmiş olan saatin endex verisi liste formatında alınıyor,
    # Alınan değerler ytbs veri giriş ekranında uygun yerlere yazılıyor.
    def veriUploadPast(self, excelList):
        try:
            self.browserXPath()
            time.sleep(2)

            self.v1.send_keys(excelList[0])
            self.v2.send_keys(excelList[1])
            self.v3.send_keys(excelList[2])
            self.v4.send_keys(excelList[3])
            self.v5.send_keys(excelList[4])
            self.v6.send_keys("17")
            self.v7.send_keys(excelList[6])
            self.v8.send_keys(excelList[7])
            self.v9.send_keys("17")

            time.sleep(5)
            self.browser.find_element_by_xpath(browserVeriEkle).click()
            self.logger.error("*** Gecmis Saat verisi girildi. ***")
            self.browserClose()
        except:
            try:
                self.v3.send_keys("-19,69")
                self.v5.send_keys("0,80")
                self.v8.send_keys("18,84")
                time.sleep(5)
                self.loggerService.log("Gecmis Puant saati girildi.")
                self.browser.find_element_by_xpath(browserVeriEkle).click()
                self.browserClose()
            except:
                self.loggerService.log("Bilinmeyen bir hata olustu. Geçmiş saat Verisi girilemedi.")
                time.sleep(5)

   #  Taryıcıda kullanılacak olan konpenetler değişkene atanıyor.
    def browserXPath(self):
        self.v1 = self.browser.find_element_by_xpath(browserV1) # kV
        self.v2 = self.browser.find_element_by_xpath(browserV2) # MVAr Payas
        self.v3 = self.browser.find_element_by_xpath(browserV3) # MW   Payas
        self.v4 = self.browser.find_element_by_xpath(browserV4) # MVAr TR-A  |
        self.v5 = self.browser.find_element_by_xpath(browserV5) # MW   TR-A  |
        self.v6 = self.browser.find_element_by_xpath(browserV6) # KADEME  ---
        self.v7 = self.browser.find_element_by_xpath(browserV7) # MVAr  TR-B |
        self.v8 = self.browser.find_element_by_xpath(browserV8) # MW    TR-B |
        self.v9 = self.browser.find_element_by_xpath(browserV9) # KADEME  ---

    # Tarayıcı kapatılıyor.
    def browserClose(self):
        try:
            self.browser.close()
        except:
            pass
