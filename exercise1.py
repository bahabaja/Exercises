import re
import ipaddress

def converter (MASK):
    if MASK == '8':
        return '255.0.0.0'
    elif MASK == '9':
        return '255.128.0.0'
    elif MASK == '10':
        return '255.192.0.0'
    elif MASK == '11':
        return '255.224.0.0'
    elif MASK == '12':
        return '255.240.0.0'
    elif MASK == '13':
        return '255.248.0.0'
    elif MASK == '14':
        return '255.252.0.0'
    elif MASK == '15':
        return '255.254.0.0'
    elif MASK == '16':
        return '255.255.0.0'
    elif MASK == '17':
        return '255.255.128.0'
    elif MASK == '18':
        return '255.255.192.0'
    elif MASK == '19':
        return '255.255.224.0'
    elif MASK == '20':
        return '255.255.240.0'
    elif MASK == '21':
        return '255.255.248.0'
    elif MASK == '22':
        return '255.255.252.0'
    elif MASK == '23':
        return '255.255.254.0'
    elif MASK == '24':
        return '255.255.255.0'
    elif MASK == '25':
        return '255.255.255.128'
    elif MASK == '26':
        return '255.255.255.192'
    elif MASK == '27':
        return '255.255.255.224'
    elif MASK == '28':
        return '255.255.255.240'
    elif MASK == '29':
        return '255.255.255.248'
    elif MASK == '30':
        return '255.255.255.252'
    elif MASK == '31':
        return '255.255.255.254'
    elif MASK == '32':
        return '255.0.0.0'



def binaryconverter(ipadres):
    ip_array =ipadres.split(".")
    for x in ip_array:
        z = bin(int(x))[2:].zfill(8)
        print (z,end=" "),

def printip(ipadres):
    ip_array1 = ipadres.split(".")
    for no in ip_array1:
        print(no.rjust(8),end=" ")



while True:
    ipadres = input('Please enter the IP address: ')
    if not re.match("(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)",ipadres):
        print('Please enter a valid IP adress ')
    else:
        break

while True:
    subnetmask = input('Please enter the subnet mask in decimal notation:/ ')
    if not re.match ("[8-9]|[1][1-9]|[2][1-9]|[3][1-2]",subnetmask):
        print ('You should enter a valid number')
    else:
        break

MASK = subnetmask
SM = converter(MASK)
host = ipaddress.IPv4Address(ipadres)
net = ipaddress.IPv4Network(ipadres + '/' + SM, False)
networkad = ipaddress.IPv4Address(int(host) & int(net.netmask))
broadcast = net.broadcast_address

printip(ipadres)
print("\n")
binaryconverter(ipadres)
print("\n")
print ('Network address is :' + str(networkad)+'/'+subnetmask)
print("\n")
print('Broadcast address is :' + str(broadcast)+'/'+subnetmask)






