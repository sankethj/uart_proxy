import threading
import serial

# Open real device
dev = serial.Serial('/dev/pts/6', baudrate=9600, timeout=0)

# Open fake device
fake = serial.Serial('/tmp/spy_out', baudrate=9600, timeout=0)

def dev_to_fake():
    while True:
        data = dev.read(1024)
        if data:
            print(f"[DEVICE -> MONITOR] {data}")
            fake.write(data)

def fake_to_dev():
    while True:
        data = fake.read(1024)
        if data:
            print(f"[MONITOR -> DEVICE] {data}")
            dev.write(data)

# Start threads
t1 = threading.Thread(target=dev_to_fake)
t2 = threading.Thread(target=fake_to_dev)

t1.start()
t2.start()
t1.join()
t2.join()
