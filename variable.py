# Programda kullanılan değişkenler burada tutuluyor.
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
# Gerkli olan Path adresleri
driverPath = dir_path + "/chromedriver"
logPath = dir_path + "/log.log"
excelPath = dir_path + "/teias_bilgi.xls"
excelFilePath = dir_path + '/saat/'
browserAdress = "https://ytbs.teias.gov.tr/ytbs/frm_login.jsf"

# Kullanıcı adı ve şifre
username = "kullanici adi"
password = "Password"

#Tarayıcıda kullanılacak olan blokların adresleri
browserKullaniciAdi = "//*[@id='loginForm:username']"
browserPassword = "//*[@id='loginForm:password']"
browserLoginClick = "//*[@id='loginForm:btnLogin']/span"

browserV1 = "/html/body/div[1]/div[4]/div/div/div/div/form/div/table/tbody/tr[4]/td/div/div/table/thead/tr[3]/th[3]/span/span/input[1]" # kV
browserV2 = "/html/body/div[1]/div[4]/div/div/div/div/form/div/table/tbody/tr[4]/td/div/div/table/thead/tr[3]/th[4]/span/span/input[1]" # MVAr Payas
browserV3 = "/html/body/div[1]/div[4]/div/div/div/div/form/div/table/tbody/tr[4]/td/div/div/table/thead/tr[3]/th[5]/span/span/input[1]" # MW   Payas
browserV4 = "/html/body/div[1]/div[4]/div/div/div/div/form/div/table/tbody/tr[4]/td/div/div/table/thead/tr[3]/th[6]/span/span/input[1]" # MVAr TR-A  |
browserV5 = "/html/body/div[1]/div[4]/div/div/div/div/form/div/table/tbody/tr[4]/td/div/div/table/thead/tr[3]/th[7]/span/span/input[1]" # MW   TR-A  |
browserV6 = "/html/body/div[1]/div[4]/div/div/div/div/form/div/table/tbody/tr[4]/td/div/div/table/thead/tr[3]/th[8]/span/span/input[1]" # KADEME  ---
browserV7 = "/html/body/div[1]/div[4]/div/div/div/div/form/div/table/tbody/tr[4]/td/div/div/table/thead/tr[3]/th[9]/span/span/input[1]" # MVAr  TR-B |
browserV8 = "/html/body/div[1]/div[4]/div/div/div/div/form/div/table/tbody/tr[4]/td/div/div/table/thead/tr[3]/th[10]/span/span/input[1]" # MW    TR-B |
browserV9 = "/html/body/div[1]/div[4]/div/div/div/div/form/div/table/tbody/tr[4]/td/div/div/table/thead/tr[3]/th[11]/span/span/input[1]" # KADEME  ---

browserVeriEkle = "//*[@id='veriGirisForm:dtVeriGiris:ekle']"

browserDialogClose = "//*[@id='diyalog']/div[1]/a"
browserVeriGirisEkranı = "/html/body/div[1]/div[4]/div/div/form/div/div[2]/div[2]/div[3]/button"

browserNextHour = "/html/body/div[1]/div[4]/div/div/div/div/form/div/table/tbody/tr[4]/td/div/div/table/thead/tr[3]/th[2]/span/div/label"

