import math
import time
import statistics
from datetime import datetime
from time import sleep		 
import board
import adafruit_mpu6050
import adafruit_tca9548a

print("Welcome!")

currentDay = datetime.today()
currentTime = datetime.now()
fileDate = currentDay.strftime("%m%d")#("%y%m%d")
fileTime = currentTime.strftime("%H%M")#("%H%M%S")
file = open("GyroCalibration.csv", "a")
print("Enter amount of IMUS:")
imus = input()
calibrationTime = 20
stop = False

s = ""
for i in range(imus):
    s += "P"+str(i)+","+"R"+str(i)+","
s = s[:-1] 
s += "\n"
file.write(s)

i2c = board.I2C()  # uses board.SCL and board.SDA
tca = adafruit_tca9548a.TCA9548A(i2c)
i = 0

print("Initializing ...")

if imus >= 1:
    print("1/" + str(imus) + " IMUS ...")
    mpu0 = adafruit_mpu6050.MPU6050(tca[0])
    p1 = []
    r1 = []
if imus >= 2:
    print("2/" + str(imus) + " IMUS ...")
    mpu1 = adafruit_mpu6050.MPU6050(tca[1])
    p2 = []
    r2 = []
if imus >= 3:
    print("3/" + str(imus) + " IMUS ...")
    mpu2 = adafruit_mpu6050.MPU6050(tca[2])
    p3 = []
    r3 = []
if imus >= 4:
    print("4/" + str(imus) + " IMUS ...")
    mpu3 = adafruit_mpu6050.MPU6050(tca[3])
    p4 = []
    r4 = []
if imus >= 5:
    print("5/" + str(imus) + " IMUS ...")
    mpu4 = adafruit_mpu6050.MPU6050(tca[4])
    p5 = []
    r5 = []
if imus >= 6:
    print("6/" + str(imus) + " IMUS ...")
    mpu5 = adafruit_mpu6050.MPU6050(tca[5])
    p6 = []
    r6 = []
if imus >= 7:
    print("7/" + str(imus) + " IMUS ...")
    mpu6 = adafruit_mpu6050.MPU6050(tca[6])
    p7 = []
    r7 = []
if imus >= 8:
    print("8/" + str(imus) + " IMUS ...")
    mpu7 = adafruit_mpu6050.MPU6050(tca[7])
    p8 = []
    r8 = []

print("Initializing done!\n")

print("Calibration of " + imus + "IMUS ...")
start = datetime.now()

while stop == False:

    p1.append(math.atan2(mpu0.acceleration[1], mpu0.acceleration[2]) * 180/math.pi)
    r1.append(math.atan2(mpu0.acceleration[0], math.sqrt(mpu0.acceleration[1]**2 +  mpu0.acceleration[2]**2)) * 180/math.pi)
    
    p2.append(math.atan2(mpu1.acceleration[1], mpu1.acceleration[2]) * 180/math.pi)
    r2.append(math.atan2(mpu1.acceleration[0], math.sqrt(mpu1.acceleration[1]**2 +  mpu1.acceleration[2]**2)) * 180/math.pi)
    
    p3.append(math.atan2(mpu2.acceleration[1], mpu2.acceleration[2]) * 180/math.pi)
    r3.append(math.atan2(mpu2.acceleration[0], math.sqrt(mpu2.acceleration[1]**2 +  mpu2.acceleration[2]**2)) * 180/math.pi)
    
    p4.append(math.atan2(mpu3.acceleration[1], mpu3.acceleration[2]) * 180/math.pi)
    r4.append(math.atan2(mpu3.acceleration[0], math.sqrt(mpu3.acceleration[1]**2 +  mpu3.acceleration[2]**2)) * 180/math.pi)
    
    p5.append(math.atan2(mpu4.acceleration[1], mpu4.acceleration[2]) * 180/math.pi)
    r5.append(math.atan2(mpu4.acceleration[0], math.sqrt(mpu4.acceleration[1]**2 +  mpu4.acceleration[2]**2)) * 180/math.pi)
    
    p6.append(math.atan2(mpu5.acceleration[1], mpu5.acceleration[2]) * 180/math.pi)
    r6.append(math.atan2(mpu5.acceleration[0], math.sqrt(mpu5.acceleration[1]**2 +  mpu5.acceleration[2]**2)) * 180/math.pi)
    
    p7.append(math.atan2(mpu6.acceleration[1], mpu6.acceleration[2]) * 180/math.pi)
    r7.append(math.atan2(mpu6.acceleration[0], math.sqrt(mpu6.acceleration[1]**2 +  mpu6.acceleration[2]**2)) * 180/math.pi)
    
    p8.append(math.atan2(mpu7.acceleration[1], mpu7.acceleration[2]) * 180/math.pi)
    r8.append(math.atan2(mpu7.acceleration[0], math.sqrt(mpu7.acceleration[1]**2 +  mpu7.acceleration[2]**2)) * 180/math.pi)
    
    #time.sleep(1)
    end = datetime.now()
    delta = end-start
    if delta.seconds >= calibrationTime:
        stop = True

s = str(statistics.mean(p1)) + "," + str(statistics.mean(r1)) + "," + str(statistics.mean(p2)) + "," + str(statistics.mean(r2)) + ","  + str(statistics.mean(p3)) + ","  + str(statistics.mean(r3)) + ","  + str(statistics.mean(p4)) + ","  + str(statistics.mean(r4)) + ","  + str(statistics.mean(p5)) + "," + str(statistics.mean(r5)) + "," + str(statistics.mean(p6)) + "," + str(statistics.mean(r6)) + "," + str(statistics.mean(p7)) + "," + str(statistics.mean(r7)) + "," + str(statistics.mean(p8)) + "," + str(statistics.mean(r8))

file.write(s)
