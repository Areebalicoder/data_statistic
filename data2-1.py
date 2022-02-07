import statistics
import csv
from collections import Counter

with open('data2.csv',newline='') as f:
    reader=csv.reader(f)
    data=list(reader)
data.pop(0)
a=[]

for i in range(len(data)):
    b=data[i][1]
    a.append(float(b))

d=len(a)
h=Counter(a)
#print(h)

x=statistics.mean(a)
#print("mean", x)
y=statistics.mode(a)
#print("mode", y)
z=statistics.median(a)
#print("median", z)

m1=[]
m2=[]
m3=[]
midc=dict(h)

for k,l in midc.items():
    k=float(k)
    if 50 < k > 60:
        if l == max(list(h.values())):
             m1.append(k)
             
    elif 60 < k > 70:
        if l == max(list(h.values())):
             m2.append(k)
             
    elif 70 < k > 75:
        if l == max(list(h.values())):
             m3.append(k)

if len(m1)>len(m2) and len(m3):
    print("mode"+", ".join(map(str,m1)))

if len(m2)>len(m1) and len(m3):
    print(m2)

if len(m3)>len(m2) and len(m1):
    print(m3)
        
 
