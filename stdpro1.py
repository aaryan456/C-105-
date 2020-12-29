import math 
import csv
with open("C:/Users/HOME/Downloads/datacsv.csv", newline="") as d:
    data = csv.reader(d)
    filedata = list(data)
file = filedata[0]
def mean(file):
    length = len(file)
    total=0
    for i in file:
        total+=int(i)
    mean = total/length
    return mean

sqlist = []
for number in file:
    find = int(number)-mean(file)
    find = find**2
    sqlist.append(find)

sum = 0
for i in sqlist:
    sum = sum+1

answer = sum/(len(file)-1)
stddev = math.sqrt(answer)
print(stddev)    



