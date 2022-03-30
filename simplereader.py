# -*- coding: cp1252 -*-
import threading
import serial

class simpleReader():
    def __init__(self, port, baud):
        self.port = port
        self.baud = baud

    def connection(self):
        try:
            self.connection = serial.Serial(self.port, self.baud)
            print("Connected")
        except:
            print("Connection failed")

linuxPort = "/dev/ttyUSB0"
windowsPort = "COM5"
appMonitor = simpleReader(linuxPort, 115200)
appMonitor.connection()
while True:
    pass