#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

# See https://docs.pycom.io for more information regarding library specifics

from pysense import Pysense
from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE

py = Pysense()
#mp = MPL3115A2(py,mode=ALTITUDE) # Returns height in meters. Mode may also be set to PRESSURE, returning a value in Pascals
mp = MPL3115A2(py,mode=PRESSURE) # Returns height in meters. Mode may also be set to PRESSURE, returning a value in Pascals
si = SI7006A20(py)
lt = LTR329ALS01(py)
li = LIS2HH12(py)

import _thread
from time import sleep
from simple import MQTTClient
import uos
import pycom

pycom.heartbeat(False)
pycom.rgbled(0xff00) 

def send_sensor_data():
    my_list = []
    while (pybytes):
        pybytes.send_signal(1, si.humidity())

        pybytes.send_signal(3, sum(lt.light()))

        print(lt.light())
        print(len(my_list))
        my_list.append(lt.light())
        if(len(my_list) > 5):
            pycom.rgbled(0x055f) 
            print(my_list)
            my_list = list()
            #send data

        sleep(1)
        pycom.rgbled(0xff00) 


_thread.start_new_thread(send_sensor_data, ())
