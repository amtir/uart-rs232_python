
import serial

#ser = serial.Serial('/dev/ttyAMA0', 9600)  # open serial port
ser = serial.Serial('/dev/serial0', 9600)  # open serial port
print(ser.name) # check which port was really used

ser.write(b'uart-rs232 test\n') # write a string

line = ser.readline()   # read a '\n' terminated line
print(line)

ser.close()



