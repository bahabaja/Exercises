import re

file = open('commands.txt','r')

t=[]
for line in file:
    vlan1 = re.findall('switchport trunk allowed vlan.*',line)
    for line in vlan1:
        vlan2 = re.findall('\d+',line)
        t = t + vlan2
#print(t)
file = open('commands.txt','r')

def getfilelength(file):
    counter = 0
    for line in file:
        if re.match('switchport trunk allowed vlan.*',line):
            counter += 1
        else :
            continue
    return (counter)

comm = getfilelength(file)

k = []
def commons(t):
    m = []
    for item in t:
        co = t.count(item)
        if co >= comm:
            k.append(item)
    m = m + k

    z = list(set(m))
    n = [int(i) for i in z]
    n.sort()
    b = [str(i) for i in n]
    return(b)

l = []
def unique(t):
    n = []
    for item in t:
        co = t.count(item)
        if (co == 1):
            l.append(item)
    n = n + l
    n =  [int(i) for i in n]
    n.sort()
    b = [str(i) for i in n]
    return(b)

print ('List 1 =' + str(commons(t)))
#print (commons(t))
print ("\n")
print ('List 2=' + str(unique(t)))
#print (unique(t))













