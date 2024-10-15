input_data = open('input.txt' , 'r')
data = input_data.read()
from math import sqrt , fabs
data = data.split() 
r = int(data[2])
x1 = int(data[0])
y1 = int(data[1])
x2  = int(data[3])
y2 = int(data[4])
R = int(data[5])
print(y1, y2)
if x1 == x2 and abs(y2-y1)>= r+R:
    output = open('output.txt', 'w')
    output.write(str('NO'))
if y1 == y2 and abs(x2-x1)>= r+R:
    output = open('output.txt', 'w')
    output.write(str('NO'))
if x1 == x2 and abs(y2-y1)<= r+R:
        output = open('output.txt', 'w')
        output.write(str('YES'))
if y1 == y2 and abs(x2-x1)<= r+R:
        output = open('output.txt', 'w')
        output.write(str('YES'))
BC = int(y2 - y1)
AC = int(x2-x1)
AB = sqrt(BC**2 + AC**2)
if AB < r +R:
    output = open('output.txt', 'w')
    output.write(str('YES'))
if AB >= r+R:
    output = open('output.txt', 'w')
    output.write(str('NO'))


input_data.close()
output.close()