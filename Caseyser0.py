#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 07:47:44 2017

@author: caseyhoward
"""


import sys
import serial

port = "/dev/tty.usbserial-DN01ITKA"
baud = 9600

ser = serial.Serial()
ser.port = port
ser.baudrate = baud

try:
    ser.open()
except:
    sys.stderr.write("Error opening serial port %s\n" % (ser.portstr) )
    sys.exit(1)
   
#ser.setRtsCts(0)

while 1:
   # Read from serial port, blocking
   data = ser.read(1)
   print (data)

   # If there is more than 1 byte, read the rest
   n = ser.inWaiting()
   if n:
       data = data + ser.read(n)
       
   sys.stdout.write(data)
