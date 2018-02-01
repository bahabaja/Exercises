import re

f = open("ShowIpRoute.txt","r")

def protocoltype(capital):
    if capital == 'L':
        return ('Local')
    elif capital == 'C':
        return('Connected')
    elif capital == 'S':
        return('Static')
    elif capital == 'R':
        return ('RIP')
    elif capital == 'M':
        return ('Mobile')
    elif capital == 'B':
        return ('BGP')
    elif capital == 'D':
        return ('EIGRP')
    elif capital == 'D EX':
        return ('EIGRP External')
    elif capital == 'O':
        return ('OSPF')
    elif capital == 'O IA':
        return ('OSPF Inter Area')
    elif capital == 'O N1':
        return ('OSPF NSSA external type 1')
    elif capital == 'O N2':
        return ('OSPF NSSA external type 2')
    elif capital == 'O E1':
        return ('OSPF  external type 1')
    elif capital == 'O E2':
        return ('OSPF  external type 2')
    elif capital == 'E':
        return ('EGP')
    elif capital == 'i':
        return ('IS-IS')
    elif capital == 'i su':
        return ('IS-IS summary')
    elif capital == 'i L1':
        return ('IS-IS level 1')
    elif capital == 'i L2':
        return ('IS-IS level 2')
    elif capital == 'i ia':
        return ('IS-IS inter-area')
    elif capital == '*':
        return ('candidate default')
    elif capital == 'U':
        return ('per-user static route')
    elif capital == 'o':
        return ('ODR')
    elif capital == 'P':
        return ('periodic downloaded static route')
    elif capital == 'H':
        return ('NHRP')
    elif capital == 'l':
        return ('LISP')
    elif capital == 'a':
        return ('application route')
    elif capital == '+':
        return ('replicated route')
    elif capital == '%':
        return ('next hop override')


ipadresses = re.compile("(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)")
ipadresses2 = re.compile("via\s(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)")
timestamp = re.compile('\d+:\d+:\d+')
admetric = re.compile("\[.*/.*]")
outinterface = re.compile('([A-Z][a-z][a-z]*\d.*)')
protocol = re.compile('([A-Z]\s[A-Z][0-9])|([a-z]\s[A-Z][0-9])|([A-Z]|[a-z]|\W)')

for line in f:
    ip = ipadresses.search(line)
    ip2 = ipadresses2.search(line)
    adm = admetric.search(line)
    tstmp = timestamp.search(line)
    outint = outinterface.search(line)
    prot = protocol.search(line)
    if ip and ip2 and adm and tstmp and outint and prot:
        ip1 = ip.group()
        ip2= ip2.group()
        ad = adm.group()
        t =  tstmp.group()
        oi = outint.group()
        capital = prot.group()
        print(line)
        print('Protocol :' + protocoltype(capital))
        print("\n")
        print('Prefix :' + (ip1))
        print("\n")
        print ('AD/Metric :' + (ad))
        print("\n")
        print('Next-hop :' + (ip2[4:]))
        print("\n")
        print('Last-update :' + (t))
        print("\n")
        print('Outbound interface :' + (oi))
        print("\n")

