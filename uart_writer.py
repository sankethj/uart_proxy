import serial
import time

# Change this to your /dev/pts/XXX
port = '/dev/pts/5'  # <-- adjust based on your socat output

ser = serial.Serial(port, baudrate=9600, timeout=0)

counter = 0
print(f"[Writer] Opened {port}")

while True:
    ser.write(bytes([counter % 256]))
    print(f"[Writer] Sent byte: {counter % 256}")
    counter += 1
    # 9600 baud => send each byte naturally, no need to sleep manually
    time.sleep(0.5)  # Optional fine-tune
