import serial

ser = serial.Serial('/dev/ttyACM0',9600)
ser2 = serial.Serial('/dev/ttyACM1',9600)
s = [0,1]
s2 = [0,2]
def veBlink(x,sPort,ard):
        if  x % 4 == 0:
                print("blink arduino:",ard)
                sPort.write(1)
while True:
        read_serial=ser.readline()
        s[0] = int(ser.readline(),16)
        s2[0] = int(ser2.readline(),16)
        print ('Do Arduino 1: ',s[0])
        veBlink(s[0],ser,1)
        print ('Do Arduino 2: ',s2[0])
        veBlink(s2[0],ser2,2)
