import sys
import random


fio = "Skorobohatko Stanislav"
fio_bits = ''.join(format(ord(x),'b')for x in fio)
seq = 0,1
prbs1=''
prbs2=''


for i in range (0, len(fio_bits)*2):
    a = random.choice(seq)
    prbs1= prbs1 + str(a)

for i in range (0, int(len(fio_bits)*1.7)):
    a = random.choice(seq)
    prbs2= prbs2 + str(a)

print(fio_bits)
print(prbs1)
print(prbs2)

