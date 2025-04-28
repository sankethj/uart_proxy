# uart_proxy
- This tool is used to create UART Proxy pipe using socat and a simple python script.
- It is useful in sceanrios where one needs to access the already in-use specific port /dev/ttyACM0.

## Virtual UART setup
- Ignore this step if you want to try in real device port and modify the code mentioned in next block (port name)
- `sudo socat -d -d pty,raw,echo=0 pty,raw,echo=0`
- This will create /dev/pts/5 and /dev/pts/6

## Proxy setup
- `sudo sudo socat -d -d PTY,link=/tmp/spy_in,raw,echo=0 PTY,link=/tmp/spy_out,raw,echo=0`
