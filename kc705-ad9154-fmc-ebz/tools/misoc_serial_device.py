import serial.tools.list_ports

p = serial.tools.list_ports
hwid = 'USB VID:PID=10C4:EA60 SER=0001 LOCATION=1-9.2'
s = next(p.grep(hwid))
print('device file for MiSoC chatter: {:}'.format(s))
