import serial
import time

# Change this to your /dev/pts/YYY
port = '/tmp/spy_in'  # <-- adjust based on your socat output

ser = serial.Serial(port, baudrate=9600, timeout=0)

print(f"[Reader] Opened {port}")

while True:
    byte = ser.read(1)
    if byte:
        print(f"[Reader] Received byte: {int.from_bytes(byte, byteorder='little')}")
