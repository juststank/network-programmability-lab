import getpass
import telnetlib

HOST = "192.168.122.111"
user = input("Enter your telent username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
for n in range (2,11):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"name Py_Vlan_" + str(n).encode('ascii') + b"\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
