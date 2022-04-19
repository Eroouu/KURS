import numpy as np
import matplotlib.pyplot as plt
from math import *
from random import randint
from PID import PID
import pymysql

def Function( i):
    return sin(i * 0.5)


plt.style.use('seaborn-whitegrid')

fig, ax = plt.subplots()

#count = int( input() )
count = 30
levelNeeded = 30
FirstLevel = 10
AddedLevel = 1
#print("write the level that you need")
#levelNeeded = float( input() )

#print("write the number of newwhater")
#FirstLevel = float( input() )

#print("write the number of AddedLevel")
#AddedLevel = float( input() )


MyPID = PID(levelNeeded)
levelNow = FirstLevel
print()
Y0 = []
Y0.append(levelNow)
for i in range(count):
    levelNow += AddedLevel
    print(levelNow)

    mv = MyPID.update(levelNow, 0.5)
    print(mv)

    levelNow += mv
    print(levelNow)
    Y0.append(levelNow)
    print()
X0 = [i for i in range(count + 1)]
print(len(Y0))
print(len(X0))
ax.plot(X0, Y0, color ='blue')
plt.show()


