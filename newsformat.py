import csv

import NewsPaperContinent
mainInfo=[]
newspaperName = []
class newsformat:
    newspapers = ""
    date = ""
    newsPaperDetails = []



def __init__():
    print ("ess")

def analyse(newspaper):
    # date extractor
    global newspapers
    newspapers = newspaper
    for x in newspaper:
        # print('line')
        # print (x)

        for y in x:  # word wise
            a = y

            if y.find ("Date:") != -1:
                # print (a)
                print ("found")
                global date
                date = a
                date=date.replace ("Date: ", "")
                with open ("output.txt", "a") as scorefile:
                    scorefileWriter = csv.writer (scorefile)
                   # print (date)
                    scorefileWriter.writerow ([date])
                scorefile.close ()
            for x in newspaper:
                # print('line')
                # print (x)

                for y in x:  # word wise
                    a = y

    print (date)


    # continent news  name finder
    for x in newspaper:
        p=NewsPaperContinent.Newspaper("",0.0);
        name=""

        for y in x:  # word wise
            a = y
            i = 0
            lenN = len (x) - 1
            #print (y)
            if y.find ("Date:") != -1:
                break
            elif y.find ("NewsPaper name") != -1:
              #  print (y)
                print ("found")
               # print (lenN)
                i = 1
                while i <=lenN:
                    global newspaperName

                   # print (x[i])
                    newspaperName.append(x[i])
                    i+=1

            elif x[0].find ("NewsPaper name") == -1:
               # print ()
                i = 1
                sum=0.0
                name = x[0]
                #print (name)

                while i <= lenN:
                    #print (lenN)
                   # print (i)
                    #print(x[i])
                    sum=sum+float(x[i])

                    i+=1
                    if(i>lenN):
                        # print (sum/(lenN))
                        p = NewsPaperContinent.Newspaper (name, sum/(lenN))
                        avg=0.0
                        avg=sum/(lenN)
                        global mainInfo
                        mainInfo.append(p)

                        with open ("output.txt", "a") as scorefile:
                            scorefileWriter = csv.writer (scorefile)

                            scorefileWriter.writerow ([name,avg])
                        scorefile.close ()
                break


#print (mainInfo)


