import keyboard
import time
import serial

ser = serial.Serial('COM4', baudrate = 9600, timeout = 1)

def gamePressKey(key):
            for x in range(0, 10):
                keyboard.press(key)
                time.sleep(0.01)
            keyboard.release(key)
             
while 1:
    arduinoData = ser.readline().decode('ascii')[:-2]

    if arduinoData:
        if arduinoData == '1':
            gamePressKey('w')

        if arduinoData == '0':
            gamePressKey('s')