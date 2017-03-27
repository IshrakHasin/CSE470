import csv
import newsformat
scoreList=[]
process = []
Megacoutner=0
#reads the csv file
with open("SII.csv","r") as scorefile:
    scorefileReader= csv.reader(scorefile)


    for row in scorefileReader:
       if len (row) !=0:
        scoreList=scoreList+[row]
        process.append(row)

       # print (row)
    scorefile.close()

#print (process[0])
#processing csv file
p=""
i=0
#DATEX=process[0]
#DATEX[0]=DATEX[0].replace("Date: ","")
#print (DATEX[0])
#print("SS")
#print (process[1])

#split by date in future then for loop

#sliting by 8
arraya = []

i = 0
#print (0*8+i)

for y in process:
   # print (process[Megacoutner*8+i])
    arraya.append(process[Megacoutner*8+i])

   # print (i)
    i += 1
    if i >7:
       # print ("enuf")
        a = newsformat.analyse (arraya)
        i=0
        arraya=[]
        Megacoutner+=1

#print (p[i])
#    lenString=len(p)
#    print(x[0])


    #for y in p:
       # print(y)
        #if y.find("Date"):
         #    a =newsformat("date","")
            # if len (y) !=0:
            # print ("1")
             #if y.find('Date:'):
               #  print (y)
               #  print ("0")