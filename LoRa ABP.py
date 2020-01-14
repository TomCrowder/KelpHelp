from network import LoRa
import socket
import ubinascii
import struct

# Initialise LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=Asia)

# create an ABP authentication params
dev_addr = struct.unpack(">l", ubinascii.unhexlify('26041B32'))[0]
nwk_swkey = ubinascii.unhexlify('07835009548BF728D46C04A5E9433FA2')
app_swkey = ubinascii.unhexlify('748D6C57634D90FC73FAA15743A6C92E')

# join a network using ABP (Activation By Personalization)
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)

# send some data
s.send(bytes([0x01, 0x02, 0x03]))
print('date sent')

# make the socket non-blocking
# (because if there's no data received it will block forever...)
s.setblocking(False)

# get any data received (if any...)
data = s.recv(64)
print(data)
