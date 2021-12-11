# Yapılan işlemleri loglamak için kullanılıyor.
# Log kayıtları hata analizi için kullanıyor.

import time
import logging
from variable import logPath

class BaseLogger:
    def __init__(self):
        pass
        

class TextLoging(BaseLogger):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(logPath)
        self.logger.addHandler(handler)
        self.consoleLogging = ConsoleLoging()

    def log(self, log):
        self.logger.error(time.strftime('%Y-%m-%d %H:%M') + " " + log)
        print(time.strftime('%Y-%m-%d %H:%M') + " " + log)


class ConsoleLoging(BaseLogger):
    def log(log):
        print(time.strftime('%Y-%m-%d %H:%M') + " " + log)

