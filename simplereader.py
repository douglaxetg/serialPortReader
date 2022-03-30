# -*- coding: cp1252 -*-
import threading
import serial

class simpleReader():
    def __init__(self, port, baud):
        self.port = port
        self.baud = baud

    def connectTo(self):
        try:
            self.connection = serial.Serial(self.port, self.baud)
            print("Connected, waiting for data")
        except:
            print("Connection failed")
    
    def onThread(self):
        thread = threading.Thread(target=self.getData)
        thread.daemon = True
        thread.setDaemon(1)
        thread.start()
    
    def getData(self):
        while True:
            try:
                if self.connection.isOpen():
                    readingData = self.connection.read()
                    print(ord(readingData)) #convert Unicode character to integer Unicode code
            except:
                print("error getting data")
                break

linuxPort = "/dev/ttyUSB0"
windowsPort = "COM5"
appMonitor = simpleReader(linuxPort, 115200)
appMonitor.connectTo()
appMonitor.onThread()

while True:
    pass