#encoding:utf-8
import xlrd
import xlwt
from variable import excelPath, excelFilePath
import logger

loggerText = logger.TextLoging()

class Excel:
    def __init__(self, loggerService):
        # Excel için gerekli ayarlar yapılıyor.
        self.loggerService = loggerService
        self.data = xlrd.open_workbook(excelPath)
        self.ws = self.data.sheet_by_index(0)
        self.workbook = xlwt.Workbook()
        self.worksheet = self.workbook.add_sheet('Sayfa1')
        self.dataList = []

    def read(self):
        # Excelden anlık endexler okunuyor.
        try:
            self.dataList.clear()
            self.dataList.append(self.ws.cell_value(rowx=2, colx=0)) # kV
            self.dataList.append(self.ws.cell_value(rowx=2, colx=1)) # MVAr Payas
            self.dataList.append(self.ws.cell_value(rowx=2, colx=2)) # MW   Payas
            self.dataList.append(self.ws.cell_value(rowx=2, colx=3)) # MVAr TR-A
            self.dataList.append(self.ws.cell_value(rowx=2, colx=4)) # MW   TR-A
            self.dataList.append(17)
            self.dataList.append(self.ws.cell_value(rowx=2, colx=6)) # MVAr TR-B
            self.dataList.append(self.ws.cell_value(rowx=2, colx=7)) # MW   TR-B
            self.dataList.append(17)
            return self.dataList
        except:
            self.loggerService.log("Excel anlık veri okumada hata oluştu.")

    def readFile(self, dateTimeObj):
        # Geçmiş saat için belirtilen excel dosyasından o saatin endex verileri okunuyor.
        try:
            self.dataList.clear()
            self.data = xlrd.open_workbook(excelFilePath + dateTimeObj + ".xls")
            self.ws = self.data.sheet_by_index(0)

            self.dataList.append(self.ws.cell_value(rowx=2, colx=0)) # kV
            self.dataList.append(self.ws.cell_value(rowx=2, colx=1)) # MVAr Payas
            self.dataList.append(self.ws.cell_value(rowx=2, colx=2)) # MW   Payas
            self.dataList.append(self.ws.cell_value(rowx=2, colx=3)) # MVAr TR-A
            self.dataList.append(self.ws.cell_value(rowx=2, colx=4)) # MW   TR-A
            self.dataList.append(17)
            self.dataList.append(self.ws.cell_value(rowx=2, colx=6)) # MVAr TR-B
            self.dataList.append(self.ws.cell_value(rowx=2, colx=7)) # MW   TR-B
            self.dataList.append(17)
            return self.dataList
        except:
            self.loggerService.log("Excel dosyadan geçmiş saat verisini okumada hata oluştu.")

    def save(self, dateTimeObj):
        # Anlık olarak okunan endexler o saat adıyla excel dosyası olarak kaydediliyor.
        try:
            d1 = str(self.dataList[0]).split(".")
            d2 = str(self.dataList[1]).split(".")
            d3 = str(self.dataList[2]).split(".")
            d4 = str(self.dataList[3]).split(".")
            d5 = str(self.dataList[4]).split(".")
            d7 = str(self.dataList[6]).split(".")
            d8 = str(self.dataList[7]).split(".")
            
            self.worksheet.write(2, 0, d1[0]+","+d1[1])
            self.worksheet.write(2, 1, d2[0]+","+d2[1])
            self.worksheet.write(2, 2, d3[0]+","+d3[1])
            self.worksheet.write(2, 3, d4[0]+","+d4[1])
            self.worksheet.write(2, 4, d5[0]+","+d5[1])
            self.worksheet.write(2, 5, "17")
            self.worksheet.write(2, 6, d7[0]+","+d7[1])
            self.worksheet.write(2, 7, d8[0]+","+d8[1])
            self.worksheet.write(2, 8, "17")
            
            self.workbook.save(excelFilePath + dateTimeObj + ".xls")
            
        except:
            self.loggerService.log("Dosyaya anlık endex verisini kaydederken hata oluştu.")

