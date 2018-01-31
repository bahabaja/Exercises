import re
import sys

access_template = ['switchport mode access', 'switchport access vlan {}', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable']
trunk_template = ['switchport trunk encapsulation dot1q', 'switchport mode trunk', 'switchport trunk allowed vlan {}']

interfacemode = input('Enter interface mode(access/trunk):' )
if not re.match('access|trunk',interfacemode):
  print  ("Only access or trunk can be chosen")
  input('Enter interface mode(access/trunk):')
interfacenumber = input('Enter interface type and number:' )

if interfacemode == 'access':
    vlanno = input('Enter VLAN number:')
    print ('Interface ' + (interfacenumber))
    print ("\n")
    print (access_template[0])
    print("\n")
    print(access_template[1].replace("{}",vlanno))
    print("\n")
    print(access_template[2])
    print("\n")
    print(access_template[3])
    print("\n")
    print(access_template[4])

elif interfacemode == 'trunk':
    allowedvlans = input('Enter allowed VLANs:' )
    x = re.findall("\d+",allowedvlans)
    #print(x)
    print('Interface ' + interfacenumber)
    print("\n")
    print (trunk_template[0])
    print("\n")
    print(trunk_template[1])
    print("\n")
    print(trunk_template[2].replace("{}",','.join(x)))