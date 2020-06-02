import getpass
import telnetlib

HOST = "192.168.122.110"
user = input("Enter your telent username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"lameras\n")
tn.write(b"conf t\n")
tn.write(b"int loop 1\n")
tn.write(b"ip add 1.1.1.1 255.255.255.255\n")
tn.write(b"int loop 2\n")
tn.write(b"ip add 2.2.2.2 255.255.255.255\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))