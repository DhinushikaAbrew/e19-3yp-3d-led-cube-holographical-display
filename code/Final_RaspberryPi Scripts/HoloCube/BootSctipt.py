from HoloCube import *
from saveToJson import LoadSatartup
from bluetooth_connect import blue_connect
import serial
import rotation_translation
import json

import time
import multiprocessing
import threading
import RPi.GPIO as GPIO


data_lock = threading.Lock()

towerA = Towers(mode="BCM", data_1=16 , data_2=12 , data_3=1  , data_4=7  , clock=21, ics=2)
towerD = Towers(mode="BCM", data_1=8  , data_2=25 , data_3=24 , data_4=23 , clock=18, ics=2)
towerC = Towers(mode="BCM", data_1=2  , data_2=3  , data_3=4  , data_4=17 , clock=27, ics=2)
towerB = Towers(mode="BCM", data_1=22 , data_2=10 , data_3=9  , data_4=11 , clock=0, ics=2)

uart_channel = serial.Serial("/dev/ttyAMA0", baudrate = 9600, timeout=2)
signals = []
data1 = ''
cube_list_global = []


#to get raw data from the bluetooth connection
def get_data():
    ls = []
    while 1:
        #print('secondary')
        data = uart_channel.read(1)
        if len(data)>0:
            if ord(data) == 122:
                break
            ls.append(ord(data))
        else:
            break
        uart_channel.flush()
    return ls

def cube(lst):
    #cube_ls = []
    cube_str = ''
    dic = {48: '0000', 49: '0001', 50: '0010', 51: '0011', 52: '0100', 53: '0101', 54: '0110', 55: '0111', 56: '1000', 57: '1001', 97: '1010', 98: '1011', 99: '1100', 100: '1101', 101: '1110', 102: '1111'}
    for i in lst:
        cube_str += dic[i]
    return cube_str



layers = Layers(mode="BCM", data=13, clock=6, latch=5, ics=2)
masterlatch = MasterLatch(mode="BCM",latch=20 )



def showCube():
    
    global data_lock
    
    while True:  
        with data_lock:  
            # Read data from the JSON file
            with open("test.json", "r") as file:
                data = json.load(file)

            listA, listB, listC, listD = data["A"], data["B"], data["C"], data["D"]
            
            #print(len(listA))
            
            
            for i in range (16):
                idx = 64*i
                for j in range(15,-1,-1):
                    #Tower A
                    GPIO.output(16, listA[idx+j])
                    GPIO.output(12, listA[idx+j+16])
                    GPIO.output(1, listA[idx+j+32])
                    GPIO.output(7,listA[idx+j+48])
                    
                    #Tower B
                    GPIO.output(8, listC[idx+j])
                    GPIO.output(25, listC[idx+j+16])
                    GPIO.output(24,listC[idx+j+32])
                    GPIO.output(23, listC[idx+j+48])
                    
                    #Tower C
                    GPIO.output(2, listB[idx+j])
                    GPIO.output(3, listB[idx+j+16])
                    GPIO.output(4, listB[idx+j+32])
                    GPIO.output(17, listB[idx+j+48])
                    
                    #Tower D
                    GPIO.output(22, listD[idx+j])
                    GPIO.output(10, listD[idx+j+16])
                    GPIO.output(9, listD[idx+j+32])
                    GPIO.output(11, listD[idx+j+48])
                    
                    GPIO.output(21, GPIO.HIGH)
                    GPIO.output(18, GPIO.HIGH)
                    GPIO.output(27, GPIO.HIGH)
                    GPIO.output(0, GPIO.HIGH)
                    #time.sleep(0.0000001)
                    GPIO.output(21, GPIO.LOW)
                    GPIO.output(18, GPIO.LOW)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(0, GPIO.LOW)
            
                masterlatch.master_latch()
                layers.set_layer(i)

def doNothing(A,B,C,D,a,b,c,d):
    while True:
        #time.sleep(0.1)
        for i in range(1024):
            a[i]=A[i]
            b[i]=B[i]
            c[i]=C[i]
            d[i]=D[i]



if __name__ == "__main__":
    
    LoadSatartup()
#         showCube(A,B,C,D)
#         blue_connect()
  
    process2 =threading.Thread(target=blue_connect)
    process1 =threading.Thread(target=showCube)


    process1.start()
    process2.start()

    process1.join()
    process2.join()

